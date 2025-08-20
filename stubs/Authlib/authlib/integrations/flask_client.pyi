class FlaskOAuth2App:
    def authorize_redirect(self, redirect_uri: str, **kwargs: object) -> object: ...
    def authorize_access_token(self, **kwargs: object) -> object: ...
    def parse_id_token(
        self,
        token: dict[str, object],
        nonce: str | None = None,
        claims_cls: type | None = None,
        leeway: int = 60,
    ) -> object: ...

class OAuth:
    def create_client(self, name: str) -> FlaskOAuth2App: ...
    def register(self, name: str, **kwargs: object) -> None: ...
    def __init__(
        self,
        app: object = None,
        cache: object = None,
        fetch_token: object = None,
        update_token: object = None,
    ) -> None: ...
