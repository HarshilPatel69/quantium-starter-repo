import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

df = pd.read_csv("formatted_sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

app = Dash(__name__)

colors = {
    "background": "#f4f1ea",
    "panel": "#ffffff",
    "text": "#4b2e2e",
    "accent": "#e75480",
}

app.layout = html.Div(
    style={
        "backgroundColor": colors["background"],
        "fontFamily": "Verdana, sans-serif",
        "minHeight": "100vh",
        "padding": "30px",
    },
    children=[
        html.H1(
            "Pink Morsel Sales Visualiser",
            id="header",
            style={
                "textAlign": "center",
                "color": colors["accent"],
                "marginBottom": "5px",
            },
        ),
        html.P(
            "Were sales higher before or after the price increase on 15 Jan 2021?",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        html.Div(
            style={
                "backgroundColor": colors["panel"],
                "borderRadius": "12px",
                "padding": "20px",
                "maxWidth": "900px",
                "margin": "20px auto",
                "boxShadow": "0 2px 8px rgba(0,0,0,0.1)",
            },
            children=[
                html.Label(
                    "Filter by region:",
                    style={"color": colors["text"], "fontWeight": "bold"},
                ),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                        {"label": "All", "value": "all"},
                    ],
                    value="all",
                    inline=True,
                    labelStyle={"marginRight": "15px", "color": colors["text"]},
                    style={"marginTop": "10px", "marginBottom": "10px"},
                ),
                dcc.Graph(id="sales-chart"),
            ],
        ),
    ],
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value"),
)
def update_chart(region):
    data = df if region == "all" else df[df["Region"] == region]
    data = data.groupby("Date", as_index=False)["Sales"].sum()

    fig = px.line(data, x="Date", y="Sales", title=f"Pink Morsel Sales ({region})")
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales ($)",
        plot_bgcolor=colors["panel"],
        paper_bgcolor=colors["panel"],
        font_color=colors["text"],
    )
    fig.add_vline(x="2021-01-15", line_dash="dash", line_color="red")
    return fig


if __name__ == "__main__":
    app.run(debug=True)
