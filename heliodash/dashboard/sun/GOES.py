import streamlit as st

from heliodash.packages.sun.goes.goes_proton_flux import goes_proton_flux
from heliodash.packages.sun.goes.goes_suvi import goes_suvi_image
from heliodash.packages.sun.goes.goes_xray_flux import goes_xray_flux

plot_type = st.selectbox(
    "Plot Type",
    ("GOES X-ray Flux", "GOES Proton Flux", "GOES SUVI Images"),
)
primary = st.sidebar.toggle("Primary", value=True)

if plot_type == "GOES X-ray Flux" or plot_type == "GOES Proton Flux":
    data_type = st.sidebar.selectbox(
        "Zoom",
        ("6-hour", "1-day", "3-day", "7-day"),
    )

    kst = st.sidebar.checkbox("KST", value=False)

    if plot_type == "GOES X-ray Flux":
        flare = st.sidebar.toggle("Show Flares", value=True)
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

        # GOES X-ray Flux
        st.markdown(
            """
            # GOES X-ray Flux

            Source: [NOAA/SWPC](https://www.swpc.noaa.gov/products/goes-x-ray-flux)
            """
        )
        with st.spinner("Wait for it...", show_time=True):
            fig = goes_xray_flux(
                data_type=data_type,
                primary=primary,
                kst=kst,
                flare_config=flare_config,
            )
        st.pyplot(fig)
    elif plot_type == "GOES Proton Flux":
        # GOES Proton Flux
        st.markdown(
            """
            # GOES Proton Flux

            Source: [NOAA/SWPC](https://www.swpc.noaa.gov/products/goes-proton-flux)
            """
        )
        with st.spinner("Wait for it...", show_time=True):
            fig = goes_proton_flux(
                data_type=data_type, primary=primary, kst=kst
            )
        st.pyplot(fig)

if plot_type == "GOES SUVI Images":
    products = st.sidebar.multiselect(
        "Products",
        ["094", "131", "171", "195", "284", "304", "map"],
        ["094", "131", "171", "195", "284", "304", "map"],
    )

    # GOES SUVI Images
    info = goes_suvi_image(primary=primary, products=products)
    st.markdown(
        """
        # GOES SUVI Images

        Source: [NOAA/SWPC](https://www.swpc.noaa.gov/products/goes-solar-ultraviolet-imager-suvi)
        """
    )
    for wl, image in info.items():
        st.image(image, use_container_width=True)
