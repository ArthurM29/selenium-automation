import yaml


class Config:
    def __init__(self, file_path):
        with open(file_path, 'r') as yaml_file:
            try:
                self.configs = yaml.safe_load(yaml_file)
            except yaml.YAMLError as e:
                raise Exception(f"Failed to parse '{file_path}'") from e

    def get(self, key):
        key = key.lower()
        if self.configs.get(key) is None:
            raise Exception(f"The config file does not contain '{key}'.")
        return self.configs.get(key)
