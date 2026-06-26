import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

df = pd.read_csv("formatted_sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

fig = px.line(df, x="Date", y="Sales", title="Pink Morsel Sales Over Time")
fig.update_layout(xaxis_title="Date", yaxis_title="Sales ($)")

# price increase happened on this date
fig.add_vline(x="2021-01-15", line_dash="dash", line_color="red")

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig),
])

if __name__ == "__main__":
    app.run(debug=True)
