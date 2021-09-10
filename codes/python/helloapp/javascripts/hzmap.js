var map, GDir1, GDir2, normalProj, waypoints=[], gpolys=[], routeNodes=[], myNode, markerDragged, isDragged, lastIndex, prevIndex;

if (!GBrowserIsCompatible()) {
    alert("Sorry, the Google Maps API is not compatible with this browser");
}
else {
	// Display the map with some controls and set the initial location 
	map = new GMap2(document.getElementById("mapDiv"), {draggableCursor:"crosshair"});
	map.setCenter(new GLatLng(30.265, 120.151), 12);
	map.enableDoubleClickZoom();    
	map.enableScrollWheelZoom();                     
	map.enableContinuousZoom();	
	
	map.addControl(new GMapTypeControl());
	map.addControl(new GLargeMapControl());
	map.addControl(new GScaleControl()); 

	normalProj = G_NORMAL_MAP.getProjection(); // for conversion between LatLng and screen pixels
	
	GDir1 = new GDirections(); // for extending route to additional point
	GDir2 = new GDirections(); // for recalculating of route when dragging line
	
	//GEvent.addListener(GDir1, "error", function() {	alert("Directions Failed: "+GDir1.getStatus().code); });
	//GEvent.addListener(GDir2, "error", function() {	alert("Directions Failed: "+GDir2.getStatus().code); });
			
	GEvent.addListener(map, 'mousemove', getProximity); // for detecting if mouse is above displayed route
	
	GEvent.addListener(map, "zoomend", function() {
		routeNodes = []; // clear cached coordinates in pixels of displayed route vertexes, the coordinates have to be recalculated on new zoom level
	});
	
	GEvent.addListener(map, "click", function(overlay, point) {
		if (point) {
			if (waypoints.length == 0) { // no waypoints exist yet - map was clicked for start of the route
				GDir1.loadFromWaypoints([point.toUrlValue(6), point.toUrlValue(6)], {getPolyline:true}); // get directions from that point to itself to snap it to street
			} 
			else { // map was clicked for additional waypoint
				GDir1.loadFromWaypoints([waypoints[waypoints.length-1].getPoint(), point.toUrlValue(6)], {getPolyline:true}); //get directions from last waypoint to clicked point
			}
		}			
	});

	iconNode = new GIcon();	iconNode.image = 'node.gif';
	iconNode.shadow = ''; iconNode.iconSize = new GSize(10,10); iconNode.shadowSize = new GSize(0,0);
	iconNode.iconAnchor = new GPoint(5,5); iconNode.infoWindowAnchor = new GPoint(5,5);
	iconNode.dragCrossImage = 'empty.gif'; // undocumented String: indicates an image to be used as the drag cross. If you set it to the null string, you get the default drag_cross_67_16.png image.
	iconNode.dragCrossSize = GSize(1, 1); //undocumented GSize(): indicates the size of the drag cross. 
	iconNode.maxHeight = 1; //undocumented integer: The maximum difference in height between the marker anchor and the drag cross anchor during dragging. Setting the maxHeight to zero causes it to use the default 13.
	
	// create marker for displaying and dragging when mouse is over displayed route
	myNode = new GMarker(map.getCenter(), {icon:iconNode, draggable:true, bouncy:false, zIndexProcess:function(marker,b) {return 1;}});
	map.addOverlay(myNode);
	myNode.show(); // sometimes .hide() does not work without .show() at first ???
	myNode.hide(); // hide this marker initially
	
	GEvent.addListener(myNode, "drag", function() { // mouse was over displayed route and user drags the displayed marker
		myNode.show();
		
		if (isDragged == 2) { // already waiting for GDir2.load to complete - so just remember that marker was dragged again
			markerDragged = myNode; // remember which marker was dragged
			return;
		}
		
		if (myNode.MyIndex < waypoints.length) {
			isDragged = 2; // tag that GDir2.load is started
			markerDragged = false;
			
			lastIndex = myNode.MyIndex;	
			prevIndex = -1;
			// recalculate route between waypoints before and after myNode on the displayed line
			GDir2.loadFromWaypoints([waypoints[lastIndex].getPoint(), myNode.getPoint().toUrlValue(6), waypoints[lastIndex + 1].getPoint()], {getPolyline:true});
		}
	});
	
	GEvent.addListener(myNode, "dragend", function() { // when user finished dragging the line, create new waypoint with permanent marker at the location
		var point = myNode.getPoint();
		var marker = new GMarker(point, {icon:iconNode, draggable:true, dragCrossMove:false, bouncy:false, zIndexProcess:function(marker,b) {return 1;}});
		waypoints.splice(myNode.MyIndex + 1, 0, marker); //insert new waypoint into waypoints array
		
		for (var i = myNode.MyIndex; i < waypoints.length; i++) // reindex next waypoints
			waypoints[i].MyIndex = i;
		
		var dummy = new GPolyline([point]); // insert empty segment into route segments array - GDir2.load will replace it with new route segment
		map.addOverlay(dummy);
		gpolys.splice(myNode.MyIndex + 1, 0, dummy); 
		
		// add event listeners for marker of new waypoint - so route will be recalculated when user drags waypoint
		GEvent.addListener(marker, "dragstart", function() { isDragged = 1; myNode.hide(); });
		GEvent.addListener(marker, "dragend", function() { isDragged = 0; } );
		GEvent.addListener(marker, "drag", dragMarker);
		
		map.addOverlay(marker);
		
		if (myNode.MyIndex < waypoints.length) {
			lastIndex = myNode.MyIndex + 1; prevIndex = lastIndex - 1;
			// recalculate route between previous and next waypoints going through new inserted waypoint
			GDir2.loadFromWaypoints([waypoints[lastIndex - 1].getPoint(),point.toUrlValue(6), waypoints[lastIndex + 1].getPoint()], {getPolyline:true});
		}
	});		
			
	GEvent.addListener(GDir1, "load", function() { 
		var gp = GDir1.getPolyline();
		var point = gp.getVertex(gp.getVertexCount() - 1); // snap to last vertex in the polyline
		var marker = new GMarker(point, {icon:iconNode, draggable:true, dragCrossMove:false, bouncy:false, zIndexProcess:function(marker,b) {return 1;}});
		
		if (waypoints.length == 0) {	
			marker.title = GDir1.getRoute(0).getStartGeocode().address;
		}
		else {
			waypoints[waypoints.length-1].title = GDir1.getRoute(0).getStartGeocode().address;
			marker.title = GDir1.getRoute(0).getEndGeocode().address
		}
		
		GEvent.addListener(marker, "dragstart", function() { isDragged = 1; myNode.hide(); });
		GEvent.addListener(marker, "drag", dragMarker); 
		GEvent.addListener(marker, "dragend", function() { isDragged = 0; }); 
		
		marker.MyIndex = waypoints.length;
		waypoints.push(marker);
		map.addOverlay(marker);
				
		if (waypoints.length > 1) { // if this was not the first waypoint - display the route to this waypoint
			map.addOverlay(gp);
			gpolys.push(gp);
			
			routeNodes = [];
			getProximity();
		}
	});

	GEvent.addListener(GDir2, "load", function() {
		var gp = GDir2.getPolyline();
		
		map.removeOverlay(gpolys[lastIndex]);
						
		if (prevIndex >= 0) { // not the last waypoint was dragged
			map.removeOverlay(gpolys[lastIndex-1]);

			var minD, minI, points=[];
			var p0 = waypoints[lastIndex].getPoint();
					
			for (var i = 0; i < gp.getVertexCount(); i++) { // search closest vertex to dragged waypoint for splitting received route at it into two routes between waypoints
				var p = gp.getVertex(i);
				points.push(p);
			
				var d = p0.distanceFrom(p);
			
				if (i == 0 || minD > d) {
					minD = d;
					minI = i;
				}	
			}

			gpolys[lastIndex - 1] = new GPolyline(points.slice(0, minI + 1)); //+1,  because slice extracts up to, but not including, the 'end' element
			gpolys[lastIndex] = new GPolyline(points.slice(minI, points.length));
			
			map.addOverlay(gpolys[lastIndex - 1]);
			
			waypoints[lastIndex-1].title = GDir2.getRoute(0).getStartGeocode().address;
			waypoints[lastIndex].title = GDir2.getRoute(0).getEndGeocode().address;
			waypoints[lastIndex+1].title = GDir2.getRoute(1).getEndGeocode().address;
		}
		else { // last waypoint was dragged
			gpolys[lastIndex] = gp;
			waypoints[lastIndex].title = GDir2.getRoute(0).getStartGeocode().address;
			waypoints[lastIndex+1].title = GDir2.getRoute(0).getEndGeocode().address;
		}
		map.addOverlay(gpolys[lastIndex]);
		
		routeNodes = [];
		getProximity();
		
		isDragged = 0; // tag that there is no dragged waypoints or waiting for GDir to complete 
	
		if (markerDragged) { // marker was dragged again until GDir2 was loaded
			isDragged = 1; // tag that there is dragged waypoint
			GEvent.trigger(markerDragged, 'drag'); // trigger recalculation of route
		}
	});
	
}	

