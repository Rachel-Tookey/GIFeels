document.addEventListener('DOMContentLoaded', () => {

    let currentLocation = window.location;

    const deleteButton = document.getElementById('delBut');

    deleteButton.addEventListener('click', () => sendRequest() );

    function sendRequest() {
            $.ajax({
            url: currentLocation,
            type: 'DELETE',
            success: function (result) {
                window.location.href = "url_for(show_overview)";
            }
        });
    };


});