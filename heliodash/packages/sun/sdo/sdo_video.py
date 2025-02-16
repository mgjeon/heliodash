def sdo_video(
    products=[],
):
    product_information = {
        "0094": r"AIA 094 $\AA$",
        "0131": r"AIA 131 $\AA$",
        "0171": r"AIA 171 $\AA$",
        "0193": r"AIA 193 $\AA$",
        "0211": r"AIA 211 $\AA$",
        "0304": r"AIA 304 $\AA$",
        "0335": r"AIA 335 $\AA$",
        "1600": r"AIA 1600 $\AA$",
        "1700": r"AIA 1700 $\AA$",
    }

    root = "https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_"
    suffix = ".mp4"
    info = {}
    for p in products:
        video = root + p + suffix
        info[p] = video

    return info, product_information
