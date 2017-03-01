# CMPS 263 - Final Project

### The Effects of California Wildfires
How much are people affected by California wildfires and what characteristics of the fires are problematic?

### Data Sources
- Fire
	- Cal Fire Yearly Fire Lists (2000-2015)
- Population
	- CA Department of Finance County Population (2000-2016)
- Under Consideration
	- Traffic data from Caltrans

### Data Processing Scripts
- remove-spaces.py
	- For use with the Yearly Fire Lists. First, convert downloaded pdf to txt via `pdftotext -layout <file name>.pdf <file name>.txt`. Then manually edit the txt file in an editor to remove page headers/footers and all pre-existing commas. Next, run `python remove-spaces.py -f <file name>.txt`. Finally, edit the csv file to fix any column alignment issues from missing data.

:fire:
