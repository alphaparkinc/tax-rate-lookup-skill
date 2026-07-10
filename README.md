# genpark-tax-rate-lookup-skill

> **GenPark AI Agent Skill** -- US state and local ZIP sales tax calculator.

## Quick Start

```python
from client import TaxRateLookupClient
client = TaxRateLookupClient()
result = client.calculate_tax(state_code="NY", order_amount=50.00)
print(result["tax_amount"])
```
