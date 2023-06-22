document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('points-form').addEventListener('submit', function (event) {
        if (!validatePoints()) {
            event.preventDefault();
        }
    });
});


function filterByLatitude(element) {
    var name = element.getAttribute('name');
    var regex = /^latitude-(\d+)$/;
    return regex.test(name);
}


function filterByLongitude(element) {
    var name = element.getAttribute('name');
    var regex = /^longitude-(\d+)$/;
    return regex.test(name);
}


function validatePoints() {
    var lat = Array.from(document.querySelectorAll("[name]")).filter(filterByLatitude);
    var lon = Array.from(document.querySelectorAll("[name]")).filter(filterByLongitude);
    var valid = true;

    lat.forEach(function (element) {
        if (element.value < -90 || element.value > 90 || element.value == "") {
            element.classList.add("invalid");
            element.nextElementSibling.textContent = "The value must be between -90 and 90";
            valid = false;
            return valid;
        }
        else {
            element.classList.remove("valid");
            element.nextElementSibling.textContent = "";
        }
    });

    lon.forEach(function (element) {
        if (element.value < -180 || element.value > 180 || element.value == "") {
            element.classList.add("invalid");
            element.nextElementSibling.textContent = "The value must be between -180 and 180";
            valid = false;
            return valid;
        }
        else {
            element.classList.remove("valid");
            element.nextElementSibling.textContent = "";
        }
    });

    return valid;
}