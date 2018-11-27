import pickle

path = './video_info/'
#total exp numbers = 18
exp = 1
exp_file_name = path+'exp_'+str(exp)+'.pk'
file_object = open(exp_file_name,'rb') 
vid_info = pickle.load(file_object)
file_object.close()

start_time = vid_info['start_timestamps']
stop_time = vid_info['stop_timestamps']
start_offsets = vid_info['start_offsets']
stop_offsets = vid_info['stop_offsets']
video_file_durations = vid_info['video_durations']
event_recording_durations = vid_info['event_recording_durations']

for a,b,c,d,e,f in zip(start_time, stop_time, start_offsets, stop_offsets, video_file_durations, event_recording_durations):
	print('video recording start time:',a)
	print('video recording end time:',b)
	print('video recording duration:',e)
	print('event recording start time:',a+c)
	print('event recording stop time:',b-d)
	print('event recording duration:',b-a-c-d)
	
	

