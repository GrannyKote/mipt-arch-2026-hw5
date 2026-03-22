from converters import BaseCurrencyConverter

class UsdCnyConverter(BaseCurrencyConverter):
    def __init__(self):
        super().__init__(__name__, "USD", "CNY")