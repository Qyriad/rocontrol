# Interface de Fusée ![Python 3](https://img.shields.io/badge/python-3-blue.svg)
An interface for fusée gelée.

## Requirements
 * Python 3
 * *libusb (for Linux only)*

The requirements in *italics* are a requirement of fusée gelée, not interface de fusée.

## Setup
```
git clone --recursive https://github.com/moriczgergo/interface-de-fusee
cd interface-de-fusee/
pip3 install -r requirements.txt
```

*NOTE:* You may need to use `pip` instead of `pip3`, if your Python 3 PIP installation is named `pip` instead of `pip3`.

## Usage
```
python3 app.py
```

*NOTE:* You may need to use `python` instead of `python3`, if your Python installation is named `python` instead of `python3`.

### Arguments
You can specify some command arguments for Interface de Fusée.

 * `--port`: Set the port. (`1355` by default) (alternative names: `-p`) (int)
 * `--host`: Set the hostname. (`127.0.0.1` by default) (alternative names: `--hostname`) (string)
