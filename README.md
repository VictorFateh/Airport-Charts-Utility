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

## Plans
* Better error handling (not just saying 'oops couldn't download from XXXX')
* Pre-populated airport lists (state/region selected)
* Accurate progress bar
* Release as utility on [XP forum](https://forums.x-plane.org/index.php?/files/)

## Dev Notes
* Look into GUI switch (PyQt5, Ortho4xp)
* ~~Switch from airnav to flightaware for data~~
