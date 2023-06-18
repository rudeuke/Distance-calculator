var numberOfPoints = 0;

function addPoint() {
    numberOfPoints++;

    var mainContainer = document.createElement("div");
    mainContainer.classList.add("container", "py-1", "my-1", "border", "rounded");

    var h5 = document.createElement("h5");
    h5.textContent = "Point " + numberOfPoints + ":";
    mainContainer.appendChild(h5);

    var divRow = document.createElement("div");
    divRow.classList.add("row");
    mainContainer.appendChild(divRow);

    var labelLatitude = document.createElement("label");
    labelLatitude.setAttribute("for", "latitude-" + numberOfPoints);
    labelLatitude.classList.add("col-1", "offset-2", "col-form-label");
    labelLatitude.textContent = "Latitude:";
    divRow.appendChild(labelLatitude);

    var divLatitude = document.createElement("div");
    divLatitude.classList.add("col-2", "noArrows");
    divRow.appendChild(divLatitude);

    var inputLatitude = document.createElement("input");
    inputLatitude.setAttribute("type", "number");
    inputLatitude.setAttribute("name", "latitude-" + numberOfPoints);
    inputLatitude.setAttribute("value", "0.0");
    inputLatitude.setAttribute("min", "-90");
    inputLatitude.setAttribute("max", "90");
    inputLatitude.setAttribute("step", ".0000001");
    inputLatitude.classList.add("form-control");
    inputLatitude.setAttribute("required", "");
    divLatitude.appendChild(inputLatitude);

    var spanLatitude = document.createElement("span");
    spanLatitude.classList.add("error-message", "text-danger");
    divLatitude.appendChild(spanLatitude);

    var labelLongitude = document.createElement("label");
    labelLongitude.setAttribute("for", "longitude-" + numberOfPoints);
    labelLongitude.classList.add("col-1", "offset-2", "col-form-label");
    labelLongitude.textContent = "Longitude:";
    divRow.appendChild(labelLongitude);

    var divLongitude = document.createElement("div");
    divLongitude.classList.add("col-2", "noArrows");
    divRow.appendChild(divLongitude);

    var inputLongitude = document.createElement("input");
    inputLongitude.setAttribute("type", "number");
    inputLongitude.setAttribute("name", "longitude-" + numberOfPoints);
    inputLongitude.setAttribute("value", "0.0");
    inputLongitude.setAttribute("min", "-180");
    inputLongitude.setAttribute("max", "180");
    inputLongitude.setAttribute("step", ".0000001");
    inputLongitude.classList.add("form-control");
    inputLongitude.setAttribute("required", "");
    divLongitude.appendChild(inputLongitude);

    var spanLongitude = document.createElement("span");
    spanLongitude.classList.add("error-message", "text-danger");
    divLongitude.appendChild(spanLongitude);

    var divButton = document.createElement("div");
    divButton.classList.add("col-1", "offset-1");
    divRow.appendChild(divButton);

    var removeButton = document.createElement("button");
    removeButton.textContent = "-";
    removeButton.classList.add("btn", "btn-danger", "btn-block");
    removeButton.setAttribute("type", "button");
    removeButton.setAttribute("id", "delete-button-" + numberOfPoints);
    removeButton.addEventListener("click", removePoint);
    divButton.appendChild(removeButton);

    var pointsContainer = document.getElementById("points");
    pointsContainer.appendChild(mainContainer);

    updateButtons()
}

function removePoint(event) {
    var button = event.target;
    var container = button.closest(".container");
    var number = container.querySelector("input").getAttribute("name").match(/\d+/)[0];

    container.remove();
    updateElementNumbers(number - 1);
    numberOfPoints--;

    updateButtons();
}

function updateElementNumbers(startingNumber = 0) {
    var elements = document.querySelectorAll(".container");
    for (var i = startingNumber; i < elements.length; i++) {
        var h5 = elements[i].querySelector("h5");
        if (h5) {
            h5.textContent = "Point " + (i) + ":";
            updateElement(elements[i]);
        }
    }
}

function updateElement(element) {
    var counterElement = element.querySelector("h5");
    var labelLatitude = element.querySelector("label[for^='latitude']");
    var labelLongitude = element.querySelector("label[for^='longitude']");
    var inputLatitude = element.querySelector("input[name^='latitude']");
    var inputLongitude = element.querySelector("input[name^='longitude']");

    var counter = parseInt(counterElement.textContent.match(/\d+/)[0]);
    var updatedCounter = counter + 1;
    counterElement.textContent = counterElement.textContent.replace(/\d+/, updatedCounter);

    var newLatitudeName = "latitude" + updatedCounter;
    var newLongitudeName = "longitude" + updatedCounter;
    inputLatitude.setAttribute("name", newLatitudeName);
    inputLongitude.setAttribute("name", newLongitudeName);
    labelLatitude.setAttribute("for", newLatitudeName);
    labelLongitude.setAttribute("for", newLongitudeName);
}

function updateButtons() {
    var addButton = document.getElementById("add-button");
    var deleteButtons = document.querySelectorAll("[id^='delete-button-']");

    if (numberOfPoints >= 50) {
        addButton.disabled = true;
    }
    else {
        addButton.disabled = false;
    }

    if (numberOfPoints <= 2) {
        for (var i = 0; i < deleteButtons.length; i++) {
            deleteButtons[i].disabled = true;
        }
    }
    else {
        for (var i = 0; i < deleteButtons.length; i++) {
            deleteButtons[i].disabled = false;
        }
    }
}

document.addEventListener("DOMContentLoaded", function () {
    addPoint();
    addPoint();
});