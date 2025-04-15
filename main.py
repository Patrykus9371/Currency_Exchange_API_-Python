import re
import sys
import argparse
from dist import Dist

# This script is a command-line tool for performing currency conversions and arithmetic operations on amounts in different currencies.
def parse_expression(expression):
    expression = expression.replace(" ", "")
    tokens = re.findall(r'[\+\-\*/]|\d+\.?\d*[A-Za-z]+', expression)

    if not tokens:
        raise ValueError("Niepoprawne wyrażenie.")

    parsed = []
    for token in tokens:
        if token in "+-*/":
            parsed.append(token)
        else:
            match = re.match(r'(\d+\.?\d*)([A-Za-z]+)', token)
            if match:
                amount = float(match.group(1))
                currency = match.group(2).upper()
                parsed.append(Dist(amount, currency))
            else:
                raise ValueError(f"Niepoprawny token: {token}")
    return parsed

# This function evaluates the parsed expression.
def evaluate_expression(tokens):
    result = tokens[0]
    i = 1
    while i < len(tokens):
        op = tokens[i]
        next_val = tokens[i + 1]
        if op == "+":
            result = result + next_val
        elif op == "-":
            result = result - next_val
        elif op == "*":
            result = result * next_val.amount
        elif op == "/":
            result = result / next_val.amount
        i += 2
    return result

#Example usage of the Dist class and the conversion operations.
def run_examples():
    a = Dist(100, "EUR")
    b = Dist(200, "PLN")
    c = Dist(50, "USD")
    d = Dist(300, "GBP")
    e = Dist(10000, "JPY")
    f = Dist(500, "CHF")
    g = Dist(100, "NOK")

    print("EUR + PLN =", a + b)
    print("USD + EUR =", c + a)
    print("PLN - USD =", b - c)
    print("GBP + CHF =", d + f)
    print("JPY + PLN =", e + b)
    print("NOK + GBP =", g + d)
    print("USD * 2 =", c * 2)
    print("EUR / 2 =", a / 2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Konwerter walut z operacjami.")
    parser.add_argument("expression", nargs="?", help='Wyrażenie np. "100EUR + 200PLN - 50USD"')
    parser.add_argument("--examples", action="store_true", help="Pokaż przykłady operacji")

    args = parser.parse_args()

    if args.examples:
        run_examples()
    elif args.expression:
        try:
            tokens = parse_expression(args.expression)
            result = evaluate_expression(tokens)
            print("Wynik:", result)
        except Exception as e:
            print("Błąd:", e)
    else:
        print("Użycie:\n  python main.py \"100EUR + 200PLN\"\n  python main.py --examples")
