from dataclasses import dataclass
from datetime import date

from quotelab.quote.domain.errors import InvalidQuoteError


@dataclass(frozen=True)
class Insured:
    name: str
    document: str  
    birth_date: date

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise InvalidQuoteError("insured name cannot be empty")
        if not self.document.isdigit() or len(self.document) != 11:
            raise InvalidQuoteError("insured document must have 11 digits")
        if self.birth_date >= date.today():
            raise InvalidQuoteError("insured birth date must be in the past")