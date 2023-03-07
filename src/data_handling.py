import json
import urllib.request


def read_conv_conf(conf_path: str = "conv_conf.json") -> dict:
    """
    Read the json config file

    Parameters
    ----------
    conf_path : str, optional
        path to config .json, by default 'conv_conf.json'

    Returns
    -------
    dict
        information for further processing
    """
    return json.load(open(conf_path))


def overwrite_conv_conf(new_config: dict) -> None:
    """
    overwrite_conv_conf updates the json configuration file.

    Parameters
    ----------
    config : dict
        configuration dataclass with .__dict__ method
    """
    with open("conv_conf.json", "w") as fp:
        json.dump(new_config, fp)
    print(f"Config is changed to: \n {new_config}")


def remove_word(title: str) -> str:
    """
    deletes the given words from "delete_words.txt" inside a string.

    Parameters
    ----------
    title : str
        string that has to be checked

    Returns
    -------
    str
        cheared string
    """
    f = open("delete_words.txt", "r")
    del_wrds = f.read().split("\n")
    for wrds in del_wrds:
        title = title.replace(wrds, "")
    return title


def get_title_from_url(url: str, substitute_str: bool = True) -> str:
    """
    Extract the video title from a YouTube url.

    Parameters
    ----------
    url : str
        video url
    substitute_str : bool, optional
        enable or diable word substitution, by default True

    Returns
    -------
    str
        title, by default cleared string
    """
    with urllib.request.urlopen(url) as url:
        title = url.read().decode("utf-8")
        title = title.split("<title>")[1]
        title = title.split("- YouTube</title>")[0]
        print(title)
        if substitute_str:
            title = remove_word(title)
    return title
