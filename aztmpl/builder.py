class CustomJson:
    def to_json(self):
        return self.json


class Header(CustomJson):
    def __init__(self, schema_ver="2015-01-01", content_ver="1.0.0.0"):
        # Note: no comma at content end since we ",".join() it later
        self.json = f"""{
            "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
            "contentVersion": "1.0.0.0"
            """

class Footer(CustomJson):
    def __init__(self):
        self.json = f"""}"""


class Build:
    def __init__(self, templates=None):
        self.variables = []
        self.parameters = []
        self.resources = []

        self.header = [Header()]
        self.footer = [Footer()]

        for tmpl in templates:
            try:
                # Call add_<model_type> function
                getattr(self, f"add_{tmpl.model_type}")(tmpl)
            except:
                raise AttributeError(f"Unrecognized model_type: {tmpl.model_type}")

    def add_variable(self, template):
        return self.variables.append(template)

    def add_parameter(self, template):
        return self.parameters.append(template)

    def add_resource(self, template):
        return self.resources.append(template)

    def generate(self):
        return ",".join([ obj.to_json() for obj in self.header + \
                                                    self.parameters + \
                                                    self.variables + \
                                                    self.resources + \
                                                    self.outputs ]) + self.footer
