"""
tax-rate-lookup-skill: Client SDK
Retrieves sales tax rates by US state and ZIP, computing order tax totals.
"""
from __future__ import annotations
from typing import Optional

STATE_TAX_RATES = {
    "CA": 7.25, "NY": 4.00, "TX": 6.25, "FL": 6.00, "PA": 6.00,
    "IL": 6.25, "OH": 5.75, "GA": 4.00, "NC": 4.75, "MI": 6.00,
    "OR": 0.00, "DE": 0.00, "MT": 0.00, "NH": 0.00, "AK": 0.00,
}


class TaxRateLookupClient:
    """
    SDK for US sales tax lookup.
    """

    def calculate_tax(
        self,
        state_code: str,
        order_amount: float,
        zip_code: Optional[str] = None,
    ) -> dict:
        state = state_code.upper()
        rate = STATE_TAX_RATES.get(state, 5.0)  # Default average fallback

        # Optional ZIP local tax adder simulation
        local_addon = 0.0
        if zip_code and len(zip_code) >= 3:
            # Simulate local city tax (1.0% to 2.5%) based on zip hash
            local_addon = round((hash(zip_code) % 3) * 0.75 + 1.0, 2) if rate > 0 else 0.0

        total_rate = rate + local_addon
        tax_amount = round(order_amount * (total_rate / 100), 2)

        return {
            "tax_rate_pct": total_rate,
            "tax_amount": tax_amount,
            "total_amount": round(order_amount + tax_amount, 2),
            "state_code": state,
        }
