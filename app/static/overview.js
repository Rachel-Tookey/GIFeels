document.addEventListener('DOMContentLoaded', () => {

    const daysContainer = document.getElementById('days');
    const monthYearDisplay = document.getElementById('monthYear');
    const prevMonthButton = document.getElementById('prevMonth');
    const nextMonthButton = document.getElementById('nextMonth');
    const statsTitle = document.querySelector('.overview p');

    let currentDate = new Date();

    let monthlyData = [];

    function renderCalendar() {
        const year = currentDate.getFullYear();
        const month = currentDate.getMonth();

        // Get the first day of the month and the total number of days in the month
        const firstDayOfMonth = new Date(year, month, 1).getDay();
        const daysInMonth = new Date(year, month + 1, 0).getDate();

        // Set the month and year in the header
        const monthAndYear = currentDate.toLocaleDateString('en-US', { month: 'long', year: 'numeric' });
        monthYearDisplay.textContent = monthAndYear;
        statsTitle.textContent = "Your moods for " + monthAndYear;


        // Clear the previous days
        daysContainer.innerHTML = '';


        // Fill in the days of the month
        // Add empty divs for the days of the week before the start of the month
        for (let i = 0; i < firstDayOfMonth; i++) {
            const emptyDiv = document.createElement('div');
            emptyDiv.classList.add('empty');
            daysContainer.appendChild(emptyDiv);
        }

        // Add the actual days of the month
        for (let day = 1; day <= daysInMonth; day++) {
            const dayDiv = document.createElement('div');
            const link = document.createElement('a');
            link.textContent = day;
            link.href = `/archive/${year}-${String(month + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
            dayDiv.appendChild(link);
            daysContainer.appendChild(dayDiv);
        }



    }

    function changeMonth(delta) {
        currentDate.setMonth(currentDate.getMonth() + delta);
        renderCalendar();
        renderGraph(); // this is mine
    }

    prevMonthButton.addEventListener('click', () => changeMonth(-1));
    nextMonthButton.addEventListener('click', () => changeMonth(1));

    renderCalendar();

    renderGraph();

    function renderGraph() {
        $(document).ready(function(){
        $.ajax({
          data : {
            month : currentDate
          },
          type : 'POST',
          url : '/overview'})
        .done (function(data){
        monthlyData = data.output;
        renderMonthlyGraph(monthlyData)
            });
        e.preventDefault();
        });
    };


   function renderMonthlyGraph(monthlyData) {

       const colors = {
        "happy": "#FFEEA8",
        "calm": "#D5E386",
        "sad": "#D9E8F5",
        "worried": "#D9D9D9",
        "frustrated": "#F2BDC7",
        "angry": "#ff9c78"};


        const barsContainer = document.getElementById('bars');
        barsContainer.innerHTML = ''; // Clear any existing bars

        // Find the data for the current month
        const currentMonthData = monthlyData;

        constMaxVal = 0;

        currentMonthData.forEach(emotion => {
            if (constMaxVal < emotion.value) {
                constMaxVal = emotion.value;

            }

         });

        const unitSize = 250 / constMaxVal;


        // Render the graph for the current month
        currentMonthData.forEach(emotion => {
            const bar = document.createElement('div');
            bar.className = 'bar';
            bar.style.height = `${emotion.value * unitSize}px`; // Adjust height multiplier as needed

            const barValue = document.createElement('div');
            barValue.className = 'bar-value';
            barValue.innerText = emotion.value;
            bar.style.backgroundColor = colors[emotion.name];

            bar.appendChild(barValue);
            barsContainer.appendChild(bar);
        });
    }




    });
