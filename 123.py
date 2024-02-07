# # # import asyncio
# # # # async def task_one():
# # # #     print("Задача 1: Начало выполнения")
# # # #     await asyncio.sleep(2)
# # # #     print("Задача 1: Завершение выполнения")
# # # #
# # # # async def task_two():
# # # #     print('Задача 2: Начало')
# # # #     await asyncio.sleep(1)
# # # #     print("Задача 2: Конец")
# # # #
# # # # async def main():
# # # #     await asyncio.gather(task_one(), task_two())
# # # #
# # # # asyncio.run(main())
# # #
# # # async def createGenerator() :
# # #     mylist = range(3)
# # #     for i in mylist :
# # #         await asyncio.sleep(2)
# # #         yield i*i
# # # createGenerator()
# # #
# # # mygenerator = createGenerator()
# # # print(mygenerator)
# # # for i in mygenerator:
# # #      print(i)
# #
# #
# # import asyncio
# # async def async_generator():
# #     for i in range(5):
# #         print(f"Значение {i}")
# #         await asyncio.sleep(1)
# #         yield i
# #
# # async def main():
# #     async for a in async_generator():
# #         print(f"Получено значение: {a}")
# # asyncio.run(main())
#
#
# # import asyncio
# # import random
# #
# # async def generate_matrix_row(row_length):
# #     return [random.randint(0, 9) for _ in range(row_length)]
# #
# # async def generate_matrix(num_rows, row_length):
# #     matrix = []
# #     for _ in range(num_rows):
# #         row = await generate_matrix_row(row_length)
# #         matrix.append(row)
# #         await asyncio.sleep(1)
# #     return matrix
# #
# # async def print_matrix(matrix):
# #     for row in matrix:
# #         print(row)
# #         await asyncio.sleep(1)
# #
# # async def main():
# #     num_rows = 5
# #     row_length = 5
# #     generated_matrix = await generate_matrix(num_rows, row_length)
# #     await print_matrix(generated_matrix)
# #
# #
# # asyncio.run(main())
#
# import asyncio
# import random
#
# async def generate_matrix_row(length):
#     return [random.randint(0, 9) for _ in range(length)]
#
# async def generate_matrix(num_rows, length):
#     matrix = []
#     for _ in range(num_rows):
#         row = await generate_matrix_row(length)
#         matrix.append(row)
#         print(row)
#         await asyncio.sleep(1)
#     return matrix
#
# async def main():
#     num_rows = 5
#     row_length = 5
#     await generate_matrix(num_rows, row_length)
#
# asyncio.run(main())


import asyncio
import aiohttp
from bs4 import BeautifulSoup
import random

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            text = soup.get_text()
            return text.splitlines()

async def simulate_user_behavior():
    await asyncio.sleep(random.randint(1, 5))

async def display_data(data):
    for line in data:
        print(line)
        await asyncio.sleep(0.125)

async def main():
    url = 'https://www.vidal.ru/'
    data = await fetch_data(url)
    await simulate_user_behavior()
    await display_data(data)


asyncio.run(main())
