class MPTClientError(Exception):
    """Base exception for MPTClient."""

class MPTAPIError(MPTClientError):
    """API error from mpt server."""

class MPTMissingAPIKeyError(MPTClientError):
    """Raised when the FINAI_API_KEY environment variable is not set."""
