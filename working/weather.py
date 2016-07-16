import requests

#r = requests.get(create_url("San Francisco"))
#print (r.status_code)



def main():
    forecast = Forecast("Austin")
    print(forecast.one_max)

# creates a request URL
def create_url(city, type, param):
    base = "http://api.openweathermap.org/data/2.5/" + type + "?q="
    key = "2c03335f9552691480c68fd9bc03d907"
    return base + city + param + "&appid=" + key

# current weather
class Weather(object):

    def __init__(self, city):

        # Request
        self.r = requests.get(create_url(city, "weather", ""))
        self.data = self.r.json()

        # Response
        self.desc_main = self.data["weather"][0]["main"]
        self.temp = self.data["main"]["temp"]
        self.temp_min = self.data["main"]["temp_min"]
        self.temp_max = self.data["main"]["temp_max"]
        self.humidity = self.data["main"]["humidity"]
        self.city_name = self.data["name"] + ", " + self.data["sys"]["country"]

# 7 day weather forecast
class Forecast(object):

    def __init__(self, city):
        # Request
        self.r = requests.get(create_url(city, "forecast/daily", "&mode=json&units=metric&cnt=7"))
        self.data = self.r.json()

        #Response
        self.one_max = self.data["list"][0]["temp"]["max"]
        self.one_min = self.data["list"][0]["temp"]["min"]
        self.one_humidity = self.data["list"][0]["humidity"]

        self.two_max = self.data["list"][1]["temp"]["max"]
        self.two_min = self.data["list"][1]["temp"]["min"]
        self.two_humidity = self.data["list"][1]["humidity"]

        self.three_max = self.data["list"][2]["temp"]["max"]
        self.three_min = self.data["list"][2]["temp"]["min"]
        self.three_humidity = self.data["list"][2]["humidity"]

        self.four_max = self.data["list"][3]["temp"]["max"]
        self.four_min = self.data["list"][3]["temp"]["min"]
        self.four_humidity = self.data["list"][3]["humidity"]

        self.five_max = self.data["list"][4]["temp"]["max"]
        self.five_min = self.data["list"][4]["temp"]["min"]
        self.five_humidity = self.data["list"][4]["humidity"]

        self.six_max = self.data["list"][5]["temp"]["max"]
        self.six_min = self.data["list"][5]["temp"]["min"]
        self.six_humidity = self.data["list"][5]["humidity"]

        self.seven_max = self.data["list"][6]["temp"]["max"]
        self.seven_min = self.data["list"][6]["temp"]["min"]
        self.seven_humidity = self.data["list"][6]["humidity"]


if __name__=="__main__":
    main()
