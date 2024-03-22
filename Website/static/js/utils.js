const currentPage ="{{ isactive }}";
const navbar = document.querySelector('.navbar');
const navLinks = document.querySelectorAll('.nav-link');
        
function handleScroll() {
    const top = document.documentElement.scrollTop;
    if(top > 20){
        navbar.classList.add('scroll-Nav')
        navLinks.forEach(link => {
            link.classList.add('scroll-Nav-Link')
        })
    }else{
        navbar.classList.remove('scroll-Nav')
        navLinks.forEach(link => {
            link.classList.remove('scroll-Nav-Link')
        })
    }
}

window.addEventListener('scroll', handleScroll);


document.addEventListener("DOMContentLoaded", function() {
    feather.replace();
  });

document.addEventListener("DOMContentLoaded", function() {
    initAccordion();
});


document.addEventListener("DOMContentLoaded", function() {
    initMap();
});


function initAccordion(){
    var acc = document.getElementsByClassName("accordion");
    var i;

    for (i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var panel = this.nextElementSibling;
            if(panel.style.maxHeight){
                panel.style.maxHeight = null;
            } else{
                panel.style.maxHeight = panel.scrollHeight + "px";
            }
        });
    }
}


function initMap() {
    //Access latitude and longitude values from the HTML element's data attributes
    let mapElement = document.getElementById('map');
    let latitude = parseFloat(mapElement.getAttribute('latitude'));
    let longitude = parseFloat(mapElement.getAttribute('longitude'));
    
    //Create the location object
    let location = {lat: latitude, lng: longitude };
    
    //Create the map and marker
    let map = new google.maps.Map(
        document.getElementById('map'), {zoom: 17, center: location}
    );

    let marker = new google.maps.Marker({position: location, map: map});
}










                
  