import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import os, shutil
from flask import send_from_directory

from handle_upload import parse_uploaded_fasta, save_fasta_and_align
from src.build_tree import build_parsimony_tree, build_likelihood_tree
from src.visualize_tree import visualize_tree

# ─── Set up Dash & Flask server ─────────────────────────────────────────────
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
server = app.server

# Serve static output images
@server.route("/output/tree_images/<path:filename>")
def serve_tree_image(filename):
    return send_from_directory("output/tree_images", filename)

# ─── File paths ──────────────────────────────────────────────────────────────
ALIGNED_FASTA = "output/aligned_sequences.fasta"
TREE_FILE_PARS  = "output/parsimony_tree.newick"
TREE_IMG_PARS   = "output/tree_images/parsimony_tree.png"
TREE_FILE_ML    = "output/ml_tree.newick"
TREE_IMG_ML     = "output/tree_images/ml_tree.png"

# ─── Theme colors (we’ll now only use “light”) ───────────────────────────────
LIGHT_BG = "white"
LIGHT_TEXT = "black"

# ─── Begin UPDATED layout block (no more Light/Dark toggle) ──────────────────
app.layout = html.Div(
    id="page-container",
    # Make the entire page a flex-column so the footer can sit at the bottom
    style={
        "display": "flex",
        "flexDirection": "column",
        "minHeight": "100vh",
        # Watermark background (always visible, dimmed if you like)
        "backgroundImage": f"url('{app.get_asset_url('PB_logo_watermark.png')}')",
        "backgroundSize":  "cover",
        "backgroundPosition": "center",
        "backgroundRepeat":  "no-repeat",
        "backgroundColor": LIGHT_BG,
        "padding": "20px"
    },
    children=[
        # ─── Main “content” wrapper ────────────────────────────────────────
        html.Div(
            # Let this section expand to fill everything above the footer
            style={"flex": "1 0 auto"},
            children=[

                # ─── 1) Top welcome banner ────────────────────────────────────
                dbc.Row(
                    dbc.Col(
                        html.Div(
                            [
                                html.H4("Welcome to SimplePhylo", style={"marginBottom": "0.25rem"}),
                                html.P(
                                    "This tool aligns your FASTA sequences (best with 10 or fewer at a time) "
                                    "and builds parsimony/ML‐style trees. Please be patient—alignments can take a minute or two ✌️💜",
                                    style={"marginTop": "0", "fontSize": "0.95rem"}
                                )
                            ],
                            style={
                                "backgroundColor": "#D4BEF5",   # very light lavender
                                "padding": "10px 20px",
                                "borderRadius": "5px",
                                "marginBottom": "20px",
                                "opacity": "0.95"  # let a bit of the watermark show through
                            }
                        ),
                        width=10, className="mx-auto"
                    )
                ),

                # ─── 2) Main container (header + upload + button + output) ─────
                dbc.Container(
                    children=[

                        # ─── 2a) Header (“SimplePhylo”) ─────────────────────────
                        dbc.Row(
                            dbc.Col(
                                html.H1(
                                    [
                                        # If you ever want the small logo next to the text, uncomment the lines below:
                                        # html.Img(
                                        #     src=app.get_asset_url("PB_logo_noback_solid.png"),
                                        #     style={
                                        #         "height": "36px",
                                        #         "marginRight": "10px",
                                        #         "verticalAlign": "middle"
                                        #     }
                                        # ),
                                        html.Span("🌿 SimplePhylo", style={"verticalAlign": "middle"})
                                    ],
                                    className="text-center my-4",
                                    style={"fontWeight": "600", "color": LIGHT_TEXT}
                                )
                            )
                        ),

                        # ─── 2b) Upload & analyze area ─────────────────────────
                        dbc.Row(
                            dbc.Col(
                                [
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

                                    # ─── Wrap the output in a dcc.Loading spinner ───
                                    dcc.Loading(
                                        id="loading-analysis",
                                        type="circle",      # “circle” spinner
                                        children=html.Div(
                                            id="analysis-output",
                                            className="mt-4"
                                        )
                                    )
                                ],
                                width=8, className="mx-auto"
                            )
                        ),

                        # ─── 2c) Tooltips ───────────────────────────────────────
                        dbc.Tooltip(
                            "Upload a DNA or protein FASTA file. Sequences will be aligned for tree building.",
                            target="upload-fasta", placement="bottom"
                        ),
                        dbc.Tooltip(
                            "Run alignment and generate both trees.",
                            target="analyze-button", placement="right"
                        )
                    ]
                )
            ]
        ),

        # ─── 3) Footer with clickable links and logo ────────────────────────
        html.Footer(
            dbc.Container(
                dbc.Row(
                    dbc.Col(
                        html.Div(
                            [
                                # “Created by:” text
                                html.Span(
                                    "Created by:",
                                    style={"color": "white", "marginRight": "8px", "fontSize": "0.9rem"}
                                ),

                                # Tiny logo → LinkedIn
                                html.A(
                                    html.Img(
                                        src=app.get_asset_url("PB_logo_noback_solid.png"),
                                        style={
                                            "height": "24px",
                                            "marginRight": "5px",
                                            "verticalAlign": "middle"
                                        }
                                    ),
                                    href="https://www.linkedin.com/in/mae-w",
                                    target="_blank",
                                    title="Mae Warner on LinkedIn"
                                ),

                                # “Mae Warner” → LinkedIn
                                html.A(
                                    "Mae Warner",
                                    href="https://www.linkedin.com/in/mae-w",
                                    target="_blank",
                                    style={
                                        "color": "white",
                                        "marginRight": "12px",
                                        "verticalAlign": "middle",
                                        "fontSize": "0.9rem"
                                    }
                                ),

                                # Heart separator
                                html.Span(
                                    "🤍",
                                    style={"marginRight": "12px", "fontSize": "1rem", "verticalAlign": "middle"}
                                ),

                                # “Pipeline Bio” → Teachers Pay Teachers
                                html.A(
                                    "Pipeline Bio",
                                    href="https://www.teacherspayteachers.com/Store/Pipeline-Bio",
                                    target="_blank",
                                    style={"color": "white", "fontSize": "0.9rem", "verticalAlign": "middle"}
                                )
                            ],
                            style={
                                "display": "flex",
                                "justifyContent": "center",
                                "alignItems": "center",
                                "padding": "10px 0"
                            }
                        )
                    )
                ),
                fluid=True,
                # Push footer to bottom with "marginTop: auto"
                style={"backgroundColor": "#4B0082", "marginTop": "auto"}
            )
        )
    ]
)
# ─── End UPDATED layout block ────────────────────────────────────────────────


