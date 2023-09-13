from app.web.config import DatabaseConfig
import yaml


def db_info():
    config_path = "config.yml"
    with open(config_path, "r") as f:
        raw_config = yaml.safe_load(f)

    return DatabaseConfig(**raw_config["database"])


db = db_info()


