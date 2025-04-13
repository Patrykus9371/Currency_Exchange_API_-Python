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

### [🧪 Example Usage
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

