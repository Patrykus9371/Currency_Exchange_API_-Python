# 💱 Currency Exchange Calculator

A simple and extendable Python project for **automatic currency conversion** and **arithmetic operations** on monetary values, powered by real-time exchange rates from the **National Bank of Poland (NBP)**.

> Supports operations like `+`, `-`, `*`, `/` on values in different currencies with proper conversion.

---

## 📚 Table of Contents

- [🚀 Getting Started](#-getting-started)
- [🧪 Example Usage](#-example-usage)
- [📁 Project Structure](#-project-structure)
- [💡 Supported Currencies](#-supported-currencies)
- [📘 API Overview](#-api-overview)
- [🧰 Development](#-development)

- ## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.7+
- `requests` library

### 📥 Installation

```bash
git clone https://github.com/yourusername/currency-exchange.git
cd currency-exchange
pip install requests
```

- ## 🧪 Example Usage
        ```bash
        from dist import Dist
        
        a = Dist(100, "EUR")
        b = Dist(200, "PLN")
        c = Dist(50, "USD")
        d = Dist(300, "GBP")
        
        print("EUR + PLN =", a + b)
        print("USD + EUR =", c + a)
        print("PLN - USD =", b - c)
        print("GBP + PLN =", d + b)
        ```
        
        #### 💬 Output
        ```bash
        EUR + PLN = 143.07 EUR
        USD + EUR = 142.92 USD
        PLN - USD = 35.68 PLN
        GBP + PLN = 360.89 GBP
        ```

- ## 📁 Project Structure
    ```bash
    Currency_exchange/
    ├── dist.py                # Dist class - handles currency-aware values and arithmetic
    ├── currency_converter.py  # CurrencyConverter - handles conversion between currencies
    ├── nbp_api_client.py      # NBPApiClient - fetches currency rates from NBP
    ├── main.py                # Script for running examples
    └── README.md              # Project documentation
    ```
- ## 💡 Supported Currencies

    The app supports all currencies from NBP Table A. Examples:
    
    - 🇺🇸 USD – US Dollar
    
    - 🇪🇺 EUR – Euro
    
    - 🇵🇱 PLN – Polish Zloty
    
    - 🇬🇧 GBP – British Pound
    
    - 🇨🇭 CHF – Swiss Franc
    
    - 🇯🇵 JPY – Japanese Yen
    
    - 🇳🇴 NOK – Norwegian Krone
    
    - 🇸🇪 SEK – Swedish Krona
    
    - 🇨🇿 CZK – Czech Koruna
    
    - 🇭🇺 HUF – Hungarian Forint
    
    - ...and many more


- ## 📘 API Overview

    🔹 NBPApiClient
    Fetches currency exchange rates from the NBP API.
    
    ```bash
    converter = CurrencyConverter(client)
    amount_in_usd = converter.convert(100, 'PLN', 'USD')
    ```
    
    🔹 Dist
    Represents a monetary value in a specific currency with automatic conversion logic.
    
    ```bash
    a = Dist(100, 'EUR')
    b = Dist(200, 'PLN')
    print(a + b)  # Output in EUR
    ```
    Supports:
    
    - + Addition
    
    - - Subtraction
    
    - * Multiplication by scalar
    
    - / Division by scalar

- ## 🧰 Development
    To run the example script:
    
    ```bash
    python main.py
    ```
    You can customize main.py to test other combinations or scenarios.

