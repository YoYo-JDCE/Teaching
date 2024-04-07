#import all the package needed
import pandas as pd
import numpy as np
from datetime import date



#Customize your code based on your class below

#replace ### by document name of your class roster
roster=pd.read_csv('#####.csv')

#replace ### by zoom report of attendance
attendance=pd.read_csv('######.CSV')
#enter the minimum length students having to attend the class (in minutes)such as 60 mininues, please enter 60
Minimum_Time=##

#replace ##### by the name you want to call for your attendance report. such as ECON220SECTION1
filename="#####"

#Enter location of where you want to save the attendance report. such as C:\DESKTOP, please enter C:\\DESKTOP
filepath="C:\\####\\"

#End of customization



#identify students not attending classes
attendance=attendance.merge(roster,how='outer',left_on='User Email',right_on='Email')


absence=attendance[attendance['User Email'].isna()]

absence=absence[['First Name','Last Name','Email']]
print(absence)


#identify students did not attend the whole class (late or leave earlier).
#my threshold is 60 minutes, since my class last 75 minutes
incomplete=attendance[attendance['Duration (Minutes)']<Minimum_Time]


#save the attendance to certain folder
def get_filename_datetime():
    # Use current date to get a text file name.
    return filename + str(date.today()) + ".xlsx"

# Get full path for writing.
name = get_filename_datetime()
print("NAME", name)

path = filepath + name
print("PATH", path);


#export your the record to a spreed sheet named as "attendance"
absence.to_excel(path,sheet_name='absence')
with pd.ExcelWriter(path,mode='a') as writer:
   incomplete.to_excel(writer,sheet_name='incomplete')
