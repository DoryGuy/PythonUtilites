
# Using Recursive Functions
def convert_to_json(obj):
    if isinstance(obj, dict):
        return {key: convert_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_json(item) for item in obj]
    else:
        return obj
