from fastapi import APIRouter
from src.eth_provider import w3
from src.mcp_schema import build_mcp_response, build_mcp_error

router = APIRouter()

def clean_data(data):
    """Convert byte fields to hex strings recursively."""
    if isinstance(data, bytes):
        return data.hex()
    elif isinstance(data, dict):
        return {k: clean_data(v) for k, v in data.items()}
    elif isinstance(data, (list, tuple)):
        return [clean_data(i) for i in data]
    else:
        return data

@router.get("/{block_id}")
def get_block(block_id: str):
    try:
        block = (
            w3.eth.get_block(int(block_id))
            if block_id.isdigit()
            else w3.eth.get_block(block_id)
        )
        block_data = clean_data(dict(block))
        return build_mcp_response("block", block_data)
    except Exception as e:
        print("Error fetching block:", str(e))
        return build_mcp_error(str(e))
