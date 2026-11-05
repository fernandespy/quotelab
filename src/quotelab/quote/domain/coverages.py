from dataclasses import dataclass

from quotelab.quote.domain.errors import InvalidQuoteError


@dataclass(frozen=True)
class Coverages:
    collision: bool = False
    theft: bool = False
    third_party_liability: bool = False

    def __post_init__(self) -> None:
        if not (self.collision or self.theft or self.third_party_liability):
            raise InvalidQuoteError("at least one coverage is required")