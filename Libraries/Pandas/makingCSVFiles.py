import pandas as pd
import numpy as np
'''make a dictionary and then convert into csv file '''
dict_data ={
    "NAME":['ANDREW','FATIMA','NG','MUSK','MARK','JOBS'],
    'AGE':[45,21,34,54,23,45],
    'CITY':['LONDON','NEWARK','DELHI','MAXICO','CHICAGO','CANADA']
    }
# MAKE  A DATA FRAME
data_frame= pd.DataFrame(dict_data)
# print(data_frame)

# convert to csv file,Ignoreindex====False)
data_frame.to_csv('Data_csv.csv',index=False)# remove row number


# now read the same csv file
df = pd.read_csv(r'basics-of-python-and-python-libraries\Libraries\Pandas\Data_csv.csv',encoding='utf-8')
print(df)