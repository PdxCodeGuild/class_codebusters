- Use the [OpenWeatherMap API](https://openweathermap.org/api/one-call-api) to get weather data for a given location
  - API_KEY will be given
- OpenWeatherMap API requires the latitude and longitude to get weather at a given location
- There are two APIs that will allow us to get the lat/long of the user.
  - [IPIFY](https://www.ipify.org) to get the users ip address
  - [IPStack](https://ipstack.com/documentation) to turn an ip address into a lat/long
- Once we have the lat/long we can make a request to OpenWeatherMap API to get the current weather
- OpenWeatherMap API also provides icons for each weather forecast
  - `{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}`
- We can use the icon code inside an image src to get the relevant image.
  - `<img src="http://openweathermap.org/img/wn/04d.png"/>`