import requests


class FetchWeatherOpenweathermap:

    def __init__(self):

        #CONSTANTS
        self.api_url: str = 'https://api.openweathermap.org/data/2.5/weather'
        self.api_key: str = 'your api key' 

        #GET
        self.city: str = ""

        #PREPARE
        self.request_url: str = ""

    def main(self) ->bool:
        """Get <city> weather data from Openweather map 
        """
        if not self.get_weather_info():
            print("Error ........")
        else:
            return True
        return False

    def get_weather_info(self):
        self.prepare_request_url()
        response = requests.get(self.request_url)

        if response.status_code == 200:
            weather_data = response.json()
            weather = weather_data.get('weather', [])[0].get('description', '')
            temperature = round(weather_data.get("main", {}).get("temp") - 273.15, 2)
            print(f"Weather: {weather}")
            print(f"Temperature: {temperature} celsius")
            return True
        return False

    def prepare_request_url(self) -> bool:
        if not self.request_url:
            self.request_url = f"{self.api_url}?appid={self.api_key}&q={self.get_city_name()}"
        return True

    @staticmethod
    def get_city_name() -> str:
        """Get city name from user

        :return str: entered city name
        """
        city = input("Enter city name: ")
        return city


weather = FetchWeatherOpenweathermap()
weather.main()