function dragMarker() { // when waypoint marker is being dragged, start calculation of new route
	if (isDragged == 2) { // exit if already waiting for GDir2.load to complete 
		markerDragged = this;
		return; 
	}				
	isDragged = 2; // tag that calculation of new route is started
	
	if (markerDragged) { //determine which marker triggered the recalculation
		marker = markerDragged;
		markerDragged = false;
	}
	else {
		marker = this;
	}
	
	lastIndex = marker.MyIndex;
	var point = marker.getPoint();
			
	if (lastIndex > 0) {
		if (lastIndex < waypoints.length - 1) {
			prevIndex = lastIndex - 1;	
			GDir2.loadFromWaypoints([waypoints[lastIndex - 1].getPoint(),point.toUrlValue(6),waypoints[lastIndex + 1].getPoint()],{getPolyline:true});	
		}
		else {
			prevIndex = -1; lastIndex = lastIndex - 1; // recalculate path to this point
			GDir2.loadFromWaypoints([waypoints[lastIndex].getPoint(),point.toUrlValue(6)],{getPolyline:true});
		}
	}
	else if (waypoints.length > 1) {
		prevIndex = -1;
		GDir2.loadFromWaypoints([point.toUrlValue(6),waypoints[1].getPoint()],{getPolyline:true});
	}
}

