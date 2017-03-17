# CMPS 263 - Final Project

### The Effects of California Wildfires, 2000 - 2015

To install Python dependencies: `pip install -r requirements.txt`

### Visualizations

#### Jupyter Notebooks
- CA\_Wildfire\_Acres - Discrete heatmap of number of acres burned per year and month.
- CA\_Wildfire\_Causes - Bar chart of number of wildfires by cause.
- CA\_Wildfire\_Counts - Discrete heatmap of number of fires per year and month.
- CA\_Wildfire\_Fatalities - Bar chart of number of wildfire fatalities by year.
- CA\_Wildfire\_Structures - Bar chart of number of structures damaged/destroyed by year.

#### Poster
- poster.svg - SVG version of the visualization poster.
- poster.pdf - Final PDF version of the visualization poster.

### Data Sources
- Fire
	- [Cal Fire Yearly Fire Lists (2000-2015)](http://cdfdata.fire.ca.gov/incidents/incidents_statsevents)

### Data Processing
Fire data gathered from Cal Fire Yearly Fire Lists (2000-2015). Download the pdfs called `YYYY Large Fires List` for each year. Convert the downloaded pdf to txt via `pdftotext -layout <file name>.pdf <file name>.txt`. Then manually edit the txt file in an editor to remove page headers/footers. Next, run `python remove-spaces.py -f <file name>.txt` to generate a csv. Finally, edit the csv file to fix any column alignment issues from missing data.

#### Data Processing Scripts
- remove-spaces.py
	- For use with the Yearly Fire Lists. Will take the file path to a txt as an argument. Parses the txt by removing any commas (usually number formatting commas) and replaces multiple spaces with a comma to separate attributes. Then writes to a csv. 

:fire:
