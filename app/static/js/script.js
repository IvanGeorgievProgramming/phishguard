'use strict';

/* Add event on multiple elements */

const addEventOnElement = function (elements, evetType, callback) {
    for (let i = 0, len = elements.length; i < len; i++) {
        elements[i].addEventListener(evetType, callback);
    }
}

/* Navbar toggle for mobile */

const navbar = document.querySelector("[data-navbar]");
const navToggleBtn = document.querySelector("[data-nav-toggle-btn]");
const overlay = document.querySelector("[data-overlay]");

const toggleNavbar = function () {
    navbar.classList.toggle("active");
    navToggleBtn.classList.toggle("active");
    overlay.classList.toggle("active");
    document.body.classList.toggle("nav-active");
}

addEventOnElement([navToggleBtn, overlay], "click", toggleNavbar);

/* Parallax effect */

const parallaxElements = document.querySelectorAll("[data-parallax]");

window.addEventListener("mousemove", event => {
  for (let i = 0, len = parallaxElements.length; i < len; i++) {

    const movementX = (event.clientX / window.innerWidth) * Number(parallaxElements[i].dataset.parallaxSpeed);
    const movementY = (event.clientY / window.innerHeight) * Number(parallaxElements[i].dataset.parallaxSpeed);

    parallaxElements[i].animate({
        transform: `translate(${movementX}px, ${movementY}px)`
    }, { duration: 500, fill: "forwards" });
  }
})

/* Alerts */

document.addEventListener('DOMContentLoaded', function() {
    updateAlertPositions(); 
});

function closeAlert(element) {
    var alertElement = element.closest('.alert');
    if (alertElement) {
        alertElement.style.opacity = '0'; 
        alertElement.addEventListener('transitionend', function handler(e) {
            if (e.propertyName === 'opacity') { 
                alertElement.removeEventListener('transitionend', handler); 
                alertElement.remove(); 
                updateAlertPositions(); 
            }
        });
    }
}

function updateAlertPositions() {
    const alerts = document.querySelectorAll('.flashes .alert');
    let currentTop = 10; 
    alerts.forEach(alert => {
        alert.style.top = `${currentTop}px`; 
        const alertHeight = alert.offsetHeight + 10; 
        currentTop += alertHeight;
    });
}

function closeAlertSpecific(button) {
    var alertElement = button.closest('.alert');
    if (alertElement) {
        alertElement.style.opacity = '0';
        alertElement.addEventListener('transitionend', function handler(e) {
            if (e.propertyName === 'opacity') {
                alertElement.removeEventListener('transitionend', handler);
                alertElement.remove();
                updateAlertPositions();
            }
        });
    }
}
