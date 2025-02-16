import streamlit as st

from heliodash.packages.sun.sdo.sdo_image import sdo_image
from heliodash.packages.sun.sdo.sdo_video import sdo_video

st.markdown(
    """
    # SDO

    Source: [NASA/SDO](https://sdo.gsfc.nasa.gov/)
    """
)

plot_type = st.selectbox(
    "Plot Type",
    ("Image", "Video"),
)

if plot_type == "Image":
    list_of_products = (
        "0094",
        "0131",
        "0171",
        "0193",
        "0211",
        "0304",
        "0335",
        "1600",
        "1700",
    )
    list_of_products += ("304_211_171", "094_335_193", "HMImag_171")
    list_of_products += ("HMIB", "HMIBC")
    list_of_products += ("HMII", "HMIIC", "HMIIF", "HMID")

    products = st.sidebar.multiselect(
        "Products",
        list_of_products,
        list_of_products,
    )
    pfss = st.sidebar.toggle("PFSS", value=False)

    info, prod_info = sdo_image(products=products, pfss=pfss)

    for p in products:
        st.image(info[p], caption=prod_info[p], use_container_width=True)

if plot_type == "Video":
    list_of_products = (
        "0094",
        "0131",
        "0171",
        "0193",
        "0211",
        "0304",
        "0335",
        "1600",
        "1700",
    )

    products = st.sidebar.multiselect(
        "Products",
        list_of_products,
        list_of_products,
    )

    info, prod_info = sdo_video(products=products)

    for p in products:
        st.video(info[p], start_time=0, loop=True, autoplay=True)
