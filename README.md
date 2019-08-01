# Airport-Charts-Utility

A tool to help batch-download airport instrument procedure charts from flightaware.com


## Installation
In a python 3 virtualenv
1. ```pip install -r requirements.txt```
2. ``python app.py``

## Usage
1. Select or create destination folder (Airports will each be individual directories)
2. Type a list of US ICAO airport codes (separate each airport with a space)
3. Click download and wait for "Done" message

## Future Plans
* Better error handling
* Pre-populated airport lists (state/region selected)
* Update button to let use update all charts in specific directory
* ~~Accurate progress bar~~
* ~~Switch from airnav to flightaware for data~~
* Release as utility on [XP forum](https://forums.x-plane.org/index.php?/files/)
