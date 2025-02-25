import pydantic
from typing import Optional, Type
from errors import HttpError


def validate(
        json_data: dict,
        model_class: Type['CreateUser'] | Type['UpdateUser'] | Type['CreateAdvertisement'] | Type['UpdateAdvertisement']
        ):
    try:
        model_item = model_class(**json_data)
        return model_item.model_dump(exclude_none=True)
    except pydantic.ValidationError as error:
        raise HttpError(400, error.errors())


class CreateUser(pydantic.BaseModel):

    name: str
    user_pass: str

    @pydantic.field_validator('name')
    def validate_name(cls, value):
        if len(value) > 50:
            raise ValueError('Name is too big')
        return value

    @pydantic.field_validator('user_pass')
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError('password is too short')
        if len(value) > 100:
            raise ValueError('password is too big')
        return value


class UpdateUser(pydantic.BaseModel):
    name: Optional[str]
    user_pass: Optional[str]

    @pydantic.field_validator('user_pass')
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError('password is too short')
        if len(value) > 100:
            raise ValueError('password is too big')
        return value


class CreateAdvertisement(pydantic.BaseModel):
    header: str
    desc: Optional[str]
    owner_id: int


class UpdateAdvertisement(pydantic.BaseModel):
    header: str
    desc: Optional[str]