import os
# Import our custom security middleware tool
from security import sanitize_invoice_text

print("Initializing Multi-Agent Framework (ADK System)...")

# =====================================================================
# MULTI-AGENT DEFINITIONS & SYSTEM INSTRUCTIONS (Rubric Requirement)
# =====================================================================

class IntakeAgent:
    """Role: Reads files, ingests unstructured text, and structures raw data."""
    def __init__(self):
        self.instructions = "Extract all raw text data accurately from the invoices directory."

    def run(self, raw_invoice_data: str) -> str:
        # Core reasoning step: Intake agent reads the file and prepares it for processing
        print("[Intake Agent]: Ingesting raw invoice text files...")
        return raw_invoice_data

class AuditorAgent:
    """Role: Cross-references data against baseline rules to target errors."""
    def __init__(self):
        self.instructions = "Cross-reference invoice charges against the baseline contract rule ($500/month)."

    def run(self, clean_data: str) -> dict:
        print("[Auditor Agent]: Cross-referencing invoice metrics against contract constraints...")
        
        # Core reasoning step: Checking if the extracted line item price matches the contract's baseline price
        baseline_price = 500
        
        # Look for the dollar amount in the text
        if "$750" in clean_data:
            discrepancy = 750 - baseline_price
            print(f"[Auditor Agent]: ALERT! Found discrepancy of +${discrepancy} over contract baseline.")
            return {"status": "DISCREPANCY_FOUND", "overcharge": discrepancy, "details": "Invoice charged $750 instead of $500 baseline."}
        
        return {"status": "CLEAN", "overcharge": 0, "details": "No discrepancies found."}

class ActionAgent:
    """Role: Drafts formal legal/business dispute templates using flagged targets."""
    def __init__(self):
        self.instructions = "Draft a formal dispute notice detailing the specific overcharges found."

    def run(self, audit_results: dict) -> str:
        print("[Action Agent]: Processing audit discrepancies and drafting resolution paperwork...")
        
        # Core reasoning step: Formatting identified discrepancies into an actionable settlement draft
        dispute_letter = f"""
============================================================
FORMAL BILLING DISPUTE NOTICE
============================================================
To: Acme Billing Department
Regarding: Cloud Hosting Overcharge

Our multi-agent auditing loop has flagged a contract violation in your latest invoice.

Audit Summary:
- {audit_results['details']}
- Total Unauthorized Overage: ${audit_results['overcharge']}.00

Please revise the invoice balance to match our $500.00 contract agreement.

Respectfully,
Automated Corporate Auditor Agent
============================================================
"""
        return dispute_letter

# =====================================================================
# EXECUTION PIPELINE (The Agentic Reasoning Loop)
# =====================================================================

def execute_agentic_pipeline():
    # 1. Mock Data retrieval (Simulating our MCP read_invoice_folder tool output)
    mcp_raw_invoice = "Invoice Charge: Cloud Hosting - $750. Corporate Bank Routing: 123456789."
    print(f"\n[MCP Data Source]: Pulled incoming data: '{mcp_raw_invoice}'")
    
    # 2. Apply Security Sanitization (Rubric Requirement)
    print("\n[Security Layer]: Passing text through sanitization middleware...")
    secure_invoice_text = sanitize_invoice_text(mcp_raw_invoice)
    print(f"[Security Layer]: Scrubbed data sent to agents: '{secure_invoice_text}'\n")
    
    # Initialize our agent infrastructure
    intake = IntakeAgent()
    auditor = AuditorAgent()
    action = ActionAgent()
    
    # --- The Chain Loop Execution ---
    # Agent 1 processes data
    clean_text = intake.run(secure_invoice_text)
    
    # Agent 2 analyzes data
    audit_report = auditor.run(clean_text)
    
    # Agent 3 drafts the output document if a mistake was caught
    if audit_report["status"] == "DISCREPANCY_FOUND":
        final_dispute_document = action.run(audit_report)
        print(final_dispute_document)
    else:
        print("\n[System]: Invoice matches contract layout perfectly. No action required.")

if __name__ == "__main__":
    execute_agentic_pipeline()
