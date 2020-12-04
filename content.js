function toggleClass(){
    const body = document.querySelector('body');
    body.classList.toggle('light');
}

document.addEventListener('DOMContentLoaded', function() {
    var link = document.getElementById('toggleClass');
    link.addEventListener('click', toggleClass);
});

const deg = 6;
const hr = document.querySelector('#hr');
const mn = document.querySelector('#mn');
const sc = document.querySelector('#sc');

setInterval(() => {

    let day = new Date();
    let hh = day.getHours() * 30;
    let mm = day.getMinutes() * deg;
    let ss = day.getSeconds() * deg;

    hr.style.transform = `rotateZ(${hh+mm/12}deg)`;
    mn.style.transform = `rotateZ(${mm + 180}deg)`;
    sc.style.transform = `rotateZ(${ss + 180}deg)`;

})
