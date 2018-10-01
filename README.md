# Airport-Charts-Utility

A tool to help batch-download airport instrument procedure charts from airnav.com


## Installation
In a python 3 virtualenv
1. ```pip install -r requirements.txt```
2. ``python app.py``

## Usage
1. Type a list of US ICAO airport codes (separate each airport with a space)
2. Click download and wait for "Done" message

## Plans
* Better input checking/correcting (live ICAO crosscheck?)
* Pre-populated airport lists (state/region selected)
* Accurate progress bar
* Auto update
    * Run as a chart updater to user dir and check against latest charts for differences
    * Or just force overwrite
* Release as utility on [XP forum](https://forums.x-plane.org/index.php?/files/)

## Dev Notes
* Look into GUI switch (PyQt5, Ortho4xp)
* ~~Switch from airnav to flightaware for data~~
