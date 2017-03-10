# CMPS 263 - Final Project

### The Effects of California Wildfires, 2000 - 2015
How much are people effected by California wildfires and what characteristics of the fires are problematic?

### Visualizations

#### Jupyter Notebooks
- CA\_Wildfire\_Causes - Bar chart of number of wildfires by cause.
- CA\_Wildfire\_Fatalities - Bar chart of number of wildfire fatalities by year.
- CA\_Wildfire\_Structures - Bar chart of number of structures damaged/destroyed by year.

### Data Sources
- Fire
	- [Cal Fire Yearly Fire Lists (2000-2015)](http://cdfdata.fire.ca.gov/incidents/incidents_statsevents)
- Population
	- CA Department of Finance County Population (2000-2016)

### Data Processing
Fire data gathered from Cal Fire Yearly Fire Lists (2000-2015). Download the pdfs called `YYYY Large Fires List` for each year. Convert the downloaded pdf to txt via `pdftotext -layout <file name>.pdf <file name>.txt`. Then manually edit the txt file in an editor to remove page headers/footers. Next, run `python remove-spaces.py -f <file name>.txt` to generate a csv. Finally, edit the csv file to fix any column alignment issues from missing data.

#### Data Processing Scripts
- remove-spaces.py
	- For use with the Yearly Fire Lists. Will take the file path to a txt as an argument. Parses the txt by removing any commas (usually number formatting commas) and replaces multiple spaces with a comma to separate attributes. Then writes to a csv. 

:fire:
