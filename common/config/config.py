import os

import yaml


class Config:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(current_dir, 'config.yaml')

    def __init__(self):
        with open(self.config_path, 'r') as yaml_file:
            try:
                self.configs = yaml.safe_load(yaml_file)
            except yaml.YAMLError as e:
                raise Exception(f"Failed to parse '{self.config_path}'") from e

    def get(self, key):
        key = key.lower()
        if self.configs.get(key) is None:
            raise Exception(f"The config file does not contain '{key}'.")
        return self.configs.get(key)
