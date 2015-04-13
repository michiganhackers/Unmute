(function() {
    var startLatitude = 42.277;
    var startLongitude = -83.7383985;
    // Load map, centered at diag
    function ready() {
        var map = L.map('map').setView([startLatitude, startLongitude], 17);
        L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; OpenStreetMap',
            maxZoom: 18
        }).addTo(map);

        var storiesAdded = [];

        var timeToNewPopups = 1300;
        var varianceFactor = 500;

        setInterval(function () {
            API.list(function(statuscode, stories) {
                if (statuscode != 200) return;

                var numStoriesAdded = 0;
                for (var i = 0, len = stories.objects.length; i < len; i++) {
                    var story = stories.objects[i];
                    if (storiesAdded.indexOf(story.id) < 0) {
                        var marker = L.marker([story.latitude, story.longitude]).addTo(map);
                        marker.bindPopup("<b>" + story.title + "</b><p>" + story.story_body + "</p>");
                        storiesAdded.push(story.id);
                        numStoriesAdded++;
                    }
                }

                if (numStoriesAdded > 0) {
                    timeToNewPopups += varianceFactor*(Math.random()-0.5);
                }
            });
        }, 1300);
    }
     
    document.addEventListener("DOMContentLoaded", ready, false);
}());
