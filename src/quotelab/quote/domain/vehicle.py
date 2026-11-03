import re
from dataclasses import dataclass
from datetime import date

from quotelab.quote.domain.errors import InvalidQuoteError

# Placa antiga (ABC1234) ou Mercosul (ABC1D23)
_PLATE_RE = re.compile(r"^[A-Z]{3}[0-9][A-Z0-9][0-9]{2}$")


@dataclass(frozen=True)
class Vehicle:
    plate: str
    model: str
    year: int

    def __post_init__(self) -> None:
        if not _PLATE_RE.match(self.plate):
            raise InvalidQuoteError(f"invalid plate: {self.plate!r}")
        if not self.model.strip():
            raise InvalidQuoteError("vehicle model cannot be empty")
        if not 1900 <= self.year <= date.today().year + 1:
            raise InvalidQuoteError(f"invalid vehicle year: {self.year}")