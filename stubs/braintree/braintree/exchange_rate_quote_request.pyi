from _typeshed import Incomplete

from braintree.exchange_rate_quote_input import ExchangeRateQuoteInput as ExchangeRateQuoteInput

class ExchangeRateQuoteRequest:
    quotes: Incomplete
    def __init__(self) -> None: ...
    def add_exchange_rate_quote_input(self, attributes): ...
    def to_graphql_variables(self): ...