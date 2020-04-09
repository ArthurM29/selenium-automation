import yaml


class Config:
    #TODO change hard coded path
    CONFIG_PATH = '/Users/amanasyan/PycharmProjects/selenium-automation/common/config/config.yaml'

    def __init__(self):
        with open(self.CONFIG_PATH, 'r') as yaml_file:
            try:
                self.configs = yaml.safe_load(yaml_file)
            except yaml.YAMLError as e:
                raise Exception(f"Failed to parse '{self.CONFIG_PATH}'") from e

    def get(self, key):
        key = key.lower()
        if self.configs.get(key) is None:
            raise Exception(f"The config file does not contain '{key}'.")
        return self.configs.get(key)
