# Players-Page-web scraping
Basic webscraping tools for the [Mario Kart 7 Players' Page](https://www.mariokart64.com/mk7/). This tool is aimed to help the writers of the [news](https://www.mariokart64.com/mk7/) by automating the retrieval of important data such as AF-cuts and the improvements of site records.

This repo containt 3 Python codes. AF_cuts.py and SiteRecords.py. AF_cuts.py retrieves the data from the [AF charts](https://www.mariokart64.com/mk7/afc.php) and creates an overview of all players that have managed to improve on their AF rating. In a similar way, SiteRecords.py checks if any [Site Records](https://www.mariokart64.com/mk7/wr.php) were beaten during the period for which the news is being written.  The third code is optional for the news writers, as it retrieves the [Glitch and No-Glitch World Records](https://mkwrs.com/mk7/). I personally used this code to create some PowerBI dashboards and statistics on World Record data, and can imagine that some players might have other creative uses for it.

The codes can be run from any Python editor. Alternatively, one may open a command prompt like CMD, drag the files to the command prompt and hit enter.

Both AF_cuts.py and SiteRecords.py will ask you to input where you want to save the file. For this type location/filename.xlsx.
SiteRecords.py will also ask for the year and then month. For this answer the given prompts by just typing out the year (e.g. 2023) and the month (e.g. 9) in numeric form.

Each python file should create one Excel file. One contains AF cuts and the other contains site records.

Both files will ask you to input where you want to save the file. For this type location/filename.xlsx.
The Site Records file will also ask for the year and month. For this input in numbers first the year and then the month.

**If this is your first time working with these codes** please do not forget to install the required packages. For this, you can open any command or Anaconda prompt and type !pip install -r requirements.txt.
