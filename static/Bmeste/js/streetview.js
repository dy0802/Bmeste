function set_streetview(details_location){
    const map = new google.maps.StreetViewPanorama(document.getElementById("map"), {
      position: details_location[0],
      pov: { heading: 165, pitch: 0 },
      zoom: 1,
    });
}

export {set_streetview};