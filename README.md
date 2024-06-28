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

    Replace the `RPC_URL` and `TOKEN_CONTRACT` values with your own.

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

## Output

The script will save the wallet balances to an Excel file named `solana_<TOKEN_CONTRACT>.xlsx`.
