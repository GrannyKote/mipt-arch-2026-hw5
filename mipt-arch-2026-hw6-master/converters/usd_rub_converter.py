from converters import BaseCurrencyConverter

class UsdRubConverter(BaseCurrencyConverter):
    def __init__(self):
        super().__init__(__name__, "USD", "RUB")