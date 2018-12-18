import '../scss/app.scss'

import Vue from 'vue'
import L from 'leaflet'
import 'leaflet.markercluster'

var app = new Vue({
  data: {
    map: null,
    position: [38, -94.33, 5],
    dots: null,
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
     * 
     */
    setMarkers: function(){
      
    }
  }
})