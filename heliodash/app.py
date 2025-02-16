import streamlit as st


def main():
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
                st.Page(
                    home,
                    title="Home",
                    default=True,
                    icon=":material/home:",
                    url_path="",
                ),
                st.Page(
                    "dashboard/Position.py",
                    title="Positions of Planets and Spacecrafts",
                ),
            ],
            "Sun": [
                st.Page("dashboard/sun/GOES.py", title="GOES"),
            ],
            "Jupiter": [
                st.Page("dashboard/jupiter/Juno.py", title="Juno"),
            ],
        }
    )

    pg.run()


if __name__ == "__main__":
    main()
