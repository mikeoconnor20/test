#!C:\Users\moconnor\.virtualenvs\test-YVpzeIj4\Scripts\python.exe

import fileutil


def get_file_info(full_fname):
    file_path = fileutil.get_path(full_fname)
    return file_path


filename = __file__
filename_path = get_file_info(filename)
print(f'path = {filename_path}')
