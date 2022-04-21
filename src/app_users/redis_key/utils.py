import os
from uuid import uuid4
from datetime import timedelta

import redis

from django.contrib.auth.models import User


class CreateRedisKey:
    def __init__(self):
        self.red = redis.Redis(
            host=os.getenv("REDIS_HOST"),
            port=int(os.getenv("REDIS_PORT")),
            db=int(os.getenv("REDIS_DB"))
        )

    def create_redis_key(self, token: uuid4, user_id: User) -> None:
        self.red.set(
            f'{token}',
            f'{user_id}',
            timedelta(hours=5),
        )

    def get(self, uuid):
        return self.red.get(uuid)
