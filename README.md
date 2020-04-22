# theZoo - A Live Malware Repository
theZoo is a project created to make the possibility of malware analysis open and available to the public. Since we have found out that almost all versions of malware are very hard to come by in a way which will allow analysis, we have decided to gather all of them for you in an accessible and safe way.
theZoo was born by Yuval and later it was carried by lot of developers to help him maintain. 

This updated repository is maintained by **Qirit0** so bugs can be reported accordingly with the DAILYHIJACKS subs

**theZoo is open and welcoming visitors!**

If you are about to interact with our community please make sure to read our `CODE-OF-CONDUCT.md` prior to doing so. If you plan to contribute, first - thank you. However, do make sure to follow the standards on `CONTRIBUTING.md`.

![](https://github.com/ytisf/theZoo/raw/gh-pages/MalDB-Logo-Thumb.png)

## Disclaimer
theZoo's purpose is to allow the study of malware and enable people who are interested in malware analysis (or maybe even as a part of their job) to have access to live malware, analyse the ways they operate, and maybe even enable advanced and savvy  people to block specific malware within their own environment.

**Please remember that these are live and dangerous malware! They come encrypted and locked for a reason!  Do NOT run them unless you are absolutely sure of what you are doing! They are to be used only for educational purposes (and we mean that!) !!!**

We recommend running them in a VM which has no internet connection (or an internal virtual network if you must) and without guest additions or any equivalents. Some of them are worms and will automatically try to spread out. Running them unconstrained means that you **will infect yourself or others with vicious and dangerous malware!!!**

## Getting Started

Clone the repository with `git clone https://www.github.com/DAILYHIJACKS/theZoo`. Go to the directory and run `pip install --user -r requirements.txt`. This should install all latest requirements needed. In total can be "scripted" like so:

```bash
git clone https://www.github.com/DAILYHIJACKS/theZoo
cd theZoo
pip install --user -r requirements.txt
``` 

Start by running the console:

`python theZoo.py`


## License
theZoo - the most awesome free malware database on the air
Copyright (C) 2015, Yuval Nativ, Lahad Ludar, 5fingers
DEV: Qirit0
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.

You can also find more information in `LICENSE.md`.

## Documentation and Notes

### Background
theZoo's objective is to offer a fast and easy way of retrieving malware samples and source code in an organized fashion in hopes of promoting malware research.

### Root Files
Since version 0.42 theZoo has been undergoing dramatic changes. It now runs in both CLI and ARGVS modes. You can call the program with the same command line arguments as before.
The current default state of theZoo runtime is the CLI. The following files and directories are responsible for the application's behaviour.

`/conf` - The conf folder holds files relevant to the particular running of the program but are not part of the application. You can find the EULA file in the conf and more.

`/imports` - Contains .py import files used by the rest of the application

`/malwares/Binaries` - The actual malwares samples - be careful! These are very live.
 
`/malware/Source` -  Malware source code.  

Malware under the folder `Original` is supposed to be (NO PROMISES!) the original source of the malware that leaked. Malware under the folder `Reversed` is either reversed, decompiled or partially reconstructed.


## Directory Structure:
Each directory is composed of 4 files:
- Malware files in an encrypted ZIP archive.
- SHA256 sum of the 1st file.
- MD5 sum of the 1st file.
- Password file for the archive.


## Bugs and Reports

The repository holding all files is currently
	https://github.com/DAILYHIJACKS/theZoo

### Submit Malware
Get the file you want to submit and just run `python prep_file.py file_tosubmit.exe`. It will create a directory for you. Then just submit that along with the changes to the `conf/maldb.db` so that we know which malware it is.

### Hopeful
- [ ] A GUI. 
- [ ] Package releases. 

If you have any suggestions or malware that you have indexed (in the manner laid out in the documentation) please send it to us to - DAILYHIJACKS [a-t] GMAIL [.d0t.] com - so we can add it for everyone's enjoyment.
