import requests

#r = requests.get(create_url("San Francisco"))
#print (r.status_code)



def main():
    weather = Weather("Austin")
    print(weather.humidity)

# creates a request URL
def create_url(city, type):
    base = "http://api.openweathermap.org/data/2.5/" + type + "?q="
    key = "2c03335f9552691480c68fd9bc03d907"
    return base + city + "&appid=" + key

class Weather(object):

    def __init__(self, city):

        # Request
        self.r = requests.get(create_url(city, "weather"))
        self.data = self.r.json()

        # Response
        self.desc_main = self.data["weather"][0]["main"]
        self.temp = self.data["main"]["temp"]
        self.temp_min = self.data["main"]["temp_min"]
        self.temp_max = self.data["main"]["temp_max"]
        self.humidity = self.data["main"]["humidity"]
        self.city_name = self.data["name"] + ", " + self.data["sys"]["country"]


class Forecast(object):

    def __init__(self, city):
        # Request
        self.r = requests.get(create_url(city, "weather"))
        self.data = self.r.json()

        #Response
        


if __name__=="__main__":
    main()
