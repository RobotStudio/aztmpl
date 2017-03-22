from .models import Pipeline


class HDInsightHivePipe(Pipeline):
    name = "[variables('pipelineName')]"
    required_parameters = [
        "blobContainer",
        "hiveScriptFolder",
        "hiveScriptFile",
        "storageAccountName",
        "inputBlobFolder",
        "outputBlobFolder",
        "storageAccountName",
    ]

    required_variables = [
        "dataFactoryName",
        "azureStorageLinkedServiceName",
        "hdInsightOnDemandLinkedServiceName",
        "blobInputDatasetName",
        "blobOutputDatasetName",
    ]

    dependsOn = [
      "[variables('dataFactoryName')]",
      "[variables('azureStorageLinkedServiceName')]",
      "[variables('hdInsightOnDemandLinkedServiceName')]",
      "[variables('blobInputDatasetName')]",
      "[variables('blobOutputDatasetName')]"
    ]

    properties = {
      "description": "Pipeline that transforms data using Hive script.",
      "activities": [
        {
          type: "HDInsightHive",
          "typeProperties": {
            "scriptPath": "[concat(parameters('blobContainer'), '/', parameters('hiveScriptFolder'), '/', parameters('hiveScriptFile'))]",
            "scriptLinkedService": "[variables('azureStorageLinkedServiceName')]",
            "defines": {
              "inputtable": "[concat('wasb://', parameters('blobContainer'), '@', parameters('storageAccountName'), '.blob.core.windows.net/', parameters('inputBlobFolder'))]",
              "partitionedtable": "[concat('wasb://', parameters('blobContainer'), '@', parameters('storageAccountName'), '.blob.core.windows.net/', parameters('outputBlobFolder'))]"
            }
          },
          "inputs": [
            {
              name: "[variables('blobInputDatasetName')]"
            }
          ],
          "outputs": [
            {
              name: "[variables('blobOutputDatasetName')]"
            }
          ],
          "policy": {
            "concurrency": 1,
            "retry": 3
          },
          "scheduler": {
            "frequency": "Month",
            "interval": 1
          },
          name: "RunSampleHiveActivity",
          "linkedServiceName": "[variables('hdInsightOnDemandLinkedServiceName')]"
        }
      ],
      "start": "2016-10-01T00:00:00Z",
      "end": "2016-10-02T00:00:00Z",
      "isPaused": False
    }


class HDInsightPySparkPipe(Pipeline):
    name = "[variables('pipelineName')]"
    required_parameters = [
        "blobContainer",
        "sparkScriptFolder",
        "sparkScriptFile",
        "storageAccountName",
        "outputBlobFolder",
        "storageAccountName",
        "storageAccountKey",
    ]

    required_variables = [
        "piplineName",
        "dataFactoryName",
        "azureStorageLinkedServiceName",
        "hdInsightOnDemandLinkedServiceName",
        "blobInputDatasetName",
        "blobOutputDatasetName",
    ]

    dependsOn = [
      "[variables('dataFactoryName')]",
      "[variables('azureStorageLinkedServiceName')]",
      "[variables('hdInsightOnDemandLinkedServiceName')]",
      "[variables('blobInputDatasetName')]",
      "[variables('blobOutputDatasetName')]",
    ]

    properties = {
      "description": "Pipeline that transforms data using PySpark script.",
      "activities": [
        {
          type: "HDInsightMapReduce",
          "typeProperties": {
            "className": "com.adf.sparklauncher.AdfSparkJobLauncher",
            "jarFilePath": "[concat(parameters('blobContainer'), '/com.adf.sparklauncher.jar')]",
            "jarLinkedService": "[variables('azureStorageLinkedServiceName')]",
            "arguments": [
              "--appFile",
              "[parameters('sparkScriptFolder'), '/', parameters('sparkScriptFile'))]",
              "--connectionString",
              "[concat('DefaultEndpointsProtocol=https;AccountName=', parameters('storageAccountName'), ';AccountKey=', parameters('storageAccountKey'))]"
            ],
          },
          "inputs": [
            {
              name: "[variables('blobInputDatasetName')]"
            }
          ],
          "outputs": [
            {
              name: "[variables('blobOutputDatasetName')]"
            }
          ],
          "policy": {
            "concurrency": 1,
            "retry": 3
          },
          "scheduler": {
            "frequency": "Month",
            "interval": 1
          },
          name: "RunSampleHiveActivity",
          "linkedServiceName": "[variables('hdInsightOnDemandLinkedServiceName')]"
        }
      ],
      "start": "2016-10-01T00:00:00Z",
      "end": "2016-10-02T00:00:00Z",
      "isPaused": False
    }
