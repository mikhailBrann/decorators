import requests
from lib.castom_decorators import logger_decorator
from lib.Classes import Hero

# в декаратор в передовать путь в желаемую директорию для логирования, по умолчанию логи пишет в директорию logs 
@logger_decorator()
def get_intelligence(url, names):

    result_list = []
    for name in names:
        reqst = requests.get(f"{url}/search/{name}")

        if reqst.status_code == 200:
            request_result = reqst.json()

            if request_result['results']:
                for result in request_result['results']:
                    if result['name'] == name and result['powerstats']['intelligence']:
                        result_list.append({'name': result['name'], 'intelligence': result['powerstats']['intelligence']})

    if result_list:
        result_list = sorted(result_list, key=lambda hero_: hero_['intelligence'])
        wiseacre = Hero(result_list[0]['name'], result_list[0]['intelligence'])
        
        return wiseacre
    else:
        return 'Некорректно введены данные'

if __name__ == '__main__':
    api_url = 'https://superheroapi.com/api.php/2619421814940190'
    heroes_list = ['Hulk', 'Captain America', 'Thanos']
    wiseacre_hero = get_intelligence(api_url, heroes_list)
    