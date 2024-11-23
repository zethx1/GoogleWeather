from bs4 import BeautifulSoup
import requests 


def weather_check(city):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    res = requests.get(
        f'https://www.google.com/search?q={city}+weather',
        headers=headers
    )

    soup = BeautifulSoup(res.text, 'html.parser')


    try:
            time = soup.select('#wob_dts')[0].getText().strip()
            precipitation = soup.select('#wob_dc')[0].getText().strip()  
            weather = soup.select('#wob_tm')[0].getText().strip()
    except IndexError:  
        print("Не удалось найти данные по погоде.")
        return
    
    print(f'''День недели и время: {time}
Погода: {precipitation}
Температура: {weather}°С''')


if __name__ == '__main__':
    city_input = input('Введи город: ')
    weather_check(f'{city_input} погода')
