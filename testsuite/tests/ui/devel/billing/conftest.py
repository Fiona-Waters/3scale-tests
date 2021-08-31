"""Conftest for billing tests"""
import pytest
from threescale_api.resources import InvoiceState

from testsuite.ui.objects import BillingAddress
from testsuite.ui.views.admin.audience.account import InvoiceDetailView


@pytest.fixture
def line_items():
    """List of all items to be added to an invoice"""
    return [{'name': "test-item", 'description': 'test_item', 'quantity': '1', 'cost': 10}]


@pytest.fixture(scope="module")
def billing_address():
    """Billing address"""
    return BillingAddress("aaa", "bbb", "Brno", "Czech Republic", "", "123456789", "12345")


@pytest.fixture
def api_invoice(account, threescale, line_items):
    """Invoice created through API"""
    invoice = threescale.invoices.create(dict(account_id=account['id']))
    for line_item in line_items:
        invoice.line_items.create(line_item)

    invoice.state_update(InvoiceState.PENDING)
    invoice.charge()


@pytest.fixture
def ui_invoice(custom_admin_login, navigator, account, line_items):
    """Invoice created through UI"""
    custom_admin_login()
    view = navigator.navigate(InvoiceDetailView, account=account)
    for line_item in line_items:
        view.add_item(**line_item)

    view.issue()
    view.charge()