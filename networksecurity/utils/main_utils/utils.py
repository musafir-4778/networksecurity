import yaml
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import os, sys
import numpy as np
import dill
import pickle

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e

def write_yaml_file(file_path: str, content: dict, replace: bool = False) -> None:
    """
    Writes a dictionary or serializable content to a YAML file.

    :param file_path: Path where the YAML file will be written.
    :param content: Dictionary or serializable content to write.
    :param replace: If True, replaces existing file; if False, skips writing if file exists.
    """
    try:
        if replace or not os.path.exists(file_path):
            with open(file_path, "w") as file:
                yaml.dump(content, file)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e
