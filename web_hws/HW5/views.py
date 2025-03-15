import json

from aiohttp import web
from sqlalchemy.exc import IntegrityError

from models import User, Advertisement
from function import get_orm_item, hash_password
from schema import validator, CreateUser, UpdateUser, CreateAdvertisement, UpdateAdvertisement


class UserView(web.View):
    async def get(self):
        user_id = int(self.request.match_info.get('user_id'))
        user = await get_orm_item(User, user_id, session=self.request.get('session'))
        response = web.json_response({'user_id': user.id, 'user_name': user.name})
        return response

    async def post(self):
        user_data = await self.request.json()
        validated_data = validator(json_data=user_data, model_class=CreateUser)
        user_password = validated_data.get('user_pass')
        hashed_pass = hash_password(user_password)
        validated_data['user_pass'] = hashed_pass
        new_user = User(**validated_data)
        self.request.get('session').add(new_user)
        try:
            await self.request.get('session').commit()
        except IntegrityError:
            raise web.HTTPConflict(text=json.dumps({'status': 'user already exists'}),
                                   content_type='application/json')

        return web.json_response({'user_id': new_user.id})

    async def patch(self):
        user_id = int(self.request.match_info.get('user_id'))
        user_data = await self.request.json()
        user_validated_data = validator(json_data=user_data, model_class=UpdateUser)
        if 'user_pass' in user_validated_data:
            user_validated_data['user_pass'] = hash_password(user_validated_data.get('user_pass'))

        user = await get_orm_item(item_class=User, id=user_id, session=self.request['session'])
        for field, value in user_validated_data.items():
            setattr(user, field, value)
        self.request['session'].add(user)
        await self.request['session'].commit()

        return web.json_response({'user_id': user_id})

    async def delete(self):
        user_id = int(self.request.match_info.get('user_id'))
        user = await get_orm_item(item_class=User, id=user_id, session=self.request['session'])
        session = self.request['session']
        await session.delete(user)
        await session.commit()
        return web.json_response({'status': 'user is deleted'})


class AdvertisementView(web.View):

    async def get(self):
        adv_id = int(self.request.match_info.get('advertisement_id'))
        adv = await get_orm_item(item_class=Advertisement, id=adv_id, session=self.request.get('session'))
        response = web.json_response({'advertisement_id': adv.id, 'header': adv.header, 'owner_id': adv.owner_id})
        return response

    async def post(self):
        adv_data = await self.request.json()
        validated_data = validator(json_data=adv_data, model_class=CreateAdvertisement)
        new_adv = Advertisement(**validated_data)
        self.request.get('session').add(new_adv)
        await self.request.get('session').commit()
        return web.json_response({'advertisement_header': new_adv.header})

    async def patch(self):
        adv_id = int(
            self.request.match_info.get('advertisement_id'))
        adv_data = await self.request.json()
        validated_data = validator(json_data=adv_data, model_class=UpdateAdvertisement)

        adv = await get_orm_item(item_class=Advertisement, id=adv_id, session=self.request.get('session'))
        for field, value in validated_data.items():
            setattr(adv, field, value)
        self.request.get('session').add(adv)
        await self.request.get('session').commit()

        return web.json_response({'adv_id': adv.id})

    async def delete(self):

        adv_id = int(
            self.request.match_info.get('advertisement_id'))
        adv = await get_orm_item(item_class=Advertisement, id=adv_id, session=self.request.get('session'))
        await self.request.get('session').delete(adv)
        await self.request.get('session').commit()

        return web.json_response({'status': f'advertisement {adv_id} is deleted'})
