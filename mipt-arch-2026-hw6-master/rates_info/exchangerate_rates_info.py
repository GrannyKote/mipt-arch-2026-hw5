import json
import time

import requests
from rates_info.rates_info import RatesInfo

ADDRESS_TO_GET_RATES = "https://api.exchangerate-api.com/v4/latest/"
REQUEST_TIMEOUT = 10
MAX_RETRIES_COUNT = 3
RETRY_DELAY = 2

class ExchangerateRatesInfo(RatesInfo):
    def __init__(self, logger):
        self.logger = logger

    def get_current_rates(self, currency: str):
        current_attempt = 0
        while current_attempt < MAX_RETRIES_COUNT:
            try:
                address_to_request_currency_rates = ADDRESS_TO_GET_RATES + currency
                response = requests.get(address_to_request_currency_rates,  timeout=REQUEST_TIMEOUT) 
                response.raise_for_status()
                data = response.json()
                rates = data['rates']
                return rates
            
            except requests.exceptions.RequestException as e:
                    current_attempt += 1
                    self.logger.error(f"Request failed (attempt {current_attempt}/{MAX_RETRIES_COUNT}): {e}")
                    if current_attempt < MAX_RETRIES_COUNT:
                        time.sleep(RETRY_DELAY)
                    else:
                        self.logger.error("Max retries reached.  Unable to fetch rates.")
                        return None

            except (json.JSONDecodeError, KeyError) as e:
                    self.logger.error(f"Error processing JSON response: {e}")
                    return None