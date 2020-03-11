import pickle

source_dict = {1:"6",2:"2",3:"f"}

#serialize the dictonary into a bytestream
pickle_out = open("dict.pickle","wb")
pickle.dump(source_dict, pickle_out)
pickle_out.close()


#deserialize the bytestream into the original source object
pickle_in = open("dict.pickle","rb")
result_obj = pickle.load(pickle_in)

print(result_obj)
