from datetime import date

import pytest

from quotelab.quote.domain.coverages import Coverages
from quotelab.quote.domain.enums import QuoteStatus
from quotelab.quote.domain.errors import InvalidQuoteError
from quotelab.quote.domain.insured import Insured
from quotelab.quote.domain.quote import Quote
from quotelab.quote.domain.vehicle import Vehicle


def make_quote() -> Quote:
    return Quote.create(
        insured=Insured("Maria", "12345678901", date(1990, 5, 20)),
        vehicle=Vehicle("ABC1D23", "Gol", 2020),
        coverages=Coverages(collision=True),
    )


def test_new_quote_starts_as_draft():
    assert make_quote().status is QuoteStatus.DRAFT


def test_confirm_twice_fails():
    quote = make_quote()
    quote.confirm()
    with pytest.raises(InvalidQuoteError):
        quote.confirm()


def test_vehicle_rejects_invalid_plate():
    with pytest.raises(InvalidQuoteError):
        Vehicle("123", "Gol", 2020)


def test_coverages_require_at_least_one():
    with pytest.raises(InvalidQuoteError):
        Coverages()