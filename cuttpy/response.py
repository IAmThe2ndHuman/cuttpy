from typing import Union


class CuttpyResponse(object):
    """The response class. Internal use only."""

    def __init__(self, raw: Union[dict, None], http_code: int):
        if raw is None:
            self.code = 0
            self.http = http_code
            self.description = "A serverside error has occurred."
        else:
            self.http = 200
            raw = raw["url"]
            code = raw["status"]
            self.code = code
            if code == 1:
                self.description = "This URL has already been shortened."
            elif code == 2:
                self.description = "The entered URL is not a URL."
            elif code == 3:
                self.description = "The preferred URL name is already taken."
            elif code == 4:
                self.description = "Invalid API key."
            elif code == 5:
                self.description = "The URL did not pass the validation. Includes invalid characters."
            elif code == 6:
                self.description = "The URL provided is from a blocked domain."
            elif code == 7:
                self.description = "The URL has been shortened successfully."

                self.original_url = raw["fullLink"]
                self.shortened_url = raw["shortLink"]
                self.code = code
