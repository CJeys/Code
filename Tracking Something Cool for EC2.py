import pandas as pd
import plotly.express as px
url = 'http://api.open-notify.org/iss-now.json'
dataframe = pd.read_json(url)
dataframe['latitude'] = dataframe.loc['latitude', 'ISS_position']
dataframe['longtitude'] = dataframe.loc['longitude', 'ISS_position']
dataframe.reset_index(inplace=True)
print(dataframe)


df