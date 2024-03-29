'''
Question 2889
'''

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.pivot(index='month',columns='city',values='temperature')
    return weather