window.onload = getLatLong

// Step 1 IPIFY
function getLatLong(){
  const IPIFYURL = 'https://geo.ipify.org/api/v1?apiKey=' + IPGEOLOCATION_API

  fetch(IPIFYURL)
  .then(function(data){
    data.json()
    .then(function(ipData){
      lat = ipData.location.lat
      long = ipData.location.lng
      getWeather(lat, long)
    })
  })
}

// Step 2 OpenWeatherMap API
function getWeather(lat, long){
  const weatherAPI = `https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${long}&appid=${OPEN_WEATHER_API}&units=imperial&exclude=minutely,hourly,alerts`

  fetch(weatherAPI)
  .then(function(data){
    data.json()
    .then(weatherData => {
      console.log(weatherData)

      const feelsLike = weatherData.current.feels_like
      const humidity = weatherData.current.humidity
      const temp = weatherData.current.temp
      const sunrise = weatherData.current.sunrise
      const sunset = weatherData.current.sunset
      const description = weatherData.current.weather[0].description
      const icon = weatherData.current.weather[0].icon

      displayCurrentWeather(feelsLike,humidity,temp,sunrise,sunset,description,icon)
    })
  })
}

// Display Current Weather Data
function displayCurrentWeather(feelsLike,humidity,temp,sunrise,sunset,description,icon){
  const $ = (arg) => document.getElementById(arg)
  const weatherIcon = `http://openweathermap.org/img/wn/${icon}.png`

  const currentTemp = $('current-temp')
  currentTemp.innerHTML = temp + ' &deg;F'

  const currentFeels = $('current-feels')
  currentFeels.textContent = 'Feels like: ' + feelsLike

  const currentHumidity = $('current-humidity')
  currentHumidity.textContent = 'Humidity: ' + humidity + '%'

  const currentSunrise = $('current-sunrise')
  currentSunrise.textContent = new Date(sunrise * 1000)

  const currentSunset = $('current-sunset')
  currentSunset.textContent = new Date(sunset * 1000)

  const currentDescription = $('current-description')
  currentDescription.textContent = description

  const currentImage = $('current-image')
  currentImage.src = weatherIcon
  currentImage.alt = description
}