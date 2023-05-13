from astrotraders.api.wrapper import HttpxClientWrapper


class BaseResource:
    def __init__(self, client: HttpxClientWrapper):
        self._client = client
