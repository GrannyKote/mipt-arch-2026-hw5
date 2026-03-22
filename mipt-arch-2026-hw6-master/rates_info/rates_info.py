from abc import ABC, abstractmethod

class RatesInfo(ABC):
    @abstractmethod
    def get_current_rates(self, currency: str):
        pass