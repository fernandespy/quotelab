from uuid import UUID

import pytest

from quotelab.quote.domain.quote import Quote


class InMemoryQuoteRepository:
    def __init__(self) -> None:
        self.items: dict[UUID, Quote] = {}

    def add(self, quote: Quote) -> None:
        self.items[quote.id] = quote

    def get_by_id(self, quote_id: UUID) -> Quote | None:
        return self.items.get(quote_id)


@pytest.fixture
def repository() -> InMemoryQuoteRepository:
    return InMemoryQuoteRepository()