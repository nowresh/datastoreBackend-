import time
import json
from os import path,getcwd
maxsize=1024**3
valuesize=16*1024*2024
data={} #data is the dictionary used 
class Datastore:
    def __init__(self,a=getcwd()): #getcwd is used to get the current working directory
        self.file_location=a
        if(path.isdir(self.file_location)): #checks wheather the location exists
            try:
                self.filename='\\'+input("Enter the file name : ")+".json" #Name of the json file created
                f = open(str(self.file_location)+self.filename,"x")
                f.write(json.dumps(data))
                print("Welcome to datastore \n Methods used here are:\n 1)create(key,value,timestamp)*timestamp is optional \n 2)read(key) \n 3)delete(key) \n 4)store_data() *used to store data in json file ")
            except:
                print("Error : File name already exist .")
        else:
            print("Error : File directory does not exist")
    def create(self,key,value,time_seconds=0):
        if key in data:
            print("Error : Key already exists") #checks for key existance in dictionary
        else:
            if key.isalpha():
                if len(data) < maxsize and value<=valuesize: #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                    if(len(key)>32): #constrints for key capped at 32 characters
                        print("Error : The key should not exceed 32 characters")
                    else:
                        etime=time_seconds
                        if time_seconds!=0:
                            etime=int(time.time())+time_seconds
                        data[key]=[value,etime]
                        print("Success : data is successfully created!")
                else:

                    print("Error : Memory limit reached")
            else:
                print("Error : Please enter a key with alphabets only")
    def read(self,key):
        if key in data:
            values=data[key]
            if values[1] < int(time.time()) and values[1]!=0: #checks the time-to-live property
                print("Error : Time-to-live for the key is expired")
            else:
                print(str(key)+":"+str(values[0]))#for returning the JSON format
        else:
            print("Error : Key does not exist")
            
    def delete(self,key):
        if key in data:
            values=data[key]
            if values[1] < int(time.time()) and values[1]!=0:
                print("Error : Time-to-live for the key is expired")
            else:
                del data[key]
                print("Success : The key has been deleted!")
        else:
            print("Error : Key does not exist")
    def store_data(self):
        for i in data:
            data[i]=data[i][0]
        json_data = json.dumps(data, indent=2) #converts the dictionary to Json 
        with open(str(self.file_location)+self.filename,"w") as f:
            f.write(json_data) #writing the file
        print("Success : Data has been stored")

