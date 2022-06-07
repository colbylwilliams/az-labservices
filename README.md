# az-labservices

[![Create Release](https://github.com/colbylwilliams/az-labservices/actions/workflows/release.yml/badge.svg)](https://github.com/colbylwilliams/az-labservices/actions/workflows/release.yml)

Microsoft Azure CLI Lab Services (v2) Extension.

## Install

To install the Azure CLI Lab Services (v2 extension, simply run the following command:

```sh
az extension add --source https://github.com/colbylwilliams/az-labservices/releases/latest/download/labservices-0.1.0-py2.py3-none-any.whl -y
```

### Update

To update Azure CLI Lab Services extension to the latest version:

```sh
az labservices upgrade
```

or for the latest pre-release version:

```sh
az labservices upgrade --pre
```

## Commands

This extension adds several commands that can be referenced [here](https://github.com/colbylwilliams/az-labservices/labservices).  Use `az labservices -h` for more information.
