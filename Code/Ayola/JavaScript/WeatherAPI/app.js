console.log("It worked")





// 1. IPIFY
const IPIFYURL = "https://geo.ipify.org/api/v1?apiKey=" + IPGEOLOCATION_API
fetch(IPIFYURL)
.then(function(data){
    (data.json())
    .then(function(ipData){
        lat = ipData.location.lat
        lon = ipData.location.lng
        getWeather(lat, lon)
    })
})

// 3. OpenWeatherMap API
function getWeather(lat, lon){
const weatherApi = `https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${lon}&appid=${OPEN_WEATHER_API}`

fetch(weatherApi)
.then(function(data){
    data.json()
    .then(function(weatherData)
})
}


