import os

# # создаем папку в текущей дириктории
# if not os.path.exists("data"):
#     os.mkdir("data")
# # создаем файл txt
# with open("data/info.txt", "a") as file:
#     text = ""
#     for i in range(10):
#         text += "Ivan|Minsk|45\n"
#     file.write(text)

# создаем папку в текущей дириктории
if not os.path.exists("data"):
    os.mkdir("data")
# создаем файл csv
with open("data/info.csv", "a") as file:
    text = ""
    for i in range(10):
        text += "Ivan|Minsk|45\n"
    file.write(text)
