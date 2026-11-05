from dataclasses import dataclass
from datetime import date

from quotelab.quote.application.ports.quote_repository import QuoteRepository
from quotelab.quote.domain.coverages import Coverages
from quotelab.quote.domain.insured import Insured
from quotelab.quote.domain.quote import Quote
from quotelab.quote.domain.vehicle import Vehicle


@dataclass(frozen=True)
class CreateQuoteCommand:
    # Só tipos primitivos: o adapter HTTP monta isso a partir do schema.
    insured_name: str
    insured_document: str
    insured_birth_date: date
    vehicle_plate: str
    vehicle_model: str
    vehicle_year: int
    collision: bool = False
    theft: bool = False
    third_party_liability: bool = False


class CreateQuote:
    def __init__(self, repository: QuoteRepository) -> None:
        self._repository = repository

    def execute(self, command: CreateQuoteCommand) -> Quote:
        quote = Quote.create(
            insured=Insured(
                name=command.insured_name,
                document=command.insured_document,
                birth_date=command.insured_birth_date,
            ),
            vehicle=Vehicle(
                plate=command.vehicle_plate,
                model=command.vehicle_model,
                year=command.vehicle_year,
            ),
            coverages=Coverages(
                collision=command.collision,
                theft=command.theft,
                third_party_liability=command.third_party_liability,
            ),
        )
        self._repository.add(quote)
        return quote