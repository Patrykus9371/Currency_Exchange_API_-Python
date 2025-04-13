from dist import Dist

if __name__ == "__main__":
    # Przykłady konwersji między różnymi walutami
    a = Dist(100, "EUR")    # 100 euro
    b = Dist(200, "PLN")    # 200 złotych
    c = Dist(50, "USD")     # 50 dolarów
    d = Dist(300, "GBP")    # 300 funtów
    e = Dist(10000, "JPY")  # 10000 jenów
    f = Dist(500, "CHF")    # 500 franków szwajcarskich
    g = Dist(100, "NOK")    # 100 koron norweskich

    # Operacje
    print("EUR + PLN =", a + b)
    print("USD + EUR =", c + a)
    print("PLN - USD =", b - c)
    print("GBP + CHF =", d + f)
    print("JPY + PLN =", e + b)
    print("NOK + GBP =", g + d)
    print("USD * 2 =", c * 2)
    print("EUR / 2 =", a / 2)