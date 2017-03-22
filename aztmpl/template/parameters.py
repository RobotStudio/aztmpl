from az.template.models import Parameter


class LocationParam(Parameter):
    """
    >>> p = LocationParam("South Central US")
    >>> p.serialize(p)['location']['value']
    'South Central US'
    """
    name = "location"
    metadata = { "description": "The location where all azure resources will be deployed." }
    defaultValue = "East US"

    allowedValues = [
        "East US",
        "East US 2",
        "North Central US",
        "South Central US",
        "West US",
        "North Europe",
        "West Europe",
        "East Asia",
        "Southeast Asia",
        "Japan East",
        "Japan West",
        "Australia East",
        "Australia Southeast"
    ]

    def __init__(self, location=None):
        if location:
            self.value = location
        super().__init__()


class HDIClusterParam(Parameter):
    """
    >>> p = HDIClusterParam(value="spark")
    >>> p.serialize(p)['clusterType']['value']
    'spark'
    """
    name = "clusterType"
    defaultValue = "hadoop"
    metadata = "The type of the HDInsight cluster to create."
    allowedValues = [
        "hadoop",
        "hbase",
        "storm",
        "spark",
    ]


class GenericSecureStringParam(Parameter):
    """
    >>> n = GenericSecureStringParam("clusterName", value="asdf")
    >>> n.to_json()
    '{"clusterName": {"type": "securestring", "value": "asdf"}}'
    """
    type = "securestring"


class GenericIntParam(Parameter):
    """
    >>> n = GenericIntParam("clusterWorkerNodeCount", value=3)
    >>> n.to_json()
    '{"clusterWorkerNodeCount": {"type": "int", "value": 3}}'
    """
    type = "int"
