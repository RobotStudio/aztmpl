# Azure Resource Manager (ARM) Template Generator

This is a set of Python 3 utilities to assist with the generation of Azure ARM templates used for cloud automation and resource management.

**Note that this project is currently a work in progress.**

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

At this point, the only requirement is Python 3.6.

### Installing

```
git clone https://github.com/RobotStudio/aztmpl.git
```

### Running the tests

To run the tests associated with this project, run `make test`.

You may also run `pytest`

For code coverage, run `make coverage`.

**Note: at this point in the project, only doctests have been implemented.**

## Contributing

To contribute to this project, go ahead and clone it and issue a pull request.

###Coding Guidelines

Please conform to [PEP-8](https://www.python.org/dev/peps/pep-0008/) standards for all developm
ent.

The `pep8` and `autopep8` modules are a part of the `dev-requirements`, and has been added to the `Makefile`.  Please edit for your project, and change `sample` to the module for your project.  Once this is completed, you can run `make pep8` for statistics, or `make pep8-verbose` for a detailed breakout of violations.

If you wish to automatically manage adherance to the PEP8 standard, use the module `autopep8`.  You can learn more about it [here](https://pypi.python.org/pypi/autopep8).  An `autopep8` action has been included in the `Makefile` for a sane default use as needed.


## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://nexthealth.visualstudio.com/NextHealthProducts/_git/project/tags).

## Authors

* **Bobby Larson** - *Initial Project Skeleton* - [karma0](https://github.com/karma0)

See also the list of [contributors](CONTRIBUTORS.md) who participated in this project.

## License

This project is protected software - see the [LICENSE.txt](LICENSE.txt) file for details.

