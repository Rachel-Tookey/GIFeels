document.addEventListener('DOMContentLoaded', () => {

    const daysContainer = document.getElementById('days');
    const monthYearDisplay = document.getElementById('monthYear');
    const prevMonthButton = document.getElementById('prevMonth');
    const nextMonthButton = document.getElementById('nextMonth');
    const statsTitle = document.querySelector('.overview p');
    const colors = {"happy": "#FFEEA8","calm": "#D5E386","sad": "#D9E8F5","worried": "#D9D9D9","frustrated": "#F2BDC7","angry": "#ff9c78"};

    let currentDate = new Date();
    let monthlyData = [];
    let activeDates = [];


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
            activeDates = data.dates;
            renderMonthlyGraph(monthlyData);
            renderCalendar();
            });
        e.preventDefault();
        });
    };

    renderGraph();

    function clearContainer(container) {
        while(container.firstChild) {
                container.removeChild(container.firstChild);
            };
    };

    function mouseOnCal(container, color) {
             const bar = document.getElementById(color);
             container.style.backgroundColor = color;
             const anotherGif = container.querySelector("img");
             anotherGif.style.maxWidth = '200px';
             anotherGif.style.display = "block";
             anotherGif.style.position = "absolute";
             document.body.style.backgroundColor = color;
             container.style.boxShadow = '0 0 10px #7c6cac';
             bar.style.boxShadow = '0 0 10px #7c6cac';
     };


    function mouseOffCal(container, color) {
            const bar = document.getElementById(color);
            container.style.backgroundColor = '#FFFFFF';
            document.body.style.backgroundColor = '';
            const anotherGif = container.querySelector("img");
            anotherGif.style.display = "none";
            bar.style.boxShadow = '0 0 0px';
            container.style.boxShadow = '0 0 0px';
    };



    function renderCalendar() {

        const year = currentDate.getFullYear();
        const month = currentDate.getMonth();
        const firstDayOfMonth = new Date(year, month, 1).getDay();
        const daysInMonth = new Date(year, month + 1, 0).getDate();
        const monthAndYear = currentDate.toLocaleDateString('en-US', { month: 'long', year: 'numeric' });


        // Set the month and year in the header
        monthYearDisplay.textContent = monthAndYear;
        statsTitle.textContent = "Your moods for " + monthAndYear;

        // Clear the previous days
        clearContainer(daysContainer);

        // Add empty divs for the days of the week before the start of the month
        for (let i = 0; i < firstDayOfMonth; i++) {
            const emptyDiv = document.createElement('div');
            emptyDiv.classList.add('empty');
            daysContainer.appendChild(emptyDiv);
        }

        // Add the actual days of the month
        for (let day = 1; day <= daysInMonth; day++) {

            const dayDiv = document.createElement('div');
            let date = String(year) + String(month + 1).padStart(2, '0') + String(day).padStart(2, '0');

            // check if there is an entry for that date
            if (date in activeDates) {

                    dayDiv.className = activeDates[date]['color'];

                    // hyperlink it to the archive page:
                    const link = document.createElement('a');
                    link.textContent = day;
                    link.color = '#ffffff';
                    link.href = `/archive/${year}-${String(month + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
                    dayDiv.appendChild(link);

                    // create the gif display on hover
                    const gif = document.createElement('img');
                    gif.src = activeDates[date]['url'];
                    gif.style.display = "none";
                    dayDiv.appendChild(gif);

                    // day div styling:
                    dayDiv.style.backgroundColor = '#FFFFFF';
                    dayDiv.style.border = '1px dotted #574000';

                    dayDiv.addEventListener('mouseenter', function() {
                        mouseOnCal(dayDiv, activeDates[date]['color']);
                    });

                    dayDiv.addEventListener('mouseleave', function() {
                        mouseOffCal(dayDiv, activeDates[date]['color']);
                    });
            } else {
                    const link = document.createElement('p');
                    link.textContent = day;
                    dayDiv.style.backgroundColor =  '#f2f2f2';
                    link.style.color = '#c2c2c2';
                    dayDiv.appendChild(link);
            }
            daysContainer.appendChild(dayDiv);
        }
    };

    renderCalendar();

    function changeMonth(delta) {
        currentDate.setMonth(currentDate.getMonth() + delta);
        renderGraph();
    }

    prevMonthButton.addEventListener('click', () => changeMonth(-1));
    nextMonthButton.addEventListener('click', () => changeMonth(1));


    function hoverOnBar(bar, colorCode) {
         const collection = document.getElementsByClassName(colorCode);
         bar.style.boxShadow = '0 0 10px #7c6cac';
         document.body.style.backgroundColor = colorCode;

         [...collection].forEach(function(d) {
            d.style.backgroundColor = colorCode;
            d.style.backgroundColor = '0 0 10px #7c6cac';
            const child = d.querySelector('img');
            child.style.maxWidth = '50px';
            child.style.display = "block";
            child.style.position = "absolute";
         })
         };

    function hoverOffBar(bar, colorCode) {

         document.body.style.backgroundColor = '';
         bar.style.boxShadow = '0 0 0px';
         const collection = document.getElementsByClassName(colorCode);

         [...collection].forEach(function(d) {
            d.style.backgroundColor = '#FFFFFF';
            d.style.boxShadow = '0 0 0px';
            const child = d.querySelector('img');
            child.style.display = "none";

    })};


   function getUnitSize(data) {
       let MaxVal = 0;
       data.forEach(emotion => {
            if (MaxVal < emotion.value) {
                MaxVal = emotion.value;
            }
         });
       const unit = 250 / MaxVal;
       return unit;
   }

   function renderMonthlyGraph(monthlyData) {

        const barsContainer = document.getElementById('bars');

        clearContainer(barsContainer);

        const unitSize = getUnitSize(monthlyData);

        monthlyData.forEach(emotion => {
            const bar = document.createElement('div');
            bar.className = 'bar';
            bar.style.height = `${emotion.value * unitSize}px`;
            bar.style.backgroundColor = colors[emotion.name];
            bar.id = colors[emotion.name];

            bar.addEventListener('mouseenter', function() { hoverOnBar(bar, colors[emotion.name]) });
            bar.addEventListener('mouseleave', function() { hoverOffBar(bar, colors[emotion.name])});

            const barValue = document.createElement('div');
            barValue.className = 'bar-value';
            barValue.innerText = emotion.value;

            bar.appendChild(barValue);
            barsContainer.appendChild(bar);
        });
    }


    });
