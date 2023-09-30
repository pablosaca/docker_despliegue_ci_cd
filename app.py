from pathlib import Path

import pandas as pd

from shiny import App, Inputs, Outputs, Session, render, ui, reactive
from htmltools import css

from aux_params import user_input_select, output_model
from _utils import columns_table

name_path = os.path.dirname(__file__)
name_path = os.path.join(name_path, 'model')

style = css(font_weight="bold", color="yellow")

app_ui = ui.page_fluid(
    {"style": "background-color: rgba(176, 242, 194, 0.25)"},
    ui.img(src="uned_image.png", _add_ws=False, style="width: 200px; height: 100px"),
    ui.markdown(
        """
        # Prediction of annual earnings - Shiny Web App
        """,
    ),
    ui.navset_pill(
        ui.nav("Input Data",
               ui.layout_sidebar(
                   user_input_select(),
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
                    )
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
               ui.output_table("table"),
               ui.markdown(
                   """
                   ## Model Output
                   """
               ),
               ui.output_text("txt")
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
        features_table = pd.DataFrame([[input_feature.age(),
                                        input_feature.workclass(),
                                        input_feature.education(),
                                        input_feature.marital_status(),
                                        input_feature.occupation(),
                                        input_feature.relationship(),
                                        input_feature.race(),
                                        input_feature.gender(),
                                        input_feature.capital_gain(),
                                        input_feature.capital_loss(),
                                        input_feature.hours_week(),
                                        input_feature.native_country()
                                        ]
                                       ],
                                      columns=columns_table
                                      )

        # input data table is presented in the app (real values)
        features_table_copy = features_table.copy()  # age value must be normalized

        pred = output_model(df=features_table_copy, path=name_path)
        del features_table_copy

        @output
        @render.text()
        def txt():
            return f"Probability of annual earning more than 50k is: {pred}"

        @output
        @render.table
        def table():
            return features_table

        session.close()


image_dir = Path(__file__).parent / "images"
app = App(app_ui, server, debug=True, static_assets=image_dir)
