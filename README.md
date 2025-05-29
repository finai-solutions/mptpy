# mpt_client

Python library for interacting with the finai-solutions mpt server API.

## Installation

```
pip install .
```

## Usage

```python
import os
from mpt_client import MPTClient

# Set your API key before initializing the client
os.environ["FINAI_API_KEY"] = "your-api-key"

client = MPTClient("https://finai.solutions/")

# Portfolio
portfolio = client.post_portfolio(
    asset_type="crypto",
    start_date="2024-01-01-00-00",
    tickers=["BTC", "ETH"]
)

# Ultimate
ultimate = client.post_ultimate(
    asset_type="stock",
    start_date="2024-01-01-00-00"
)

# Subscribe
subscription = client.post_subscribe(
    asset_type="crypto",
    start_date="2024-01-01-00-00",
    email="user@example.com",
    weights=["0.5", "0.5"],
    tickers=["BTC", "ETH"]
)

# Analyzer
analysis = client.post_analyzer(
    asset_type="stock",
    start_date="2024-01-01-00-00",
    ticker="AAPL"
)

# Update
updated_portfolio = client.post_update(
    tickers=["BTC", "ETH"],
    actions=["0.2", "-0.2"],
    portfolio_id="YOUR_PORTFOLIO_ID"
)
```
