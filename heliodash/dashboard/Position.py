from datetime import datetime, timezone

import streamlit as st

from heliodash.packages.body_position import plot_body_position

names = st.sidebar.multiselect(
    "Select bodies",
    [
        "Mercury",
        "Venus",
        "Mars",
        "STEREO-A",
        "Parker Solar Probe",
        "Solar Orbiter",
    ],
    [
        "Mercury",
        "Venus",
        "Mars",
        "STEREO-A",
        "Parker Solar Probe",
        "Solar Orbiter",
    ],
)

now = st.sidebar.toggle("Now", value=True)
if now:
    obstime = datetime.now(timezone.utc)
else:
    odate = st.date_input("Observation Date", value=datetime.now(timezone.utc))
    otime = st.time_input("Observation Time", value=datetime.now(timezone.utc))
    obstime = datetime.combine(odate, otime, timezone.utc)

# period = st.sidebar.slider("Period", 1, 1000, 60)
period = st.sidebar.number_input("Days", value=60, step=1)
direction = st.sidebar.selectbox(
    "Direction", ["forward", "backward", "both"], index=1
)
earth_adjust = st.sidebar.toggle("Adjust Earth Position", value=False)
earth_lon = None
if earth_adjust:
    # earth_lon = st.sidebar.selectbox(
    #     "Position",
    #     ["E", "W", "S", "N"],
    #     index=2,
    # )
    earth_lon = st.sidebar.number_input("Position", 0, 360, value=270, step=1)

st.markdown(
    """
    # Positions of Planets and Spacecrafts

    Refs: [Solar-MACH](https://solar-mach.github.io/), [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/), [SunPy](https://docs.sunpy.org/en/stable/generated/gallery/showcase/where_is_stereo.html)
    """
)

with st.spinner("Wait for it...", show_time=True):
    fig = plot_body_position(
        names, obstime, period, direction, earth_adjust, earth_lon
    )
st.pyplot(fig)
