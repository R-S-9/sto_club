import uuid


class ShortToken:
    @staticmethod
    def create_short_token() -> str:
        return str(uuid.uuid4())[:8]
