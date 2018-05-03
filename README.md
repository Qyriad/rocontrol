# rocontrol ![Python 3](https://img.shields.io/badge/python-3-blue.svg)
Interface de Fusée is an interface for fusée gelée. It runs a webserver that lets you easily do Switch haxing.

## Requirements
 * Python 3
 * *libusb (for Linux only)*

The requirements in *italics* are a requirement of fusée gelée, not rocontrol.

## Setup
```
git clone --recursive https://github.com/moriczgergo/interface-de-fusee
cd interface-de-fusee/
```

## Usage
```
python3 app.py
```

*NOTE:* You may need `sudo -H` if you're getting a "No access to USB" error.

*NOTE:* You may need to use `python` instead of `python3`, if your Python installation is named `python` instead of `python3`.

## Troubleshooting

#### It says there's No access to USB.
It seems like rocontrol doesn't have access to your USB ports. You'll need to run the script with `sudo -H`.

#### It says there's an unknown error.
Uh-oh, that's not good. [Open up an issue](https://github.com/moriczgergo/rocontrol/issues/new) with the exact error message, and some more info. (e.g.: your payload, the machine you're running the script on)
