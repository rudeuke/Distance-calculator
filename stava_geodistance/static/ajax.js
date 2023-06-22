$(document).ready(function () {
    $('#points-form').submit(function (event) {
        event.preventDefault();
        var formData = $(this).serialize();

        document.querySelector('#submit-button').innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>';
        document.querySelector('#submit-button').disabled = true;

        $.ajax({
            type: 'POST',
            url: `${document.location.origin}`,
            data: formData,
            
        }).done(function (response) {
            console.log(response);
            $('#results').addClass("bg-light border border-secondary rounded");
            $('#total-distance').text("Total distance: " + response.total_distance + " km");
            $('#calculation-time').text("Calculation time: " + response.calculation_time + " s");

        }).fail(function () {
            alert("Error contacting API");

        }).always(function () {
            document.querySelector('#submit-button').innerHTML = '<span><h5>Calculate distance</h5></span>';
            document.querySelector('#submit-button').disabled = false;
        });
    });
});