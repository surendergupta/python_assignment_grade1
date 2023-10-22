import json
import pymongo
def convert(mylist):
   res_dict = {}
   for i in range(0, len(mylist), 2):
       res_dict[mylist[i]] = mylist[i + 1]
   return res_dict
try:
    
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["assignment1"]
    dblist = myclient.list_database_names()
    if "assignment1" in dblist:
        #print("The database exists.")
        mycol = mydb["config_tbl"]
        collist = mydb.list_collection_names()
        if "config_tbl" in collist:
            #print("The collection exists.")
            myConfigFile = open("config.txt", "r")
            data = myConfigFile.read()

            # print(data)
            data_into_list = data.split('\n')
            # print(data_into_list)
            data = []
            databaseObj = {}
            serverObj = {}

            for i in range(0, len(data_into_list), 1):
                if(data_into_list[i] == '[Database]'):
                    continue
                elif(data_into_list[i] == '[Server]'):
                   break
                else:
                   databaseObj[data_into_list[i].split(' = ')[0]] = data_into_list[i].split(' = ')[1]
                   data.append(databaseObj)
                   
            
            print(data)
            # for i in range(0, len(data_into_list), 1):
            #     if(data_into_list[i] == '[Database]'):
            #         continue
            #     elif(data_into_list[i] == '[Server]'):
            #        continue
            #     else:
            #        serverObj[data_into_list[i].split(' = ')[0]] = data_into_list[i].split(' = ')[1]
            # print(databaseObj)
            # print(serverObj)

            #json_config = json.dumps(data_into_list)
            #print(type(json_config))
            # x = mycol.insert_one(json_config)
            # print(x.inserted_id)
            # myConfigFile.close()
        else:
           print("The collection not found.")
    else:
       print("The database not exists.")
        
            # # defining a params dict for the parameters to be sent to the API
            # PARAMS = {'address':location}
            
            # # sending get request and saving the response as response object
            # r = requests.get(url = URL, params = PARAMS)
            
            # # extracting data in json format
            # data = r.json()
except Exception as error:
  print("File not found...", error)

