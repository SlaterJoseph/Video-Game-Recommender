import yaml

path = '../application.yaml'

def retrieve_yaml(data: str) -> str:
    """
    Get data from the yaml file
    :param data: The requested field
    :return: The requested information
    """
    with open(path, 'r') as f:
        file = yaml.safe_load(f)
    return file[data]

def save_field(fields: dict) -> None:
    """
    Saves new fields/replace outdated fields to the yaml file
    :param fields: A list of tuples in (field, value) format
    :return: None
    """
    with open(path, 'a') as f:
        for field in fields.keys():
            yaml.dump({field: fields[field]}, f)
