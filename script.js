function getWeather() {
    var city = document.getElementById("cityInput").value;
    var apiKey = 'YOUR_API_KEY_HERE';
    var url = `http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.cod == 200) {
                var weatherInfo = document.getElementById("weatherInfo");
                weatherInfo.innerHTML = `
                    <h2>Weather in ${city}</h2>
                    <p>Description: ${data.weather[0].description}</p>
                    <p>Temperature: ${data.main.temp}°C</p>
                    <p>Humidity: ${data.main.humidity}%</p>
                    <p>Wind Speed: ${data.wind.speed} m/s</p>
                `;
            } else {
                alert("City not found or error in retrieving data.");
            }
        })
        .catch(error => console.log('Error:', error));
}
