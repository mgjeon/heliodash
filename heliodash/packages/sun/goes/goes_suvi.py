"""
https://data.ngdc.noaa.gov/platforms/solar-space-observing-satellites/goes
"""


def goes_suvi_image(
    primary=True, products=["094", "131", "171", "195", "284", "304", "map"]
):
    sat_class = "primary" if primary else "secondary"

    root = (
        f"https://services.swpc.noaa.gov/images/animations/suvi/{sat_class}/"
    )
    suffix = "/latest.png"

    info = {}
    for p in products:
        image = root + p + suffix
        info[p] = image

    return info
