
import tabula

df = (r'C:\Users\jjian\Desktop\Nov.pdf')
tabula.convert_into(r'C:\Users\jjian\Desktop\Nov.pdf', r'C:\Users\jjian\Desktop\Nov2020BOA.csv' , output_format="csv",pages='all', stream=True)
