# Airport-Charts-Bot

A tool to help batch-download airport instrument procedure charts from airnav.com


## Installation
In a python 3 virtualenv
1. ```pip install -r requirements.txt```
2. ``python app.py``

## Usage
1. Type a list of US ICAO airport codes
2. Separate each airport with a space
3. Click download and wait for "Done" message

## Future goals
* Better input checking/correcting
* Pre-populated airport lists (state/region selected)
* Download from text file list
* Accurate definite progress bar (with file logs)
* Auto update?
    * Run as a chart updater to user dir and check against latest charts for differences
    * Or just force overwrite
* Release as utility on [XP forum](https://forums.x-plane.org/index.php?/files/)