# Introduction<br>

> #### This program creates a covid dashboard, found at http://127.0.0.1:5000/index, with the following functionality<br>
>
> - displaying statistics related to Covid19 (as held by the uk_covid19 Cov19API)<br>
> - displaying news articles (as held by the newsAPI)<br>
> - providing the ability to schedule and cancel updates to displayed information<br>
>
> **In addition, the program stores newly acquired covid statistics locally in a csv file (name specified within the config file)**<br>

`covid_data_handler.py` holds functions relevant to obtaining, parsing, and storing covid statistics<br>
`covid_news_handling.py` holds functions relevant to obtaining, parsing, and storing news articles<br>
`main.py` holds functions relevant to forming the covid dashboard and tying in the functions found within covid_data_handler and covid_news_handling<br>
`__init__.py` runs the package<br>

---
---

# Prerequisites<br>

> Python 3.9.7 or above<br>
> OS independant<br>
> the 5 modules (`__init__.py`, `main.py`, `covid_data_handler.py`, `covid_news_handling.py`, and `tests.py`) should be stored together in the Covid19_Dashboard_pkg directory<br>
> any relevant files (config file, status file, log file, csv file, nation_2021-10-28.csv, tests.csv, test_config.json, and results file) should also be stored in the Covid19_Dashboard_pkg directory<br>
> before any of the functionality of `covid_news_handling.py` can be utilised, one should first obtain a valid API key from the newsAPI, https://newsapi.org/, and place it within the config file with the key "API_key"<br>

---
---

# Installation<br>

> ## Modules required<br>
>
> - os<br>
> - datetime<br>
> - requests<br>
> - json<br>
> - sched<br>
> - time<br>
> - flask<br>
> - logging<br>

at the command prompt, type<br>
`cd Documents/Covid19_Dashboard_pkg`<br>
(*note that if the Covid19_Dashboard_pkg directory is stored elsewhere, navigate to there instead*)<br>
`pip install os datetime requests json sched time flask logging`<br>

---
---

# Getting started tutorial<br>

**note that a valid API key for the newsAPI, https://newsapi.org/, should first be obtained and saved to the config file with the key "API_key"**<br>

