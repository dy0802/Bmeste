function set_streetview(details_location, details_pov){
    const map = new google.maps.StreetViewPanorama(document.getElementById("map"), {
      position: details_location[0],
      pov: details_pov,
      zoom: 1,
    });
    console.log(details_pov);
}

export {set_streetview};