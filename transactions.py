from fastapi import APIRouter
from src.eth_provider import w3
from src.mcp_schema import build_mcp_response, build_mcp_error

router = APIRouter()

def clean_data(data):
    if isinstance(data, bytes):
        return data.hex()
    elif isinstance(data, dict):
        return {k: clean_data(v) for k, v in data.items()}
    elif isinstance(data, (list, tuple)):
        return [clean_data(i) for i in data]
    return data

@router.get("/{tx_hash}")
def get_transaction(tx_hash: str):
    try:
        tx = w3.eth.get_transaction(tx_hash)
        tx_data = clean_data(dict(tx))
        return build_mcp_response("transaction", tx_data)
    except Exception as e:
        return build_mcp_error(str(e))
