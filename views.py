import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Wallet
from .serializers import WalletSerializer

ETHERSCAN_API_KEY = "YOUR_ETHERSCAN_API_KEY"
OPENSEA_API_URL = "https://api.opensea.io/api/v1/assets"

@api_view(["GET"])
def get_wallet_balance(request, address):
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url).json()
    balance = int(response["result"]) / 10**18  # Convert from Wei
    return JsonResponse({"balance": balance})

@api_view(["GET"])
def get_tokens(request, address):
    url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&address={address}&tag=latest&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url).json()
    return JsonResponse({"tokens": response["result"]})

@api_view(["GET"])
def get_nfts(request, address):
    url = f"{OPENSEA_API_URL}?owner={address}&limit=5"
    response = requests.get(url).json()
    return JsonResponse({"nfts": response.get("assets", [])})
