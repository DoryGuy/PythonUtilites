"""
Using Recursive Functions traverse the object.
"""

def convert_to_json(obj):
    """ convert a dictionary or list to an object for easy serialization """
    if isinstance(obj, dict):
        return {key: convert_to_json(value) for key, value in obj.items()}
    if isinstance(obj, list):
        return [convert_to_json(item) for item in obj]
    return obj
