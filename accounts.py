from fastapi import APIRouter
from src.eth_provider import w3
from src.mcp_schema import build_mcp_response, build_mcp_error

router = APIRouter()

def clean_data(data):
    """Recursively convert bytes and complex objects to JSON-safe data."""
    if isinstance(data, bytes):
        return data.hex()
    elif isinstance(data, dict):
        return {k: clean_data(v) for k, v in data.items()}
    elif isinstance(data, (list, tuple)):
        return [clean_data(i) for i in data]
    else:
        return data

@router.get("/{address}")
def get_account(address: str):
    try:
        if not w3.is_address(address):
            return build_mcp_error("Invalid Ethereum address")

        # Get account details
        balance = w3.eth.get_balance(address)
        nonce = w3.eth.get_transaction_count(address)
        code = w3.eth.get_code(address)

        data = {
            "address": address,
            "balance_wei": balance,
            "balance_eth": w3.from_wei(balance, 'ether'),
            "nonce": nonce,
            "is_contract": len(code) > 0
        }

        clean_result = clean_data(data)
        return build_mcp_response("account", clean_result)

    except Exception as e:
        print("Error fetching account:", str(e))
        return build_mcp_error(str(e))
