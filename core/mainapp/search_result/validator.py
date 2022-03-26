from pydantic import BaseModel, validator


class SearchWordValidator(BaseModel):
    search: str

    @validator('search')
    def validator_search_word(cls, search: str) -> str:
        if not search:
            raise ValueError('search is none')
        return search.capitalize()
