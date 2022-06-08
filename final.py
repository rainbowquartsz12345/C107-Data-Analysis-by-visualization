import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
#df.loc will help us filter out all the rows with the given student id
studentdf = df.loc[ df["student_id"] =="TRL_abc"]
fig = go.Figure(go.Bar(
     x = studentdf.groupby("level")["attempt"].mean(),
     y = ["Level 1", "Level 2", "Level 3", "Level 4"],  
     orientation = "h"

) )
fig.show()