class DomainError(Exception):
    """Base para erros de regra de negócio."""


class InvalidQuoteError(DomainError):
    """Cotação com dados inválidos."""