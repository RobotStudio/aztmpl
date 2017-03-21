from az.template.models import Serializable

import json


class LinkedService(Serializable):
    """
    >>> ls = LinkedService(name="asdf", depends_on=["321", 321], properties="asdf")
    >>> ls.serialize(ls)['name']
    'asdf'
    """
    def __init__(self, name=None, api_version=None, depends_on=None, properties=None):
        self.name = name if name else self.name
        self.type = "linkedservices"

        if depends_on:
            self.dependsOn = depends_on
        elif hasattr(self, "dependsOn"):
            self.dependsOn = self.dependsOn

        if api_version:
            self.apiVersion = api_version if api_version else self.apiVersion
        else:
            try:
                self.apiVersion = self.apiVersion
            except:
                self.apiVersion = "[parameters('defaultApiVersion')]"

        self.properties = properties if properties else self.properties

    def serialize(self, obj):
        return obj.__dict__.copy()


class DataSet(LinkedService):
    """
    >>> ds = DataSet(name="asdf", depends_on=["321", 321], properties="asdf")
    >>> ds.serialize(ds)['name']
    'asdf'
    """
    type = "datasets"


class Pipeline(LinkedService):
    """
    >>> p = Pipeline(name="asdf", depends_on=["321", 321], properties="asdf")
    >>> p.serialize(p)['name']
    'asdf'
    """
    type = "datapipelines"
