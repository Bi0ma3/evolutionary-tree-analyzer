import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import os
import shutil
from flask import send_from_directory

from handle_upload import parse_uploaded_fasta, save_fasta_and_align
from src.build_tree import build_parsimony_tree, build_likelihood_tree
from src.visualize_tree import visualize_tree

# Set up app and server
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
server = app.server

# Serve static output images via Flask
@server.route("/output/tree_images/<path:filename>")
def serve_tree_image(filename):
    return send_from_directory("output/tree_images", filename)

# File paths
ALIGNED_FASTA = "output/aligned_sequences.fasta"
TREE_FILE_PARS = "output/parsimony_tree.newick"
TREE_IMG_PARS = "output/tree_images/parsimony_tree.png"
TREE_FILE_ML = "output/ml_tree.newick"
TREE_IMG_ML = "output/tree_images/ml_tree.png"

# Theme definitions
app_colors = {
    "light": {"background": "white", "text": "black"},
    "dark": {"background": "#121212", "text": "white"}
}

# Layout
app.layout = html.Div(id="page-container", children=[

    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("🌿 Evolutionary Tree Analyzer"), className="text-center my-4")
        ]),

        dbc.Row([
            dbc.Col([
                dcc.RadioItems(
                    id="theme-toggle",
                    options=[
                        {"label": "🌞 Light", "value": "light"},
                        {"label": "🌙 Dark", "value": "dark"}
                    ],
                    value="light",
                    inline=True,
                    labelStyle={"marginRight": "10px"},
                    style={"textAlign": "center", "marginBottom": "20px"}
                ),

                dcc.Upload(
                    id='upload-fasta',
                    children=html.Div([
                        '📁 Drag and Drop or ',
                        html.A('Select a FASTA File')
                    ]),
                    style={
                        'width': '100%',
                        'height': '80px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px'
                    },
                    multiple=False
                ),

                html.Div(id='file-status'),
                dbc.Button("Analyze", id="analyze-button", color="success", className="mt-3"),
                html.Div(id="analysis-output", className="mt-4")
            ])
        ]),

        # Tooltips
        dbc.Tooltip(
            "Upload a DNA or protein FASTA file. Sequences will be aligned for tree building.",
            target="upload-fasta", placement="bottom"
        ),
        dbc.Tooltip(
            "Run alignment and generate both trees.",
            target="analyze-button", placement="right"
        ),
    ]),

    html.Footer([
        html.Div([
            html.Img(src=app.get_asset_url("PB_logo_noback_solid.png"),
                     style={"height": "50px", "marginRight": "10px"}),
            html.Span("Created by Mae Warner • Pipeline Bio", style={"color": "white", "fontSize": "1rem"})
        ],
        style={
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "center",
            "padding": "10px"
        })
    ], style={"backgroundColor": "#4B0082", "marginTop": "30px"})
])

# Upload feedback
@app.callback(
    Output("file-status", "children"),
    Input("upload-fasta", "contents"),
    State("upload-fasta", "filename")
)
def handle_upload(contents, filename):
    if contents:
        return f"✅ Uploaded file: {filename}"
    return ""

# Tree analysis callback
@app.callback(
    Output("analysis-output", "children"),
    Input("analyze-button", "n_clicks"),
    State("upload-fasta", "contents"),
    State("upload-fasta", "filename")
)
def run_analysis(n_clicks, contents, filename):
    if n_clicks and contents:
        try:
            records = parse_uploaded_fasta(contents)
            num_seqs = len(records)

            align_message = save_fasta_and_align(contents)

            build_parsimony_tree(os.path.abspath(ALIGNED_FASTA), os.path.abspath(TREE_FILE_PARS))
            build_likelihood_tree(os.path.abspath(ALIGNED_FASTA), os.path.abspath(TREE_FILE_ML))

            visualize_tree(os.path.abspath(TREE_FILE_PARS), os.path.abspath(TREE_IMG_PARS), show_plot=False)
            visualize_tree(os.path.abspath(TREE_FILE_ML), os.path.abspath(TREE_IMG_ML), show_plot=False)

            return html.Div([
                html.P(f"✅ Parsed {num_seqs} sequence(s). {align_message}"),
    
                html.Div([
                    html.H5("Parsimony Tree"),
                    html.H5("ML-style Tree", style={"marginTop": "20px"}),
                    html.Div(
                        [
                            html.P("🔍 What's the difference?", style={"fontWeight": "bold"}),
                            html.Ul([
                                html.Li("Parsimony minimizes the number of evolutionary changes. It’s simple and fast."),
                                html.Li("ML-style uses UPGMA with identity-based distances. It can reflect evolutionary rates better.")
                            ])
                        ],
                        style={
                            "backgroundColor": "#f8f9fa",
                            "border": "1px solid #ccc",
                            "borderRadius": "5px",
                            "padding": "10px",
                            "marginTop": "20px",
                            "fontSize": "0.9rem"
                        }
                    )
                ]),

                html.Img(src=f"/output/tree_images/parsimony_tree.png", style={"maxWidth": "100%", "marginTop": "20px"}),
                html.Img(src=f"/output/tree_images/ml_tree.png", style={"maxWidth": "100%", "marginTop": "20px"})
            ])

        except Exception as e:
            return f"❌ Error: {str(e)}"
    return "⚠️ No file uploaded."

# Theme switching
@app.callback(
    Output("page-container", "style"),
    Input("theme-toggle", "value")
)
def update_theme(theme):
    return {
        "backgroundColor": app_colors[theme]["background"],
        "color": app_colors[theme]["text"],
        "minHeight": "100vh",
        "padding": "20px"
    }

# Launch app
def main():
    app.run(debug=False)

if __name__ == "__main__":
    main()