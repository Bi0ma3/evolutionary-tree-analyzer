import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import os
import shutil
from flask import send_from_directory

from handle_upload import parse_uploaded_fasta, save_fasta_and_align
from src.build_tree import build_parsimony_tree
from src.visualize_tree import visualize_tree

# Define paths
ALIGNED_FASTA = "output/aligned_sequences.fasta"
TREE_FILE = "output/parsimony_tree.newick"
TREE_IMG = "output/tree_images/parsimony_tree.png"
ASSET_PATH = "output/tree_images"

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = "Evolutionary Tree Analyzer"

# Route to serve image from output directory
@app.server.route("/output/tree_images/<path:filename>")
def serve_tree_image(filename):
    return send_from_directory(ASSET_PATH, filename)

# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("🌿 Evolutionary Tree Analyzer"), className="text-center my-4")
    ]),
    dbc.Row([
        dbc.Col([
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
    ])
])

# File upload feedback
@app.callback(
    Output("file-status", "children"),
    Input("upload-fasta", "contents"),
    State("upload-fasta", "filename")
)
def handle_upload(contents, filename):
    if contents:
        return f"✅ Uploaded file: {filename}"
    return ""

# Trigger analysis
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

            build_parsimony_tree(os.path.abspath(ALIGNED_FASTA), os.path.abspath(TREE_FILE))

            visualize_tree(
                os.path.abspath(TREE_FILE),
                os.path.abspath(TREE_IMG),
                show_plot=False
            )

            return (
                f"✅ Parsed {num_seqs} sequence(s). {align_message}",
                html.Img(src="/output/tree_images/parsimony_tree.png", style={"maxWidth": "100%", "marginTop": "20px"})
            )
        except Exception as e:
            return (f"❌ Error: {str(e)}", "")
    return ("⚠️ No file uploaded.", "")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
