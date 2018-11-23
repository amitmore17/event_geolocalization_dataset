import pickle
path = './dataset/'
exp_numbers = 18
exp_data = []
for exp in range(exp_numbers):
	exp_file_name = path+'exp_'+str(exp)+'.pk'
	file_object = open(exp_file_name,'rb') 
	exp_data.append(pickle.load(file_object))
	file_object.close()
