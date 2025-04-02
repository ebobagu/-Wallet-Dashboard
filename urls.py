from django.urls import path
from wallet.views import get_wallet_balance, get_tokens, get_nfts

urlpatterns = [
    path("balance/<str:address>/", get_wallet_balance),
    path("tokens/<str:address>/", get_tokens),
    path("nfts/<str:address>/", get_nfts),
]
