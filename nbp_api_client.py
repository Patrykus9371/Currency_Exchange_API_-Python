import requests

class NBPApiClient:
    """Klient API NBP do pobierania kursów walut."""
    BASE_URL = "https://api.nbp.pl/api/exchangerates/tables/A/?format=json"

    def fetch_rates(self):
        try:
            response = requests.get(self.BASE_URL)
            response.raise_for_status()
            data = response.json()[0]["rates"]
            rates = {item["code"]: item["mid"] for item in data}
            rates["PLN"] = 1.0
            return rates
        except requests.RequestException as e:
            raise RuntimeError(f"Błąd podczas pobierania danych z NBP: {e}")
