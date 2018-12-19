import '../scss/app.scss'

import Vue from 'vue'
import L from 'leaflet'

var app = new Vue({
  data: {
    map: null,
    markers: [],
    position: [38, -94.33, 5]
  },
  created: function(){
    this.initMap();
    this.setMarkers();
  },
  methods: {

    /**
     *  Initialize and build a Leaflet map. Called on page load
     */
    initMap: function(){
      // Create Leaflet map instance
      this.map = L.map('map', {
        center: [this.position[0], this.position[1]],
        zoom: this.position[2]
      });

      // Initialize dots canvas where points will be displayed
      this.dots = L.canvas({ padding: 0.5 });

      // Set mapbox tiles
      L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoicG9iaSIsImEiOiJjanBudTZmeWswNmRvM3htd3pzcmcxOGNzIn0.dQCX-P4i8DxT6aapOM76gg', {
		    maxZoom: 18,
		    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			    '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			    'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		    id: 'mapbox.light'
	    }).addTo(this.map);
    },

    /**
     * Fetch data points and place markers on the map
     */
    setMarkers: function(){
      var self = this;
      var req = new Request("/api/all");

      var allSourcesCanvas = L.canvas({ padding: 0 });

      fetch(req)
      .then(function(res) {
        if (res.status === 200) {
          return res.json();
        } else {
          throw new Error("Something went wrong on api server!");
        }
      })
      .then(function(data) {
        for(var item of data) {
          self.addMarker(item, allSourcesCanvas)
        }

        self.map.on('zoomend', function(){
          var circleSize = self.getMarkerSize();

          for(var marker of self.markers){
            marker.setRadius(circleSize)
          }
        })
      })
      .catch(function(err) {
        console.error("Error - ", err);
      })
    },

    /**
     * Place the marker into the map, defines the style
     * @param {*} item 
     * @param {*} layer 
     */
    addMarker: function(item, canvas){
      var self = this;

      // Create marker
      var marker = L.circleMarker([item.lat, item.long], {
        renderer: canvas,
        weight: 0,
        fillColor: '#FF7F50',
        fillOpacity: 0.6,
        title: item.city || null,
      }).on('click', function(){
        console.log('lol');
      })
      .setRadius(self.getMarkerSize())
      .addTo(self.map);
      
      self.markers.push(marker)
    },

    /**
     * Compute marker size
     * @return Integer
     */
    getMarkerSize: function(){
      var zoom = this.map.getZoom();
      var circleSize = 3

      if(zoom >this.position[2]){
        circleSize = 3 + (1 * (zoom - this.position[2]))
      }

      return circleSize;
    }
  }
})