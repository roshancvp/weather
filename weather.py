import requests

#r = requests.get(create_url("San Francisco"))
#print (r.status_code)
def main():
    city = input("Enter a city: ")
    r = requests.get(create_url(city))
    data = r.json()
    print("Sending request: " + create_url(city))
    print("Status Code: " + str(r.status_code))
    print("Weather in " + data["name"] + ": " + data["weather"][0]["description"])

def create_url(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q="
    key = "2c03335f9552691480c68fd9bc03d907"
    return url + city + "&appid=" + key

if __name__=="__main__":
    main()
