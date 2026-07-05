"""
example_usage.py -- Demonstrates TaxRateLookupClient
"""
from client import TaxRateLookupClient

def main():
    client = TaxRateLookupClient()
    result = client.calculate_tax(state_code="CA", order_amount=100.00, zip_code="90210")
    print("[Tax Rate Lookup Result]")
    print(f"Tax Rate: {result['tax_rate_pct']}%")
    print(f"Tax Amount: ${result['tax_amount']}")
    print(f"Total: ${result['total_amount']}")

if __name__ == "__main__":
    main()
