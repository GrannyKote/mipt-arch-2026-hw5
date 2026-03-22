from converters import BaseCurrencyConverter

class UsdGbpConverter(BaseCurrencyConverter):
    def __init__(self):
        super().__init__(__name__, "USD", "GBP")