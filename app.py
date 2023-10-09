import os
import pandas as pd

from shiny import App, Inputs, Outputs, Session, render, ui, reactive
from htmltools import css
from src.aux_params import user_input_select, output_model


name_path = os.path.dirname(__file__)
name_path = os.path.join(name_path, 'model')

style = css(font_weight="bold", color="yellow")

app_ui = ui.page_fluid(
    {"style": "background-color: rgba(255, 128, 128, 0.25)"},
    ui.img(src="uned_image.png", _add_ws=False, style="width: 200px; height: 100px"),
    ui.markdown(
        """
        # Prediction of annual earnings - Shiny Web App
        """,
    ),
    ui.navset_pill(
        ui.nav("Input Data",
               ui.panel_sidebar(
                   user_input_select()

               ),
               ui.panel_main(
                       {"style": "font-weight: bold;"},
                       ui.tags.style(
                           """
                           body {
                               font-family: Dubai
                               }
                           """
                            ),
                        ),
               ),
        ui.nav("Prediction Model",
               ui.tags.style(
                   """
                   body {
                       font-family: Dubai
                       }
                   """
               ),
               ui.markdown(
                   """
                   ## Input Data Table
                   """
               ),
               ui.output_table("table_input"),
               ui.markdown(
                   """
                   ## Model Output
                   """
               ),
               ui.output_table("table_probs"),
               ui.output_table("table_exp")
               ),
    ),
)


def server(input_feature: Inputs, output: Outputs, session: Session):
    # The @reactive.event() causes the function to run only when input.btn is
    # invalidated.

    @reactive.Effect
    @reactive.event(input_feature.btn)
    def out():
        # Input data
        features_table = pd.DataFrame([[input_feature.text()]],
                                      columns=["text"]
                                      )

        probs_df, focus_tokens_df = output_model(features_table, name_path)

        @output
        @render.table
        def table_input():
            return features_table

        @output
        @render.table
        def table_probs():
            return probs_df

        @output
        @render.table
        def table_exp():
            return focus_tokens_df

        session.close()


app = App(app_ui, server, debug=True)
