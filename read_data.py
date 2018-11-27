import pickle
path = './dataset/'
#total exp numbers = 18
exp = 1
exp_file_name = path+'exp_'+str(exp)+'.pk'
file_object = open(exp_file_name,'rb') 
exp_data = pickle.load(file_object)
file_object.close()
	
	
	
	
	
	
	
	
	
	

	
