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

## Questions (and Answers)

#### Why can't I reach the UI from another device?
If they're in the same network, you'll need to set the `--host` parameter to your local IP address. (you know, the one starting with `192.168.`)

If they're not in the same network, and you'd like to reach the interface remotely, you'd have to do port forwarding on your router, and **exposing your UI to the whole wild world is NOT RECOMMENDED**, since anybody could just launch a malicious payload that wipes all your stuff from your Switch, if they find your IP address. (which they will, via Shodan, or some other service)

#### It says there's a USB Error.
It seems like the interface doesn't have access to your USB ports. You'll need to run the script with `sudo`.

Also note, that if you're viewing the interface from another device, than the one it the script is running on, you'll still need to plug your Switch into the machine that runs the script.

#### It says there's an unknown error.
Uh-oh, that's not good. [Open up an issue]() with the exact error message, and some more info. (e.g.: your payload, the machine you're running the script on)
