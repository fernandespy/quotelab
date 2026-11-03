from typing import Protocol
from uuid import UUID

from quotelab.quote.domain.quote import Quote


class QuoteRepository(Protocol):
    def add(self, quote: Quote) -> None: ...

    def get_by_id(self, quote_id: UUID) -> Quote | None: ...