(function() {
    var doXHR = function(method, url, payload, callback) {
        var xhr = new XMLHttpRequest();
        xhr.onload = function() {
            callback(this.status, JSON.parse(this.responseText));
        };
        xhr.open(method, url, true);
        if (method == "POST" || method == "PUT" || method == "PATCH") {
            var payloadJson = JSON.stringify(payload);
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.setRequestHeader("Content-Length", payloadJson.length);
            xhr.send(payload);
        } else {
            xhr.send();
        }
    };

    API = {};

    API.create = function(obj, callback) {
        doXHR("POST", "/api/stories", obj, callback);
    };

    API.list = function(callback) {
        doXHR("GET", "/api/stories", null, callback);
    };

    API.byId = function(id, callback) {
        doXHR("GET", "/api/stories/" + id, null, callback);
    };

    API.patch = function(id, obj, callback) {
        doXHR("PATCH", "/api/stories/" + id, obj, callback);
    };

    API.replace = function(id, obj, callback) {
        doXHR("PUT", "/api/stories/" + id, obj, callback);
    };

    API.delete = function(id, callback) {
        doXHR("DELETE", "/api/stories/" + id, null, callback);
    };
}(window));
