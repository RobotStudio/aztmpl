#from az.template.resources.datafactory.models import DataSet
from .models import DataSet


class AzureBlobDS(DataSet):
    name = "[variables('blobInputDatasetName')]",

    required_parameters = [
        "blobContainer",
        "inputBlobFolder",
        "inputBlobName",
    ]

    required_variables = [
        "dataFactoryName",
        "azureStorageLinkedServiceName",
    ]

    dependsOn = [
        "[variables('dataFactoryName')]",
        "[variables('azureStorageLinkedServiceName')]"
    ]

    properties = {
        "type": "AzureBlob",
        "linkedServiceName": "[variables('azureStorageLinkedServiceName')]",
        "typeProperties": {
            "fileName": "[parameters('inputBlobName')]",
            "folderPath": "[concat(parameters('blobContainer'), '/', parameters('inputBlobFolder'))]",
            "format": {
                "type": "TextFormat",
                "columnDelimiter": ","
            },
            "availability": {
            "frequency": "Month",
            "interval": 1
            },
            "external": True
        }
    }
