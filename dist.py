from currency_converter import CurrencyConverter
from nbp_api_client import NBPApiClient

class Dist:
    """Klasa do obsługi wartości z walutą z możliwością konwersji."""
    _converter = CurrencyConverter(NBPApiClient())

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit.upper()

    def _convert_other(self, other):
        if not isinstance(other, Dist):
            raise TypeError("Oczekiwano obiektu klasy Dist")
        if self.unit == other.unit:
            return other.value
        return self._converter.convert(other.value, other.unit, self.unit)

    def __add__(self, other):
        return Dist(self.value + self._convert_other(other), self.unit)

    def __sub__(self, other):
        return Dist(self.value - self._convert_other(other), self.unit)

    def __mul__(self, factor):
        return Dist(self.value * factor, self.unit)

    def __truediv__(self, divisor):
        return Dist(self.value / divisor, self.unit)

    def __repr__(self):
        return f"{self.value:.2f} {self.unit}"
