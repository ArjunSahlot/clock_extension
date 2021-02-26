function toggleClass(){
    const body = document.querySelector('body');
    body.classList.toggle('light');
}

document.addEventListener('DOMContentLoaded', function() {
    var link = document.getElementById('toggleClass');
    link.addEventListener('click', toggleClass);
});

const deg = 6;
const hour = document.querySelector('#hr');
const minute = document.querySelector('#mn');
const second = document.querySelector('#sc');

setInterval(() => {

    let day = new Date();
    let hr = day.getHours() * 30;
    let min = day.getMinutes() * deg;
    let sec = day.getSeconds() * deg;

    hour.style.transform = `rotateZ(${hr+min/12}deg)`;
    minute.style.transform = `rotateZ(${min + 180}deg)`;
    second.style.transform = `rotateZ(${sec + 180}deg)`;

})
