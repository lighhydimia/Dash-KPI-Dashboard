import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv("sample_data.csv")

app = dash.Dash(__name__)

fig_sales = px.line(df, x="month", y="sales", title="Monthly Sales")
fig_customers = px.bar(df, x="month", y="customers", title="Customer Growth")

app.layout = html.Div(children=[
    html.H1("Business KPI Dashboard"),
    dcc.Graph(figure=fig_sales),
    dcc.Graph(figure=fig_customers),
])

if __name__ == "__main__":
    app.run_server(debug=True)
