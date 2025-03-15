from aiohttp import web
from function import orm_context, session_middleware
from views import UserView, AdvertisementView

app = web.Application()

app.cleanup_ctx.append(orm_context)

app.middlewares.append(session_middleware)

app.add_routes(
    [
        web.post('/users/', UserView),
        web.get('/users/{user_id:\d+}', UserView),
        web.patch('/users/{user_id:\d+}', UserView),
        web.delete('/users/{user_id:\d+}', UserView),

        web.post('/advertisements/', AdvertisementView),
        web.get('/advertisements/{advertisement_id:\d+}', AdvertisementView),
        web.patch('/advertisements/{advertisement_id:\d+}', AdvertisementView),
        web.delete('/advertisements/{advertisement_id:\d+}', AdvertisementView),
    ]
)

web.run_app(app)
