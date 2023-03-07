def update_ydl_opts(preferredcodec: str) -> dict:
    """
    update_ydl_opts

    Parameters
    ----------
    preferredcodec : str
        data type

    Returns
    -------
    dict
        youtube download option
    """
    ydl_opts = {
        "format": "bestaudio",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": preferredcodec,
            }
        ],
    }
    return ydl_opts
