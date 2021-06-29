import enum

api_root = "/api/v1"


class ApiGroup(enum.Enum):
    USER = f"{api_root}/user"
    PROJECT = f"{api_root}/project"
    FLOWER = f"{api_root}/flower"
    SLACK_MEMBER = f"{api_root}/slack"  
