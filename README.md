# NavDataPro2FlightGear
This repository contains instructions and helper scripts that allow NavDataPro subscribers to update FlightGear' nav data. This process will update the airport procedures (SIDs and STARs), the Fixes, Navaids and Airways to the latest AIRAC cycle available in your NavDataPro subscription. Please follow the detailed instructions below. 

## Requirements
- Python 3.8 or higher
- A valid [Aerosoft NavDataPro](https://www.aerosoft.com/en/flight-simulation/flight-simulator-2004/tools-missions/1750/navdatapro-one-year-subscription-13-datasets) Subscription
- [FlightGear 2020.2.0](https://www.flightgear.org/download/daily-build-download/) or higher
- Florent Rougon's [extract-navdata.py](http://frougon.net/python_dumping_ground/short_scripts/extract-navdata.py) for Navigraph

## Instructions
1. Clone this repository: `git clone --depth 1 TODO NavDataPro2FlightGear` or download as zip from github.
2. Create a folder for the Level-D data, e.g. `leveld`. Copy the absolute path. We will refer to it as `<LD_PATH>` in the following.
3. Open NavDataPro, select 'All' and scroll down to 'Level-D 767 FSX'.
4. Set the target path to `<LD_PATH>`.
5. Let NavDataPro install the Level-D 767 nav data into that folder.
6. Run `python3 rename_procedure.py "<LD_PATH>"` in the folder cloned from git in step 1. The quotation marks are needed in case your path contains blanks.
7. The names of the `.xml` files in the `navdata` folder of the path from step 2 should now end in `.procedure.xml`
8. Identify the path of your FlightGear scenery folder (`<FG_SCENERY>`, see `$FG_SCENERY` FlightGear Wiki). It should contain a folder `Airports` and inside that folders from `0` to `9` and `A` to `Z`. Do not confuse with the `Airports` folder in your FlightGear data folder, which instead contains `apt.dat.gz` and `metar.dat.gz`.
9. Use Florent Rougon's `extract-navdata.py` to copy the procedure files to the FlightGear scenery folder: `python3 extract-navdata.py "<NDPATH>\navdata" "<FG_SCENERY>"`. The quotation marks are needed in case your paths contains blanks.
10. Create a folder for the X-Plane 10 data, e.g. `xplane`. Copy the absolute path. We will refer to it as `<XP10_PATH>` in the following.
11. Open NavDataPro, select 'X-Plane 10' and scroll down to 'X-Plane 10 (V 10.30 - V X.YZ)'.
12. Set the target path to `<XP10_PATH>`.
13. Let NavDataPro install the X-Plane 10 nav data into that folder.
14. Identify the path of your FlightGear data folder (`<FG_DATA>`, see `$FG_ROOT` in FlightGear Wiki). It should contain a folder `Navaids`.
15. Run `python3 navaids.py "<XP10_PATH>" "<FG_DATA>"` in the folder cloned from git in step 1. The quotation marks are needed in case your paths contains blanks.

## See Also
- [FlightGear Wiki: SIDs and STARs](http://wiki.flightgear.org/Route_manager#SIDs_and_STARs)
- [FlightGear Wiki: $FG_SCENERY](http://wiki.flightgear.org/$FG_SCENERY)
- [FlightGear Wiki: $FG_ROOT](http://wiki.flightgear.org/$FG_ROOT)

