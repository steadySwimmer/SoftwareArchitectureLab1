""" Module for serialization """

import pickle
import yaml
import JsonSerialize as jsn


def load(file_obj, serialize_method):
    """ deserialize data """
    if serialize_method == "pickle":
        return pickle.load(file_obj)
    elif serialize_method == "yaml":
        return yaml.load(file_obj)
    elif serialize_method == "json":
        return jsn.jload(file_obj)



def save(data, file_obj, serialize_method):
    """ serialize data """
    try:
        if serialize_method == "pickle":
            pickle.dump(data, file_obj)
        elif serialize_method == "yaml":
            yaml.dump(data, file_obj, default_flow_style=False)
        elif serialize_method == "json":
            jsn.jdump(data, file_obj)
    except ValueError:
        raise Exception("[ERROR]::Serialization failed")

