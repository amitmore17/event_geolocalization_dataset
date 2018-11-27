# event_geolocalization_dataset

## Getting Started
Please refer following paper for details on the experiments in this dataset:  
"A Pseudo-likelihood Approach For Geo-localization of Events From Crowd-sourced Sensor-Metadata".

The metadata corresponding to the ith experiment can be found in "dataset/exp_i.pk".  
The information about the video files can be found in "video_info/exp_i.pk".  
The individual files can be read using python2.7 pickle syntax as shown in ```read_data.py``` and ```read_video_info.py```, respectively. 

## Sensor Metadata
The file "dataset/exp_i.pk" contains dictionary with following fields:
* **geovid_server_query_parameters**:

	its a tuple containing parameters ```(start_date,start_time,end_date,end_time,SW_lat,SW_lng,NE_lat,NE_lng,location_timezone_UTC)``` used for searching the videos of the experiments uploaded on the geovid.org server.  
	The tuple contains data *(start_date, start_time, end_date, end_time)* used for defining temporal bound for searching, *(SW_lat, SW_lng, NE_lat, NE_lng)*, *i.e.* south-west lattitude and longitude, and north-east lattitude and longitude used for defining geographic bounds, and *location_timezone_UTC* time zone of the locations where experiments were carried out.  
	Please refer "Sakire Arslan Ay, Lingyan Zhang, Seon Ho Kim, Ma He, and Roger Zimmermann. 2009. GRVS: A georeferenced video search engine. In ACM Proc. Multimedia. 977–978" for more details on how to use these parameters for creating a query url and searching the videos and sensor data. 
 
 * **is_event_track_gps_available**:  
 	this field indicates whether gps data for the event track is available.
 	 
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
    
## Video Data
The file "video_info/exp_i.pk" contains a dictionary with information about video recordings. 
Each entry in the dictionary is a list of length N (or N+1 if *is_event_track_gps_available* is True).
The video recordings are also available to [download](https://github.com/amitmore17).

* **start_timestamps**:  
	a list containing sequence of *UTC timestamp since unix epoch* indicating time when the individual video recordings started.
	 
* **stop_timestamps**:  
	a list containing sequence of *UTC timestamp since unix epoch* indicating time when the individual video recordings ended. 
	
* **video_durations**:  
	a list containing sequence of time durations in milliseconds indicating durations of individual video recordings. 
	
* **start_offsets**:  
	a list containing sequence of offset values in milliseconds with respect to *start_timestamps* indicating when the event video recordings started. 
	
* **stop_offsets**:  
	a list containing sequence of offset values in milliseconds with respect to *stop_timestamps* indicating when the event video recordings ended. 
	
* **event_recording_durations**:  
	a list containing sequence of time durations in milliseconds indicating durations of individual event video recordings. 

Please refer ```read_video_info.py``` for more details.
Whenever an experiment have *is_event_track_gps_available* to be True, the last entries in the above lists corresponds to a video camera moving along with the event. 

## Authors

* **Amit More** - [amitmore17](https://github.com/amitmore17)

contact:amitmore@ee.iitb.ac.in,amitmore17@gmail.com.  
Please send an email on both email addresses for quick reply.  	

