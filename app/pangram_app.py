import dash 
import dash_core_components as dcc
import dash_html_components as html

from app.figures.pangram_counts import pangram_counts_barplot

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="My first app", id="title"),

        html.Div(children="Short description of the app", id="short_description"),

        dcc.Graph(
            id="pangram-counts-barplot",
            figure=pangram_counts_barplot
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)