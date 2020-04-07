import logging.config
import os
from datetime import datetime

import yaml


def load_logging_config(logs_dir):
    path = 'common/custom_logger/logging.yaml'
    try:
        with open(path, 'rt') as f:
            timestamp = datetime.now().strftime("%d.%m.%Y.%H.%M.%S")
            filepath = os.path.join(logs_dir, f'{timestamp}.log')
            config = yaml.safe_load(f.read())
            config['handlers']['empty_file_handler']['filename'] = filepath
            config['handlers']['pretty_file_handler']['filename'] = filepath
    except yaml.YAMLError as e:
        raise Exception(f"Failed to parse '{path}'") from e

    logging.config.dictConfig(config)
