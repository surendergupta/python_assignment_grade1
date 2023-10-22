import shutil 
import calendar
import time
import os 
import sys 

if __name__ == "__main__":
    try:
        os.chdir(sys.path[0]) 
        #print(os.chdir(sys.path[0]))
        
        sourceFol = sys.argv[1:]        
        # print(sourceFol[0])
        
        src_files = os.listdir(sourceFol[0])        
        # print(src_files)

        desc_files = os.listdir(sourceFol[1])
        # print(desc_files)

        for file_name in src_files:
            # construct full file path
            source = sourceFol[0] + file_name
            destination = sourceFol[1] + file_name
            if os.path.isfile(destination):
                gmt = time.gmtime()
                timestamp = calendar.timegm(gmt)
                destination = sourceFol[1]+str(timestamp)+'_'+file_name
                shutil.copy2(source, destination)     
                print("Backup Successful!")         
            else:
                shutil.copy2(source, destination) 
                print("Backup Successful!") 
    except: 
        print("File does not exists!, or source and destination path not find") 

#  python q4.py  "C:/Users/~/Desktop/pythons/assignment1/souces/" "C:/Users/~/Desktop/pythons/assignment1/destination/"
    
