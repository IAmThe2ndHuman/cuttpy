import requests
import json
from cuttpy.response import CuttpyResponse


class Cuttpy:
    """The main class for Cuttpy. You need a Cuttly API key to use this wrapper. Generate one by signing up at
    https://cutt.ly/"""

    def __init__(self, key: str):
        self.key = key

    def shorten(self, url: str):
        """Returns the shortened version of a URL.

        :type url: str
        :arg url: The URL which you would like to shorten
        :returns: Attributes like shortened URL, original URL, and more.
        """
        response = requests.get(f"https://cutt.ly/api/api.php?key={self.key}&short={url}")
        return CuttpyResponse(raw=json.loads(response.content), http_code=response.status_code)
