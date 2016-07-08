$(document).ready(function() {
    
    // getting user input
    var city;
    var country;
    
    $('#go').click(function() {
        city = $('#city').val();
        country = $('#country').val();
    
        // making the request
        var url = "http://api.openweathermap.org/data/2.5/weather?q="
        var key = "2c03335f9552691480c68fd9bc03d907";

        var request = new XMLHttpRequest();
        request.open("GET", 
                     url + 
                     city + 
                     "," + country + 
                     "&appid=" + 
                     key, false);
        request.send();

        // parsing json data
        var json = JSON.parse(request.responseText);

        $('#weather-desc').text(
            json.weather[0].description);
        
    });
        
});