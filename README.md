
[![Join our Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/hidden_coding)

# Solana Token Balance Checker

This script fetches the balance of a specified Solana token for all addresses listed in a JSON file. It supports checking the native SOL balance as well as SPL token balances.

## Requirements

- Python 3.6+

## Setup

1. Clone the repository and navigate to the project directory.

2. Create a `.env` file with the following content:

    ```env
    RPC_URL=https://api.mainnet-beta.solana.com
    TOKEN_CONTRACT=B6h248NJkAcBAkaCnji889a26tCiGXGN8cxhEJ4dX391
    ```

    Replace the `RPC_URL` and `TOKEN_CONTRACT` values with your own. For tracking the native SOL balance, set `TOKEN_CONTRACT` to `0x0`.

3. Create a `solana_wallet.json` file with the following content:

    ```json
    [
      {
        "isConnected": true,
        "address": "DHAzXyqVFqw31qX6Jhvm8o6QPBKy67dAYRjMiVMuG4tm",
        "balance": null,
        "isDisabled": false,
        "type": "SOL",
        "phrase": "-=--=-=-=-",
        "label": null,
        "ens": null,
        "group": ["Personal Group"]
      }
    ]
    ```

    You can also generate a sample JSON file using the Makefile:

    ```bash
    make example
    ```

## Usage

1. To install dependencies and run the script:

    ```bash
    make all
    ```

2. To install dependencies only:

    ```bash
    make setup
    ```

3. To run the script only:

    ```bash
    make run
    ```

4. To clean up generated Excel files:

    ```bash
    make clean
    ```

5. To create a sample `solana_wallet.json` file:

    ```bash
    make example
    ```

6. To display help information:

    ```bash
    make help
    ```

## Tracking Native SOL Token

To track the native SOL balance, set the `TOKEN_CONTRACT` variable in your `.env` file to `0x0`:

```env
RPC_URL=https://api.mainnet-beta.solana.com
TOKEN_CONTRACT=0x0
```

This will make the script query the native SOL balance for the given wallet addresses.

## Tracking SPL Tokens

To track an SPL token balance, set the `TOKEN_CONTRACT` variable in your `.env` file to the mint address of the SPL token:

```env
RPC_URL=https://api.mainnet-beta.solana.com
TOKEN_CONTRACT=B6h248NJkAcBAkaCnji889a26tCiGXGN8cxhEJ4dX391
```

Replace `B6h248NJkAcBAkaCnji889a26tCiGXGN8cxhEJ4dX391` with the mint address of your desired SPL token.

## Output

The script will save the wallet balances to an Excel file named `solana_<TOKEN_CONTRACT>.xlsx`.

[![Join our Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/hidden_coding)
