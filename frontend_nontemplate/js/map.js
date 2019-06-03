const india = new google.maps.LatLng(20.5937, 78.9629);
const initMap = () => {
    map = new google.maps.Map(document.getElementById('map'), {
        center: india,
        zoom: 4.5
    });
}
console.log("hello")