# ─── Callbacks for upload & analysis (UNCHANGED aside from loading spinner) ───

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

            # Build both trees:
            build_parsimony_tree(
                os.path.abspath(ALIGNED_FASTA),
                os.path.abspath(TREE_FILE_PARS)
            )
            build_likelihood_tree(
                os.path.abspath(ALIGNED_FASTA),
                os.path.abspath(TREE_FILE_ML)
            )

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

            # Now return a container that places each H5 immediately above its own image:
            return html.Div(
                [
                    # 1) Status paragraph
                    html.P(f"✅ Parsed {num_seqs} sequence(s). {align_message}"),

                    # 2) “What’s the difference?” explanation block (unchanged)
                    html.Div(
                        [
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

                    # 3) Parsimony Tree section (label + image)
                    html.Div(
                        [
                            html.H5("Parsimony Tree", style={"marginTop": "20px"}),
                            html.Img(
                                src="/output/tree_images/parsimony_tree.png",
                                style={"maxWidth": "100%", "marginTop": "10px"}
                            )
                        ]
                    ),

                    # 4) ML‐style Tree section (label + image)
                    html.Div(
                        [
                            html.H5("ML‐style Tree", style={"marginTop": "20px"}),
                            html.Img(
                                src="/output/tree_images/ml_tree.png",
                                style={"maxWidth": "100%", "marginTop": "10px"}
                            )
                        ]
                    )
                ]
            )

        except Exception as e:
            return f"❌ Error: {str(e)}"

    # If the user hasn’t uploaded a file yet:
    return "⚠️ No file uploaded."


# ─── Run server ───────────────────────────────────────────────────────────────
def main():
    app.run(debug=False)

if __name__ == "__main__":
    main()
