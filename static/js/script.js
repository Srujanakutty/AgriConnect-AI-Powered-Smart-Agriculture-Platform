function showContact(id) {
    var contact = document.getElementById("contact-" + id);

    if (contact.style.display === "none") {
        contact.style.display = "block";
    } else {
        contact.style.display = "none";
    }
}

function getLocation() {
    navigator.geolocation.getCurrentPosition(showPosition);
}

function showPosition(position) {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;

    window.location.href = "/weather_location?lat=" + lat + "&lon=" + lon;
}
