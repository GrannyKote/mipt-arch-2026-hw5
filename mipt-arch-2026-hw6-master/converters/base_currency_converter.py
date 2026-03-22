import json
import os
import time
from converters.currency_converter import CurrencyConverter
from helper.helper import convert_currency
from helper.helper import get_logger
from rates_info.exchangerate_rates_info import ExchangerateRatesInfo

class BaseCurrencyConverter(CurrencyConverter):
    def __init__(self, name, base_currency, target_currency):
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.logger = get_logger(name)
        self.current_rates_info = ExchangerateRatesInfo(self.logger)
        self.cache_file="exchange_rates.json"

    def get_rates(self):
        return self.current_rates_info.get_current_rates(self.base_currency)

    def convert(self, amount):
        return convert_currency(amount, self.get_rates()[self.target_currency])
    
    def _load_from_cache(self):
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r') as f:
                    data = json.load(f)
                    if time.time() - data['timestamp'] < self.cache_expiry:
                        return data['rates']
            except (json.JSONDecodeError, KeyError):
                print("Invalid cache file. Fetching from API.")
                return None
        return None

    def _save_to_cache(self, rates):
        try:
            data = {'timestamp': time.time(), 'rates': rates}
            with open(self.cache_file, 'w') as f:
                json.dump(data, f)
        except IOError as e:
            print(f"Error saving to cache: {e}")