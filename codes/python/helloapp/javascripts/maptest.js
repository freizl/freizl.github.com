	map = new GMap2(document.getElementById("mapDiv"), {draggableCursor:"crosshair"});
    map.setCenter(new GLatLng(30.265, 120.151), 15);
	map.enableDoubleClickZoom();    
	map.enableScrollWheelZoom();                     
	map.enableContinuousZoom();	
	map.addControl(new GMapTypeControl());
	map.addControl(new GLargeMapControl());
	map.addControl(new GScaleControl()); 
