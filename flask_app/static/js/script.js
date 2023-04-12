// ===== LOGIN/REGISTER =====
const form = document.getElementById("form");
const btn = document.getElementById("btn");
const cart = document.getElementById("cart")

function loginField() {
  form.style.left = "-340px";
  btn.style.left = "127px"
  
}

function registerField() {
  form.style.left = "100px";
  btn.style.left = "18px"
}

// ===== MAP API =====
let map; 
let infowindow; 
let service;

function initMap() {
  // DEFAULT MAP VIEW
  infowindow = new google.maps.InfoWindow();
  map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: 33.75, lng: -84.39}, 
    zoom: 7});

  // AUTOCOMPLETE SEARCH FIELD
  let input = document.getElementById('searchTextField');
  let autocomplete = new google.maps.places.Autocomplete(input)

  autocomplete.bindTo('bounds', map)

  // ADD MAP MARKER
  let marker = new google.maps.Marker({
      map: map
  })

  google.maps.event.addListener(autocomplete, 'place_changed', () => {
      let place = autocomplete.getPlace()

      if (place.geometry.viewport) {
          map.fitBounds(place.geometry.viewport)
      } else {
          map.setCenter(place.geometry.location)
          map.setZoom(17)
      }
      marker.setPosition(place.geometry.location)
      marker.setVisible(true)

      service = new google.maps.places.PlacesService(map)
  })

}

window.initMap = initMap;