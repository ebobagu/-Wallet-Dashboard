from web3 import Web3

# Ethereum network provider (use Infura, Alchemy, or a local node)
INFURA_URL = 'https://mainnet.infura.io/v3/bc3892a3315441c9b816171ebbcdb48d'

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if Web3 is connected
if not web3.is_connected():
    print("Failed to connect to Ethereum network!")
    exit()
else:
    print("Connected to Ethereum network successfully!")

# Function to get Ethereum balance
def get_eth_balance(wallet_address):
    try:
        balance = web3.eth.get_balance(wallet_address)
        eth_balance = web3.fromWei(balance, 'ether')  # Convert from Wei to Ether
        return eth_balance
    except Exception as e:
        return f"Error: {e}"

# Function to get ERC-20 token balance
def get_token_balance(wallet_address, token_contract_address):
    try:
        # ERC-20 ABI to interact with the contract
        ERC20_ABI = [
            {
                "constant": True,
                "inputs": [{"name": "_owner", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "balance", "type": "uint256"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            }
        ]
        
        # Initialize the contract
        token_contract = web3.eth.contract(address=token_contract_address, abi=ERC20_ABI)
        
        # Get the balance
        balance = token_contract.functions.balanceOf(wallet_address).call()
        return balance
    except Exception as e:
        return f"Error: {e}"

# Function to get ERC-721 (NFT) balance
def get_nft_balance(wallet_address, nft_contract_address):
    try:
        # ERC-721 ABI to interact with the contract
        ERC721_ABI = [
            {
                "constant": True,
                "inputs": [{"name": "_owner", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "balance", "type": "uint256"}],
                "payable": False,
                "stateMutability": "view",
                "type": "function",
            }
        ]

        # Initialize the NFT contract
        nft_contract = web3.eth.contract(address=nft_contract_address, abi=ERC721_ABI)
        
        # Get the NFT balance
        balance = nft_contract.functions.balanceOf(wallet_address).call()
        return balance
    except Exception as e:
        return f"Error: {e}"

# Example Usage
if __name__ == "__main__":
    # Replace with the Ethereum wallet address you want to check
    wallet_address = '0xYourEthereumWalletAddressHere'

    # ETH balance
    eth_balance = get_eth_balance(wallet_address)
    print(f"Ethereum Balance: {eth_balance} ETH")

    # Replace with the token contract address (e.g., ERC-20 token)
    token_contract_address = '0xYourTokenContractAddressHere'
    token_balance = get_token_balance(wallet_address, token_contract_address)
    print(f"Token Balance: {token_balance} Tokens")

    # Replace with the NFT contract address (e.g., ERC-721 NFT)
    nft_contract_address = '0xYourNFTContractAddressHere'
    nft_balance = get_nft_balance(wallet_address, nft_contract_address)
    print(f"NFT Balance: {nft_balance} NFTs")
