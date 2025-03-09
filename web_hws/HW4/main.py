import asyncio
from more_itertools import chunked
from function import get_swapi_obj
from aiohttp import ClientSession
from function import prepare_orm, add_to_db, make_db_table, drop_db_table
from datetime import datetime

REQUEST_LIMIT = 5


async def main(number_of_person: int):
    await drop_db_table()
    await make_db_table()

    async with ClientSession() as client:
        for chunk in chunked(range(1, number_of_person + 1), REQUEST_LIMIT):
            chunk_coro_list = [get_swapi_obj(group_name='people', object_id=id_, api_client=client) for id_ in chunk]

            result = await asyncio.gather(*chunk_coro_list)

            coro_list = [prepare_orm(json_data=dict_, client=client) for dict_ in result]

            result = await asyncio.gather(*coro_list)

            coro_to_paste = add_to_db(result)

            task = asyncio.create_task(coro_to_paste)

    tasks = asyncio.all_tasks() - {asyncio.current_task(), }
    for task in tasks:
        await task

if __name__ == '__main__':
    number_of_persons = int(input('Print number of persons to add in db: '))
    stat = datetime.now()
    result = asyncio.run(main(number_of_persons))
    print(datetime.now() - stat)