function getProximity(mouseLatLng, marker) { // detecting if mouse is over displayed route
	var dist, zoom;
	
	if (routeNodes.length == 0) { // calculate and cache coordinates of displayed polylines in pixels for better performance in routeNodes array
		dist = 0;
		zoom = map.getZoom();
		
		if (gpolys.length > 0 && gpolys[0].getVertexCount() > 0 ) //store first point
			routeNodes.push(normalProj.fromLatLngToPixel(gpolys[0].getVertex(0), zoom));
				
		for (var i = 0; i < gpolys.length; i++) {
			dist += gpolys[i].getLength();
			
			for (var j = 1; j < gpolys[i].getVertexCount(); j++) {
				var point = normalProj.fromLatLngToPixel(gpolys[i].getVertex(j), zoom)
				point.MyIndex = i; // store the index of polyline containing this node
				routeNodes.push(point);
			}
		}

		// display route length if 'panel' element is present
		var panel = document.getElementById('panel');
		
		if (panel) { 
			panel.innerHTML = (dist/1000).toFixed(1) + " km";
		}		
	}
	
	if (!mouseLatLng || routeNodes.length <= 1 || isDragged > 0) // no route is displayed or route is already being dragged
		return;

	zoom = map.getZoom();
	var mousePx = normalProj.fromLatLngToPixel(mouseLatLng, zoom);
	
	var minDist = 999;
	var minX = mousePx.x; // we will search closest point on the line to mouse position for displaying marker there available for dragging
	var minY = mousePx.y;
	
	if (routeNodes.length > 1) {
		var x,y, d1,d2,d;
		var dx = mousePx.x - routeNodes[0].x;
		var dy = mousePx.y - routeNodes[0].y;
		d2 = dx*dx + dy*dy; // distance^2 from mouse to start of segment 1 in pixels
		
		for (var n = 0 ; ++n < routeNodes.length; ) {
			d1 = d2; // distance^2 from mouse to start of segment n in pixels
			
			x = routeNodes[n].x; dx = mousePx.x - x;
			y = routeNodes[n].y; dy = mousePx.y - y;
			d2 = dx*dx + dy*dy; // distance^2 from mouse to end of segment n in pixels
			
			dx = x - routeNodes[n-1].x; 
			dy = y - routeNodes[n-1].y;
			d = dx*dx + dy*dy; // lenght^2 of segment n			

			var u = ((mousePx.x - x) * dx + (mousePx.y - y) * dy) / d; // a bit of vector algebra :)
			x += (u*dx); // x,y coordinates in pixels of closest point to mouse in segment n
			y += (u*dy);
				
			dx = mousePx.x - x;
			dy = mousePx.y - y;
			dist = dx*dx + dy*dy; // distance^2 from mouse to closest point in segment n

			if ((d1 - dist) + (d2 - dist) > d) { // closest point is outside the segment, so the real closest point is either start or end of segment
				if (d1 < d2) {
					dist = d1; 
					x = routeNodes[n-1].x;
					y = routeNodes[n-1].y;
				}
				else {
					dist = d2; 
					x = routeNodes[n].x;
					y = routeNodes[n].y;
				}				
			};  

			if (minDist > dist) { // closest point in segment n is closest point overall so far
				minDist = dist;
				minX = x;
				minY = y;
				myNode.MyIndex = routeNodes[n].MyIndex; // remember segment closest to mouse
			}
		}
		
		if (minDist > 25) { // mouse is not close enough to the displayed line
			myNode.hide(); // do not display marker for dragging the polyline
		}	
		else {	
			for (n = waypoints.length; --n >= 0;) { // check if mouse is not too close to existing waypoints markers
				var markerPx = normalProj.fromLatLngToPixel(waypoints[n].getPoint(), zoom);
				
				dx = markerPx.x - minX;
				dy = markerPx.y - minY;
				
				if (dx*dx + dy*dy < 25) { // mouse is too close to existing marker
					myNode.hide(); // do not show additional marker for dragging the line - the user is about to drag existing waypoint
					return;
				}	
			}
			
			myNode.setPoint(normalProj.fromPixelToLatLng(new GPoint(minX, minY), zoom));
			myNode.show(); // display marker for dragging the polyline
		}

		//document.getElementById('panel').innerHTML = '<br>Mouse distance to line ' + n + ': ' + minDist.toFixed(2);		
	}
}

