function requestButtonClicked(numberOfPoints) {
    let pointsString = new String()
    let validFlag = true

    for (let i = 1; i <= numberOfPoints; i++) {
        let currentPoint = document.getElementById(`point${i}`)
        let latitude = currentPoint.querySelector('#id_pointLatitude')
        let longitude = currentPoint.querySelector('#id_pointLongitude')

        // alert(`latitude ${i} valid: ${latitude.checkValidity()}`)
        // alert(`longitude ${i} valid: ${longitude.checkValidity()}`)

        if (latitude.checkValidity() && longitude.checkValidity()) {
            pointsString += latitude.value + ',' + longitude.value + '_'
        }
        else {
            validFlag = false
            break
        }
    }

    if (validFlag) {
        pointsString = pointsString.slice(0, -1)
        location.replace(`/temp1/${pointsString}`)
    }
    else {
        alert("Data not valid.")
    }
}