""" Module for serialization """

import pickle
import yaml
import JsonSerialize as jsn


def load(serialize_method):
    pass



def save(data, file_obj, serialize_method):
    """ serialize data """
    try:
        if serialize_method == "pickle":
            pickle.dump(data, file_obj)
        elif serialize_method == "yaml":
            yaml.dump(data, file_obj, default_flow_style=False)
        elif serialize_method == "json":
            pass
    except ValueError:
        raise Exception("[ERROR]::Serialization failed")

