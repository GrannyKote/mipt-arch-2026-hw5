from converters import BaseCurrencyConverter

class UsdEurConverter(BaseCurrencyConverter):
    def __init__(self):
        super().__init__(__name__, "USD", "EUR")