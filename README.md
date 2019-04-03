# AutoKey Configuration for Ubuntu
This repository contains AutoKey configuration data for Mac OS X keybindings.

Note:   
  - Switch Alt and Super key behavior
  - Windows minimize, Open home folder, Alt-Tab and Desktop switching set through system shortcuts


## Pre-Requisites

Install AutoKey:

```bash
sudo apt install autokey-gtk;
```

Verify that the configuration directory exists:

```bash
stat ~/.config/autokey;
```

## Usage
1. Navigate to your AutoKey configuration directory
2. Make a backup of the `data` directory
3. Clone this repository into the `data` directory

This can be achieved using the following shell commands:

```bash
set -x;
cd ~/.config/autokey \
  && mv data data.backup.$(date +'%Y%m%d%H%M%S') \
  && git clone git@github.com:glennr/autokey-osx-ify.git data;
```

Then start AutoKey and you should have the shortcuts applied.

Enjoy!

## Tested On
- Ubuntu 18.10
- Autokey-gtk 0.90.4

## Credits

- [viktorot](https://github.com/viktorot) and [nikarul](https://github.com/nikarul) for the base configuration
- [zephinzer](https://github.com/zephinzer/config-ubuntu-autokey) for the quick installation 
