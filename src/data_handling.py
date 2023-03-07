import json


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
