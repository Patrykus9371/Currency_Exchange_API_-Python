from nbp_api_client import NBPApiClient

class CurrencyConverter:
    """Konwertuje waluty przy użyciu danych z NBP API."""
    def __init__(self, api_client):
        self.api_client = api_client
        self.rates = self.api_client.fetch_rates()
        print("Pobrane kursy walut:", self.rates)  


    # Download rates from NBP API
    def convert(self, amount, from_currency, to_currency):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()


        # Check if the currencies are supported
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError(f"Nieobsługiwana waluta: {from_currency} lub {to_currency}")

        amount_in_pln = amount * self.rates[from_currency]
        return amount_in_pln / self.rates[to_currency]