>> from within the Covid19_Dashboard_pkg directory, run `__init__.py`<br>
>> open a browser and navigate to http://127.0.0.1:5000/index<br>
>> set a time, provide a name in place of *'Update label'*, select *'Update Covid data'*<br>
>> click Submit<br>
>
>> we would expect to see an item appear in the *'Scheduled updates'* column<br>
>> the item should share the name given and have the content *'**[time given]**, Covid data'*<br>
>
>> waiting until the given time, we would expect to see the covid statistics update the next time the dashboard refreshes (assuming the statistics weren't already up to date)<br>
>> at the same time, the update item should disappear from the *'Scheduled updates'* column<br>

>> from within the Covid19_Dashboard_pkg directory, run `__init__.py`<br>
>> open a browser and navigate to http://127.0.0.1:5000/index<br>
>> set a time, provide a name in place of *'Update label'*, select *'Update news articles'*<br>
>> click Submit<br>
>
>> we would expect to see an item appear in the *'Scheduled updates'* column<br>
>> the item should share the name given and have the content *'**[time given]**, news articles'*<br>
>
>> waiting until the given time, we would expect to see new items in the *'News headline'* column the next time the dashboard refreshes<br>
>> - each item should have the name of an article, some level of description, and a link to the full article<br>
>> at the same time, the update item should disappear from the *'Scheduled updates'* column<br>

>> from within the Covid19_Dashboard_pkg directory, run `__init__.py`<br>
>> open a browser and navigate to http://127.0.0.1:5000/index<br>
>> set a time, provide a name in place of *'Update label'*, select both *'Update Covid data'* and *'Update news articles'*<br>
>> click Submit<br>
>
>> we would expect to see 2 items appear in the *'Scheduled updates'* column<br>
>> both items should share the name given<br>
>> the first item should have the content *'**[time given]**, Covid data'*<br>
>> the second item should have the content *'**[time given]**, news articles'*<br>
>
>> click the x button on the update item<br>
>
>> we would expect to see the update item disappear from the *'Scheduled updates'* column<br>
>
>> waiting until the given time, we would not expect to see any related changes the next time the dashboard refreshes<br>

---
---

# Usage<br>

## running<br>

### startup<br>

from within the Covid19_Dashboard_pkg directory, run `__init__.py`<br>
navigate to http://127.0.0.1:5000/index in a web browser<br>
the dashboard is now visible from which to interact with the Covid19_Dashboard_pkg<br>
additionally, the news articles displayed (if any) as well as the values for "local_7day_infections", "national_7day_infections", "hosptial_cases", and "deaths_total" will match what they were in the previous usage<br>
additionally, any updates that should have been completed since the previous usage will be inacted immediately<br>
additionally, any updates that were scheduled for beyond the current time in the previous usage will be scheduled once more<br>


### scheduling a covid update<br>

having navigated to the dashboard as in **startup**,<br>
give a time and enter a name where indicated<br>
select *'Update Covid data'* and click submit<br>
an update has now been added (visible on the left of the dashboard under '*Scheduled updates:*') with the name, time, and type of update all indicated<br>
additionally, `covid_data_handler.covid_update` has been scheduled to run at the specified time<br>
additionally, the updates stored within the status json file will now include this new update<br>

when the time is reached, `covid_data_handler.covid_update` will run, resulting in:<br>
- the variables present on the dashboard updating to the result of calculations on the latest data from the uk_covid19 Cov19API (*note that if no new data was available then no change will be visible*)<br>
- the contents of the covid file updating to store the latest data from the uk_covid19 Cov19API (*note that if no new data was available then no change will be visible*)<br>
additionally, the update will be removed (visibly absent on the left of the dashboard under '*Scheduled updates:*')<br>
additionally, the updates stored within the status json file will no longer include this update<br>
additionally, the values for "local_7day_infections", "national_7day_infections", "hosptial_cases", and "deaths_total" within the status json file will now match those shown on the dashboard<br>


### scheduling a repeating covid update<br>

having navigated to the dashboard as in **startup**,<br>
interacting with the dashboard as in **scheduling a covid update**, but this time additionally selecting '*Repeat update*' before pressing submit,<br>

the program performs as in **scheduling a covid update** with the distinction that the update is no longer removed (remaining visible on the left of the dashboard under '*Scheduled updates:*')<br>
additionally, the update is no longer removed from the updates stored within the status json file<br>
additionally, `covid_data_handler.covid_update` has been scheduled to run again at the specified time (in 24 hours)<br>
this update will continue to remain and be rescheduled in this manner every time it occurs<br>


### cancelling a covid update<br>

having navigated to the dashboard as in **startup**,<br>
interacting with the dashboard as in **scheduling a covid update** or **scheduling a repeating covid update**, but this time additionally clicking to remove the update icon before the time is reached,<br>
the update will be removed (visibly absent on the left of the dashboard under '*Scheduled updates:*')<br>
additionally, the updates stored within the status json file will no longer include this update<br>
additionally, the scheduled running of `covid_data_handler.covid_update` has been cancelled<br>

when the time is reached, nothing will happen<br>


### scheduling a news API request<br>

**note that a valid API key for the newsAPI, https://newsapi.org/, should first be obtained and saved to the config file with the key "API_key"**<br>

having navigated to the dashboard as in **startup**,<br>
give a time and enter a name where indicated<br>
select *'Update news articles'* and click submit<br>
an update has now been added (visible on the left of the dashboard under '*Scheduled updates:*') with the name, time, and type of update all indicated<br>
additionally, `covid_news_handling.news_API_request` has been scheduled to run at the specified time<br>
additionally, the updates stored within the status json file will now include this new update<br>

when the time is reached, `covid_news_handling.news_API_request` will run, resulting in the articles present on the right of the dashboard (under '*News headlines:*') being updated to contain the most popular articles since yesterday from the newsAPI that have not already been displayed<br>
additionally, the update will be removed (visibly absent on the left of the dashboard under '*Scheduled updates:*')<br>
additionally, the updates stored within the status json file will no longer include this update<br>
additionally, the value for "news" (as well as for "date" and "remove") within the status json file will now match those of the program<br>
additionally, whenever `covid_news_handling.news_API_request`, the news articles shown now will no longer be returned<br>


### scheduling a repeating news API request<br>

**note that a valid API key for the newsAPI, https://newsapi.org/, should first be obtained and saved to the config file with the key "API_key"**<br>

having navigated to the dashboard as in **startup**,<br>
interacting with the dashboard as in **scheduling a news API request**, but this time additionally selecting '*Repeat update*' before pressing submit,<br>

the program performs as in **scheduling a news API request** with the distinction that the update is no longer removed (remaining visible on the left of the dashboard under '*Scheduled updates:*')<br>
additionally, the update is no longer removed from the updates stored within the status json file<br>
additionally, `covid_news_handling.news_API_request` has been scheduled to run again at the specified time (in 24 hours)<br>
this update will continue to remain and be rescheduled in this manner every time it occurs<br>


### cancelling a news API request<br>

**note that a valid API key for the newsAPI, https://newsapi.org/, should first be obtained and saved to the config file with the key "API_key"**<br>

having navigated to the dashboard as in **startup**,<br>
interacting with the dashboard as in **scheduling a news API request** or **scheduling a repeating news API request**, but this time additionally clicking to remove the update icon before the time is reached,<br>
the update will be removed (visibly absent on the left of the dashboard under '*Scheduled updates:*')<br>
additionally, the updates stored within the status json file will no longer include this update<br>
additionally, the scheduled running of `covid_news_handling.news_API_request` has been cancelled<br>

when the time is reached, nothing will happen<br>


### scheduling a combined covid update and news API request<br>

**note that a valid API key for the newsAPI, https://newsapi.org/, should first be obtained and saved to the config file with the key "API_key"**<br>

having navigated to the dashboard as in **startup**,<br>
interacting with the dashboard as in **scheduling a covid update**, but this time additionally selecting *'Update news articles'* before pressing submit,<br>
two updates have now been added (visible on the left of the dashboard under '*Scheduled updates:*') with the shared name, shared time, and types of both updates all indicated<br>
additionally, both `covid_data_handler.covid_update` and `covid_news_handling.news_API_request` have been scheduled to run at the specified time<br>
additionally, the updates stored within the status json file will now include both of these updates<br>

when the time is reached, both `covid_data_handler.covid_update` and `covid_news_handling.news_API_request` will run, resulting in:
- the variables present on the dashboard updating to the result of calculations on the latest data from the uk_covid19 Cov19API (*note that if no new data was available then no change will be visible*)<br>
- the contents of the covid file updating to store the latest data from the uk_covid19 Cov19API (*note that if no new data was available then no change will be visible*)<br>
- the articles present on the right of the dashboard (under '*News headlines:*') being updated to contain the most popular articles since yesterday from the newsAPI that have not already been displayed<br>
additionally, the updates will be removed (visibly absent on the left of the dashboard under '*Scheduled updates:*')<br>
additionally, the updates stored within the status json file will no longer include these updates<br>
additionally the value for "news", "data", "remove", "local_7day_infections", "national_7day_infections", "hosptial_cases", and "deaths_total" within the status json file will now match those of the program<br>
additionally, whenever `covid_news_handling.news_API_request`, the news articles shown now will no longer be returned<br>


### scheduling a repeating combined covid update and news API request<br>

**note that a valid API key for the newsAPI, https://newsapi.org/, should first be obtained and saved to the config file with the key "API_key"**<br>

having navigated to the dashboard as in **startup**,<br>
interacting with the dashboard as in **scheduling a combined covid update and news API request**, but this time additionally selecting '*Repeat update*' before pressing submit,<br>

the program performs as in **scheduling a combined covid update and news API request** with the distinction that both updates are no longer removed (remaining visible on the left of the dashboard under '*Scheduled updates:*')<br>
additionally, the updates are no longer removed from the updates stored within the status json file<br>
additionally, both `covid_data_handler.covid_update` and `covid_news_handling.news_API_request` have been scheduled to run again at the specified time (in 24 hours)<br>
these updates will continue to remain and be rescheduled in this manner every time they occurs<br>


### cancelling a combined covid update and news API request<br>

**note that a valid API key for the newsAPI, https://newsapi.org/, should first be obtained and saved to the config file with the key "API_key"**<br>

having navigated to the dashboard as in **startup**,<br>
interacting with the dashboard as in **scheduling a combined covid update and news API request** or **scheduling a repeating combined covid update and news API request**, but this time additionally clicking to remove either update icon before the time is reached,<br>
both updates will be removed (visibly absent on the left of the dashboard under '*Scheduled updates:*')<br>
additionally, the updates stored within the status json file will no longer include these updates<br>
additionally, the scheduled running of both `covid_data_handler.covid_update` and `covid_news_handling.news_API_request` have been cancelled<br>

when the time is reached, nothing will happen<br>


### removing a news article<br>

**note that a valid API key for the newsAPI, https://newsapi.org/, should first be obtained and saved to the config file with the key "API_key"**<br>

having navigated to the dashboard as in **startup**,<br>
clicking to remove a news article icon,<br>
the news article will be removed (visibly absent on the right of the dashboard under '*News headlines:*')<br>
additionally, the news stored within the status json file will no longer include this news article<br>

---

## testing<br>

### tests during runtime<br>

every function within the 3 modules (`covid_data_handler.py`, `covid_news_handling.py`, and `main.py`) inspects the modules, functions, globals and arguments it is expected to interact with. in the case of the former 3, the module will attempt to make suitable alterations to what it is given if it finds it to not be of the correct type, format etc.<br>
In this manner, any function that behaves incorrectly and changes any global content in any meaningful unintentional way has its changes immediately revoked by the next module that would use that piece of global content<br>
Logging is used to make note of when such corrections are required (typically WARNINGS) giving a short description of what was found to be the issue as well as which module spotted the issue<br>


### tests outside of runtime<br>

**note that a valid API key for the newsAPI, https://newsapi.org/, should first be obtained and saved to the config file with the key "API_key" in order to test the `covid_news_handling.py` module**<br>

the module `tests.py` holds the functions for testing the functionality of the other 3 modules (`covid_data_handler.py`, `covid_news_handling.py`, and `main.py`)<br>
running the tests module from within the Covid19_Dashboard_pkg directory will see the name of each test, together with short descriptions, and ultimately the results written to the "results.txt" file also stored within the Covid19_Dashboard_pkg directory<br>

to test individual functions, import and run the corresponding function within the Covid19_Dashboard_pkg directory<br>
the corresponding test function of each other function will have the same name, preffixed by "test_"<br>

---
---

# Developer Documentation<br>

## files<br>

**all files are stored within the Covid19_Dashboard_pkg directory**<br>

### templates folder<br><br>

**a folder containing the html template for the covid dashboard**<br>

#### index.html<br>

**a static html file used as a template for the covid dashboard**<br>

this file should remain stored within the templates directory, which in turn should remain stored within the Covid19_Dashboard_pkg directory<br>

### config file<br>

**a json file containing configuration information**<br>

named **config.json** by default<br>
referenced in main.py, decleration of json_read, line 3,<br>
`def json_read(json_filename = "`**config.json**`", mode = 0, *args, log = True, **kwargs):`<br>
referenced in main.py, decleration of json_write, line 77,<br>
`def json_write(json_filename = "`**config.json**`", new_data = {}, mode = 1, *args, log = True, **kwargs):`<br>

this file should remain stored within the Covid19_Dashboard_pkg directory<br>

>#### contents<br>
>
> - "log_level"<br>
> - - indicating the minimum severity an event must be in order to be logged<br>
> - - defaulting to "DEBUG"
> - "csv_filename"<br>
> - - referring to the csv file for storing and retrieving covid statisitics<br>
> - - defaulting to "covid.csv"
> - "log_filename"<br>
> - - referring to the log file for storing any events occuring during runtime<br>
> - - defaulting to "sys.log"
> - "status_filename"<br>
> - - referring to the json file for storing any variables that should be kept track of between runs<br>
> - - defaulting to "status.json"
> - "AreaName"<br>
> - - referring to the 'areaName' argument to be given to the uk_covid19 Cov19API for retrieval of local statistics<br>
> - - defaulting to "Exeter"<br>
> - "AreaType"<br>
> - - referring to the 'areaType' argument to be given to the uk_covid19 Cov19API for retrieval of local statistics<br>
> - - defaulting to "ltla"<br>
> - "API_key"<br>
> - - referring to the 'apiKey' argument to be given to the newsAPI for verification/validation purposes<br>
> - - defaulting to ""<br>


### csv file<br>

**a csv file containing covid statistics**<br>

named **covid.csv** by default in the config file<br>

this file should remain stored within the Covid19_Dashboard_pkg directory<br>

> #### columns<br>
>
> - areaCode<br>
> - areaName<br>
> - areaType<br>
> - date<br>
> - cumDailyNsoDeathsByDeathDate<br>
> - hospitalCases<br>
> - newCasesBySpecimenDate<br>


### status file<br>

**a json file that stores values generated during runtime that should be kept between uses**<br>

named **status.json** by default in the config file<br>

this file should remain stored within the Covid19_Dashboard_pkg directory and should not be edited<br>

> #### contents<br>
>
> - "local_7day_infections", a string<br>
> - - defaulting to "N/A"<br>
> - "national_7day_infections", a string<br>
> - - defaulting to "N/A"<br>
> - "hosptial_cases", a string<br>
> - - defaulting to "N/A"<br>
> - "deaths_total", a string<br>
> - - defaulting to "N/A"<br>
> - "updates", a list of dictionaries<br>
> - - defaulting to []<br>
> - "remove", a dictionary<br>
> - - defaulting to {}<br>
> - "news", a list of dictionaries<br>
> - - defaulting to []<br>

### logging file<br>

**a log file that stores any events logged during the program's runtime**

named **sys.log** by default in the config file<br>

### nation_2021-10-28.csv<br>

**a static csv file, the contents of which are known and must remain unchanged. This file is used by tests.py**<br>

### test csv file<br>

**a dynamic csv file, used by tests.py**<br>

named **tests.csv** by default<br>
referenced in tests.py, lines 2, 461, 525, 585,<br>
`tests_csv = "`**tests.csv**`"`<br>

### test_config.json<br>

**a dynamic json file, used by tests.py**<br>

named **test_config.json** by default<br>
referenced in tests.py, lines 3, 923, 996,<br>
`test_config_json = "`**test_config.json**`"`<br>

### results file<br>

**a txt file that stores the results of tests performed on the 3 modules (as produced when running tests.py)**<br>

named **results.txt** by default<br>
referenced in tests.py, lines 1, 32, 107, 193, 294, 404, 459, 523, 583, 667, 750, 838, 921, 994, 1066, 1118, 1176, 1255,<br>
`filename = "`**results.txt**`"`

this file should remain stored within the Covid19_Dashboard_pkg directory<br>

---

## covid_data_handler<br>

**a module for covid data handling functionality**<br>

### parse_csv_data<br>

**a function to read a csv file**<br>

determine what method of logging is appropriate within parse_csv_data<br>
determine if all desired functions are present (attempting to import if not)<br>
determine if a file name was given and if it is appropriate (ended in ".csv")<br>
determine if the file exists within the Covid19_Dashboard_pkg directory<br>
if applicable, read from the file and split line by line into a list of strings<br>

> #### module dependancy<br>
>
> - logging<br>
> - - used to log events to a file<br>
> - - logging is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logging is not found to be present, `log` is set to `False`<br>
> - os.path.isfile<br>
> - - used to determine whether or not a file exists within the Covid_dashboard_pkg directory<br>

> #### global dependancy<br>
>
> - logger<br>
> - - an object from the logging module used as a framework when logging to files<br>
> - - logger is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logger is not found to be present, `log` is set to `False`<br>

> #### arguments<br>
>
> - csv_filename<br>
> - - a string, naming the file to attempt to read<br>
> - - csv_filename is expected to end in ".csv" and should point to an existing csv file that is accessible within the Covid_Dashboard_pkg directory<br>
> - - csv_filename defaults to `None`<br>
> - args<br>
> - - a list, catching any arguments in excess of those expected<br>
> - - args is expected to remain an empty list<br>
> - - args defaults to `[]`<br>
> - log<br>
> - - a boolean, dictating whether to attempt to log to a file or directly to the python terminal<br>
> - - log is expected to be set to `True` only if the logging framework has been established elsewhere (typically in main.startup in standard runtime)<br>
> - - log defaults to `True`<br>
> - kwargs<br>
> - - a dictionary, catching any keyword arguments beyond those expected<br>
> - - kwargs is expected to remain an empty dictionary<br>
> - - kwargs defaults to `{}`<br>

with modules, globals and arguments given as expected,<br>
the csv file is read and each line is put into a seperate string<br>
all strings are then stored together in a list which is then returned<br>

with the exception of logging, any modules not available will cause an appropriate log to be made (typically a WARNING if not present followed by a CRITICAL if attempts to import fail) and will result in parse_csv_data returning None if unable to import<br>

with the exception of args and kwargs (for which any discrepencies merely log an INFO) and log (which is set to `True` if found to be anything other than a boolean),<br>
any arguments given in an unexpected manner will cause an appropriate log to be made (typically a WARNING) and will result in parse_csv_data returning None<br>


### parse_csv_data2<br>

**a function to convert and validate the list of strings as read from a csv into a dictionary**<br>

determine what method of logging to use within parse_csv_data2<br>
determine if any covid_csv_data was given and if it is of the correct type (a list of strings)<br>
determine if the list of lists given by splitting all elements of covid_csv_data by "," are all of expected length (7)<br>
take the first line (as split into a list of strings by ",") to be a list of headers<br>
group elements of covid_csv_data by the value at index 1 (expected to be areaName for this application)<br>
order elements of covid_csv_data by the value at index 3 (expected to be date for this application) within these groupings<br>
place the remaining key/value pairings of each covid_csv_data element into a dictionary (one per element), the keys are taken to be the corresponding headers for each values index<br>

> #### module dependancy<br>
>
> - logging<br>
> - - used to log events to a file<br>
> - - logging is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logging is not found to be present, `log` is set to `False`<br>

> #### global dependancy<br>
>
> - logger<br>
> - - an object from the logging module used as a framework when logging to files<br>
> - - logger is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logger is not found to be present, `log` is set to `False`<br>

> #### arguments<br>
>
> - covid_csv_data<br>
> - - a non-empty list of strings as would be returned from `parse_csv_data`<br>
> - - when split by ",", each element of covid_csv_data is expected to be of length 7<br>
> - - the first element of covid_csv_data when split by "," is expected to be a list of 7 unique headers<br>
> - - covid_csv_data defaults to `None`<br>
> - log<br>
> - - a boolean, dictating whether to attempt to log to a file or directly to the python terminal<br>
> - - log is expected to be set to `True` only if the logging framework has been established elsewhere (typically in main.startup in standard runtime)<br>
> - - log defaults to `True`<br>
> - args<br>
> - - a list, catching any arguments in excess of those expected<br>
> - - args is expected to remain an empty list<br>
> - - args defaults to `[]`<br>
> - kwargs<br>
> - - a dictionary, catching any keyword arguments beyond those expected<br>
> - - kwargs is expected to remain an empty dictionary<br>
> - - kwargs defaults to `{}`<br>

with modules, globals, and arguments given as expected,<br>
the list of strings is converted into a dictionary<br>
each unique value from index1 of the elements of the original list when split by "," is used as a key, paired to a  dictionary<br>
these sub dictionaries use the value from index3 of the elements of the original list when split by "," as keys (placed in order), paired to a dictionary<br>
these sub sub dictionaries pair the remaining values (indexes not including 1 and 3 of the elements of the original list when split by ",") with keys as taken from the corresponding index of the first element of the original list when split by ","<br>
the overall dictionary is then returned<br>

with the exception of args and kwargs (for which any discrepencies merely log an INFO) and log (which is set to `True` if found to be anything other than a boolean),<br>
any arguments given in an unexpected manner will cause an appropriate log to be made (typically a WARNING) and will result in parse_csv_data2 returning None<br>

#### modification<br>

parse_csv_data2 is specialised for its role within the Covid19_Dashboard_pkg<br>
this specialisation is hard coded, but can be altered, if desired, to enable a wider range of usability<br>

the expected length of each element of covid_csv_data (defaulting to 7) is set in covid_data_handler.py, within parse_csv_data2, line 88,<br>
`if len(covid_csv_data[a]) != `**7**`:`<br>

the index by which to group elements (defaulting to 1) is referenced multiple times within covid_data_handler.py, within parse_csv_data2, lines 111, 114, and 120,<br>
`areaName = covid_csv_data[0][`**1**`]`<br>
`group = filter(lambda item : item[`**1**`] == areaName, group)`<br>
`if a in [`**1**`, 3]:`<br>

the index by which to sort grouped elements (defaulting to 3) is referenced multiple times within covid_data_handler.py, within parse_csv_data2, lines 116, and 120<br>
`date = item[`**3**`]`<br>
`if a in [1, `**3**`]:`<br>


### subprocess_covid_csv_data<br>

**a function to extract a cell from the contents read from a csv**<br>

determine what method of logging to use within subprocess_covid_csv_data<br>
determine if all desired arguments were given and whether they are appropriate<br>
determine if the target row exceeds the number of rows present<br>
determine if the target column header exists<br>
find the value at the given row/column intersection<br>
return either the value or, if desired and if the value is non-empty, the corresponding date<br>

> #### module dependancy<br>
>
> - logging<br>
> - - used to log events to a file<br>
> - - logging is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logging is not found to be present, `log` is set to `False`<br>

> #### global dependancy<br>
>
> - logger<br>
> - - an object from the logging module used as a framework when logging to files<br>
> - - logger is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logger is not found to be present, `log` is set to `False`<br>

> #### arguments<br>
>
> - data<br>
> - - a dictionary containing further dictionaries, each containing a number of further dictionaries, wherein all values are strings, as would be returned from `parse_csv_data2` or `covid_API_request`<br>
> - - data defaults to `None`
> - row<br>
> - - an integer pointing to the desired row (the index for the key of the desired dictionary within the ordered list of keys within the appropriate dictionary within `data`, as specified by `areaName`)<br>
> - - row is expected to be less than the number of elements in the appropriate dictionary (as specified by `areaName`)<br>
> - - row defaults to `None`<br>
> - col<br>
> - - a string, pointing to the key of the desired value<br>
> - - col is expected to be present within the list of keys of each sub sub dictionary of `data`<br>
> - - col defaults to `None`<br>
> - areaName<br>
> - - a string, indicating which of the sub-dictionaries within `data` should be searched<br>
> - - areaName is expected to be present within the list of keys of `data`<br>
> - - areaName defaults to `None`<br>
> - latestUpdate<br>
> - - a boolean, dictating whether it is the targeted value itself or the key of the sub sub dictionary storing that value that is desired (provided the value itself is non-empty)<br>
> - - if latestUpdate is set to `True` but the targeted value is an empty string, `subprocess_covid_csv_data` returns `None`<br>
> - - latestUpdate defaults to `False`<br>
> - log<br>
> - - a boolean, dictating whether to attempt to log to a file or directly to the python terminal<br>
> - - log is expected to be set to `True` only if the logging framework has been established elsewhere (typically in main.startup in standard runtime)<br>
> - - log defaults to `True`<br>
> - args<br>
> - - a list, catching any arguments in excess of those expected<br>
> - - args is expected to remain an empty list<br>
> - - args defaults to `[]`<br>
> - kwargs<br>
> - - a dictionary, catching any keyword arguments beyond those expected<br>
> - - kwargs is expected to remain an empty dictionary<br>
> - - kwargs defaults to `{}`<br>

with modules, globals, and arguments given as expected,<br>
returns the value for the key `col` within the dictionary who's key is at index `row` within the list of keys for the dictionary with key `areaName` within `data`<br>
alternatively, if latestUpdate is set to `True`,<br>
verifies whether or not the value is an empty string (""), returning None if it is or the key at index `row` within the list of keys for the dictionary with key `areaName` within `data` if it isn't<br>

with the exception of args and kwargs (for which any discrepencies merely log an INFO) and log (which is set to `True` if found to be anything other than a boolean),<br>
any arguments given in an unexpected manner will cause an appropriate log to be made (typically a WARNING) and will result in subprocess_csv_data returning None<br>


### process_covid_csv_data<br>

**a function to process the contents read from a csv**<br>

determine what method of logging to use within process_covid_csv_data<br>
determine if all desired functions are present (attempting to import if not)<br>
determine if all desired arguments were given and whether they are appropriate<br>
if necessary, convert the given covid_csv_data by way of parse_csv_data2<br>
for each target, iterate through each row until `subprocess_covid_csv_data` for that target and row returns a non-empty string<br>
if `target[header]` is "newCasesBySpecimenDate", take the next non-empty string value after this<br>
if `target[mode]` isn't "sum" or "rate", add this value to the dictionary of returns (keyed to by a name derived from the target)<br>
otherwise, sum the next n non-empty values (as specified by `target[index]`)<br>
if `target[mode]` isn't "rate", add the summed values to the dictionary of returns (keyed to by a name derived from the target)<br>
otherwise, divide the summed values by `target[index]` then add this result to the dictionary of returns (keyed to by a name derived from the target)<br>
if `subprocess_covid_csv_data` returns None at any point for a given target, add None to the dictionary of returns (keyed to by a name derived from the target)<br>

the name for each value in the dictionary of returns is derived from the target,<br>
`key = target["mode"] + "_" + ["", "last" + str(target["extra"]) + "days_"][target["mode"] in ["sum", "rate"]] + target["header"]`<br>

> #### module dependancy<br>
>
> - logging<br>
> - - used to log events to a file<br>
> - - logging is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logging is not found to be present, `log` is set to `False`<br>
> - covid_data_handler.parse_csv_data2<br>
> - - used to convert a non-empty list of strings (as would be returned by parse_csv_data) into a a dictionary containing further dictionaries, each containing a number of further dictionaries, wherein all values are strings<br>
> - - covid_data_handler.parse_csv_data2 is only expected to be present globally if the argument `csv` is set to `True`<br>
> - covid_data_handler.subprocess_covid_csv_data<br>
> - - used to find the value (or corresponding date as indicated by latestUpdate) within a dictionary (as would be returned from `parse_csv_data2` or `covid_API_request`) for a given areaName (specifying a sub dictionary to search), row (specifying the index of the dictionary within the sub dictionary that should be searched), and col (specifying the key of the value)<br>

> #### global dependancy<br>
>
> - logger<br>
> - - an object from the logging module used as a framework when logging to files<br>
> - - logger is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logger is not found to be present, `log` is set to `False`<br>

> #### arguments<br>
>
> - covid_csv_data
> - - if `csv` is set to `True`, covid_csv_data is expected to be a list of strings as would be returned from `parse_csv_data`
> - - if `csv` is set to `False`, covid_csv_data is expected to be a dictionary containing further dictionaries, each containing a number of further dictionaries, as would be returned from `parse_csv_data2` or `covid_API_request`<br>
> - - covid_csv_data defaults to `None`
> - args<br>
> - - a list, catching any arguments in excess of those expected<br>
> - - args is expected to remain an empty list<br>
> - - args defaults to `[]`<br>
> - targets
> - - a list of dictionaries
> - - each dictionay is expected to contain, in order, the keys "header" (matching one of the keys present in sub sub dictionaries of covid_csv_data (after it has been acted on by parse_csv_data2 if appropriate)), "mode" (one of "latest", "latestUpdate", "sum", or "rate"), "extra" (either None, or an integer depending on mode)<br>
> - - targets defaults to `targets = [{"header" : "newCasesBySpecimenDate", "mode" : "sum", "extra" : 7}, {"header" : "hospitalCases", "mode" : "latest", "extra" : None}, {"header" : "cumDailyNsoDeathsByDeathDate", "mode" : "latest", "extra" : None}]`<br>
> - areaName<br>
> - - a string, indicating which of the sub-dictionaries of covid_csv_data (after it has been acted on by parse_csv_data2 if appropriate) should be searched<br>
> - - areaName defaults to `"England"`
> - csv<br>
> - - a boolean indicating whether `covid_csv_data` requires `parse_csv_data2`<br>
> - - csv is expected to be set to `True` if `covid_csv_data` is a list of strings, as would be returned by `parse_csv_data`<br>
> - - csv is expected to be set to `False` if `covid_csv_data` is a dictionary containing further dictionaries, each containing a number of further dictionaries, as would be returned from `parse_csv_data2` or `covid_API_request`<br>
> - - csv defaults to `True`
> - log<br>
> - - a boolean, dictating whether to attempt to log to a file or directly to the python terminal<br>
> - - log is expected to be set to `True` only if the logging framework has been established elsewhere (typically in main.startup in standard runtime)<br>
> - - log defaults to `True`<br>
> - kwargs<br>
> - - a dictionary, catching any keyword arguments beyond those expected<br>
> - - kwargs is expected to remain an empty dictionary<br>
> - - kwargs defaults to `{}`<br>

with modules, globals, and arguments given as expected,<br>
returns a dictionary where each target in targets keys to the corresponding value / sum of values / average of values within the sub dictionary of covid_csv_data as specified by areaName<br>

with the exception of logging (and parse_csv_data2 if csv is set to `False`), any modules not available will cause an appropriate log to be made (typically a WARNING if not present followed by a CRITICAL if attempts to import fail) and will result in process_csv_data returning None if unable to import<br>

with the exception of args and kwargs (for which any discrepencies merely log an INFO) and log (which is set to `True` if found to be anything other than a boolean),<br>
any arguments given in an unexpected manner will cause an appropriate log to be made (typically a WARNING) and will result in process_csv_data returning None<br>

#### Target Translation<br>

**the `targets` argument is used to indicate what data is to be extracted or calculated from the given covid_csv_data**<br>
**it is interpretted as follows**<br>

> ##### header<br>
>
> indicates what piece of covid data is desired, naming the desired header of the covid csv file (not including date or areaName)<br>
> header can be one of:<br>
> - "areaCode"<br>
> - "areaType"<br>
> - "cumDailyNsoDeathsByDeathDate"<br>
> - "hospitalCases"<br>
> - "newCasesBySpecimenDate"<br>
> the latter 3 sre likely the norm<br>
> other values can be given for header (which could be useful if this function is modified to work on other csv files, in which case the header should be one from the csv file in use - not including the ones used for grouping and sorting the data within parse_csv_data2).<br>
> if an invalid value for headers is used (one not present in sub sub dictionaries of data as returned from parse_csv_data2), the returned dictionary will key this translated target to `None`<br>

> ##### mode<br>
>
> indicates what operation should be performed on the data<br>
> mode can be one of:<br>
> - "latest", requesting the first non-empty value for the specified header<br>
> - "latestUpdate", requesting the corresponding date (the header by which data is sorted by parse_csv_data2) to the first non-empty value for the specified header<br>
> - "sum", requesting the total obtained from adding the first **n** non-empty values in the specified header, where **n** is the value given for extra<br>
> - - note, "sum" will key the translated target to `None` if the values encountered are not integers<br>
> - - note, "sum" will key the translated target to `None` if there are less than **n** non-empty values<br>
> - "rate", requesting the total (as for "sum") and then dividing it by the value given for extra<br>
> - - note, "rate" can fail and key the translated target to `None` for the same reasons as "sum"<br>

> ##### extra<br>
>
> expected to be either `None` (if mode is one of "latest" or "latestUpdate") or an integer (if mode is one of "sum" or "rate")<br>

the keys of the dictionary returned by process_csv_data (the keys to which the resulting values are keyed) are constructed as follows:<br>
`key = target["mode"] + "_" + ["", "last" + str(target["extra"]) + "days_"][target["mode"] in ["sum", "rate"]] + target["header"]`<br>
the key starts with the given "mode", followed by "_"<br>
if the given "mode" was "sum" or "rate", the key continues with the string "last", followed by the given "extra", followed by the string "days_"<br>
lastly, the key ends with the given header<br>


### covid_API_request<br>

**a function to retrieve live data from the uk_covid19 Cov19API for a given location and following a given date**<br>

determine what method of logging to use within process_covid_csv_data<br>
determine if all desired functions are present (attempting to import if not)<br>
determine if all desired arguments were given and whether they are appropriate<br>
construct an appropriate link from given arguments<br>
attempt to use this link to access the uk_covid19 Cov19API<br>
verify the response code given<br>
convert the data returned into the desired format (a dictionary containing further dictionaries, each containing a number of further dictionaries, as would be returned from `parse_csv_data2`)<br>
seperate the new/desired data (as indicated by the date argument)<br>
return this new data<br>

> #### module dependancy<br>
>
> - logging<br>
> - - used to log events to a file<br>
> - - logging is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logging is not found to be present, `log` is set to `False`<br>
> - datetime.datetime<br>
> - - used to convert between formatted strings (YYYY-mm-dd) and the total number of seconds ellapsed since 1900-01-01 and back again<br>
> - requests<br>
> - - used to send requests over the internet with appropriate links<br>
> - json<br>
> - - used to convert a string of appropriate format (containing ",", and enclosed "{}" and "[]") into a nested dictionary/list/etc as appropriate<br>

> #### global dependancy<br>
>
> - logger<br>
> - - an object from the `logging` module<br>
> - - logger is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logger is not found to be present, `log` is set to `False`<br>

> #### arguments<br>
>
> - location<br>
> - - a string, indicating what should be given for the argument areaName in the query of the link to be sent to the uk_covid19 Cov19API<br>
> - - location should be an acceptable value for the argument areaName in the query of the link to be sent to the uk_covid19 Cov19API<br>
> - - location defaults to `"Exeter"`<br>
> - location_type<br>
> - - a string, indicating what should be given for the argument areaType in the query of the link to be sent to the uk_covid19 Cov19API<br>
> - - location_type should be an acceptable value for the argument areaType in the query of the link to be sent to the uk_covid19 Cov19API<br>
> - - location_type defaults to `"ltla"`<br>
> - args<br>
> - - a list, catching any arguments in excess of those expected<br>
> - - args is expected to remain an empty list<br>
> - - args defaults to `[]`<br>
> - date<br>
> - - a string, representing the earliest date for which to retrieve new covid statistics from the uk_covid19 Cov19API<br>
> - - date is expected to be an appropriate date of the form YYYY-mm-dd<br>
> - - date defaults to `"2020-01-30"`, the earliest date for which the uk_covid19 Cov19API holds data<br>
> - structure<br>
> - - a dictionary indicating what variables are requested and in what order<br>
> - - each value in structure should indicate a valid metric within the uk_covid19 Cov19API<br>
> - - structure defaults to `{"areaCode": "areaCode", "areaType": "areaType", "date": "date", "cumDailyNsoDeathsByDeathDate": "cumDailyNsoDeathsByDeathDate", "hospitalCases": "hospitalCases", "newCasesBySpecimenDate": "newCasesBySpecimenDate"}`<br>
> - log<br>
> - - a boolean, dictating whether to attempt to log to a file or directly to the python terminal<br>
> - - log is expected to be set to `True` only if the logging framework has been established elsewhere (typically in main.startup in standard runtime)<br>
> - - log defaults to `True`<br>
> - kwargs<br>
> - - a dictionary, catching any keyword arguments beyond those expected<br>
> - - kwargs is expected to remain an empty dictionary<br>
> - - kwargs defaults to `{}`<br>

with modules, globals, and arguments given as expected,<br>
returns a dictionary containing location as a key, paired to a dictionary<br>
for this sub dictionary, the keys are the dates for each collection of covid data provided by the uk_covid19 Cov19API<br>
each of these dates keys to a dictionary containing the rest of the metrics requested (the metrics present, the keys used, and the order are dictated by structure)<br>

with the exception of logging, any modules not available will cause an appropriate log to be made (typically a WARNING if not present followed by a CRITICAL if attempts to import fail) and will result in covid_API_request returning None if unable to import<br>

with the exception of args and kwargs (for which any discrepencies merely log an INFO), log (which is set to `True` if found to be anything other than a boolean), and date (which is set to "2020-01-30" if found to be inappropriate),<br>
any arguments given in an unexpected manner will cause an appropriate log to be made (typically a WARNING) and will result in covid_API_request returning None<br>


### csv_writeup<br>

**a function to write to a csv file**<br>

determine what method of logging to use within csv_writeup<br>
determine if all desired arguments were given and whether they are appropriate<br>
add the header string, "areaCode,areaName,areaType,date,cumDailyNsoDeathsByDeathDate,hospitalCases,newCasesBySpecimenDate" to a list<br>
for each sub sub dictionary in data, place the values present into a "," seperated string, matching the position of their respective headers<br>
for areaName, use the key of the sub dictionary<br>
for date, use the key of the sub sub dictionary<br>
place each string into the list<br>
empty the existing file<br>
write each string line by line from the list to the file<br>

> #### module dependancy<br>
>
> - logging<br>
> - - used to log events to a file<br>
> - - logging is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logging is not found to be present, `log` is set to `False`<br>

> #### global dependancy<br>
>
> - logger<br>
> - - an object from the logging module used as a framework when logging to files<br>
> - - logger is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logger is not found to be present, `log` is set to `False`<br>

> #### arguments
>
> - csv_filename<br>
> - - a string, naming the file to attempt to read<br>
> - - csv_filename is expected to end in ".csv"<br>
> - - csv_filename defaults to `None`<br>
> - data<br>
> - - a dictionary containing further dictionaries, each containing a number of further dictionaries, wherein all values are strings, as would be returned from `parse_csv_data2` or `covid_API_request`<br>
> - - data defaults to `None`
> - log<br>
> - - a boolean, dictating whether to attempt to log to a file or directly to the python terminal<br>
> - - log is expected to be set to `True` only if the logging framework has been established elsewhere (typically in main.startup in standard runtime)<br>
> - - log defaults to `True`<br>
> - args<br>
> - - a list, catching any arguments in excess of those expected<br>
> - - args is expected to remain an empty list<br>
> - - args defaults to `[]`<br>
> - kwargs<br>
> - - a dictionary, catching any keyword arguments beyond those expected<br>
> - - kwargs is expected to remain an empty dictionary<br>
> - - kwargs defaults to `{}`<br>

with modules, globals, and arguments given as expected,<br>
effectively reverses the effect of performing `parse_csv_data` followed by `parse_csv_data2` on a csv file<br>
places a pre-determined header line in the csv file pointed to by `csv_filename`<br>
each sub sub dictionary of `data` is converted to a line in the csv file pointed to by `csv_filename`<br>
each line has all the values its sub sub dictionary contained as well as both its key and the key of the sub dictionary it was stored in<br>
all values are arranged to match the header line<br>

with the exception of args and kwargs (for which any discrepencies merely log an INFO) and log (which is set to `True` if found to be anything other than a boolean),<br>
any arguments given in an unexpected manner will cause an appropriate log to be made (typically a WARNING) and will result in csv_writeup returning None<br>

#### modification<br>

csv_writeup is specialised for its role within the Covid19_Dashboard_pkg<br>
this specialisation is hard coded, but can be altered, if desired, to enable a wider range of usability<br>

the header line (defaulting to "areaCode,areaName,areaType,date,cumDailyNsoDeathsByDeathDate,hospitalCases,newCasesBySpecimenDate"), is set in covid_data_handler.py, within csv_writeup, line 548,<br>
`new_data = [`**"areaCode,areaName,areaType,date,cumDailyNsoDeathsByDeathDate,hospitalCases,newCasesBySpecimenDate"**`]`<br>

the expected length of each sub sub dictionary of data (defaulting to 5) is referenced multiple times in covid_data_handler.py, within csv_writeup, lines 535, 552, and 558<br>
`if len(data[item][item2]) != `**5**`:`<br>
`for a in range(`**5**`):`<br>
`if a != `**5**` - 1:`<br>

the index in which to place the key of the sub dictionary (defaulting to 1) is set in covid_data_handler.py, within csv_writeup, line 553,<br>
`if a == `**1**`:`<br>

the index in which to place the key of the sub sub dictionary (defaulting to 3) is set in covid_data_handler.py, within csv_writeup, line 555,<br>
`if a == `**3**` - 1:`<br>

the index by which to sort grouped elements (defaulting to 3) is referenced multiple times within covid_data_handler.py, within parse_csv_data2, lines 116, and 120<br>
`date = item[`**3**`]`<br>
`if a in [1, `**3**`]:`<br>


### csv_update

**a function to update a csv file with new data obtained from uk_covid19 Cov19API**

determine what method of logging to use within csv_update<br>
determine if all desired functions are present (attempting to import if not)<br>
determine if all desired arguments were given and whether they are appropriate<br>
call `parse_csv_data(csv_filename)` to get the data stored within the csv file pointed to by `csv_filename`<br>
if `parse_csv_data` was succesful (indicating the file already existed), call `parse_csv_data2(data)` on its returned data<br>
if any problems are encountered, default data to `{}`<br>
ensure that `location` is present as one of the keys within data<br>
find the latest date for which all keys have values within data for the specified location (calling `process_covid_csv_data(data, targets = [{"header" : "cumDailyNsoDeathsByDeathDate", "mode" : "latestUpdate", "extra" : None}], areaName = location, csv = False)`)<br>
call `covid_API_request(location, location_type, date = date)` to obtain any missing data<br>
add this new data to the current data<br>
call `csv_writeup(csv_filename, data)`<br>

> #### module dependancy<br>
>
> - logging<br>
> - - used to log events to a file<br>
> - - logging is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logging is not found to be present, `log` is set to `False`<br>
> - datetime.datetime<br>
> - - used to convert between formatted strings (YYYY-mm-dd) and the total number of seconds ellapsed since 1900-01-01 and back again<br>
> - covid_data_handler.parse_csv_data<br>
> - - used to read a csv file, returning a list containing strings for each line in the csv file
> - covid_data_handler.parse_csv_data2<br>
> - - used to convert a non-empty list of strings (as would be returned by parse_csv_data) into a a dictionary containing further dictionaries, each containing a number of further dictionaries, wherein all values are strings<br>
> - covid_data_handler.covid_API_request<br>
> - - used to obtain up to date covid statistics from the uk_covid19 Cov19API<br>
> - covid_data_handler.process_covid_csv_data<br>
> - - used to find the earliest date for which all values are present<br>
> - covid_data_handler.csv_writeup<br>
> - - used to write the new data to a csv file<br>

> #### global dependancy<br>
>
> - logger<br>
> - - an object from the logging module used as a framework when logging to files<br>
> - - logger is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logger is not found to be present, `log` is set to `False`<br>

> #### arguments<br>
>
> - csv_filename<br>
> - - a string, naming the file to attempt to read<br>
> - - csv_filename is expected to end in ".csv"<br>
> - - csv_filename defaults to `None`<br>
> - location<br>
> - - a string, indicating what sub dictionary is to be updated, and what should be passed as the argument `location` to the `covid_API_request` function<br>
> - - location defaults to `"England"`<br>
> - location_type<br>
> - - a string, indicating what should be passed as the argument `location_type` to the `covid_API_request` function<br>
> - - location_type defaults to `"nation"`<br>
> - log<br>
> - - a boolean, dictating whether to attempt to log to a file or directly to the python terminal<br>
> - - log is expected to be set to `True` only if the logging framework has been established elsewhere (typically in main.startup in standard runtime)<br>
> - - log defaults to `True`<br>
> - args<br>
> - - a list, catching any arguments in excess of those expected<br>
> - - args is expected to remain an empty list<br>
> - - args defaults to `[]`<br>
> - kwargs<br>
> - - a dictionary, catching any keyword arguments beyond those expected<br>
> - - kwargs is expected to remain an empty dictionary<br>
> - - kwargs defaults to `{}`<br>

with modules, globals, and arguments given as expected,<br>
`data = parse_covid_csv_data2(parse_covid_csv_data(csv_filename))`<br>
finds the earliest date from which values are missing from sub dictionaries of the sub dictionary keyed to by `location` in `data` using `process_covid_csv_data`<br>
obtain this missing data using `covid_API_request` (giving the date, location, and location_type)<br>
add the new data to the sub dictionary of `data` keyed to by `location`<br>
write the new data to the csv file using `csv_writeup`<br>

with the exception of logging, any modules not available will cause an appropriate log to be made (typically a WARNING if not present followed by a CRITICAL if attempts to import fail) and will result in csv_update returning None if unable to import<br>

with the exception of args and kwargs (for which any discrepencies merely log an INFO), log (which is set to `True` if found to be anything other than a boolean), and date (which is set to "2020-01-30" if found to be inappropriate),<br>
any arguments given in an unexpected manner will cause an appropriate log to be made (typically a WARNING) and will result in csv_update returning None<br>


### covid_update

**a function to update covid data from uk_covid19 Cov19API**

determine what method of logging to use within covid_update<br>
if present within the global updates, have this update remove itself (creating a copy if meant to repeat)<br>
determine if all desired functions are present (attempting to import if not)<br>
determine if all desired globals are present (defaulting where possible if not)<br>
attempt to call csv_update both for "England", "Nation" and for the globals AreaName, AreaType<br>
if both calls were succesful, call parse_csv_data2(parse_csv_data(csv_filename))<br>
set data equal to this call if succesful<br>
otherwise, call covid_API_request both for "England", "Nation" and for the globals AreaName, AreaType, combining the results into a single dictionary<br>
call process_covid_csv_data to extract the desired variables from data<br>
assign each variable to its appropriate global<br>

> #### module dependancy<br>
>
> - logging<br>
> - - used to log events to a file<br>
> - - logging is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logging is not found to be present, `log` is set to `False`<br>
> - covid_data_handler.schedule_covid_updates<br>
> - - used to reschedule an update in the event that the given update is meant to repeat<br>
> - - covid_data_handler.schedule_covid_updates is only expected to be present globally if the key "repeat" for the element in global updates for which the value for the key "title" is equal to that of the argument `update_name` and the value for the key "type" is equal to 0 is equal to `True`<br>
> - covid_data_handler.csv_update<br>
> - - to update the contents of the stored csv file
> - covid_data_handler.parse_csv_data<br>
> - - used to read a csv file, returning a list containing strings for each line in the csv file
> - covid_data_handler.parse_csv_data2<br>
> - - used to convert a non-empty list of strings (as would be returned by parse_csv_data) into a a dictionary containing further dictionaries, each containing a number of further dictionaries, wherein all values are strings<br>
> - covid_data_handler.covid_API_request<br>
> - - used to obtain up to date covid statistics from the uk_covid19 Cov19API<br>
> - covid_data_handler.process_covid_csv_data<br>
> - - used to find the earliest date for which all values are present<br>

> #### global dependancy<br>
>
> - logger<br>
> - - an object from the logging module used as a framework when logging to files<br>
> - - logger is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logger is not found to be present, `log` is set to `False`<br>
> - updates<br>
> - - a list of dictionaries, storing all the scheduled updates within the program<br>
> - csv_filename<br>
> - - a string, naming the csv_file to be used by the program<br>
> - - if not present, covid_update will not attempt to update the csv file
> - local_7day_infections<br>
> - - a string, storing the most recently updated value for local 7 day infections<br>
> - - presence and content are unimportant as this global is to be overwritten only<br>
> - national_7day_infections<br>
> - - a string, storing the most recently updated value for national 7 day infections<br>
> - - presence and content are unimportant as this global is to be overwritten only<br>
> - hospital_cases<br>
> - - a string, storing the most recently updated value for hospital cases<br>
> - - presence and content are unimportant as this global is to be overwritten only<br>
> - deaths_total<br>
> - - a string, storing the most recently updated value for total deaths<br>
> - - presence and content are unimportant as this global is to be overwritten only<br>
> - AreaName<br>
> - - a string, indicating the name of the local area (to be used by `csv_update` or `covid_API_request`)<br>
> - - if not present, AreaName defaults to `"Exeter"`<br>
> - AreaType<br>
> - - a string, indicating the type of the local area (to be used by `csv_update` or `covid_API_request`)<br>
> - - if not present, AreaType defaults to `"ltla"`<br>

> #### arguments<br>
>
> - update_name<br>
> - - a string, storing the name for this update (assuming that covid_update was scheduled by `schedule_covid_updates`)<br>
> - - update_name defaults to `None`<br>
> - args<br>
> - - a list, catching any arguments in excess of those expected<br>
> - - args is expected to remain an empty list<br>
> - - args defaults to `[]`<br>
> - log<br>
> - - a boolean, dictating whether to attempt to log to a file or directly to the python terminal<br>
> - - log is expected to be set to `True` only if the logging framework has been established elsewhere (typically in main.startup in standard runtime)<br>
> - - log defaults to `True`<br>
> - kwargs<br>
> - - a dictionary, catching any keyword arguments beyond those expected<br>
> - - kwargs is expected to remain an empty dictionary<br>
> - - kwargs defaults to `{}`<br>

with modules, globals, and arguments given as expected,<br>
ensure the global updates is up to date<br>
attempt to update the csv file using csv_update<br>
if succesful, process the data within the csv file for desired variables<br>
otherwise, process the data returned from covid_API_request for desired variables<br>
update variables globally<br>

with the exception of logging, and csv_update, parse_csv_data, and parse_csv_data2 (the lack of any the latter 3 simply causing covid_update to not attempt to update the csv file) any modules not available will cause an appropriate log to be made (typically a WARNING if not present followed by a CRITICAL if attempts to import fail) and will result in covid_update returning None if unable to import<br>


### schedule_covid_updates

**a function to schedule updates to covid data**

determine what method of logging to use within schedule_covid_updates<br>
determine if all desired functions are present (attempting to import if not)<br>
determine if all desired globals are present (defaulting where possible if not)<br>
determine if all desired arguments were given and whether they are appropriate<br>
if needed, alter the update name to make it unique (eg: "repeat_name(1)")<br>
calculate the time (in the appropriate form) from the given update interval<br>
schedule an event with the `scheduler` module to run `covid_update` at the calculated time, inheriting the argument `update_name`<br>
update the global `updates` to include this new event and associated information (appending a dictionary with keys "time", "time2", "type", "title", "content", "event", "repeat")<br>

> #### module dependancy<br>
>
> - logging<br>
> - - used to log events to a file<br>
> - - logging is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logging is not found to be present, `log` is set to `False`<br>
> - sched<br>
> - - used to schedule functions to run at specified times<br>
> - time<br>
> - - used as a foundation for `schedule`, and to obtain the current time<br>
> - datetime.datetime<br>
> - - used to convert between formatted strings (YYYY-mm-dd) and the total number of seconds ellapsed since 1900-01-01 and back again<br>
> - covid_data_handler.covid_update<br>
> - - used to update covid statistics (both within the program itself and within a csv file)<br>

> #### global dependancy<br>
>
> - logger<br>
> - - an object from the logging module used as a framework when logging to files<br>
> - - logger is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logger is not found to be present, `log` is set to `False`<br>
> - updates<br>
> - - a list of dictionaries, storing all the scheduled updates within the program<br>
> - schedule<br>
> - - an object from the sched module used to schedule functions to run at a specified time<br>

> #### arguments<br>
>
> - update_interval<br>
> - - a string, storing the time for which to schedule the update<br>
> - - update_interval is expected to be an appropriate time of the format HH%3aMM (the format returned by the dashboard) or HH:MM<br>
> - - update_interval defaults to `None`<br>
> - update_name<br>
> - - a string, storing the name for the new update<br>
> - - update_name defaults to `None`<br>
> - args<br>
> - - a list, catching any arguments in excess of those expected<br>
> - - args is expected to remain an empty list<br>
> - - args defaults to `[]`<br>
> - repeat<br>
> - - a boolean, indicating whether the event being scheduled is to occur once or repeatedly<br>
> - - repeat defaults to `False`<br>
> - log<br>
> - - a boolean, dictating whether to attempt to log to a file or directly to the python terminal<br>
> - - log is expected to be set to `True` only if the logging framework has been established elsewhere (typically in main.startup in standard runtime)<br>
> - - log defaults to `True`<br>
> - kwargs<br>
> - - a dictionary, catching any keyword arguments beyond those expected<br>
> - - kwargs is expected to remain an empty dictionary<br>
> - - kwargs defaults to `{}`<br>

with modules, globals, and arguments given as expected,<br>
schedule `covid_update` to run at the time given by `update_interval`<br>
append to the global `updates` the dictionary `{"time" : converted_time, "time2" : update_interval, "type" : 0, "title" : converted_name, "content" : update_interval + ", Covid data", "event" : event, "repeat" : repeat}`<br>
where converted_time is the actual number of seconds meant by `update_interval`, converted_name is the `update_name` with any extra suffixes given for uniqueness (eg: repeat_name(1)), and event is the object representing the scheduled running of `covid_update` (this is needed if the scheduled update is to be cancelled later)<br>

with the exception of logging, any modules not available will cause an appropriate log to be made (typically a WARNING if not present followed by a CRITICAL if attempts to import fail) and will result in schedule_covid_updates returning None if unable to import<br>

with the exception of args and kwargs (for which any discrepencies merely log an INFO), log (which is set to `True` if found to be anything other than a boolean),<br>
any arguments given in an unexpected manner will cause an appropriate log to be made (typically a WARNING) and will result in schedule_covid_updates returning None<br>

---

## covid_news_handling<br>

**a module for news data handling functionality**

### news_API_request

**a function to retrieve new live news articles from the newsAPI containing given terms and following a given date**

determine what method of logging to use within covid_update<br>
if present within the global updates, have this update remove itself (creating a copy if meant to repeat)<br>
determine if all desired functions are present (attempting to import if not)<br>
determine if all desired globals are present (defaulting where possible if not)<br
determine if all desired arguments were given and whether they are appropriate<br>
remove any elements of `covid_terms` for which another element in `covid_terms` is a substring of this element<br>
until enough news articles are collected, repeatedly iterate through each element in `covid_terms`<br>
construct a link to use with the `newsapi` from the element in `covid_terms` and the globals `date` and `API_key`<br>
attempt to use this link to access the newsAPI<br>
verify the response code given<br>
remove any articles in the response that are already referenced in the global `remove` (indicating that these articles have been seen already)<br>
add any remaining articles to the temporary news variable and reference them in the global `remove`<br>
increase the page counter by 1 for the next iteration (if required)<br>
remove any outdated elements of `remove`<br>
overwrite the global `news` with the contents of the temporary news variables<br>

> #### module dependancy<br>
>
> - logging<br>
> - - used to log events to a file<br>
> - - logging is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logging is not found to be present, `log` is set to `False`<br>
> - covid_news_handling.update_news<br>
> - - used to reschedule an update in the event that the given update is meant to repeat<br>
> - - covid_news_handling.update_news is only expected to be present globally if the key "repeat" for the element in global updates for which the value for the key "title" is equal to that of the argument `update_name` and the value for the key "type" is equal to 1 is equal to `True`<br>
> - datetime.datetime<br>
> - - used to convert between formatted strings (YYYY-mm-dd) and the total number of seconds ellapsed since 1900-01-01 and back again<br>
> - datetime.timedelta<br>
> - - used to convert a given number of days to the corresponding number of seconds<br>
> - requests<br>
> - - used to send requests over the internet with appropriate links<br>
> - json<br>
> - - used to convert a string of appropriate format (containing ",", and enclosed "{}" and "[]") into a nested dictionary/list/etc as appropriate<br>

> #### global dependancy<br>
>
> - logger<br>
> - - an object from the logging module used as a framework when logging to files<br>
> - - logger is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logger is not found to be present, `log` is set to `False`<br>
> - updates<br>
> - - a list of dictionaries, storing all the scheduled updates within the program<br>
> - API_key
> - - a string, recquired for succesful interactions with the news_API<br>
> - - API_key is expected to be a valid API key for the news_API<br>
> - remove<br>
> - - a dictionary, containing the titles of news articles keyed with the date they were obtained<br>
> - - all values contained should be strings, representing dates and are therefore expected to be appropriate dates of the form YYYY-mm-dd<br>
> - news<br>
> - - a list of dictionaries, containing news articles<br>
> - - each dictionary should have the keys "title", "content"<br>

> #### arguments<br>
>
> - update_interval<br>
> - - a string, storing the time for which to schedule the update<br>
> - - update_interval is expected to be an appropriate time of the format HH%3aMM (the format returned by the dashboard) or HH:MM<br>
> - - update_interval defaults to `None`<br>

> - covid_terms<br>
> - - a string of individual terms (substrings seperated by spaces) each of which will be used as a query sent to the news_API<br>
> - - covid_terms defaults to `None`
> - args<br>
> - - a list, catching any arguments in excess of those expected<br>
> - - args is expected to remain an empty list<br>
> - - args defaults to `[]`<br>
> - update_name<br>
> - - a string, storing the name for this update (assuming that news_API_request was scheduled by `update_news`)<br>
> - - update_name defaults to `None`<br>
> - repeat<br>
> - - a boolean, indicating whether the event being scheduled is to occur once or repeatedly<br>
> - - repeat defaults to `False`<br>
> - log<br>
> - - a boolean, dictating whether to attempt to log to a file or directly to the python terminal<br>
> - - log is expected to be set to `True` only if the logging framework has been established elsewhere (typically in main.startup in standard runtime)<br>
> - - log defaults to `True`<br>
> - kwargs<br>
> - - a dictionary, catching any keyword arguments beyond those expected<br>
> - - kwargs is expected to remain an empty dictionary<br>
> - - kwargs defaults to `{}`<br>

with the exception of logging, any modules not available will cause an appropriate log to be made (typically a WARNING if not present followed by a CRITICAL if attempts to import fail) and will result in news_API_request returning None if unable to import<br>

if nothing is given for covid_terms,<br>
a WARNING log will be made and news_API_request will return None<br>


### update_news

**a function to schedule updates to news articles**

determine what method of logging to use within update_news<br>
determine if all desired functions are present (attempting to import if not)<br>
determine if all desired globals are present (defaulting where possible if not)<br>
determine if all desired arguments were given and whether they are appropriate<br>
if needed, alter the update name to make it unique (eg: "repeat_name(1)")<br>
calculate the time (in the appropriate form) from the given update interval<br>
schedule an event with the `scheduler` module to run `news_API_request` at the calculated time, inheriting the argument `update_name`<br>
update the global `updates` to include this new event and associated information (appending a dictionary with keys "time", "time2", "type", "title", "content", "event", "repeat")<br>

> #### module dependancy<br>
>
> - logging<br>
> - - used to log events to a file<br>
> - - logging is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logging is not found to be present, `log` is set to `False`<br>
> - sched<br>
> - - used to schedule functions to run at specified times<br>
> - time<br>
> - - used as a foundation for `schedule`, and to obtain the current time<br>
> - datetime.datetime<br>
> - - used to convert between formatted strings (YYYY-mm-dd) and the total number of seconds ellapsed since 1900-01-01 and back again<br>
> - covid_news_handling.news_API_request<br>
> - - used to update news articles<br>

> #### global dependancy<br>
>
> - logger<br>
> - - an object from the logging module used as a framework when logging to files<br>
> - - logger is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logger is not found to be present, `log` is set to `False`<br>
> - updates<br>
> - - a list of dictionaries, storing all the scheduled updates within the program<br>
> - schedule<br>
> - - an object from the sched module used to schedule functions to run at a specified time<br>

> #### arguments<br>
>
> - update_interval<br>
> - - a string, storing the time for which to schedule the update<br>
> - - update_interval is expected to be an appropriate time of the format HH%3aMM (the format returned by the dashboard) or HH:MM<br>
> - - update_interval defaults to `None`<br>
> - update_name<br>
> - - a string, storing the name for the new update<br>
> - - update_name defaults to `None`<br>
> - args<br>
> - - a list, catching any arguments in excess of those expected<br>
> - - args is expected to remain an empty list<br>
> - - args defaults to `[]`<br>
> - repeat<br>
> - - a boolean, indicating whether the event being scheduled is to occur once or repeatedly<br>
> - - repeat defaults to `False`<br>
> - log<br>
> - - a boolean, dictating whether to attempt to log to a file or directly to the python terminal<br>
> - - log is expected to be set to `True` only if the logging framework has been established elsewhere (typically in main.startup in standard runtime)<br>
> - - log defaults to `True`<br>
> - kwargs<br>
> - - a dictionary, catching any keyword arguments beyond those expected<br>
> - - kwargs is expected to remain an empty dictionary<br>
> - - kwargs defaults to `{}`<br>

with modules, globals, and arguments given as expected,<br>
schedule `news_API_request` to run at the time given by `update_interval`<br>
append to the global `updates` the dictionary `{"time" : converted_time, "time2" : update_interval, "type" : 0, "title" : converted_name, "content" : update_interval + ", news articles", "event" : event, "repeat" : repeat}`<br>
where converted_time is the actual number of seconds meant by `update_interval`, converted_name is the `update_name` with any extra suffixes given for uniqueness (eg: "repeat_name(1)"), and event is the object representing the scheduled running of `news_API_request` (this is needed if the scheduled update is to be cancelled later)<br>

with the exception of logging, any modules not available will cause an appropriate log to be made (typically a WARNING if not present followed by a CRITICAL if attempts to import fail) and will result in update_news returning None if unable to import<br>

with the exception of args and kwargs (for which any discrepencies merely log an INFO), log (which is set to `True` if found to be anything other than a boolean),<br>
any arguments given in an unexpected manner will cause an appropriate log to be made (typically a WARNING) and will result in update_news returning None<br>

---

## main<br>

**a module for combining the covid_news_handling and covid_data_handler modules**<br>

### json_read<br>

**a function to read from a json file**<br>

determine what method of logging is appropriate within json_read<br>
determine if all desired functions are present (attempting to import if not)<br>
determine if a file name was given and if it is appropriate (ended in ".json")<br>
determine if the file exists within the Covid19_Dashboard_pkg directory<br>
read from the file and attempt to convert it to a nested dictionary structure using json<br>
compare the format and keys to what would be expected for either the config or status file (indicated by `mode`)<br>
compare the type of each value to what would be expected for either the config or status file (indicated by `mode`)<br>
if the contents is appropriate, return this data<br>

> #### module dependancy<br>
>
> - logging<br>
> - - used to log events to a file<br>
> - - logging is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logging is not found to be present, `log` is set to `False`<br>
> - os.path.isfile<br>
> - - used to determine whether or not a file exists within the Covid_dashboard_pkg directory<br>
> - json<br>
> - - used to convert a string of appropriate format (containing ",", and enclosed "{}" and "[]") into a nested dictionary/list/etc as appropriate<br>

> #### global dependancy<br>
>
> - logger<br>
> - - an object from the logging module used as a framework when logging to files<br>
> - - logger is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logger is not found to be present, `log` is set to `False`<br>

> #### arguments<br>
>
> - json_filename<br>
> - - a string, naming the file to attempt to read<br>
> - - json_filename is expected to end in ".json" and should point to an existing json file that is accessible within the Covid_Dashboard_pkg directory<br>
> - - json_filename defaults to `"config.json"`<br>
> - mode<br>
> - - a boolean, indicating whether the file being read is the config file (0) or the status file (1)<br>
> - - mode defaults to `0`<br>
> - log<br>
> - - a boolean, dictating whether to attempt to log to a file or directly to the python terminal<br>
> - - log is expected to be set to `True` only if the logging framework has been established elsewhere (typically in main.startup in standard runtime)<br>
> - - log defaults to `True`<br>
> - args<br>
> - - a list, catching any arguments in excess of those expected<br>
> - - args is expected to remain an empty list<br>
> - - args defaults to `[]`<br>
> - kwargs<br>
> - - a dictionary, catching any keyword arguments beyond those expected<br>
> - - kwargs is expected to remain an empty dictionary<br>
> - - kwargs defaults to `{}`<br>

with modules, globals and arguments given as expected,<br>
the json file is read and converted to a nested dictionary<br>
if the format and keys of the json file are as expected (indicated by `mode`), return the nested dictionary<br>

with the exception of logging, any modules not available will cause an appropriate log to be made (typically a WARNING if not present followed by a CRITICAL if attempts to import fail) and will result in json_read returning None if unable to import<br>

with the exception of args and kwargs (for which any discrepencies merely log an INFO) and log (which is set to `True` if found to be anything other than a boolean),<br>
any arguments given in an unexpected manner will cause an appropriate log to be made (typically a WARNING) and will result in json_read returning None<br>


### json_write<br>

**a function to write to a json file**<br>

determine what method of logging is appropriate within json_write<br>
determine if all desired functions are present (attempting to import if not)<br>
determine if a file name was given and if it is appropriate (ended in ".json")<br>
determine if the `new_data` has appropriate keys for the given `mode`<br>
determine if the elements of new_data are of the appropriate type for the given `mode`<br>
call json_read with the same `json_filename` and `mode`<br>
update the data returned with the given `new_data`<br>
convert the updated data into an appropriate string using json<br>
write this data to the json_filename file<br>

> #### module dependancy<br>
>
> - logging<br>
> - - used to log events to a file<br>
> - - logging is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logging is not found to be present, `log` is set to `False`<br>
> - os.path.isfile<br>
> - - used to determine whether or not a file exists within the Covid_dashboard_pkg directory<br>
> - json<br>
> - - used to convert a nested dictionary structure into a nicely formatted string<br>
> - main.json_read<br>
> - - used to read the contents of a json file and compare it with expected format and contents<br>

> #### global dependancy<br>
>
> - logger<br>
> - - an object from the logging module used as a framework when logging to files<br>
> - - logger is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logger is not found to be present, `log` is set to `False`<br>

> #### arguments<br>
>
> - json_filename<br>
> - - a string, naming the file to attempt to read<br>
> - - json_filename is expected to end in ".json" and should point to an existing json file that is accessible within the Covid_Dashboard_pkg directory<br>
> - - json_filename defaults to `"config.json"`<br>
> - new_data<br>
> - - a nested dictionary containing keys to be updated within the relevant json file and the value to which to update them<br>
> - - the keys of new_data are expected to present in `["csv_filename", "log_filename", "status_filename", "AreaName", "AreaType", "API_key"]` or `["local_7day_infections", "national_7day_infections", "hospital_cases", "deaths_total", "updates", "remove", "news"]`, as indicated by `mode`<br>
> - - the type of each element of new_data should match that expected for its key<br>
> - - new_data defaults to `{}`<br>
> - mode<br>
> - - a boolean, indicating whether the file being read is the config file (0) or the status file (1)<br>
> - - mode defaults to `0`<br>
> - log<br>
> - - a boolean, dictating whether to attempt to log to a file or directly to the python terminal<br>
> - - log is expected to be set to `True` only if the logging framework has been established elsewhere (typically in main.startup in standard runtime)<br>
> - - log defaults to `True`<br>
> - args<br>
> - - a list, catching any arguments in excess of those expected<br>
> - - args is expected to remain an empty list<br>
> - - args defaults to `[]`<br>
> - kwargs<br>
> - - a dictionary, catching any keyword arguments beyond those expected<br>
> - - kwargs is expected to remain an empty dictionary<br>
> - - kwargs defaults to `{}`<br>

with modules, globals and arguments given as expected,<br>
the content of `new_data` is validated<br>
the content of the json file is loaded and relevant keys have their values replaced by those found for the same keys in `new_data`<br>
the updated data is saved to the json file<br>

with the exception of logging, any modules not available will cause an appropriate log to be made (typically a WARNING if not present followed by a CRITICAL if attempts to import fail) and will result in json_read returning None if unable to import<br>

with the exception of args and kwargs (for which any discrepencies merely log an INFO) and log (which is set to `True` if found to be anything other than a boolean),<br>
any arguments given in an unexpected manner will cause an appropriate log to be made (typically a WARNING) and will result in json_read returning None<br>


### reset_updates<br>

**a function to update the updates as stored in main**<br>

determine what method of logging is appropriate within reset_updates<br>
determine if all desired modules are present (attempting to import if not)<br>
ensure the `schedule` of all 3 modules (`covid_data_handler`, `covid_news_handling`, and `main`) are equal<br>
if an element is present in the `updates` of `covid_data_handler` or `covid_news_handling` but not that of `main`, add that element to the `updates` of `main`<br>
if an element is present in the `updates` of `main` but not that of `covid_data_handler` or `covid_news_handling`, remove that element from the `updates` of `main`<br>

> #### module dependancy<br>
>
> - logging<br>
> - - used to log events to a file<br>
> - - logging is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logging is not found to be present, `log` is set to `False`<br>
> - sched<br>
> - - used to schedule functions to run at specified times<br>
> - time<br>
> - - used as a foundation for `schedule`, and to obtain the current time<br>
> - covid_data_handler<br>
> - - access is required to the global namespace of covid_data_handler, specifically to the values of `schedule` and `updates`<br>
> - covid_news_handling<br>
> - - access is required to the global namespace of covid_news_handling, specifically to the values of `schedule` and `updates`<br>

> #### global dependancy<br>
>
> - logger<br>
> - - an object from the logging module used as a framework when logging to files<br>
> - - logger is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logger is not found to be present, `log` is set to `False`<br>
> - schedule<br>
> - - an object from the sched module used to schedule functions to run at a specified time<br>
> - - if not prsent, schedule defaults to a new object of the sched module<br>
> - updates<br>
> - - a list of dictionaries, storing all the scheduled updates within the program<br>
> - - if not present, updates defaults to `[]`

> #### arguments<br>
> - log<br>
> - - a boolean, dictating whether to attempt to log to a file or directly to the python terminal<br>
> - - log is expected to be set to `True` only if the logging framework has been established elsewhere (typically in main.startup in standard runtime)<br>
> - - log defaults to `True`<br>
> - args<br>
> - - a list, catching any arguments in excess of those expected<br>
> - - args is expected to remain an empty list<br>
> - - args defaults to `[]`<br>
> - kwargs<br>
> - - a dictionary, catching any keyword arguments beyond those expected<br>
> - - kwargs is expected to remain an empty dictionary<br>
> - - kwargs defaults to `{}`<br>

with modules, globals and arguments given as expected,<br>
equate the `schedule` of all 3 modules (`covid_data_handler`, `covid_news_handling`, and `main`)<br>
ensure that the `updates` of `main` contains all the elements found in the `updates` of `covid_data_handler` or `covid_news_handling` and only those elements<br>

with the exception of logging, any modules not available will cause an appropriate log to be made (typically a WARNING if not present followed by a CRITICAL if attempts to import fail) and will result in json_read returning None if unable to import<br>


### reset_news<br>

**a function to update the news as stored in main**

determine what method of logging is appropriate within reset_news<br>
determine if all desired modules are present (attempting to import if not)<br>
update the global `news` of `main` to that of `covid_news_handling` and validate<br>
update the global `remove` of main to that of `covid_news_handling` and validate<br>

> #### module dependancy<br>
>
> - logging<br>
> - - used to log events to a file<br>
> - - logging is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logging is not found to be present, `log` is set to `False`<br>
> - covid_news_handling<br>
> - - access is required to the global namespace of covid_news_handling, specifically to the values of `news`, `date` and `remove`<br>

> #### global dependancy<br>
>
> - logger<br>
> - - an object from the logging module used as a framework when logging to files<br>
> - - logger is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logger is not found to be present, `log` is set to `False`<br>
> - news<br>
> - - a list of dictionaries, containing news articles<br>
> - - each dictionary should have the keys "title", "content"<br>
> - - if not present, news defaults to `[]`<br>
> - remove<br>
> - - a dictionary, containing the titles of news articles keyed with the date they were obtained<br>
> - - all values contained should be strings, representing dates and are therefore expected to be appropriate dates of the form YYYY-mm-dd<br>
> - - if not present, remove defaults to `[]`

> #### arguments<br>
> - log<br>
> - - a boolean, dictating whether to attempt to log to a file or directly to the python terminal<br>
> - - log is expected to be set to `True` only if the logging framework has been established elsewhere (typically in main.startup in standard runtime)<br>
> - - log defaults to `True`<br>
> - args<br>
> - - a list, catching any arguments in excess of those expected<br>
> - - args is expected to remain an empty list<br>
> - - args defaults to `[]`<br>
> - kwargs<br>
> - - a dictionary, catching any keyword arguments beyond those expected<br>
> - - kwargs is expected to remain an empty dictionary<br>
> - - kwargs defaults to `{}`<br>

with modules, globals and arguments given as expected,<br>
update the globals `news` and `remove` of `main` to match those of `covid_news_handling` (following validation)<br>

with the exception of logging, any modules not available will cause an appropriate log to be made (typically a WARNING if not present followed by a CRITICAL if attempts to import fail) and will result in json_read returning None if unable to import<br>


### update_remove<br>

**a function to remove an update**

determine what method of logging to use within update_remove<br>
determine if all desired functions are present (attempting to import if not)<br>
determine if all desired globals are present (defaulting where possible if not)<br>
call `reset_updates`<br>
search for an element in `updates` with "title" matching that of the request<br>
for each found,<br>
- cancel the event stored in that element of `updates` with the `schedule`<br>
- remove the identical element from the `updates` of `covid_data_handler` or `covid_news_handling` as appropriated (indicated by the "type" of the element of `updates`)<br>
- remove the element from `updates`<br>

> #### module dependancy<br>
>
> - logging<br>
> - - used to log events to a file<br>
> - - logging is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logging is not found to be present, `log` is set to `False`<br>
> - sched<br>
> - - used to schedule functions to run at specified times<br>
> - time<br>
> - - used as a foundation for `schedule`, and to obtain the current time<br>
> - covid_data_handler<br>
> - - access is required to the global namespace of covid_data_handler, specifically to the values of `schedule` and `updates`<br>
> - covid_news_handling<br>
> - - access is required to the global namespace of covid_news_handling, specifically to the values of `schedule` and `updates`<br>
> - main.reset_updates<br>
> - - used to ensure that updates remain consistent across the 3 modules<br>
> - updates<br>
> - - a list of dictionaries, storing all the scheduled updates within the program<br>

> #### global dependancy<br>
>
> - logger<br>
> - - an object from the logging module used as a framework when logging to files<br>
> - - logger is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logger is not found to be present, `log` is set to `False`<br>
> - schedule<br>
> - - an object from the sched module used to schedule functions to run at a specified time<br>

> #### arguments<br>
> - remove_update<br>
> - - a string, indicating the "title" of the update to attempt to remove<br>
> - - remove_update defaults to `None`<br>
> - log<br>
> - - a boolean, dictating whether to attempt to log to a file or directly to the python terminal<br>
> - - log is expected to be set to `True` only if the logging framework has been established elsewhere (typically in main.startup in standard runtime)<br>
> - - log defaults to `True`<br>
> - args<br>
> - - a list, catching any arguments in excess of those expected<br>
> - - args is expected to remain an empty list<br>
> - - args defaults to `[]`<br>
> - kwargs<br>
> - - a dictionary, catching any keyword arguments beyond those expected<br>
> - - kwargs is expected to remain an empty dictionary<br>
> - - kwargs defaults to `{}`<br>

with modules, globals and arguments given as expected,<br>
search for an element in `updates` for which "title" keys to `remove_update`<br>
cancel this update with the `schedule`<br>
search the `updates` of the relevant module (`covid_data_handler` or `covid_news_handling` as indicated by the "type" of the element of `updates`) for a matching update<br>
remove that update<br>
remove this update from `updates`<br>


### news_remove<br>

**a function to remove a news article**

determine what method of logging to use within news_remove<br>
determine if all desired functions are present (attempting to import if not)<br>
determine if all desired globals are present (defaulting where possible if not)<br>
call `reset_news`<br>
search for an element in `news` with "title" matching that of the request<br>
if one is found, remove the element from `news`<br>

> #### module dependancy<br>
>
> - logging<br>
> - - used to log events to a file<br>
> - - logging is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logging is not found to be present, `log` is set to `False`<br>
> - main.reset_news<br>
> - - used to ensure that news remains consistent between `main` and `covid_news_handling`<br>

> #### global dependancy<br>
>
> - logger<br>
> - - an object from the logging module used as a framework when logging to files<br>
> - - logger is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logger is not found to be present, `log` is set to `False`<br>
> - news<br>
> - - a list of dictionaries, containing news articles<br>

> #### arguments<br>
> - remove_news<br>
> - - a string, indicating the "title" of the news article to attempt to remove<br>
> - - remove_news defaults to `None`<br>
> - log<br>
> - - a boolean, dictating whether to attempt to log to a file or directly to the python terminal<br>
> - - log is expected to be set to `True` only if the logging framework has been established elsewhere (typically in main.startup in standard runtime)<br>
> - - log defaults to `True`<br>
> - args<br>
> - - a list, catching any arguments in excess of those expected<br>
> - - args is expected to remain an empty list<br>
> - - args defaults to `[]`<br>
> - kwargs<br>
> - - a dictionary, catching any keyword arguments beyond those expected<br>
> - - kwargs is expected to remain an empty dictionary<br>
> - - kwargs defaults to `{}`<br>

with modules, globals and arguments given as expected,<br>
search for an element in `news` for which "title" keys to `remove_news`<br>
remove this element from `news`<br>


### dashboard_setup<br>

**a function to setup the covid dashboard**<br>

determine what method of logging is appropriate within dashboard_setup<br>
determine if all desired modules are present (attempting to import if not)<br>
use the functions and methods within Flask to setup a dashboard (using the `dashboard` function and routed to by http://127.0.0.1:5000/index)<br>

> #### module dependancy<br>
>
> - logging<br>
> - - used to log events to a file<br>
> - - logging is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logging is not found to be present, `log` is set to `False`<br>
> - flask.Flask<br>
> - - used to host a page (or series of pages) in a web browser that can pass any queries into appropriate functions within python

> #### global dependancy<br>
>
> - logger<br>
> - - an object from the logging module used as a framework when logging to files<br>
> - - logger is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logger is not found to be present, `log` is set to `False`<br>

> #### arguments<br>
> - log<br>
> - - a boolean, dictating whether to attempt to log to a file or directly to the python terminal<br>
> - - log is expected to be set to `True` only if the logging framework has been established elsewhere (typically in main.startup in standard runtime)<br>
> - - log defaults to `True`<br>
> - args<br>
> - - a list, catching any arguments in excess of those expected<br>
> - - args is expected to remain an empty list<br>
> - - args defaults to `[]`<br>
> - kwargs<br>
> - - a dictionary, catching any keyword arguments beyond those expected<br>
> - - kwargs is expected to remain an empty dictionary<br>
> - - kwargs defaults to `{}`<br>

with modules, globals and arguments given as expected,<br>
setup a web page and the functionality (held in `dashboard`) to run it<br>

with the exception of logging, any modules not available will cause an appropriate log to be made (typically a WARNING if not present followed by a CRITICAL if attempts to import fail) and will result in dashboard_setup returning None if unable to import<br>

### dashboard<br>

**a function to serve the covid dashboard**<br>

determine what method of logging to use within dashboard<br>
determine if all desired functions are present (attempting to import if not)<br>
determine if all desired globals are present (defaulting where possible if not)<br>
if a request has been made to remove a scheduled update, call `update_remove`<br>
if a request has been made to remove a news article, call `news_remove`<br>

attempt to run any scheduled updates<br>
call `reset_updates`<br>
call `reset_news`<br>

if a valid request to schedule a new update has been made,<br>
- alter the desired name if needed to ensure it is unique (eg : "repeat_name(1)")<br>
- call `schedule_covid_updates` or `news_update` (or both) as requested<br>

update the global `local_7day_infections` to match that of `covid_data_handler`<br>
update the global `national_7day_infections` to match that of `covid_data_handler`<br>
update the global `hospital_cases` to match that of `covid_data_handler`<br>
update the global `deaths_total` to match that of `covid_data_handler`<br>
create a copy of updates that doesn't include the "event" key-value pair<br>
call `json_write` to update the status json file with  relevant variables (local_7day_infections, national_7day_infections, hospital_cases, deaths_total, the edited copy of updates, remove, and news)<br>
re-render the web page with relevant variables (local_7day_infections, national_7day_infections, hospital_cases, deaths_total, updates, news)<br>

> #### module dependancy<br>
>
> - logging<br>
> - - used to log events to a file<br>
> - - logging is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logging is not found to be present, `log` is set to `False`<br>
> - flask.request<br>
> - - used to obtain any requests made to the webpage as variables within python<br>
> - flask.render_template<br>
> - - used to display and update the web page<br>
> - covid_data_handler<br>
> - - access is required to the global namespace of covid_data_handler, specifically to the values of `schedule`, `updates`, `local_7day_infections`, `national_7day_infections`, `hospital_cases`, and `deaths_total`<br>
> - covid_news_handling<br>
> - - access is required to the global namespace of covid_news_handling, specifically to the values of `schedule` and `updates`<br>
> - covid_data_handler.schedule_covid_updates<br>
> - - used to schedule an update to the covid data<br>
> - covid_news_handling.update_news<br>
> - - used to schedule an update to the news articles<br>
> - main.json_write<br>
> - - used to write to the status json file<br>
> - main.reset_updates<br>
> - - used to ensure that updates remain consistent across the 3 modules<br>
> - main.reset_news<br>
> - - used to ensure that news remains consistent between `main` and `covid_news_handling`<br>
> - main.update_remove<br>
> - - used to remove an update (cancelling it from the `schedule` and removing it from the `updates` of all 3 modules)<br>
> - main.news_remove<br>
> - - used to remove a news article

> #### global dependancy<br>
>
> - logger<br>
> - - an object from the logging module used as a framework when logging to files<br>
> - - logger is only expected to be present globally if the argument `log` is set to `True`<br>
> - - if `log` is set to `True` and logger is not found to be present, `log` is set to `False`<br>
> - log<br>
> - - a boolean, dictating whether to attempt to log to a file or directly to the python terminal<br>
> - status_filename<br>
> - - a string indicating the name of the status json file<br>
> - schedule<br>
> - - an object from the sched module used to schedule functions to run at a specified time<br>
> - updates<br>
> - - a list of dictionaries, storing all the scheduled updates within the program<br>
> - news<br>
> - - a list of dictionaries, containing news articles<br>
> - remove<br>
> - - a dictionary, containing the titles of news articles keyed with the date they were obtained<br>
> - local_7day_infections<br>
> - - a string, storing the most recently updated value for local 7 day infections<br>
> - - presence and content are unimportant as this global is to be overwritten only<br>
> - national_7day_infections<br>
> - - a string, storing the most recently updated value for national 7 day infections<br>
> - - presence and content are unimportant as this global is to be overwritten only<br>
> - hospital_cases<br>
> - - a string, storing the most recently updated value for hospital cases<br>
> - - presence and content are unimportant as this global is to be overwritten only<br>
> - deaths_total<br>
> - - a string, storing the most recently updated value for total deaths<br>
> - - presence and content are unimportant as this global is to be overwritten only<br>

with modules, globals and arguments given as expected,<br>
any requests made to the web page should be treated appropriately<br>
any appropriate requests to schedule a new update should result in the appropriate update being scheduled at the given time (using `covid_data_handler.schedule_covid_updates` or `covid_news_handling.update_news` as requested and taking `update_name` to be the name given (once suitably modified to be unique (eg: "repeat_name(1)")))<br>
any appropriate requests to cancel an update should result in the corresponding update being cancelled in the schedule and removed from the list of updates<br>
any appropriate requests to remove a news article should result in the corresponding article being removed from the list of news articles<br>
any changed variables should be recorded in the status file and shown on the dashboard<br>


### startup<br>

**a function to setup and start the program**<br>

determine what method of logging to use within startup<br>
determine if all desired functions are present (attempting to import if not)<br>
determine if all desired globals are present (defaulting where possible if not)<br>
extract the information from the config file using `json_read`<br>
ensure any logs present in the log file are of the appropriate format<br>
innitiate appropriate logging structure in the form of `logger`<br>
innitiate appropriate scheduling structure in the form of `schedule`<br>
extract the information from the status file using `json_read`<br>
within the extracted updates, if at least one scheduled call for `covid_data_handler.covid_update` has a time value less than the current time, call `covid_data_handler.covid_update`<br>
within the extracted updates, if at least one scheduled call for `covid_news_handling.news_API_request` has a time value less than the current time, call `covid_news_handling.news_API_request`<br>
any elements within the extracted updates with the `"repeat"` value set to `True` or a `"time"` value greater than the current time should be rescheduled (using `covid_data_handler.schedule_covid_updates` or `covid_news_handling.update_news` as indicated by the `"type"` value and using the `"title"`, `"time2"`, and `repeat` values as arguments)<br>
empty updates<br>
retrieve and return the app (a `Flask` object) by calling `dashboard_setup`<br>

> #### module dependancy<br>
>
> - covid_data_handler<br>
> - - access is required to the global namespace of covid_data_handler, specifically to the values of `schedule`, `updates`, `local_7day_infections`, `national_7day_infections`, `hospital_cases`, and `deaths_total`<br>
> - covid_news_handling<br>
> - - access is required to the global namespace of covid_news_handling, specifically to the values of `schedule` and `updates`<br>
> - covid_data_handler.schedule_covid_updates<br>
> - - used to schedule an update to the covid data<br>
> - covid_news_handling.update_news<br>
> - - used to schedule an update to the news articles<br>
> - covid_data_handler.covid_update<br>
> - - used to update covid statistics (both within the program itself and within a csv file)<br>
> - covid_news_handling.news_API_request<br>
> - - used to update news articles<br>
> - os.path.isfile<br>
> - - used to determine whether or not a file exists within the Covid_dashboard_pkg directory<br>
> - datetime.datetime<br>
> - - used to convert between formatted strings (YYYY-mm-dd) and the total number of seconds ellapsed since 1900-01-01 and back again<br>
> - logging<br>
> - - used to log events to a file<br>
> - sched<br>
> - - used to schedule functions to run at specified times<br>
> - time<br>
> - - used as a foundation for `schedule`, and to obtain the current time<br>
> - main.json_read<br>
> - - used to read the contents of a json file and compare it with expected format and contents<br>
> - main.json_write<br>
> - - used to write to the config or status json files<br>
> - main.dashboard_setup<br>
> - - used to acquire the functionality required for hosting the web page<br>

> #### arguments<br>
> - args<br>
> - - a list, catching any arguments in excess of those expected<br>
> - - args is expected to remain an empty list<br>
> - - args defaults to `[]`<br>
> - kwargs<br>
> - - a dictionary, catching any keyword arguments beyond those expected<br>
> - - kwargs is expected to remain an empty dictionary<br>
> - - kwargs defaults to `{}`<br>

with modules given as expected,<br>
returns the covid dashboard to the state it would be in were it to have continued running since its last use<br>
the contents of news, remove, date, local_7day_infections, national_7day_infections, hospital_cases, and deaths_total are restored<br>
any future updates are rescheduled<br>
any updates now past are immediately inacted<br>

---
---

# Details<br>

## Author<br>

**Autumn (Matthew) Hannon**<br>

---

## Source<br>

GitHub Link, https://github.com/AutumnT702/Covid19_Dashboard_pkg.git<br>
