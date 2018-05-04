# rocontrol ![Python 3](https://img.shields.io/badge/python-3-blue.svg)
Interface de Fusée is an interface for fusée gelée.

![](https://github.com/moriczgergo/rocontrol/blob/assets/windows_preview.png) ![](https://raw.githubusercontent.com/moriczgergo/rocontrol/assets/ubuntu_preview.png) ![](https://raw.githubusercontent.com/moriczgergo/rocontrol/assets/mac_preview.png)

## Requirements
 * Python 3
 * Git
 * *libusb (for Linux only)*

The requirements in *italics* are a requirement of fusée gelée, not rocontrol.

## Setup

### Windows

```
git clone --recursive https://github.com/moriczgergo/interface-de-fusee
cd interface-de-fusee/
pip install pyusb
```

*NOTE:* fusee-launcher does not actually work on Windows yet. All you'll have on Windows is a GUI.

### Linux

```
git clone --recursive https://github.com/moriczgergo/interface-de-fusee
cd interface-de-fusee/
pip3 install pyusb
```

*NOTE:* You may need to use `pip` instead of `pip3`, if your Python installation is named `pip` instead of `pip3`.

## Usage

### Windows

```
python app.py
```

### Linux

```
python3 app.py
```

*NOTE:* You may need `sudo -H` if you're getting a "No access to USB" error.

*NOTE:* You may need to use `python` instead of `python3`, if your Python installation is named `python` instead of `python3`.

## Troubleshooting

#### It says there's no access to USB.
It seems like rocontrol doesn't have access to your USB ports. You'll need to run the script with `sudo -H`.

#### It says there's an unknown error.
Uh-oh, that's not good. [Open up an issue](https://github.com/moriczgergo/rocontrol/issues/new) with the exact error message, and some more info. (e.g.: your payload, the machine you're running the script on)

#### It says it can't connect to the display.
Run `xhost +localhost`, and `xhost +`.
