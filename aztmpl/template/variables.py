from aztmpl.template.models import Variable


class ApiVersion(Variable):
    """
    >>> av = ApiVersion(name="defaultApiVersion")
    >>> av.to_json()
    '{"defaultApiVersion": "2015-02-28-Preview"}'
    """
    name = "apiVersion"
    defaultValue = "2015-02-28-Preview"
    allowedValues = [
        "2016-09-01",           # Service REST API
        "2015-02-28-Preview",   # Service REST API Preview
        "2015-08-19",           # Management REST API
    ]
