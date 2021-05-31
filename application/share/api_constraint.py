import enum

api_root = "/api/v1"


class ApiGroup(enum.Enum):
    USER = f"{api_root}/user"
