from az.template.models import Resource


class HDIClusterRes(Resource):
    required_parameters = [
        "clusterType",
        "clusterName",
        "clusterUserName",
        "clusterPassword",
        "sshUserName",
        "sshPassword",
        "clusterWorkerNodeCount"
    ]

    required_variables = [
        "previewApiVersion",
        "apiVersion",
        "clusterVersion",
        "clusterStorageAccountName",
        "clusterTierType",
        "headnodeTargetInstanceCount",
        "headnodeInstanceType",
        "workernodeInstanceType",
    ]

    type = "Microsoft.HDInsight/clusters"
    location = "[resourceGroup().location]"
    apiVersion = "[variables('previewApiVersion')]"

    dependsOn = []

    properties = {
        "clusterVersion": "[variables('clusterVersion')]",
        "osType": "Linux",
        "tier": "[variables('clusterTierType')]",
        "clusterDefinition": {
            "kind": "[parameters('clusterType')]",
            "configurations": {
                "gateway": {
                    "restAuthCredential.isEnabled": True,
                    "restAuthCredential.username": "[parameters('clusterUserName')]",
                    "restAuthCredential.password": "[parameters('clusterPassword')]",
                }
            },
            "storageProfile": {
                "storageAccounts": [
                    {
                        "name": "[concat(variables('clusterStorageAccountName'),'.blob.core.windows.net')]",
                        "isDefault": True,
                        "container": "[parameters('clusterName')]",
                        "key": "[listkeys(resourceId('Microsoft.Storage/storageAccounts', variables('clusterStorageAccountName')), variables('apiVersion')).key1]",
                    }
                ]
            },
            "computeProfile": {
                "roles": [
                    {
                        "name": "headnode",
                        "targetInstanceCount": "[variables('headnodeTargetInstanceCount')]",
                        "hardwareProfile": {
                            "vmsize": "[variables('headnodeInstanceType')]",
                        },
                        "osProfile": {
                            "linuxOperatingSystemProfile": {
                                "username": "[parameters('sshUserName')]",
                                "password": "[parameters('sshPassword')]",
                            }
                        }
                    },
                    {
                        "name": "workernode",
                        "targetInstanceCount": "[parameters('clusterWorkerNodeCount')]",
                        "hardwareProfile": {
                            "vmSize": "[variables('workernodeInstanceType')]",
                        },
                        "osProfile": {
                            "linuxOperatingSystemProfile": {
                                "username": "[parameters('sshUserName')]",
                                "password": "[parameters('sshPassword')]",
                            }
                        }
                    }
                ]
            }
        }
    }
