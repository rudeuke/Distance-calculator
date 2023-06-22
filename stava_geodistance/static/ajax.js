$(document).ready(function () {
    $('#points-form').submit(function (event) {
        event.preventDefault();
        var formData = $(this).serialize();

        $.ajax({
            type: 'POST',
            url: `${document.location.origin}`,
            data: formData,

            success: function (response) {
                console.log(formData);
                console.log(response);
                $('#total-distance').text(response.total_distance);
                $('#calculation-time').text(response.calculation_time);
            },

            error: function () {
                alert("Error contacting API");
            },
        });
    });
});