import re

def sanitize_invoice_text(raw_text: str) -> str:
    """
    Scrub corporate bank routing numbers, tax IDs, and sensitive data 
    before sending payload text to the LLM cloud endpoint.
    """
    sanitized = raw_text

    # 1. Target 9-Digit Bank Routing Numbers
    routing_pattern = r'(?i)(routing|rtn|acct|routing #)?\b\d{9}\b'
    sanitized = re.sub(routing_pattern, r'\1 [REDACTED_ROUTING_NUMBER]', sanitized)

    # 2. Target Tax IDs / EINs (Pattern: XX-XXXXXXX)
    tax_id_pattern = r'\b\d{2}-\d{7}\b'
    sanitized = re.sub(tax_id_pattern, '[REDACTED_TAX_ID]', sanitized)

    return sanitized

if __name__ == "__main__":
    test_data = "Invoice total: $750. Please send wire to Routing Number 123456789. TaxID: 12-3456789."
    print("--- Security Sanitization Test ---")
    print(f"Before: {test_data}")
    print(f"After:  {sanitize_invoice_text(test_data)}")
