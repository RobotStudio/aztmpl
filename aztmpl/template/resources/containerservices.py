from aztmpl.template.models import Resource


class ContainerServicesRes(Resource):
    required_parameters = [
        "dnsNamePrefix",
        "orchestratorType",
        "masterCount",
        "agentCount",
        "agentVMSize",
        "servicePrincipalClientId",
        "servicePrincipalClientSecret",
    ]

    required_variables = [
        "apiVersion",
        "servicePrincipalFields",
        "adminUsername",
        "sshRSAPublicKey",
    ]

    type = "Microsoft.ContainerService/containerServices"
    location = "[resourceGroup().location]"
    apiVersion = "[variables('apiVersion')]"

    dependsOn = []

    variables = {
      "mastersEndpointDNSNamePrefix":"[concat(parameters('dnsNamePrefix'),'mgmt')]",
      "agentsEndpointDNSNamePrefix":"[concat(parameters('dnsNamePrefix'),'agents')]",
      "useServicePrincipalDictionary": {
        "DCOS": 0,
        "Swarm": 0,
        "Kubernetes": 1
      },
      "useServicePrincipal": "[variables('useServicePrincipalDictionary')[parameters('orchestratorType')]]",
      "servicePrincipalFields": [
        None,
        {
          "ClientId": "[parameters('servicePrincipalClientId')]",
          "Secret": "[parameters('servicePrincipalClientSecret')]"
        }
      ],
    }

    properties = {
      "orchestratorProfile": {
        "orchestratorType": "[parameters('orchestratorType')]"
      },
      "masterProfile": {
        "count": "[parameters('masterCount')]",
        "dnsPrefix": "[variables('mastersEndpointDNSNamePrefix')]"
      },
      "agentPoolProfiles": [
        {
          "name": "agentpools",
          "count": "[parameters('agentCount')]",
          "vmSize": "[parameters('agentVMSize')]",
          "dnsPrefix": "[variables('agentsEndpointDNSNamePrefix')]"
        }
      ],
      "linuxProfile": {
        "adminUsername": "[variables('adminUsername')]",
        "ssh": {
          "publicKeys": [
            {
              "keyData": "[variables('sshRSAPublicKey')]"
            }
          ]
        }
      },
      "servicePrincipalProfile": "[variables('servicePrincipalFields')[variables('useServicePrincipal')]]"
    }

    outputs = {
        "masterFQDN": {
            "type": "string",
            "value": "[reference(concat('Microsoft.ContainerService/containerServices/', 'containerservice-', resourceGroup().name)).masterProfile.fqdn]"
        },
        "sshMaster0": {
            "type": "string",
            "value": "[concat('ssh ', variables('adminUsername'), '@', reference(concat('Microsoft.ContainerService/containerServices/', 'containerservice-', resourceGroup().name)).masterProfile.fqdn, ' -A -p 22')]"
        },
        "agentFQDN": {
            "type": "string",
            "value": "[reference(concat('Microsoft.ContainerService/containerServices/', 'containerservice-', resourceGroup().name)).agentPoolProfiles[0].fqdn]"
        }
    }
