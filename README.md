# Azure Resource Manager (ARM) Template Generator

This is a set of Python 3 utilities to assist with the generation of Azure ARM templates used for cloud automation and resource management.

**Note that this project is currently a work in progress and is not currently functional.**

## About

This project aims to component-ize Azure resources using a software model to allow for automation, generation, and eventual deployment of complex architectures.  While it aims to be possible to build out your entire infrastructure using templates, it's better suited to working with your projects, either as a utility or an inclusion to your applications for maintaining consistency across environments.

While this library and it's scripts generate ARM templates, a good accompaniment to this library would be a tool to actually deploy the templates that you generate.  There's a lot of ways to accomplish this, some of which are the Azure CLI, the portal, Powershell, an SDK, the REST API, or any number of 3rd party tools.

### Infrastructure As Code

While the utilitary functions of generating Azure ARM templates is pretty self-explanatory, deploying a cloud infrastructure in the form of an application can be beneficial for at least the following reasons:
* Maintainability - Use source control to manage versions of your cloud deployments.
* Portability - All developers can be on the same page in terms of the resources and requirements.
* Dynamic generation - If you're service needs change on a regular basis, you can generate new templates on the fly to meet availability, performance, load, or cost requirements.

### Why ARM templates?

ARM templates, similar to AWS Cloud Formation templates, are essentially infrastructure definitions.  This means that while you may have to learn a new format for these documents, you won't have to learn a new programming language to use them.  While this project is writting in Python, it can be ported easily, and if changes come to the API, it's less of a code change than it is a template change.  This means too that you can build templates in one environment and deploy them from another (perhaps, more secure) environment.

### When not to use this project

* If you have Visual Studio, you can actually use it to perform the necessary work for accomplishing what this library sets out to do, but with the help of Microsoft.
* If you just need to get a template to do X.  Azure's portal allows you to walk through creating services, and then it allows you to download them as an ARM template, essentially rendering this tool useless.  Also, there are a lot of templates out there distributed by [Microsoft](https://github.com/Azure/azure-quickstart-templates) and the [community](https://github.com/Azure/AzureStack-QuickStart-Templates); use them, or perhaps learn to create your own.
* You intend to use it as a basis to learn how to "do templates."  Microsoft's documentation is perhaps the better place to start.
* You want to template-ize the templates.  The templates as-is are very versatile, extensible, and include functionality for conditional statements, variable substitution, etc.

### So when **should** I use it?

##### You want to:
* Dynamically generate complex cloud infrastructures in a reproduceable way, reusing common components.
* Build a lot of templates, but don't want to spend a lot of time doing it.
* Script the generation of templates using Python or a scripting utility that supports console commands written in Python.
* Utilize a simple and universal interface for retreiving and using ARM templates that can be used similarly across all your applications.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

At this point, the only requirement is Python 3.6.  If you would like it to be ported to a previous version, please submit an issue on GitHub and explain why or feel free to create a pull request.

### Installing

To install and run the scripts locally.
```
git clone https://github.com/RobotStudio/aztmpl.git
cd aztmpl
pip install -r requirements.txt
```

To install the scripts globally, execute the above, then run the following:
```bash
pip install .
```

### Executing

#### Command line
Coming soon...

#### Script extensions
Coming soon...

### Running the tests

To run the tests associated with this project, run `make test`.

You may also run `pytest`

For code coverage, run `make coverage`.

**Note: at this point in the project, only doctests have been implemented.**

## Contributing

We're always looking to incorporate the latest/greatest offerings and changes into our templates.  To contribute to this project, go ahead and clone it and issue a pull request.

###Coding Guidelines

Please conform to [PEP-8](https://www.python.org/dev/peps/pep-0008/) standards for all developm
ent.

The `pep8` and `autopep8` modules are a part of the `dev-requirements`, and has been added to the `Makefile`.  You can run `make pep8` for statistics, or `make pep8-verbose` for a detailed breakout of violations.

If you wish to automatically manage adherance to the PEP8 standard, use the module `autopep8`.  You can learn more about it [here](https://pypi.python.org/pypi/autopep8).  An `autopep8` action has been included in the `Makefile` for a sane default use as needed.


## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/RobotStudio/aztmpl/tags).

## Authors

* **Bobby Larson** - *Initialized Project* - [karma0](https://github.com/karma0)

See also the list of [contributors](CONTRIBUTORS.md) who participated in this project.

## License

This project is protected software - see the [LICENSE.txt](LICENSE.txt) file for details.

