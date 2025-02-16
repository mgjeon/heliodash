def sdo_image(
    products=[],
    pfss=False,
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
        # "211193171": r"AIA 211, 193, 171 $\AA$",
        "HMIB": r"HMI Magnetogram",
        "304_211_171": r"AIA 304, 211, 171 $\AA$",
        "094_335_193": r"AIA 094, 335, 193 $\AA$",
        "HMImag_171": r"AIA 171 $\AA$ & HMI Magnetogram",
        "HMIBC": r"HMI Colorized Magnetogram",
        "HMIIC": r"HMI Intensitygram - Colored",
        "HMIIF": r"HMI Intensitygram - Flattened",
        "HMII": r"HMI Intensitygram",
        "HMID": r"HMI Dopplergram",
    }

    products_4096 = [
        "0094",
        "0131",
        "0171",
        "0193",
        "0211",
        "0304",
        "0335",
        "1600",
        "1700",
        "211193171",
        "HMIB",
    ]
    root_4096 = "https://sdo.gsfc.nasa.gov/assets/img/latest/latest_4096_"
    suffix = ".jpg"
    info = {}
    for p in products:
        if p not in products_4096:
            continue
        image = root_4096 + p + suffix
        info[p] = image
        if pfss:
            image = root_4096 + p + "pfss" + suffix
            info[p] = image

    products_f = ["304_211_171", "094_335_193", "HMImag_171"]
    root_f = "https://sdo.gsfc.nasa.gov/assets/img/latest/f_"
    for p in products:
        if p not in products_f:
            continue
        image = root_f + p + suffix
        info[p] = image
        if pfss:
            image = root_f + p + "pfss" + suffix
            info[p] = image

    products_4096_nopfss = ["HMIBC", "HMIIC", "HMIIF", "HMII", "HMID"]
    for p in products:
        if p not in products_4096_nopfss:
            continue
        image = root_4096 + p + suffix
        info[p] = image

    return info, product_information
