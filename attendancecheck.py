#import all the package needed
import pandas as pd
import numpy as np


#import your roster and attendance record from zoom
roster=pd.read_csv('QUAN340002.csv')
attendance=pd.read_csv('quan340128.csv')

#define the equation get_id to identify students who attended class
def get_id(x,y):
    for values in x,y:
        if x['Email'
        ].isin(y['User Email']).any()==True:
            return y['User Email']

# identify students attending class
roster['attending']=get_id(roster,attendance)



#identify students missing class
nu=roster.isnull()
rows_nu=nu.any(axis=1)
absence=roster[rows_nu]


#identify students did not attend the whole class (late or leave earlier).
#my threshold is 60 minutes, since my class last 75 minutes
incomplete=attendance[attendance['Total Duration (Minutes)']<60]


#export your the record to a spreed sheet named as "attendance"
absence.to_excel("attendance.xlsx",sheet_name='absence')
with pd.ExcelWriter('attendance.xlsx',mode='a') as writer:
    incomplete.to_excel(writer,sheet_name='incomplete')
