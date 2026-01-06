# Ethereum_mcp_server
The project implements an Ethereum Context Server compliant with the Model Context Protocol (MCP).
The server enables Large Language Models (LLMs) to retrieve Ethereum blockchain data—such as blocks, transactions, and account information—using structured context queries over an HTTP interface.

System Architecture
LLM / User
   |
   |  MCP Context Request
   v
FastAPI Context Server (Python)
   |
   |  JSON-RPC Calls
   v
Ethereum RPC Provider (Infura / Alchemy / Public RPC)

*Prerequisites
Ensure the following are installed on your system:
Python 3.9 or higher
pip (Python package manager)
An Ethereum RPC endpoint (Infura, Alchemy, or public RPC)

*Installation Instructions
1. Create a Virtual Environment (Recommended)
python -m venv venv
Activate the environment:
Windows
venv\Scripts\activate
2. Install Dependencies
pip install -r requirements.txt
Typical dependencies include:
fastapi
uvicorn
web3
pydantic

*RPC Provider Configuration
Set your Ethereum RPC URL as an environment variable:
export ETH_RPC_URL="https://mainnet.infura.io/v3/YOUR_API_KEY"
(Windows PowerShell)
setx ETH_RPC_URL "https://mainnet.infura.io/v3/YOUR_API_KEY"
Alternatively, you can hardcode the RPC URL in the configuration file (not recommended for production).

*Running the Server
Start the FastAPI server using Uvicorn:
uvicorn main:app --host 0.0.0.0 --port 8000
Once running, the server will be available at:
http://localhost:8000
API documentation (Swagger UI):
http://localhost:8000/docs
*API Details
Base URL
http://localhost:8000
1. Get Block Details
Endpoint

GET /context/block
Query Parameters

*Parameter	Type	Description
block_id	string	Block number or block hash
Example Request

GET /context/block?block_id=19384782
Sample Response

{
  "type": "block",
  "block_number": 19384782,
  "timestamp": 1710000000,
  "miner": "0xabc...",
  "gas_used": 14562321,
  "transaction_count": 172
}
2. Get Transaction Details
Endpoint

GET /context/transaction
Query Parameters

*Parameter	Type	Description
tx_hash	string	Ethereum transaction hash
Example Request

GET /context/transaction?tx_hash=0xabc123...
Sample Response

{
  "type": "transaction",
  "hash": "0xabc123...",
  "from": "0xsender...",
  "to": "0xreceiver...",
  "value_eth": 0.5,
  "gas_used": 21000,
  "input": "0x"
}
3. Get Account Information
Endpoint

GET /context/account
Query Parameters

Parameter	Type	Description
address	string	Ethereum account address
Example Request

GET /context/account?address=0x123...
Sample Response

{
  "type": "account",
  "address": "0x123...",
  "balance_eth": 2.34,
  "nonce": 15
}
*MCP Compliance
All responses follow structured JSON format
Designed for direct LLM consumption
Supports contextual relevance and composability
Graceful handling of invalid or incomplete requests

*Error Handling
Invalid block numbers, hashes, or addresses return descriptive error messages
RPC failures are handled gracefully
Input validation is enforced for all endpoints

*Conclusion
This Ethereum Context Server demonstrates a practical approach to exposing blockchain data as structured context for language models using MCP. The system is modular, extensible, and suitable for AI-powered blockchain analysis.

