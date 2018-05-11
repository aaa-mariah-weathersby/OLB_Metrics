# QuotesAttempted - Backend

Backend for the QuotesAttempted

## Setup Requirements

Requires the following:

* TSO access
* BlueZone 6.1 - mainframe terminal
This program connects to the mainframe, runs the JCL job in TSO
Installed as: `"C:\Program Files (x86)\BlueZone\6.1\bzmd.exe"`
* Anaconda / Python
Installed as: `"C:\Software\anaconda3\python.exe"`

## Files and descriptions

* `transfer2.bat`
This script does the following:
  * Start the terminal with the `transfer.zmd` configuration
  * run the python script that transforms the quote file
  * copy the transformed quote file to timestamp filename
* `transfer.zmd`
Terminal configuration that will run the `transferscript.bzs` script.
* `transferscript.bzs`
Terminal script that does the following:
  * run the JCL job
  * download quote file
* `transform_datetime_refactored.py`, `transform_datetime_refactored_unittest.py`
Python script that transforms the file to expected format, with unittest

## Usage

### Database Drop

Run the script on the command line as so:

```
C:\tools> transfer2.bat
```

### transform

Edit the `transform_datetime_refactored.py` and change the following if necessary:

* `INPUT_FILENAME` - input file from database drop, "transfertest77.txt"
* `OUTPUT_FILENAME` - output file, "testDoc.txt"

#### unittest/pylint

Run the following:

```
python transform_datetime_refactored_unittest.py
```
