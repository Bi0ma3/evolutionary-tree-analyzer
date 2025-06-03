import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import os, shutil
from flask import send_from_directory

from handle_upload import parse_uploaded_fasta, save_fasta_and_align
from src.build_tree import build_parsimony_tree, build_likelihood_tree
from src.visualize_tree import visualize_tree

# Set up Dash & Flask server
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
server = app.server

# Serve static images
@server.route("/output/tree_images/<path:filename>")
def serve_tree_image(filename):
    return send_from_directory("output/tree_images", filename)

# File paths (unchanged)
ALIGNED_FASTA = "output/aligned_sequences.fasta"
TREE_FILE_PARS  = "output/parsimony_tree.newick"
TREE_IMG_PARS   = "output/tree_images/parsimony_tree.png"
TREE_FILE_ML    = "output/ml_tree.newick"
TREE_IMG_ML     = "output/tree_images/ml_tree.png"

# Theme definitions (unchanged)
app_colors = {
    "light": {"background": "white",   "text": "black"},
    "dark":  {"background": "#121212", "text": "white"}
}

# === Begin NEW layout block ===
app.layout = html.Div(
    id="page-container",
    children=[

        # 1) Top welcome banner
        dbc.Row(
            dbc.Col(
                html.Div(
                    [
                        html.H4("Welcome to SimplePhylo", style={"marginBottom": "0.25rem"}),
                        html.P(
                            "This tool aligns your FASTA sequences (best with 10 or fewer at a time) "
                            "and builds parsimony/ML‐style trees. "
                            "Please be patient—alignments can take a minute or two.",
                            style={"marginTop": "0", "fontSize": "0.95rem"}
                        )
                    ],
                    style={
                        "backgroundColor": "#D4BEF5",  # very light lavender
                        "padding": "10px 20px",
                        "borderRadius": "5px",
                        "marginBottom": "20px"
                    }
                ),
                width=10, className="mx-auto"
            )
        ),

        # 2) Main container (header + upload + button + output)
        dbc.Container(
            [
                # 2a) Header (changed to “SimplePhylo”)
                dbc.Row(
                    dbc.Col(
                        html.H1(
                            "🧬 SimplePhylo",
                            className="text-center my-4",
                            style={"fontWeight": "600"}
                        ),
                    )
                ),

                # 2b) Upload & analyze area
                dbc.Row(
                    dbc.Col(
                        [
                            # Theme toggle (unchanged)
                            dcc.RadioItems(
                                id="theme-toggle",
                                options=[
                                    {"label": "🌞 Light", "value": "light"},
                                    {"label": "🌙 Dark",  "value": "dark"}
                                ],
                                value="light",
                                inline=True,
                                labelStyle={"marginRight": "10px"},
                                style={"textAlign": "center", "marginBottom": "20px"}
                            ),

                            # Upload box (background tinted light purple)
                            dcc.Upload(
                                id="upload-fasta",
                                children=html.Div(
                                    [
                                        "📁 Drag and Drop or ",
                                        html.A("Select a FASTA File")
                                    ]
                                ),
                                style={
                                    "width": "100%",
                                    "height": "80px",
                                    "lineHeight": "60px",
                                    "borderWidth": "1px",
                                    "borderStyle": "dashed",
                                    "borderRadius": "5px",
                                    "textAlign": "center",
                                    "margin": "10px 0",
                                    "backgroundColor": "#F3E5F5",  # light lavender
                                },
                                multiple=False
                            ),

                            # Show file‐status message
                            html.Div(id="file-status"),

                            # Analyze button
                            dbc.Button(
                                "Analyze",
                                id="analyze-button",
                                color="success",
                                className="mt-3"
                            ),

                            # Where analysis‐output (trees, messages, images) appear
                            html.Div(id="analysis-output", className="mt-4")
                        ],
                        width=8, className="mx-auto"
                    )
                ),

                # 2c) Tooltips (unchanged)
                dbc.Tooltip(
                    "Upload a DNA or protein FASTA file. Sequences will be aligned for tree building.",
                    target="upload-fasta", placement="bottom"
                ),
                dbc.Tooltip(
                    "Run alignment and generate both trees.",
                    target="analyze-button", placement="right"
                ),
            ]
        ),

        # 3) Footer with clickable links
        html.Footer(
            dbc.Container(
                dbc.Row(
                    dbc.Col(
                        html.Div(
                            [
                                # “Mae Warner” → LinkedIn
                                html.A(
                                    "Mae Warner",
                                    href="https://www.linkedin.com/in/mae-w",
                                    target="_blank",
                                    style={"color": "white", "marginRight": "15px"}
                                ),
                                # “Pipeline Bio” → TPT store
                                html.A(
                                    "Pipeline Bio",
                                    href="https://www.teacherspayteachers.com/Store/Pipeline-Bio",
                                    target="_blank",
                                    style={"color": "white"}
                                )
                            ],
                            style={"display": "flex", "justifyContent": "center", "alignItems": "center"}
                        )
                    )
                ),
                fluid=True,
                style={"backgroundColor": "#4B0082", "padding": "15px 0"}
            )
        )
    ]
)
# === End NEW layout block ===


# === Callbacks for upload & analysis (UNCHANGED aside from returning updated layout) ===

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

            visualize_tree(
                os.path.abspath(TREE_FILE_PARS),
                os.path.abspath(TREE_IMG_PARS),
                show_plot=False
            )
            visualize_tree(
                os.path.abspath(TREE_FILE_ML),
                os.path.abspath(TREE_IMG_ML),
                show_plot=False
            )

            return html.Div(
                [
                    html.P(f"✅ Parsed {num_seqs} sequence(s). {align_message}"),

                    html.Div(
                        [
                            html.H5("Parsimony Tree"),
                            html.H5("ML‐style Tree", style={"marginTop": "20px"}),
                            html.Div(
                                [
                                    html.P(
                                        "🔍 What's the difference?",
                                        style={"fontWeight": "bold"}
                                    ),
                                    html.Ul(
                                        [
                                            html.Li("Parsimony minimizes evolutionary changes; simple & fast."),
                                            html.Li("ML‐style reflects rates via UPGMA on identity‐based distances.")
                                        ]
                                    )
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
                        ]
                    ),

                    html.Img(
                        src="/output/tree_images/parsimony_tree.png",
                        style={"maxWidth": "100%", "marginTop": "20px"}
                    ),
                    html.Img(
                        src="/output/tree_images/ml_tree.png",
                        style={"maxWidth": "100%", "marginTop": "20px"}
                    )
                ]
            )

        except Exception as e:
            return f"❌ Error: {str(e)}"
    return "⚠️ No file uploaded."


# Theme switching (unchanged)
@app.callback(
    Output("page-container", "style"),
    Input("theme-toggle", "value")
)
def update_theme(theme):
    return {
        "backgroundColor": app_colors[theme]["background"],
        "color":           app_colors[theme]["text"],
        "minHeight":       "100vh",
        "padding":         "20px"
    }


# Run server
def main():
    app.run(debug=False)

if __name__ == "__main__":
    main()
