from .models import LinkedService


class DataFactoryLS(LinkedService):
        name = "[variables('azureStorageLinkedServiceName')]"

        required_parameters = [
            "storageAccountName",
            "storageAccountKey",
        ]

        required_variables = [
            "azureStorageLinkedServiceName",
            "dataFactoryName",
            "apiVersion",
        ]

        dependsOn = [
          "[variables('dataFactoryName')]"
        ]

        apiVersion = "[variables('apiVersion')]"

        properties = {
          type: "AzureStorage",
          "description": "Azure Storage linked service",
          "typeProperties": {
          "connectionString": "[concat('DefaultEndpointsProtocol=https;AccountName=',parameters('storageAccountName'),';AccountKey=',parameters('storageAccountKey'))]"
          }
        }


class HDInsightLS(LinkedService):
        name = "[variables('hdInsightOnDemandLinkedServiceName')]"

        required_parameters = []

        required_variables = [
            "azureStorageLinkedServiceName",
            "hdInsightOnDemandLinkedServiceName",
            "hdInsightOnDemandClusterSize",
            "hdInsightOnDemandVersion",
            "dataFactoryName",
            "apiVersion",
        ]

        dependsOn = [
          "[variables('dataFactoryName')]",
          "[variables('azureStorageLinkedServiceName')]"
        ]

        apiVersion = "[variables('apiVersion')]"

        properties = {
          type: "HDInsightOnDemand",
          "typeProperties": {
            "clusterSize": "[variables('hdInsightOnDemandClusterSize')]",
            "version": "[variables('hdInsightOnDemandVersion')]",
            "timeToLive": "00:05:00",
            "osType": "linux",
            "linkedServiceName": "[variables('azureStorageLinkedServiceName')]"
          }
        }
