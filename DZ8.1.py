import requests

import json

from settings import TOKEN

# ----------------------------

def hero_int(id):
    base_host = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
    uri = '/powerstats/' + str(id) + '.json'
    hero_int = base_host + uri
    response = requests.get(hero_int)
    res = json.loads(response.text)
    return res


hulk_int = hero_int(332)['intelligence']
cap_int = hero_int(149)['intelligence']
tan_int = hero_int(655)['intelligence']
heroes_int = {'Hulk': hulk_int, 'Thanos': tan_int, 'Captain America': cap_int}
smartest_hero = max(heroes_int, key=heroes_int.get)

print(f'Самый умный: {smartest_hero}')

# -------------------------------

class YaUploader:

    base_host = 'https://cloud-api.yandex.net:443'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def _get_upload_link(self, path):
        uri = 'v1/disk/resources/upload/'
        request_url = self.base_host + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(request_url, headers=self.get_headers(), params = params)
        print(response.json())
        return response.json()['href']

    def upload_to_disk(self, local_path, yandex_path):
        upload_url = self._get_upload_link(yandex_path)
        response = requests.put(upload_url, data=open(local_path, 'rb'), headers=self.get_headers())
        if response.status_code == 201:
            print('Загрузка успешна')

if __name__ == '__main__':
    ya = YaUploader(TOKEN)
    ya.upload_to_disk('C:/Users/Igor/Desktop/File1.txt', 'file1.txt')