# Niki_Shit
A collection of programs and data for the data analysis of Niki's shit

cc. Vercil Juan

## Stipulations
The collection is a group of t-tests and chi-square analysis for the data, a program to measure and collect to spread data, and a script which turns the data from the raw file into pd data frames, and another script to do calculate specific shit. Here is a checklist for the tasks to be completed

## Tasks to Complete
### Coding tasks
- [x] T-Tester modules
- [x] Toe spread pixel measurement
- [ ] Toe Spread png measurer
- [ ] Toe Spread data collector / Can be manual
- [ ] Google-Python API to collect the xlsx file to csv
- [ ] Make your own csv file with the data
- [ ] Raw excel to data frames script
- [ ] Data processing script
- [x] Calculate SFI and other relevant values
- [ ] Graphical visualization of data

### Operational tasks
- [x] Scan data W0-W1
- [x] Clean up data
- [x] Code converters, statistic functions, etc
- [ ] Image distance measurer
- [ ] Feet data collection (can be done manually)
- [ ] Process xlsx data
- [ ] Create dataframe from structure for xlsx data 
- [ ] Create program to process step data
- [ ] Process step data
- [ ] Create dataframe from struct for step data 
- [ ] Process all of it
- [ ] Generate values
- [ ] Perform statistics
- [ ] Create graphs
- [ ] Finish project

## Resources
Most of the resources is taken from the study of [Ompacan](https://drive.google.com/file/d/1tbiZ-u4lx1yt55kt_1BcRi_K1j9HZQw6/view?usp=sharing)

The raw data file can be found [here](https://docs.google.com/spreadsheets/d/176y9Tg4QkZA_H6Ec-eKRBOWocu7B78pMfoGY3x7W7bo/edit?fbclid=IwY2xjawGm1IVleHRuA2FlbQIxMQABHWCoXzEnQxFthMzRlwakixfX4Bk3g-W8euo0MKwLeTxk4nOrRt8YqWGiGA_aem_HfODvd2sFTlMnq93jEDtTQ&gid=1655045917#gid=1655045917)

And Niki's study [here](https://docs.google.com/document/d/1STxgiQR7ASBzdH0naifeZxV23L84LieEthjv1698LC4/edit?tab=t.0)

## Module Descriptions

* `stats.py` - A collection of formulae for statistical testing
* `imsys.py` - A library of functions for image analysis
* `sfi.py` - A function for calculating the sciatic functional index
* `paw_analyze.py` - an image analysis library and tool to measure the parameters for sfi
* `dataframes.py` - a module which turns the raw csv / xlsx file into pd dataframes for easier data analysis

## Utilities Description
* `converters.py` - a set of converter functions and other important tools
* `image_cleaner.py` - a script to clean the images up to acceptable tolerance
* `pdf_to_png_converter` - a script to convert the pdf files to png
* `progress.py` - dynamic progress bar

## Image Code

### Mouse Code
* NO - Normal
* P - Positive
* N - Negative
* S - Sham

Mouse number (5 per setup)

### Time Code
* B - Baseline + Duplicate
* W - Week + Week number (4 weeks)

### Example:
P1W1 - Positve 1, Week 1

## Data Code
* R - Rotation
* T - Time
* D - Distance
