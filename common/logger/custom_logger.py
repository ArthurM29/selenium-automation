import logging.config
import os
from datetime import datetime

import yaml

from common.config.config import Config


def load_logging_config():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    log_config_path = os.path.join(current_dir, 'logging.yaml')
    logs_dir = Config().get('logs_dir')

    try:
        with open(log_config_path, 'rt') as f:
            timestamp = datetime.now().strftime("%d.%m.%Y.%H.%M.%S")
            filepath = os.path.join(logs_dir, f'{timestamp}.log')
            config = yaml.safe_load(f.read())
            config['handlers']['empty_file_handler']['filename'] = filepath
            config['handlers']['pretty_file_handler']['filename'] = filepath
    except yaml.YAMLError as e:
        raise Exception(f"Failed to parse '{log_config_path}'") from e

    logging.config.dictConfig(config)
