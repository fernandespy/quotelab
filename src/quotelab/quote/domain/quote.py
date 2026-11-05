from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4

from quotelab.quote.domain.coverages import Coverages
from quotelab.quote.domain.enums import QuoteStatus
from quotelab.quote.domain.errors import InvalidQuoteError
from quotelab.quote.domain.insured import Insured
from quotelab.quote.domain.vehicle import Vehicle


@dataclass
class Quote:
    id: UUID
    insured: Insured
    vehicle: Vehicle
    coverages: Coverages
    status: QuoteStatus = QuoteStatus.DRAFT
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    @classmethod
    def create(
        cls, insured: Insured, vehicle: Vehicle, coverages: Coverages
    ) -> "Quote":
        return cls(
            id=uuid4(), insured=insured, vehicle=vehicle, coverages=coverages
        )

    def confirm(self) -> None:
        if self.status is QuoteStatus.CONFIRMED:
            raise InvalidQuoteError("quote is already confirmed")
        self.status = QuoteStatus.CONFIRMED