document.addEventListener('DOMContentLoaded', () => {

    let currentLocation = window.location;
    const deleteButton = document.getElementById('delBut');
    const reflectionArea = document.getElementById('refBox');



    reflectionArea.addEventListener('focus', () => reflectionArea.select() );

    reflectionArea.addEventListener('blur', () => {
             checkReflection();
    });

    reflectionArea.addEventListener('keypress', function(e) {
                  if (event.key === "Enter") {
                        event.preventDefault();
                        checkReflection();
                   }});


    function checkReflection() {
          if (reflectionArea.textContent.length > 4) {
              saveReflection(reflectionArea.textContent);
              reflectionArea.style.visibility = hidden;
              location.reload();
    }
    };


    function saveReflection(valueToSave) {
        $.ajax({
            url: currentLocation,
            data : {
            content : valueToSave
          },
            type: 'POST',
            success: function () {
            }
        });

    }


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
            textarea.maxLength = "350";
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