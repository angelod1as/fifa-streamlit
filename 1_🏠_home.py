import webbrowser
import streamlit as st
from get_data import get_data

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

get_data()

st.markdown("# FIFA23 OFFICIAL DATASET! ⚽️")

st.sidebar.markdown(
    """
    Developed by [Angelo Dias](https://angelodias.com.br)

    Source: [Asimov Academy](https://asimov.academy)
    """
)

btn = st.button("View complete dataset on Kaggle")
if btn:
    webbrowser.open_new_tab(
        "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    """
    The 2023 Football Players Dataset provides comprehensive information
    on professional football players.

    The dataset contains a wide range of
    attributes, including player demographics, physical characteristics,
    match statistics, contract details, and club affiliations.

    With over
    17,000 records, the full dataset provides a valuable resource for football
    analysts, researchers, and enthusiasts interested in exploring various
    aspects of the world of football, as it allows them to study player
    attributes, performance metrics, market valuation, club analysis,
    player positioning, and player development over time.
    """
)
