import requests
from pprint import pprint
from random import randint
from datetime import datetime

class YaUploader:
    def __init__(self, token):
        self.token = token

    def _get_upload_link(self, yadisk_file_path): # Функция получения временной ссылки на загрузку файла в каталог yadisk_file_path
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Authorization' : f'OAuth {self.token}'} #'Content-Type' : 'application/json' не является обязательным
        params = {'path': yadisk_file_path, 'overwrite':'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        # response.raise_for_status()
        # pprint(response.json())
        if response.status_code == 200:
            print('we got link successfully')
        return response.json()

    def upload(self, path_to_file, name_file_for_uploud):
        temp_upload_url = self._get_upload_link(path_to_file).get('href')
        response = requests.put(temp_upload_url, data=open(name_file_for_uploud,'rb'))
        # response.raise_for_status()
        if response.status_code == 201:
            print('successful upload')

def random_log():
    with open('text.txt', 'a') as file:
        data = f'{str(randint(1000,10000))} - {datetime.now()}\n'
        file.write(data)

if __name__ == '__main__':
    random_log() # Функция для наполнения тестового файла
    path_to_file = 'Home_work_Netology/text.txt'
    name_file_for_upload = 'text.txt'
    token = ''
    uploader = YaUploader(token)
    uploader.upload(path_to_file, name_file_for_upload)