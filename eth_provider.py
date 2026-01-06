from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()
print("Loaded RPC_URL:",os.getenv("RPC_URL"))

RPC_URL = os.getenv("RPC_URL")
w3 = Web3(Web3.HTTPProvider(RPC_URL))

if not w3.is_connected():
    raise Exception("Failed to connect to Ethereum network")
