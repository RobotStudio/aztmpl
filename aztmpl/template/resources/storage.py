from az.template.models import Resource


class StorageAccountRes(Resource):
    required_parameters = [
        "location",
        "clusterName",
    ]

    required_variables = [
        "previewApiVersion",
    ]

    name = "[concat(parameters('clusterName'), 'store']"
    type = "Microsoft.Storage/storageAccounts"
    location = "[parameters('location')]"
    apiVersion = "[variables('previewApiVersion')]"
    properties = { "accountType": "Standard_LRS" }

    dependsOn = []
