import pandas as pd
from datetime import datetime

df = pd.read_csv('python hands-on - dataset.csv')
print(df)

def isObsolete(benchmark_date,date):
    #date format must be 'yyyy-mm-dd'
    try:
        bm_date = datetime.strptime(benchmark_date,'%Y-%m-%d')
        date_to_check = datetime.strptime(date,'%Y-%m-%d')
        if date_to_check < bm_date:
            return 'TRUE'
        else:
            return 'FALSE'
    except TypeError as TE:
        print('Date must be a string in the format "yyyy-mm-dd"')
    except Exception as e:
        print('Some Other Error Occured: '+str(e))    

        
benchmark_date = '2021-01-01'

df['obsolete'] = df['date'].apply(lambda x: isObsolete(benchmark_date,x))
print(df)

exportname = 'python hands-on - dataset.json'
try:
    df.to_json(exportname,orient='columns')
    print('File saved to current directory as '+ exportname)
except Exception as e:
    print('Error saving json file: '+str(e))