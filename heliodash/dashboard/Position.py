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
earth_align = st.sidebar.toggle("Plot Earth at South", value=False)

st.markdown(
    """
    # Positions of Planets and Spacecrafts

    Source: [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/), [SunPy](https://docs.sunpy.org/en/stable/api/sunpy.coordinates.frames.HeliocentricInertial.html)
    """
)

fig = plot_body_position(names, obstime, period, direction, earth_align)
st.pyplot(fig)
