import json


class Serializable:
    def to_json(self):
        return json.dumps(self, default=self.serialize)


class Parameter(Serializable):
    """
    >>> p = Parameter(name="asdf", value="fdsa")
    >>> p.serialize(p)['asdf']['value']
    'fdsa'
    """
    model_type = "parameter"

    def __init__(self, name=None, param_type=None, metadata=None,
                value=None, default_value=None, allowed_values=None):
        self.name = name if name else self.name

        if param_type:
            self.type = param_type
        else:
            try:
                self.type = self.type
            except AttributeError:
                self.type = 'string'

        if value:
            self.value = value if value else self.value
        elif self.value:
            self.value = value if value else self.value

        if metadata:
            self.metadata = metadata
        elif hasattr(self, "metadata"):
            self.metadata = self.metadata

        if default_value:
            self.defaultValue = default_value
        elif hasattr(self, "defaultValue"):
            self.defaultValue = self.defaultValue

        if allowed_values:
            self.allowedValues = allowed_values
        elif hasattr(self, "allowedValues"):
            self.allowedValues = self.allowedValues

            if self.value and not self.value in self.allowedValues:
                raise AttributeError(
                        f"Parameter value '{self.value}' not one of: {self.allowedValues}")

    def serialize(self, obj):
        resp = {}
        resp[obj.name] = obj.__dict__.copy()
        del resp[obj.name]["name"]
        return resp


class Variable(Serializable):
    """
    >>> v = Variable(name="asdf", value="fdsa")
    >>> v.to_json()
    '{"asdf": "fdsa"}'
    """
    model_type = "variable"

    def __init__(self, name=None, value=None):
        self.name = name if name else self.name

        if value:
            self.value = value
        elif hasattr(self, "value"):
            self.value = self.value
        elif hasattr(self, "defaultValue"):
            self.value = self.defaultValue

        if hasattr(self, "allowedValues") and self.value and \
                    not self.value in self.allowedValues:
            raise AttributeError(
                    f"Variable value {self.value} not in allowed: {self.allowedValues}")

    def serialize(self, obj):
        return { obj.name: obj.value }


class Resource(Serializable):
    """
    >>> r = Resource(name="asdf", type="fdsa", location="123", api_version="321", properties="asdf")
    >>> r.serialize(r)['name']
    'asdf'
    """
    model_type = "resource"

    def __init__(self, name=None, type=None, location=None, api_version=None, properties=None):
        self.name = name if name else self.name
        self.type = type if type else self.type
        self.location = location if location else self.location
        self.apiVersion = api_version if api_version else self.apiVersion
        self.properties = properties if properties else self.properties

    def serialize(self, obj):
        return obj.__dict__.copy()
