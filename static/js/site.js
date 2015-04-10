(function() {
    var startLatitude = 42.2759851;
    var startLongitude = -83.7383985;
    // Load map, centered at diag
    function ready() {
        var map = L.map('map').setView([startLatitude, startLongitude], 17);
        L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; OpenStreetMap',
            maxZoom: 18
        }).addTo(map);
    }
     
    // TODO add popups

    document.addEventListener("DOMContentLoaded", ready, false);
}());
