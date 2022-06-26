function requestButtonClicked(numberOfPoints) {
    let pointsString = new String()

    for (let i = 1; i <= numberOfPoints; i++) {
        let currentPoint = document.getElementById(`point${i}`)
        let latitude = currentPoint.querySelector('#id_pointLatitude').value
        let longitude = currentPoint.querySelector('#id_pointLongitude').value
        pointsString += latitude + ',' + longitude + '_'
    }

    pointsString = pointsString.slice(0, -1)
    location.replace(`/temp1/${pointsString}`)
}