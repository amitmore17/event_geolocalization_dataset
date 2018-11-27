# event_geolocalization_dataset

## Getting Started
Please refer following paper for details on the experiments in this dataset:  
"A Pseudo-likelihood Approach For Geo-localization of Events From Crowd-sourced Sensor-Metadata".

The dataset corresponding to the ith experiment is titled "exp_i.pk".  
File can be read using python2.7 pickle syntax as shown below. 
```
with open('./exp_i.pk','rb') as fp:
	exp_data = pickle.load(fp) 
```
where ```exp_data``` is a python dictionary containing experimental data with following fields: 

* **geovid_server_query_parameters**:

	its a tuple containing parameters ```(start_date,start_time,end_date,end_time,SW_lat,SW_lng,NE_lat,NE_lng,location_timezone_UTC)``` used for searching the videos of the experiments uploaded on the geovid.org server.  
	The tuple contains data *(start_date, start_time, end_date, end_time)* used for defining temporal bound for searching, *(SW_lat, SW_lng, NE_lat, NE_lng)*, *i.e.* south-west lattitude and longitude, and north-east lattitude and longitude used for defining geographic bounds, and *location_timezone_UTC* time zone of the locations where experiments were carried out.  
	Please refer "Sakire Arslan Ay, Lingyan Zhang, Seon Ho Kim, Ma He, and Roger Zimmermann. 2009. GRVS: A georeferenced video search engine. In ACM Proc. Multimedia. 977–978" for more details on how to use these parameters for creating a query url and searching the videos and sensor data. 
 
 * **is_event_track_gps_available**:  
 	this filed indicates whether gps data for the event track is available.
 	 
 * **number_of_cameras**:  
 	number of cameras, N, video recording the event.
 	
 * **number_of_timestamps**:  
 	total number of sensor metadata samples, T, taken during the experiment. Sampling period is 200ms. 
 	
 * **mean_coords_in_meters**:  
 	the tuple (\mu_x, \mu_y), these coordinates can be added into the camera/event coordinates to get corresponding coordinates on the surface of the earth (in meters). 
 	
 * **sensor_data**:  
 	tuple containing ```(camera_x_coordinate, camera_y_coordinate, camera_orientation, camera_magnetometer_strength, camera_gps_error_variance)```. 
 	Each variable is a 2D array of size TxN such that (t,n) entry represents data for n^{th} camera for time instant t. 
 	
 * **event_track**:  
 	this field is valid if **is_event_track_gps_available** is True. It contains tuple (event_x_coordinate, event_y_coordinate, event_gps_error). Each variable is 1D array of size T such that t^{th} entry represents data for time instant t representing gps data for event location and corresponding gps error. 
 	
 * **raw_data**:  
 	dictionary with following fields: 'gps_data', 'compass_data', 'accelerometer_data'
 	* gps_data:  
	raw gps sensor measurements during the experiment in following format
 		[gps_data_cam_0, gps_data_cam_1, ..., gps_data_cam_(N-2), gps_data_cam_(N-1), gps_data_event] if "is_event_track_gps_available" is True else [gps_data_cam_0, gps_data_cam_1, ..., gps_data_cam_(N-2), gps_data_cam_(N-1)]
 		each field in above list is as below
 		gps_data_cam_x: [data(0), data(1), ... ] where data(t) is [UTC timestamp since unix epoch, Latitude, Longitude, GPSError_std, Altitude]
 		Note: sampling frequency for gps data is 1Hz. 
 		
 	* compass_data:  
	raw compass sensor measurements during the experiment in following format
 		[compass_data_cam_0, compass_data_cam_1, ..., compass_data_cam_(N-2), compass_data_cam_(N-1), compass_data_event] if "is_event_track_gps_available" is True else [compass_data_cam_0, compass_data_cam_1, ..., compass_data_cam_(N-2), compass_data_cam_(N-1)]
 		each field in above list is as below
 		compass_data_cam_x: [data(0), data(1), ... ,data(T-2),data(T-1)] where data(t) is [UTC timestamp since unix epoch, hx, hy, hz, (hx\*hx, hy\*hy, hz\*hz)\*\*.5] where (hx,hy,hz) is a magnetometer measurement. 
 		
	* accelerometer_data:  
	raw accelerometer sensor measurements during the experiment in following format
 		[accelerometer_data_cam_0, accelerometer_data_cam_1, ..., accelerometer_data_cam_(N-2), accelerometer_data_cam_(N-1), accelerometer_data_event] if "is_event_track_gps_available" is True else [accelerometer_data_cam_0, accelerometer_data_cam_1, ..., accelerometer_data_cam_(N-2), accelerometer_data_cam_(N-1)]
 		each field in above list is as below
 		accelerometer_data_cam_x: [data(0), data(1), ... ,data(T-2),data(T-1)] where data(t) is [UTC timestamp since unix epoch, ax, ay, az, (ax\*ax, ay\*ay, az\*az)\*\*.5] where (ax,ay,az) is a magnetometer measurement. 
    
    
## Authors

* **Amit More** - [amitmore17](https://github.com/amitmore17)

contact:amitmore@ee.iitb.ac.in,amitmore17@gmail.com.  
Please send an email on both email addresses for quick reply.  	

