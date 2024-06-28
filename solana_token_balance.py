import requests
import json
import pandas as pd
from dotenv import load_dotenv
import os
from tqdm import tqdm

# Load environment variables from .env file
load_dotenv()

# Solana RPC URL and token contract address from .env file
RPC_URL = os.getenv("RPC_URL")
TOKEN_CONTRACT = os.getenv("TOKEN_CONTRACT")

# Load the wallet addresses from the JSON file
with open('solana_wallet.json', 'r') as file:
    wallets = json.load(file)

def get_token_balance(wallet_address):
    headers = {
        "Content-Type": "application/json"
    }
    if TOKEN_CONTRACT == '0x0':
        body = json.dumps({
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getBalance",
            "params": [
                wallet_address
            ]
        })
    else:
        body = json.dumps({
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getTokenAccountsByOwner",
            "params": [
                wallet_address,
                {
                    "mint": TOKEN_CONTRACT
                },
                {
                    "encoding": "jsonParsed"
                }
            ]
        })

    response = requests.post(RPC_URL, headers=headers, data=body)
    result = response.json()

    if 'result' in result:
        if TOKEN_CONTRACT == '0x0':
            balance = result['result']['value'] / 1e9  # Convert lamports to SOL
            return balance
        else:
            accounts = result['result']['value']
            total_balance = sum(float(account['account']['data']['parsed']['info']['tokenAmount']['uiAmount']) for account in accounts)
            return total_balance
    else:
        return 0

# List to hold the wallet balance data
wallet_data = []

# Iterate over wallets and get token balances with a progress bar
for wallet in tqdm(wallets, desc="Fetching balances", unit="wallet"):
    if wallet['isConnected'] and not wallet['isDisabled']:
        address = wallet['address']
        balance = get_token_balance(address)
        wallet_data.append({
            "Wallet Address": address,
            "Balance": balance
        })

# Save the wallet balances to an Excel file
df = pd.DataFrame(wallet_data)
df.to_excel(f"solana_{TOKEN_CONTRACT}.xlsx", index=False)

print(f"Balances have been saved to solana_{TOKEN_CONTRACT}.xlsx")
