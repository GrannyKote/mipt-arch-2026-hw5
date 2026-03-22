from abc import ABC, abstractmethod

class CurrencyConverter(ABC):
    @abstractmethod
    def convert(self, amount):
        pass