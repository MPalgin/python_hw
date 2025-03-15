import json

from pydantic import BaseModel, field_validator, ValidationError
from typing import Optional, Type
from aiohttp import web


class CreateUser(BaseModel):
    name: str
    user_pass: str

    @field_validator('name')
    def name_validator(cls, value):
        if len(value) > 100:
            raise ValidationError('Name is too big. You have 100 symbols')
        return value

    @field_validator('user_pass')
    def password_validator(cls, value):
        if len(value) < 8:
            raise ValidationError('password is too short')
        if len(value) > 100:
            raise ValidationError('password is too big')
        return value


class UpdateUser(BaseModel):
    name: Optional[str]
    user_pass: Optional[str]

    @field_validator('name')
    def name_validator(cls, value):
        if len(value) > 100:
            raise ValidationError('Name is too big. You have 100 symbols')
        return value

    @field_validator('user_pass')
    def password_validator(cls, value):
        if len(value) < 8:
            raise ValidationError('password is too short')
        if len(value) > 100:
            raise ValidationError('password is too big')
        return value


class CreateAdvertisement(BaseModel):
    header: str
    desc: Optional[str]
    owner_id: int


class UpdateAdvertisement(BaseModel):
    header: str
    desc: Optional[str]


def validator(json_data: dict,
              model_class: Type[CreateUser] | Type[UpdateUser] | Type[CreateAdvertisement] | Type[UpdateAdvertisement]):
    try:
        model_item = model_class(**json_data)
        return model_item.model_dump(exclude_none=True)
    except ValidationError as error:
        raise web.HTTPBadRequest(
            text=json.dumps({'error': error.errors()}),
            content_type='application/json'
        )
