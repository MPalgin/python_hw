import asyncio

from models import Session, SwapiPersons, engine, Base


async def make_db_table():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


async def drop_db_table():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)


async def get_swapi_obj(group_name: str, object_id: int, api_client):
    url = 'https://swapi.dev/api'

    response = await api_client.get(f'{url}/{group_name}/{object_id}/')

    json_data = await response.json()

    return json_data


async def prepare_orm(json_data: dict, client):

    for key, value in json_data.items():
        if isinstance(value, list):
            response_coro_list = [client.get(link) for link in value]
            response_list = await asyncio.gather(*response_coro_list)

            json_coro_list = [response.json() for response in response_list]
            json_data_list = await asyncio.gather(*json_coro_list)

            tmp_list = []
            for data in json_data_list:
                if data.get('name') is not None:
                    tmp_list.append(data.get('name'))
                else:
                    tmp_list.append(data.get('title'))
            json_data[key] = (', '.join(tmp_list))

    homeworld_link = json_data.get('homeworld')

    if homeworld_link is None:
        json_data['homeworld'] = None
    else:
        response = await client.get(homeworld_link)
        data = await response.json()
        json_data['homeworld'] = data.get('name')

    return json_data


async def add_to_db(json_objects_list):
    async with Session() as session:
        prepared_data = []
        for person in json_objects_list:
            person_data = SwapiPersons(birth_year=person.get('birth_year'),
                                       eye_color=person.get('eye_color'),
                                       films=person.get('films'),
                                       gender=person.get('gender'),
                                       hair_color=person.get('hair_color'),
                                       height=person.get('height'),
                                       homeworld=person.get('homeworld'),
                                       mass=person.get('mass'),
                                       name=person.get('name'),
                                       skin_color=person.get('skin_color'),
                                       species=person.get('species'),
                                       starships=person.get('starships'),
                                       vehicles=person.get('vehicles')
                                       )
            prepared_data.append(person_data)
        session.add_all(prepared_data)
        await session.commit()
