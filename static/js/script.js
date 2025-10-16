const yearlyCalendar = document.getElementById('yearlyCalendar');
const yearDisplay = document.getElementById('year');
const prevYearBtn = document.getElementById('prevYear');
const nextYearBtn = document.getElementById('nextYear');

const festivalModal = document.getElementById('festivalModal');
const festName = document.getElementById('festName');
const festDesc = document.getElementById('festDesc');
const closeModal = document.getElementById('closeModal');

const now = new Date();
let currentYear = now.getFullYear();
let festivals = [];

// Load festivals from JSON
fetch('/json/festivals.json')
  .then(res => res.json())
  .then(data => {
    festivals = data;
    generateCalendar(currentYear);
  })
  .catch(err => {
    console.error('Failed to load festival data:', err);
    generateCalendar(currentYear);
  });

// Generate calendar for the year
function generateCalendar(year) {
  yearlyCalendar.innerHTML = '';
  yearDisplay.textContent = year;
  const monthNames = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
  ];
  for (let m = 0; m < 12; m++) {
    const monthDiv = document.createElement('div');
    monthDiv.className = "month";

    const monthName = document.createElement('div');
    monthName.className = "month-name";
    monthName.textContent = monthNames[m];
    monthDiv.appendChild(monthName);

    const daysRow = document.createElement('div');
    daysRow.className = "days";
    ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"].forEach(day => {
      const dayCell = document.createElement('div');
      dayCell.textContent = day;
      daysRow.appendChild(dayCell);
    });
    monthDiv.appendChild(daysRow);

    const datesGrid = document.createElement('div');
    datesGrid.className = "dates";
    const firstDay = new Date(year, m, 1).getDay();
    const daysInMonth = new Date(year, m + 1, 0).getDate();

    // Empty cells before first day
    for (let i = 0; i < firstDay; i++) {
      const emptyCell = document.createElement('div');
      datesGrid.appendChild(emptyCell);
    }
    // Date cells
    for (let d = 1; d <= daysInMonth; d++) {
      const dateCell = document.createElement('div');
      dateCell.className = "date";
      dateCell.textContent = d;

      const fullDate = `${year}-${String(m + 1).padStart(2,'0')}-${String(d).padStart(2,'0')}`;
      // Check if today
      const isToday =
        d === now.getDate() &&
        m === now.getMonth() &&
        year === now.getFullYear();
      if (isToday) dateCell.classList.add('today');

      // Check for festival
      const festival = festivals.find(f => f.date === fullDate);
      if (festival) {
        const festBtn = document.createElement('button');
        festBtn.className = 'festival-btn';
        festBtn.textContent = '🎉';
        festBtn.title = festival.name;
        festBtn.onclick = () => showFestivalPopup(festival);
        dateCell.appendChild(festBtn);
      }

      datesGrid.appendChild(dateCell);
    }
    monthDiv.appendChild(datesGrid);
    yearlyCalendar.appendChild(monthDiv);
  }
}

function showFestivalPopup(festival) {
  festName.textContent = festival.name;
  festDesc.textContent = festival.description;
  festivalModal.style.display = 'block';
}
closeModal.onclick = () => {
  festivalModal.style.display = 'none';
};
window.onclick = (event) => {
  if(event.target === festivalModal) {
    festivalModal.style.display = 'none';
  }
};

prevYearBtn.onclick = () => {
  currentYear--;
  generateCalendar(currentYear);
};
nextYearBtn.onclick = () => {
  currentYear++;
  generateCalendar(currentYear);
};