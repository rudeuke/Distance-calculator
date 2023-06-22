$(document).ready(function () {
    $('#points-form').submit(function (event) {
        event.preventDefault();
        var formData = $(this).serialize();

        $.ajax({
            type: 'POST',
            url: `${document.location.origin}`,
            data: formData,

            success: function (response) {
                console.log(response);
                $('#results').addClass("bg-light border border-secondary rounded");
                $('#total-distance').text("Total distance: " + response.total_distance + " km");
                $('#calculation-time').text("Calculation time: " + response.calculation_time + " s");
            },

            error: function () {
                alert("Error contacting API");
            },
        });
    });
});