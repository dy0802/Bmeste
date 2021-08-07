const default_location_lat = JSON.parse(document.getElementById('default_location_lat').textContent);
const default_location_lng = JSON.parse(document.getElementById('default_location_lng').textContent);
const default_location_zoom = JSON.parse(document.getElementById('default_location_zoom').textContent);
const default_location = { lat: default_location_lat, lng: default_location_lng };
const piece_detail_set = document.querySelectorAll('#piece_detail');
const lat_set = document.querySelectorAll('#lat');
const lng_set = document.querySelectorAll('#lng');
const heading_set = document.querySelectorAll('#heading');
const pitch_set = document.querySelectorAll('#pitch');
const details_location = [];
const details_pov = [];

for(var i = 0; i < lat_set.length; i++ )
{
    details_location[i] = [{ lat: JSON.parse(lat_set[i].textContent), lng: JSON.parse(lng_set[i].textContent) },
                            JSON.parse(piece_detail_set[i].textContent)];
    let t = Number(parseFloat(JSON.parse(pitch_set[i].textContent) - 90));             
    details_pov[i] = { heading: JSON.parse(heading_set[i].textContent), pitch: t };
    console.log(details_pov[i]);
}

// Create the script tag, set the appropriate attributes
var script = document.createElement('script');
script.src = "https://maps.googleapis.com/maps/api/js?v=weekly&key=AIzaSyBeOquyY6lNdbXUc7uYwUqxkR_x-hfRS_I&callback=initMap";
script.async = true;

// Attach your callback function to the `window` object
window.initMap = function() {
    initializing();
};

function initializing(){
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: default_location_zoom,
    center: default_location,
  });

  const tourStops = details_location;
  // Create an info window to share between markers.
  const infoWindow = new google.maps.InfoWindow();
  // Create the markers.
  tourStops.forEach(([position, title], i) => {
    const marker = new google.maps.Marker({
      position,
      map,
      title: `${i + 1}. ${title}`,
      label: `${i + 1}`,
      optimized: false,
    });
    // Add a click listener for each marker, and set up the info window.
    marker.addListener("click", () => {
      infoWindow.close();
      infoWindow.setContent(marker.getTitle());
      infoWindow.open(marker.getMap(), marker);
    });
  });
}

// Append the 'script' element to 'head'
document.head.appendChild(script);

export {details_location, details_pov, initializing};