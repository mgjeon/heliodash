import streamlit as st

from heliodash.packages.goes.goes_xray_flux import goes_primary_xray_flux

st.markdown(
    """
    # GOES X-ray Flux

    Source: [NOAA/SWPC](https://www.swpc.noaa.gov/products/goes-x-ray-flux)
    """
)


data_type = st.sidebar.selectbox(
    "Zoom",
    ("6-hour", "1-day", "3-day", "7-day"),
)

kst = st.sidebar.checkbox("KST", value=False)

flare = st.sidebar.toggle("Show flares", value=True)
x = False
m = False
c = False
if flare:
    x = st.sidebar.checkbox("X-class", value=True)
    m = st.sidebar.checkbox("M-class", value=True)
    c = st.sidebar.checkbox("C-class", value=False)
flare_config = {
    "show": flare,
    "X": x,
    "M": m,
    "C": c,
}

with st.spinner("Wait for it...", show_time=True):
    fig = goes_primary_xray_flux(data_type, kst, flare_config)
st.pyplot(fig)
