from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

DATA_FILE = Path(__file__).with_name("WK1_Airbnb_Amsterdam_listings_proj_solution.csv")
COLUMNS = [
    "Airbnb Listing ID",
    "Price",
    "Latitude",
    "Longitude",
    "Meters from chosen location",
    "Location",
]

st.set_page_config(page_title="Amsterdam Airbnb Explorer", page_icon="🏠", layout="wide")


@st.cache_data
def load_data() -> pd.DataFrame:
    """Load the project dataset and attach descriptive location labels."""
    dataframe = pd.read_csv(DATA_FILE, names=COLUMNS)
    dataframe["Airbnb Listing ID"] = dataframe["Airbnb Listing ID"].astype(int)
    dataframe["Location"] = dataframe["Location"].replace(
        {1.0: "Point of interest", 0.0: "Airbnb listing"}
    )
    return dataframe


dataframe = load_data()
point_of_interest = dataframe[dataframe["Location"] == "Point of interest"].copy()
listings = dataframe[dataframe["Location"] == "Airbnb listing"].copy()

st.title("Amsterdam Airbnb Explorer")
st.caption(
    "Explore Amsterdam Airbnb listings by nightly budget and distance from the selected point of interest."
)

min_price = int(listings["Price"].min())
max_price = int(listings["Price"].max())
default_budget = min(100, max_price)

budget = st.sidebar.slider(
    "Maximum nightly budget (£)",
    min_value=min_price,
    max_value=max_price,
    value=max(default_budget, min_price),
)

filtered_listings = listings[listings["Price"] <= budget].copy()

metric_1, metric_2, metric_3 = st.columns(3)
metric_1.metric("Matching listings", f"{len(filtered_listings):,}")
metric_2.metric(
    "Average nightly price",
    f"£{filtered_listings['Price'].mean():.2f}" if not filtered_listings.empty else "N/A",
)
metric_3.metric(
    "Closest listing",
    f"{filtered_listings['Meters from chosen location'].min() / 1000:.2f} km"
    if not filtered_listings.empty
    else "N/A",
)

st.subheader("Listings")
if filtered_listings.empty:
    st.warning("No listings match the selected budget.")
else:
    display_table = filtered_listings.copy()
    display_table["Price"] = display_table["Price"].map(lambda value: f"£{value:.2f}")
    display_table["Distance (km)"] = (
        display_table["Meters from chosen location"] / 1000
    ).round(2)
    display_table = display_table.drop(columns=["Meters from chosen location", "Location"])
    st.dataframe(display_table, use_container_width=True, hide_index=True)

    map_data = pd.concat([filtered_listings, point_of_interest], ignore_index=True)

    st.subheader("Map")
    figure = px.scatter_map(
        map_data,
        lat="Latitude",
        lon="Longitude",
        color="Location",
        zoom=10,
        height=600,
        hover_name="Location",
        hover_data={
            "Airbnb Listing ID": True,
            "Price": ":.2f",
            "Meters from chosen location": True,
            "Latitude": False,
            "Longitude": False,
        },
        labels={"Location": "Type", "Price": "Nightly price (£)"},
        map_style="open-street-map",
    )
    figure.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(figure, use_container_width=True)

st.markdown(
    "---\nEducational data-visualization project. Not affiliated with or endorsed by Airbnb."
)
