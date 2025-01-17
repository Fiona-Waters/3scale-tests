"""
Failed Challenge Authentication:
Cardholder enrolled, authentication unsuccessful. Merchants should prompt customers for another form of payment.
"""
import pytest
from threescale_api.errors import ApiClientError


def test_unsuccessful_with_challenge(custom_card, invoice):
    """
    Test scenario:
        - Clears all CC data for an account
        - Add CC details for an account
        - Verify that CC was not added
    """
    cc_view = custom_card("4000000000001109", verify_3ds=True)
    assert cc_view.alert() == "An error occurred, please review your CC details or try later."

    with pytest.raises(ApiClientError) as exc_info:
        invoice.charge()

    assert exc_info.type is ApiClientError
    assert "422 Unprocessable Entity" in exc_info.value.args[0]
    assert "Failed to charge the credit card" in exc_info.value.args[0]
