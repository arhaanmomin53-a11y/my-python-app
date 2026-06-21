import os
from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP Server named "ADK-Data-Server"
# This acts as the secure interface gateway for our agents
mcp = FastMCP("ADK-Data-Server")

# Define the absolute directory paths on our D: drive
CONTRACTS_DIR = os.path.abspath("./contracts")
INVOICES_DIR = os.path.abspath("./invoices")

@mcp.tool()
def read_contract_folder() -> str:
    """Allows the agent to list and read local contract text files dynamically."""
    # REASONING LOOP: The Intake agent calls this to scan the active contracts directory
    if not os.path.exists(CONTRACTS_DIR):
        return "Error: Contracts directory does not exist."
    
    files = [f for f in os.listdir(CONTRACTS_DIR) if f.endswith('.txt')]
    if not files:
        return "No text contract files found in the directory."
    
    output = "--- Active Project Contracts ---\n"
    for file_name in files:
        with open(os.path.join(CONTRACTS_DIR, file_name), 'r', encoding='utf-8') as f:
            output += f"\n[File: {file_name}]\n{f.read()}\n"
    return output

@mcp.tool()
def read_invoice_folder() -> str:
    """Allows the agent to look for newly submitted invoice text files."""
    # REASONING LOOP: The Auditor agent runs this tool to pick up newly uploaded invoices
    if not os.path.exists(INVOICES_DIR):
        return "Error: Invoices directory does not exist."
    
    files = [f for f in os.listdir(INVOICES_DIR) if f.endswith('.txt')]
    if not files:
        return "No new text invoice files found in the directory."
    
    output = "--- Incoming Unaudited Invoices ---\n"
    for file_name in files:
        with open(os.path.join(INVOICES_DIR, file_name), 'r', encoding='utf-8') as f:
            output += f"\n[File: {file_name}]\n{f.read()}\n"
    return output

if __name__ == "__main__":
    # Launching the server locally
    print("Starting local ADK Model Context Protocol Server...")
    mcp.run()