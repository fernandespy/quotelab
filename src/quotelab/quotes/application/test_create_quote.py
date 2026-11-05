from datetime import date

import pytest

from quotelab.quote.application.create_quote import (
    CreateQuote,
    CreateQuoteCommand,
)
from quotelab.quote.domain.errors import InvalidQuoteError


def make_command(**overrides) -> CreateQuoteCommand:
    data = dict(
        insured_name="Maria",
        insured_document="12345678901",
        insured_birth_date=date(1990, 5, 20),
        vehicle_plate="ABC1D23",
        vehicle_model="Gol",
        vehicle_year=2020,
        collision=True,
    )
    data.update(overrides)
    return CreateQuoteCommand(**data)


def test_creates_and_persists_quote(repository):
    quote = CreateQuote(repository).execute(make_command())

    assert repository.get_by_id(quote.id) is quote
    assert quote.vehicle.plate == "ABC1D23"


def test_invalid_input_does_not_persist(repository):
    with pytest.raises(InvalidQuoteError):
        CreateQuote(repository).execute(make_command(vehicle_plate="XXX"))

    assert repository.items == {}