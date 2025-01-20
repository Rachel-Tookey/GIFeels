document.addEventListener('DOMContentLoaded', () => {

    let currentLocation = window.location;
    const deleteButton = document.getElementById('delBut');

    deleteButton.addEventListener('click', () => {
        let result = confirm("Delete this record? This cannot be undone.");
        if (result === true) {
                sendRequest();
                }
            }

     );

    function sendRequest() {
            $.ajax({
            url: currentLocation,
            type: 'DELETE',
            success: function (result) {
                window.location.href = "/overview";
            }
        });
    };

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


    const diaryBox = document.getElementById('diaryText');
    const editText = document.getElementById('edit');

    editText.addEventListener('click', () => textBox() );

     function resizeInput(container) {
                container.style.height = 'auto';
                container.style.height = `${container.scrollHeight}px`;
     }

    function textBox() {

            const textarea = document.createElement("textarea");

            textarea.type = "text";
            textarea.value = diaryBox.textContent;
            textarea.className = "diary-input";
            textarea.style.wrap = "soft";
            textarea.maxlength = "350";
            textarea.textContent = diaryBox.textContent;
            diaryBox.textContent = '';
            diaryBox.appendChild(textarea);

            resizeInput(textarea);

            function updateValue() {
                    const updatedValue = textarea.value;
                    if (diaryBox.textContent != textarea.value) {
                            diaryBox.textContent = updatedValue;
                            saveJournal(updatedValue);
                    }
                    diaryBox.textContent = updatedValue;
            }

            textarea.addEventListener('focus', () => textarea.select() )

            textarea.addEventListener('input', () => resizeInput(textarea));

            textarea.addEventListener('blur', () => updateValue());

            textarea.addEventListener('keypress', function(e) {
                  if (event.key === "Enter") {
                        event.preventDefault();
                        updateValue();
            }});

            textarea.focus();
        }

});