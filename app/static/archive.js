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



    const diaryBox = document.getElementById('diaryText');
    const editText = document.getElementById('edit');

    editText.addEventListener('click', () => textBox() );

    function textBox() {

            diaryBox.innerHTML =
            `<textarea type="text" value="${diaryBox.textContent}" class="diary-input" wrap="soft" maxlength="350">
            ${diaryBox.textContent}</textarea>`;

            const textarea = diaryBox.querySelector('textarea');



            function resizeInput() {
                textarea.style.height = 'auto';
                textarea.style.height = `${textarea.scrollHeight}px`;

            }

            resizeInput();

            textarea.addEventListener(`focus`, () => textarea.select() )

            textarea.addEventListener('input', resizeInput);

            textarea.addEventListener('blur', () => {
                    const updatedValue = textarea.value;
                    if (diaryBox.textContent != textarea.value) {
                            diaryBox.textContent = updatedValue;
                            saveJournal(updatedValue);
                    }
                    diaryBox.textContent = updatedValue;
                });

            textarea.focus();

        }

        function saveJournal(valueToSave) {
        $(document).ready(function(){
        $.ajax({
          data : {
            content : valueToSave
          },
          type : 'PUT',
          url : currentLocation})
        .done ();
        e.preventDefault();
        });
    };



});