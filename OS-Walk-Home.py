import os
import time
# import subprocess
# import psutil

# print(f"Текущая директория: {os.getcwd()}")
#
# if os.path.exists('second'):
#     os.chdir('second')
# else:
#     os.mkdir('Second')
#     os.chdir('second')
# print(f"Текущая директория: {os.getcwd()}")
#
# # os.makedirs(r'third\fourth')
#
# print(os.listdir())
#
# # for i in os.walk('.'):
# #     print(i)
#
# os.chdir(r'E:\Python_Projects\Module_7')
# print(f"Текущая директория: {os.getcwd()}")
# print(os.listdir())
#
# print()
# file = [f for f in os.listdir() if os.path.isfile(f)]
# dirs = [d for d in os.listdir() if os.path.isdir(d)]
# # print(f"Файлы: {file}")
# # print(f"Директроии: {dirs}")
#
# # os.startfile('products.txt')
# for enumerate in range(len(file)):
#     print(enumerate, file[enumerate])
#
# # os.startfile(file[7])
# # time.sleep(3)
# #
# # # subprocess.Popen('taskkill /im products.txt /f')
# #
# # for proc in psutil.process_iter():
# #     if proc.name == file[7]:
# #         proc.terminate()
#
# print()
# print(os.stat(file[7]))
# print(os.stat(file[7]).st_file_attributes, os.stat(file[7]).st_size)
# print()
#
# # os.system('pip install random2')
#
# ##################################
# #######  OS.Sys - HomeWork
# ##################################
#
# print("#" * 50)
# print("Import OS - HomeWork")
# print("#" * 50)
# print()


print(os.getcwd())
for root, dirs, files in os.walk('.'):
    for file in files:
        file_path = os.path.join(root, file)
        file_time = os.path.getmtime(file_path)
        formated_time = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(file_time))
        file_size = os.path.getsize(file_path)
        parent_directory = os.path.dirname(file_path)

        print(f"Обнаружен файл: {file}\n"
              f"Путь: {file_path},\n"
              f"Размер: {file_time} байт,\n"
              f"Время изменения: {formated_time},\n"
              f"Родительская директория: {parent_directory}\n")
        print()