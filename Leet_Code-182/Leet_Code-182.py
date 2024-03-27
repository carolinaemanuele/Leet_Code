'''
Question 182
'''

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    d =  pd.DataFrame(person['email'][person["email"].duplicated()==True])
    return d.drop_duplicates()