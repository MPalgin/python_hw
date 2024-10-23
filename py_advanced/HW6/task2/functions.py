import requests

def folder_creator(folder_name, yandex_token):
    url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    result = requests.put(url=url, headers={'Authorization': f'OAuth {yandex_token}'},
                 params={'path': folder_name})
    return result.status_code
