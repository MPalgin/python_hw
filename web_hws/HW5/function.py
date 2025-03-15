import json
import bcrypt

from typing import Type
from aiohttp import web
from models import Session, User, Advertisement, engine, Base


async def get_orm_item(item_class: Type[User]| Type[Advertisement], id: int, session: Session):
    item = await session.get(item_class, id)
    if item is None: raise web.HTTPNotFound(text=json.dumps({'status': 'error', 'message': 'object is not found'}),
                                            content_type='application/json')
    return item


def hash_password(password: str):
    encoded_password = password.encode()
    hashed_password = bcrypt.hashpw(password=encoded_password, salt=bcrypt.gensalt())
    decoded_password = hashed_password.decode()
    return decoded_password


async def orm_context(app_data: web.Application):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


@web.middleware
async def session_middleware(request: web.Request, handler):
    async with Session() as session:
        request['session'] = session
        response = await handler(request)
        return response
