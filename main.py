from csv_concept_map import ConceptMap

import dash # pip install dash
from dash import html
import dash_interactive_graphviz # pip install dash_interactive_graphviz

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cg = ConceptMap("burglar_alarm")
    cg.from_file("burglar_alarm.csv")

    # Render as png
    cg.render(engine='dot')

    # Print the list of concepts
    print([c.name for c in cg.concepts])

    # Start a Dash app showing the file
    app = dash.Dash(__name__)
    app.layout = html.Div([
        dash_interactive_graphviz.DashInteractiveGraphviz(id="graph", dot_source=cg.dot.source)
    ])
    app.run(debug=False)


