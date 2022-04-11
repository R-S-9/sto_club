from pydantic import BaseModel, validator


class ActivateValidator(BaseModel):
    redis_uuid: str

    @validator('redis_uuid')
    def validator_redis_uuid(cls, redis_uuid: str) -> str:
        if redis_uuid is None or len(redis_uuid) != 36:
            raise ValueError('Uuid is not valid')
        return redis_uuid
