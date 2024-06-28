# Variables
ENV_FILE = .env
REQUIREMENTS_FILE = requirements.txt
PYTHON_SCRIPT = solana_token_balance.py
JSON_FILE = solana_wallet.json
SAMPLE_JSON_FILE = solana_wallet.json

# Targets
.PHONY: all setup run clean generate_json help

all: setup run

setup:
	@echo "Installing dependencies..."
	pip install -r $(REQUIREMENTS_FILE)
	@echo "Dependencies installed."

run: $(ENV_FILE) $(REQUIREMENTS_FILE) $(PYTHON_SCRIPT) $(JSON_FILE)
	@echo "Running the script..."
	python $(PYTHON_SCRIPT)

clean:
	@echo "Cleaning up..."
	rm -f solana_*.xlsx
	@echo "Cleanup done."

example:
	@echo "Creating sample JSON file..."
	echo '[{"isConnected": true, "address": "DHAzXyqVFqw31qX6Jhvm8o6QPBKy67dAYRjMiVMuG4tm", "balance": null, "isDisabled": false, "type": "SOL", "phrase": "-=--=-=-=-", "label": null, "ens": null, "group": ["Personal Group"]}]' > $(SAMPLE_JSON_FILE)
	@echo "Sample JSON file created: $(SAMPLE_JSON_FILE)"

help:
	@echo "Makefile commands:"
	@echo "  all           - Setup and run the script"
	@echo "  setup         - Install dependencies"
	@echo "  run           - Run the script"
	@echo "  clean         - Remove generated Excel files"
	@echo "  example 	   - Create a sample solana_wallet.json file"
	@echo "  help          - Show this help message"
