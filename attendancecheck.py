import pandas as pd
import numpy as np


#import your roster and attendance record from zoom
roster=pd.read_csv('QUAN340001.csv')
attendance=pd.read_csv('quan1.csv')

#identify students not attending classes
attendance=attendance.merge(roster,how='outer',left_on='User Email',right_on='Email')


absence=attendance[attendance['User Email'].isna()]

absence=absence[['First Name','Last Name','Email']]
print(absence)


#identify students did not attend the whole class (late or leave earlier).
#my threshold is 60 minutes, since my class last 75 minutes
incomplete=attendance[attendance['Duration (Minutes)']<60]


#export your the record to a spreed sheet named as "attendance"
absence.to_excel("attendanceQUAN1.xlsx",sheet_name='absence')
with pd.ExcelWriter('attendanceQUAN1.xlsx',mode='a') as writer:
   incomplete.to_excel(writer,sheet_name='incomplete')
