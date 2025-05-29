import os
import requests
from .logger import get_logger
from .exceptions import (
    MPTAPIError,
    MPTMissingAPIKeyError,
)
import json

class MPTClient:
    def __init__(self, base_url="https://finai.solutions/", timeout=30):
        self.base_url = base_url.rstrip('/')
        self.logger = get_logger()
        self.timeout = timeout
        self.api_key = os.environ.get('FINAI_API_KEY')
        if not self.api_key:
            self.logger.error("FINAI_API_KEY is not set in environment variables.")
            raise MPTMissingAPIKeyError("FINAI_API_KEY is not set as an environment variable.")

    def _request(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"POST {url} | Data: {payload}")
        try:
            print("url: {}".format(url))
            print("payload: {}".format(payload))
            headers = {"Content-Type": "application/json"}
            resp = requests.post(url, data=json.dumps(payload), headers=headers, timeout=self.timeout)
            self.logger.info(f"Response: {resp.status_code}")
            print(resp.text)
            print(resp.content)
            resp.raise_for_status()
            if resp.content:
                try:
                    return resp.json()
                except Exception:
                    self.logger.warning("Response is not JSON, returning raw content.")
                    return resp.content
            return None
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request failed: {e}")
            raise MPTAPIError(f"API request error: {e}")

    def post_portfolio(self, asset_type, start_date, end_date=None, granularity="86400", return_period=30, market_cap="1000000000", tickers=None):
        """POST /portfolio"""
        payload = {
            "api_key": self.api_key,
            "asset_type": asset_type,
            "start_date": start_date,
            #"granularity": granularity,
            #"return_period": return_period,
            #"market_cap": market_cap,
        }
        if end_date:
            payload["end_date"] = end_date
        if tickers:
            payload["tickers"] = str(tickers)
        return self._request("/portfolio", payload)

    def post_ultimate(self, asset_type, start_date, end_date=None, granularity="86400", return_period=30,
                      market_cap="1Billion"):
        """POST /ultimate"""
        payload = {
            "api_key": self.api_key,
            "asset_type": asset_type,
            "start_date": start_date,
            "granularity": granularity,
            "return_period": return_period,
            "market_cap": market_cap,
        }
        if end_date:
            payload["end_date"] = end_date
        return self._request("/ultimate", payload)

    def post_subscribe(self, asset_type, start_date, email, weights, tickers=None, end_date=None, granularity="86400",
                      return_period=30, market_cap="1Billion"):
        """POST /subscribe"""
        payload = {
            "api_key": self.api_key,
            "asset_type": asset_type,
            "start_date": start_date,
            "email": email,
            "weights": weights,
            "granularity": granularity,
            "return_period": return_period,
            "market_cap": market_cap,
        }
        if end_date:
            payload["end_date"] = end_date
        if tickers:
            payload["tickers"] = tickers
        return self._request("/subscribe", payload)

    def post_analyzer(self, asset_type, start_date, ticker, end_date=None, granularity="86400", return_period=30,
                      market_cap="1Billion"):
        """POST /analyzer"""
        payload = {
            "api_key": self.api_key,
            "asset_type": asset_type,
            "start_date": start_date,
            "ticker": ticker,
            "granularity": granularity,
            "return_period": return_period,
            "market_cap": market_cap,
        }
        if end_date:
            payload["end_date"] = end_date
        return self._request("/analyzer", payload)

    def post_update(self, tickers, actions, portfolio_id):
        """POST /update (No asset_type field)"""
        payload = {
            "api_key": self.api_key,
            "tickers": tickers,
            "actions": actions,
            "portfolio_id": portfolio_id
        }
        return self._request("/update", payload)
