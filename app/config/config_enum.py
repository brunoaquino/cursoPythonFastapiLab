from enum import Enum


class ConfigEnum(str, Enum):
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    ENVIRONMENT_DEV = "dev"
    ENVIRONMENT_PROD = "producao"
    ENVIRONMENT_HOMOLOG = "homolog"
