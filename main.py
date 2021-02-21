import plotly.express as px
import csv
with open("./data.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df , x="Size of TV" , y="Average Weekly TV Time")

fig.show()