import streamlit as st

st.set_page_config(
    page_title="Heliosphere Dashboard (HelioDash)",
    page_icon="☀️",
)


def home():
    st.markdown(
        """
        # Heliosphere Dashboard (HelioDash)

        Heliosphere Dashboard (HelioDash) is an open-source tool for visualizing heliosphere-related data.

        ## Available Pages
        - [GOES](/GOES)
        - [Juno](/Juno)

    """
    )


pg = st.navigation(
    {
        "Overview": [
            # Load pages from functions
            st.Page(
                home,
                title="Home",
                default=True,
                icon=":material/home:",
                url_path="",
            ),
        ],
        "Dashboard": [
            st.Page("dashboard/1_GOES.py", title="GOES"),
            st.Page("dashboard/2_Juno.py", title="Juno"),
        ],
    }
)

pg.run()
