'''a module for covid data handling functionality'''

def parse_csv_data(csv_filename : str = None, *args, log : bool = True, **kwargs) -> list[str]:
    '''a function to read a csv file'''

    if type(log) != bool:
        log = True
    if log:
        log = "logging" in globals() and "logger" in globals()
        if not log:
            print("WARNING | unable to log | parse_csv_data")
    #verify if logging is enabled

    if log: logger.debug("DEBUG | parse_csv_data called successfully | parse_csv_data")
    else: print("DEBUG | parse_csv_data called successfully | parse_csv_data")

    global isfile
    if "isfile" not in globals():
        if log: logger.warning("WARNING | isfile not imported | parse_csv_data")
        else: print("WARNING | isfile not imported | parse_csv_data")
        try:
            from os.path import isfile
        except:
            if log: logger.critical("CRITICAL | os.path not in system path | parse_csv_data")
            else: print("CRITICAL | os.path not in system path | parse_csv_data")
            return None
    #verify if necessary functions are present

    if csv_filename == None:
        if log: logger.warning("WARNING | csv_filename not given | parse_csv_data")
        else: print("WARNING | csv_filename not given | parse_csv_data")
        return None
    csv_filename = str(csv_filename)
    if csv_filename[-4:] != ".csv":
        if log: logger.warning("WARNING | invalid file extension | parse_csv_data")
        else: print("WARNING | invalid file extension | parse_csv_data")
        return None
    if not isfile(csv_filename):
        if log: logger.warning("WARNING | file does not exist | parse_csv_data")
        else: print("WARNING | file does not exist | parse_csv_data")
        return None
    if len(args) > 0:
        if log: logger.info("INFO | too many non-keyword arguements | parse_csv_data")
        else: print("INFO | too many non-keyword arguements | parse_csv_data")
    if len(kwargs) > 0:
        if log: logger.info("INFO | unexpected keyword arguments | parse_csv_data")
        else: print("INFO | unexpected keyword arguments | parse_csv_data")
    #verify given arguements


    try:
        with open(csv_filename, "r") as f:
            csv_data = f.read().split("\n")
        #read data from file (and place it into a list)
        csv_data.pop()
        #remove the empty last line
        if log: logger.debug("DEBUG | parse_csv_data successfully completed | parse_csv_data")
        else: print("DEBUG | parse_csv_data successfully completed | parse_csv_data")
        return csv_data
    except:
        if log: logger.error("ERROR | unable to open file | parse_csv_data")
        else: print("ERROR | unable to open file | parse_csv_data")


def parse_csv_data2(covid_csv_data : list[str] = None, log : bool = True, *args, **kwargs) -> dict[str, dict[str, dict[str, str]]]:
    '''a function to convert and validate the list of strings as read from a csv into a dictionary'''

    if type(log) != bool:
        log = True
    if log:
        log = "logging" in globals() and "logger" in globals()
        if not log:
            print("WARNING | unable to log | parse_csv_data2")
    #verify if logging is enabled

    if log: logger.debug("DEBUG | parse_csv_data2 called successfully | parse_csv_data2")
    else: print("DEBUG | parse_csv_data2 called successfully | parse_csv_data2")

    if covid_csv_data == None:
        if log: logger.warning("WARNING | covid_csv_data not given | parse_csv_data2")
        else: print("WARNING | covid_csv_data not given | parse_csv_data2")
        return None
    if type(covid_csv_data) != list:
        if log: logger.warning("WARNING | invalid type for covid_csv_data | parse_csv_data2")
        else: print("WARNING | invalid type for covid_csv_data | parse_csv_data2")
        return None
    for a in range(len(covid_csv_data)):
        covid_csv_data[a] = str(covid_csv_data[a])
        covid_csv_data[a] = covid_csv_data[a].split(",")
        if len(covid_csv_data[a]) != 7:
            if log: logger.warning("WARNING | not enough columns in covid_csv_data | parse_csv_data2")
            else: print("WARNING | not enough columns in covid_csv_data | parse_csv_data2")
            return None
    #split elements of covid_csv_data by ","
    if len(covid_csv_data) == 0:
        return {}
    headers = covid_csv_data.pop(0)
    for a in range(len(headers)):
        if headers.index(headers[a]) != a:
            if log: logger.warning("WARNING | repeated headers in covid_csv_data | parse_csv_data2")
            else: print("WARNING | repeated headers in covid_csv_data | parse_csv_data2")
            return None
    #take the first element of covid_csv_data to be a collection of headers
    if len(args) > 0:
        if log: logger.info("INFO | too many non-keyword arguements | parse_csv_data2")
        else: print("INFO | too many non-keyword arguements | parse_csv_data2")
    if len(kwargs) > 0:
        if log: logger.info("INFO | unexpected keyword arguments | parse_csv_data2")
        else: print("INFO | unexpected keyword arguments | parse_csv_data2")
    #verify given arguements


    new_covid_csv_data = {}
    while len(covid_csv_data) > 0:
        areaName = covid_csv_data[0][1]
        new_covid_csv_data[areaName] = {}
        group = covid_csv_data[:]
        group = filter(lambda item : item[1] == areaName, group)
        #group elements of covid_csv_data by areaName (the value at index 1)
        for item in group:
            date = item[3]
            covid_csv_data.pop(covid_csv_data.index(item))
            new_covid_csv_data[areaName][date] = {}
            for a in range(len(item)):
                if a in [1, 3]:
                    continue
                new_covid_csv_data[areaName][date][headers[a]] = item[a]
            #place the information not including areaName and date (values at indexes 1 and 3)
        sorted(new_covid_csv_data[areaName])
        #sort elements of covid_csv_data by date (the value at index 3)
    if log: logger.debug("DEBUG | parse_csv_data2 successfully completed | parse_csv_data2")
    else: print("DEBUG | parse_csv_data2 successfully completed | parse_csv_data2")
    return new_covid_csv_data


def subprocess_covid_csv_data(data : dict[str, dict[str, dict[str, str]]] = None, row : int = None, col : str = None, areaName : str = None, latestUpdate : bool = False, log : bool = True, *args, **kwargs) -> str:
    '''a function to extract a cell from the contents read from a csv'''

    if type(log) != bool:
        log = True
    if log:
        log = "logging" in globals() and "logger" in globals()
        if not log:
            print("WARNING | unable to log | subprocess_covid_csv_data")
    #verify if logging is enabled

    if log: logger.debug("DEBUG | subprocess_covid_csv_data called successfully | subprocess_covid_csv_data")
    else: print("DEBUG | subprocess_covid_csv_data called successfully | subprocess_covid_csv_data")

    if data == None:
        if log: logger.warning("WARNING | data not given | subprocess_covid_csv_data")
        else: print("WARNING | data not given | subprocess_covid_csv_data")
        return None
    if type(data) != dict:
        if log: logger.warning("WARNING | invalid type for data | subprocess_covid_csv_data")
        else: print("WARNING | invalid type for data | subprocess_covid_csv_data")
        return None
    for element in data:
        if type(data[element]) != dict:
            if log: logger.warning("WARNING | invalid type for element of data | subprocess_covid_csv_data")
            else: print("WARNING | invalid type for element of data | subprocess_covid_csv_data")
            return None
        for subElement in data[element]:
            if type(data[element][subElement]) != dict:
                if log: logger.warning("WARNING | invalid type for sub-element of data | subprocess_covid_csv_data")
                else: print("WARNING | invalid type for sub-element of data | subprocess_covid_csv_data")
                return None
    if row == None:
        if log: logger.warning("WARNING | row not given | subprocess_covid_csv_data")
        else: print("WARNING | row not given | subprocess_covid_csv_data")
        return None
    if type(row) != int:
        if log: logger.warning("WARNING | invalid type for row | subprocess_covid_csv_data")
        else: print("WARNING | invalid type for row | subprocess_covid_csv_data")
        return None
    row = abs(row)
    if col == None:
        if log: logger.warning("WARNING | col not given | subprocess_covid_csv_data")
        else: print("WARNING | col not given | subprocess_covid_csv_data")
        return None
    col = str(col)
    if areaName == None:
        if log: logger.warning("WARNING | areaName not given | subprocess_covid_csv_data")
        else: print("WARNING | areaName not given | subprocess_covid_csv_data")
        return None
    areaName = str(areaName)
    if areaName not in list(data.keys()):
        if log: logger.info("INFO | no entries found for areaName | subprocess_covid_csv_data")
        else: print("INFO | no entries found for areaName | subprocess_covid_csv_data")
        return None
    if len(list(data[areaName].keys())) <= row:
        if log: logger.info("INFO | target row exceeds number of entries for given areaName | subprocess_covid_csv_data")
        else: print("INFO | target row exceeds number of entries for given areaName | subprocess_covid_csv_data")
        return None
    if col not in data[areaName][list(data[areaName].keys())[row]].keys():
        if log: logger.warning("WARNING | no entries found for col in row | subprocess_covid_csv_data")
        else: print("WARNING | no entries found for col in row | subprocess_covid_csv_data")
        return None
    if type(latestUpdate) != bool:
        if log: logger.warning("WARNING | invalid type for latestUpdate | subprocess_covid_csv_data")
        else: print("WARNING | invalid type for latestUpdate | subprocess_covid_csv_data")
        return None
    if len(args) > 0:
        if log: logger.info("INFO | too many non-keyword arguements | subprocess_covid_csv_data")
        else: print("INFO | too many non-keyword arguements | subprocess_covid_csv_data")
    if len(kwargs) > 0:
        if log: logger.info("INFO | unexpected keyword arguments | subprocess_covid_csv_data")
        else: print("INFO | unexpected keyword arguments | subprocess_covid_csv_data")
    #verify given arguements


    value = data[areaName][list(data[areaName].keys())[row]][col]
    if latestUpdate and value != "":
        value = list(data[areaName].keys())[row]
    if log: logger.debug("DEBUG | subprocess_covid_csv_data successfully completed | subprocess_covid_csv_data")
    else: print("DEBUG | subprocess_covid_csv_data successfully completed | subprocess_covid_csv_data")
    return value


def process_covid_csv_data(covid_csv_data : list[str] = None, *args, targets : list[dict[str, str]] = [{"header" : "newCasesBySpecimenDate", "mode" : "sum", "extra" : 7}, {"header" : "hospitalCases", "mode" : "latest", "extra" : None}, {"header" : "cumDailyNsoDeathsByDeathDate", "mode" : "latest", "extra" : None}], areaName : str = "England", csv : bool = True, log : bool = True, **kwargs) -> dict[str, str]:
    '''a function to process the contents read from a csv'''
    if type(log) != bool:
        log = True
    if log:
        log = "logging" in globals() and "logger" in globals()
        if not log:
            print("WARNING | unable to log | process_covid_csv_data")
    #verify if logging is enabled

    if log: logger.debug("DEBUG | process_covid_csv_data called successfully | process_covid_csv_data")
    else: print("DEBUG | process_covid_csv_data called successfully | process_covid_csv_data")


    if type(csv) != bool:
        if log: logger.warning("WARNING | invalid type for csv | process_covid_csv_data")
        else: print("WARNING | invalid type for csv | process_covid_csv_data")
        return None
    if csv:
        global parse_csv_data2
        if "parse_csv_data2" not in globals():
            if log: logger.warning("WARNING | parse_csv_data2 not imported | process_covid_csv_data")
            else: print("WARNING | parse_csv_data2 not imported | process_covid_csv_data")
            try:
                from covid_data_handler import parse_csv_data2
            except:
                if log: logger.critical("CRITICAL | covid_data_handler not in system path | process_covid_csv_data")
                else: print("CRITICAL | covid_data_handler not in system path | process_covid_csv_data")
                return None
    global subprocess_covid_csv_data
    if "subprocess_covid_csv_data" not in globals():
        if log: logger.warning("WARNING | subprocess_covid_csv_data not imported | process_covid_csv_data")
        else: print("WARNING | subprocess_covid_csv_data not imported | process_covid_csv_data")
        try:
            from covid_data_handler import subprocess_covid_csv_data
        except:
            if log: logger.critical("CRITICAL | covid_data_handler not in system path | process_covid_csv_data")
            else: print("CRITICAL | covid_data_handler not in system path | process_covid_csv_data")
            return None
    #verify if necessary functions are present

    if covid_csv_data == None:
        if log: logger.warning("WARNING | covid_csv_data not given | process_covid_csv_data")
        else: print("WARNING | covid_csv_data not given | process_covid_csv_data")
        return None
    if type(covid_csv_data) != [dict, list][csv]:
        if log: logger.warning("WARNING | invalid type for covid_csv_data | process_covid_csv_data")
        else: print("WARNING | invalid type for covid_csv_data | process_covid_csv_data")
        return None
    if type(targets) != list:
        if log: logger.warning("WARNING | invalid type for targets | process_covid_csv_data")
        else: print("WARNING | invalid type for targets | process_covid_csv_data")
        return None
    areaName = str(areaName)
    if len(args) > 0:
        if log: logger.info("INFO | too many non-keyword arguements | process_covid_csv_data")
        else: print("INFO | too many non-keyword arguements | process_covid_csv_data")
    if len(kwargs) > 0:
        if log: logger.info("INFO | unexpected keyword arguments | process_covid_csv_data")
        else: print("INFO | unexpected keyword arguments | process_covid_csv_data")
    #verify given arguements


    if csv:
        data = covid_csv_data[:]
        if log: logger.debug("DEBUG | calling parse_csv_data2 | process_covid_csv_data")
        else: print("DEBUG | calling parse_csv_data2 | process_covid_csv_data")
        data = parse_csv_data2(data)
        if data == None:
            if log: logger.error("ERROR | parse_csv_data2 failed | process_covid_csv_data")
            else: print("ERROR | parse_csv_data2 failed | process_covid_csv_data")
            return None
        if log: logger.debug("DEBUG | parse_csv_data2 returned successfully | process_covid_csv_data")
        else: print("DEBUG | parse_csv_data2 returned successfully | process_covid_csv_data")
    #convert data into a dictionary by way of parse_csv_data2 if required
    else:
        data = covid_csv_data
    returns = {}
    for target in targets:
        check = True
        if type(target) != dict:
            if log: logger.warning("WARNING | invalid type for element of targets | process_covid_csv_data")
            else: print("WARNING | invalid type for element of targets | process_covid_csv_data")
            continue
        if list(target.keys()) != ["header", "mode", "extra"]:
            if log: logger.warning("WARNING | invalid format for element of targets | process_covid_csv_data")
            else: print("WARNING | invalid format for element of targets | process_covid_csv_data")
            continue
        target["header"] = str(target["header"])
        target["mode"] = str(target["mode"])
        if target["mode"] not in ["latest", "latestUpdate", "sum", "rate"]:
            if log: logger.warning("WARNING | invalid mode of element of targets, " + target["mode"] + " | process_covid_csv_data")
            else: print("WARNING | invalid mode of element of targets, " + target["mode"] + " | process_covid_csv_data")
            continue
        key = target["mode"] + "_" + ["", "last" + str(target["extra"]) + "days_"][target["mode"] in ["sum", "rate"]] + target["header"]
        if target["extra"] != None:
            if type(target["extra"]) != int or target["mode"] not in ["sum", "rate"]:
                if log: logger.warning("WARNING | invalid type for extra of element of targets | process_covid_csv_data")
                else: print("WARNING | invalid type for extra of element of targets | process_covid_csv_data")
                returns[key] = None
                continue
            if type(target["extra"]) == int:
                target["extra"] = abs(target["extra"])
        #verify the contents of each element of targets

        row = -1
        col = target["header"]
        while True:
            row += 1
            if log: logger.debug("DEBUG | calling subprocess_covid_csv_data | process_covid_csv_data")
            else: print("DEBUG | calling subprocess_covid_csv_data | process_covid_csv_data")
            value = subprocess_covid_csv_data(data, row, col, areaName, target["mode"] == "latestUpdate")
            if value == None:
                if log: logger.error("ERROR | subprocess_covid_csv_data failed | process_covid_csv_data")
                else: print("ERROR | subprocess_covid_csv_data failed | process_covid_csv_data")
                returns[key] = None
                break
            #if subprocess_covid_csv_data failed to return a value, log the value of the target as None
            if log: logger.debug("DEBUG | subprocess_covid_csv_data returned successfully | process_covid_csv_data")
            else: print("DEBUG | subprocess_covid_csv_data returned successfully | process_covid_csv_data")
            #attempt to obtain the targetted value
            if value == "":
                if log: logger.info("INFO | value missing from covid_csv_data | process_covid_csv_data")
                else: print("INFO | value missing from covid_csv_data | process_covid_csv_data")
                continue
            #if the targetted value is empty, move onto the next row
            if target["header"] == "newCasesBySpecimenDate":
                row += 1
                if log: logger.debug("DEBUG | calling subprocess_covid_csv_data | process_covid_csv_data")
                else: print("DEBUG | calling subprocess_covid_csv_data | process_covid_csv_data")
                value = subprocess_covid_csv_data(data, row, col, areaName, target["mode"] == "latestUpdate")
                if value == None:
                    if log: logger.error("ERROR | subprocess_covid_csv_data failed | process_covid_csv_data")
                    else: print("ERROR | subprocess_covid_csv_data failed | process_covid_csv_data")
                    returns[key] = None
                    break
                if log: logger.debug("DEBUG | subprocess_covid_csv_data returned successfully | process_covid_csv_data")
                else: print("DEBUG | subprocess_covid_csv_data returned successfully | process_covid_csv_data")
            #if the targetted header is "newCasesBySpecimenDate", skip the first non-empty result
            if target["mode"] in ["sum", "rate"]:
                extra = target["extra"] - 1
                try:
                    value = int(value)
                except:
                    if log: logger.warning("WARNING | unexpected non-integer return for value | process_covid_csv_data")
                    else: print("WARNING | unexpected non-integer return for value | process_covid_csv_data")
                    returns[key] = None
                    break
                while extra > 0:
                    row += 1
                    if log: logger.debug("DEBUG | calling subprocess_covid_csv_data | process_covid_csv_data")
                    else: print("DEBUG | calling subprocess_covid_csv_data | process_covid_csv_data")
                    value2 = subprocess_covid_csv_data(data, row, col, areaName)
                    if value2 == None:
                        if log: logger.error("ERROR | subprocess_covid_csv_data failed | process_covid_csv_data")
                        else: print("ERROR | subprocess_covid_csv_data failed | process_covid_csv_data")
                        value = None
                        break
                    #if subprocess_covid_csv_data failed to return a value, log the value of the target as None
                    if log: logger.debug("DEBUG | subprocess_covid_csv_data returned successfully | process_covid_csv_data")
                    else: print("DEBUG | subprocess_covid_csv_data returned successfully | process_covid_csv_data")
                    if value2 == "":
                        if log: logger.info("INFO | value missing from covid_csv_data | process_covid_csv_data")
                        else: print("INFO | value missing from covid_csv_data | process_covid_csv_data")
                        continue
                    #if the targetted value is empty, move onto the next row
                    try:
                        value += int(value2)
                    except:
                        if log: logger.warning("WARNING | unexpected non-integer return for value2 | process_covid_csv_data")
                        else: print("WARNING | unexpected non-integer return for value2 | process_covid_csv_data")
                        value = None
                        break
                    extra -= 1
                #if the mode of the target calls for multiple values, obtain the appropriate number of additional values
                if value != None and target["mode"] == "rate":
                    value = value / target["extra"]
                #if the mode of the target is rate, divide the value by the extra of the target
                
            returns[key] = str(value)
            break
    if log: logger.debug("DEBUG | process_covid_csv_data successfully completed | process_covid_csv_data")
    else: print("DEBUG | process_covid_csv_data successfully completed | process_covid_csv_data")
    return returns


def covid_API_request(location : str = "Exeter", location_type : str = "ltla", *args, date : str = "2020-01-30", structure : dict[str, str] = {"areaCode": "areaCode", "areaType": "areaType", "date": "date", "cumDailyNsoDeathsByDeathDate": "cumDailyNsoDeathsByDeathDate", "hospitalCases": "hospitalCases", "newCasesBySpecimenDate": "newCasesBySpecimenDate"}, log : bool = True, **kwargs) -> dict[str, dict[str, dict[str, str]]]:
    '''a function to retrieve live data from the uk_covid19 Cov19API for a given location and following a given date'''

    if type(log) != bool:
        log = True
    if log:
        log = "logging" in globals() and "logger" in globals()
        if not log:
            print("WARNING | unable to log | covid_API_request")
    #verify if logging is enabled

    if log: logger.debug("DEBUG | covid_API_request called successfully | covid_API_request")
    else: print("DEBUG | covid_API_request called successfully | covid_API_request")

    global datetime
    if "datetime" not in globals():
        if log: logger.warning("WARNING | datetime not imported | covid_API_request")
        else: print("WARNING | datetime not imported | covid_API_request")
        try:
            from datetime import datetime
        except:
            if log: logger.critical("CRITICAL | datetime not in system path | covid_API_request")
            else: print("CRITICAL | datetime not in system path | covid_API_request")
            return None
    global requests
    if "requests" not in globals():
        if log: logger.warning("WARNING | requests not imported | covid_API_request")
        else: print("WARNING | requests not imported | covid_API_request")
        try:
            import requests
        except:
            if log: logger.critical("CRITICAL | requests not in system path | covid_API_request")
            else: print("CRITICAL | requests not in system path | covid_API_request")
            return None
    global json
    if "json" not in globals():
        if log: logger.warning("WARNING | json not imported | covid_API_request")
        else: print("WARNING | json not imported | covid_API_request")
        try:
            import json
        except:
            if log: logger.critical("CRITICAL | json not in system path | covid_API_request")
            else: print("CRITICAL | json not in system path | covid_API_request")
            return None
    #verify if necessary functions are present

    location = str(location)
    location_type = str(location_type)
    if len(args) > 0:
        if log: logger.info("INFO | too many non-keyword arguements | covid_API_request")
        else: print("INFO | too many non-keyword arguements | covid_API_request")
    date = str(date)
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
    except:
        if log: logger.warning("WARNING | invalid format for date | covid_API_request")
        else: print("WARNING | invalid format for date | covid_API_request")
        date = datetime.strptime("2020-01-30", "%Y-%m-%d")
    if type(structure) != dict:
        if log: logger.warning("WARNING | structure not given | covid_API_request")
        else: print("WARNING | structure not given | covid_API_request")
        return None
    structure["date"] = "date"
    if len(kwargs) > 0:
        if log: logger.info("INFO | unexpected keyword arguments | covid_API_request")
        else: print("INFO | unexpected keyword arguments | covid_API_request")
    #verify given arguements


    filters = {"areaType": location_type, "areaName": location}
    link = "http://api.coronavirus.data.gov.uk/v1/data?filters="
    sublink = []
    for item in filters:
        sublink.append(item + "%3D" + filters[item])
    link += "%3B".join(sublink) + "&structure=%7B%22"
    sublink = []
    for item in structure:
        sublink.append(item + "%22%3A%22" + structure[item])
    link += "%22%2C%22".join(sublink) + "%22%7D&format=json&page=1"
    #construct a valid link for the uk_covid19 Cov19API
    try:
        api = requests.get(link)
    except:
        if log: logger.critical("CRITICAL | failure to attempt contact with uk_covid19 Cov19API | covid_API_request")
        else: print("CRITICAL | failure to attempt contact with uk_covid19 Cov19API | covid_API_request")
        return None
    if api.status_code != 200:
        if log: logger.error("ERROR | failure with uk_covid19 Cov19API, status_code = " + str(api.status_code) + " | covid_API_request")
        else: print("ERROR | failure with uk_covid19 Cov19API, status_code = " + str(api.status_code) + " | covid_API_request")
        return None
    #attempt to contact the uk_covid19 Cov19API
    data = json.loads(api.text)["data"]
    #convert the data into a dictionary
    new_data = {}
    new_data[location] = {}
    for item in data:
        item_date = item["date"]
        del item["date"]
        try:
            item_date2 = datetime.strptime(item_date, "%Y-%m-%d")
        except:
            if log: logger.warning('WARNING | invalid format for data["date"] as retrieved from uk_covid19 Cov19API | covid_API_request')
            else: print('WARNING | invalid format for data["date"] as retrieved from uk_covid19 Cov19API | covid_API_request')
            return None
        if item_date2 > date:
            for item2 in item:
                if item[item2] == None:
                    item[item2] = ""
            new_data[location][item_date] = item
        #filter for relevant data (from after the specified date)
    if log: logger.debug("DEBUG | covid_API_request successfully completed | covid_API_request")
    else: print("DEBUG | covid_API_request successfully completed | covid_API_request")
    return new_data


def csv_writeup(csv_filename : str = None, data : dict[str, dict[str, dict[str, str]]] = None, log : bool = True, *args, **kwargs) -> None:
    '''a function to write to a csv file'''

    if type(log) != bool:
        log = True
    if log:
        log = "logging" in globals() and "logger" in globals()
        if not log:
            print("WARNING | unable to log | csv_writeup")
    #verify if logging is enabled

    if log: logger.debug("DEBUG | csv_writeup called successfully | csv_writeup")
    else: print("DEBUG | csv_writeup called successfully | csv_writeup")

    if csv_filename == None:
        if log: logger.warning("WARNING | csv_filename not given | csv_update")
        else: print("WARNING | csv_filename not given | csv_update")
        return None
    csv_filename = str(csv_filename)
    if csv_filename[-4:] != ".csv":
        if log: logger.warning("WARNING | invalid file extension | csv_update")
        else: print("WARNING | invalid file extension | csv_update")
        return None
    if data == None:
        if log: logger.warning("WARNING | data not given | csv_writeup")
        else: print("WARNING | data not given | csv_writeup")
        return None
    if type(data) != dict:
        if log: logger.warning("WARNING | invalid type for data | csv_writeup")
        else: print("WARNING | invalid type for data | csv_writeup")
        return None
    for item in data:
        if type(data[item]) != dict:
            if log: logger.warning("WARNING | invalid type for element in data | csv_writeup")
            else: print("WARNING | invalid type for element in data | csv_writeup")
            return None
        for item2 in data[item]:
            if len(data[item][item2]) != 5:
                if log: logger.warning("WARNING | invalid format for element in data | csv_writeup")
                else: print("WARNING | invalid format for element in data | csv_writeup")
                return None
            if list(data[item][item2].keys()) != ["areaCode", "areaType", "cumDailyNsoDeathsByDeathDate", "hospitalCases", "newCasesBySpecimenDate"]:
                if log: logger.warning("WARNING | invalid keys for element in data | csv_writeup")
                else: print("WARNING | invalid keys for element in data | csv_writeup")
                return None
    if len(args) > 0:
        if log: logger.info("INFO | too many non-keyword arguements | csv_writeup")
        else: print("INFO | too many non-keyword arguements | csv_writeup")
    if len(kwargs) > 0:
        if log: logger.info("INFO | unexpected keyword arguments | csv_writeup")
        else: print("INFO | unexpected keyword arguments | csv_writeup")
    #verify given arguements


    new_data = ["areaCode,areaName,areaType,date,cumDailyNsoDeathsByDeathDate,hospitalCases,newCasesBySpecimenDate"]
    #create a header line
    for item in data:
        for item2 in data[item]:
            line = ""
            for a in range(5):
                if a == 1:
                    line += (item + ",")
                if a == 3 - 1:
                    line += (item2 + ",")
                line += str(data[item][item2][["areaCode", "areaType", "cumDailyNsoDeathsByDeathDate", "hospitalCases", "newCasesBySpecimenDate"][a]])
                if a != 5 - 1:
                    line += ","
            new_data.append(line)
    #construct a new line for each element of data
    file = open(csv_filename, "w")
    file.close()
    #empty the csv file
    for line in new_data:
        with open(csv_filename, "a") as f:
            f.write(line)
            f.write("\n")
    #write each line to the csv file
    if log: logger.debug("DEBUG | csv_writeup successfully completed | csv_writeup")
    else: print("DEBUG | csv_writeup successfully completed | csv_writeup")
    return True


def csv_update(csv_filename : str = None, location : str = "England", location_type : str = "nation", log : bool = True, *args, **kwargs) -> None:
    '''a function to update a csv file with new data obtained from uk_covid19 Cov19API'''
    if type(log) != bool:
        log = True
    if log:
        log = "logging" in globals() and "logger" in globals()
        if not log:
            print("WARNING | unable to log | csv_update")
    #verify if logging is enabled

    if log: logger.debug("DEBUG | csv_update called successfully | csv_update")
    else: print("DEBUG | csv_update called successfully | csv_update")

    global datetime
    if "datetime" not in globals():
        if log: logger.warning("WARNING | datetime not imported | csv_update")
        else: print("WARNING | datetime not imported | csv_update")
        try:
            from datetime import datetime
        except:
            if log: logger.critical("CRITICAL | datetime not in system path | csv_update")
            else: print("CRITICAL | datetime not in system path | csv_update")
            return None
    global parse_csv_data
    if "parse_csv_data" not in globals():
        if log: logger.warning("WARNING | parse_csv_data not imported | csv_update")
        else: print("WARNING | parse_csv_data not imported | csv_update")
        try:
            from covid_data_handler import parse_csv_data
        except:
            if log: logger.critical("CRITICAL | covid_data_handler not in system path | csv_update")
            else: print("CRITICAL | covid_data_handler not in system path | csv_update")
            return None
    global parse_csv_data2
    if "parse_csv_data2" not in globals():
        if log: logger.warning("WARNING | parse_csv_data2 not imported | csv_update")
        else: print("WARNING | parse_csv_data2 not imported | csv_update")
        try:
            from covid_data_handler import parse_csv_data2
        except:
            if log: logger.critical("CRITICAL | covid_data_handler not in system path | csv_update")
            else: print("CRITICAL | covid_data_handler not in system path | csv_update")
            return None
    global covid_API_request
    if "covid_API_request" not in globals():
        if log: logger.warning("WARNING | covid_API_request not imported | csv_update")
        else: print("WARNING | covid_API_request not imported | csv_update")
        try:
            from covid_data_handler import covid_API_request
        except:
            if log: logger.critical("CRITICAL | covid_data_handler not in system path | csv_update")
            else: print("CRITICAL | covid_data_handler not in system path | csv_update")
            return None
    global process_covid_csv_data
    if "process_covid_csv_data" not in globals():
        if log: logger.warning("WARNING | process_covid_csv_data not imported | csv_update")
        else: print("WARNING | process_covid_csv_data not imported | csv_update")
        try:
            from covid_data_handler import process_covid_csv_data
        except:
            if log: logger.critical("CRITICAL | covid_data_handler not in system path | csv_update")
            else: print("CRITICAL | covid_data_handler not in system path | csv_update")
            return None
    global csv_writeup
    if "csv_writeup" not in globals():
        if log: logger.warning("WARNING | csv_writeup not imported | csv_update")
        else: print("WARNING | csv_writeup not imported | csv_update")
        try:
            from covid_data_handler import csv_writeup
        except:
            if log: logger.critical("CRITICAL | covid_data_handler not in system path | csv_update")
            else: print("CRITICAL | covid_data_handler not in system path | csv_update")
            return None
    #verify if necessary functions are present

    if csv_filename == None:
        if log: logger.warning("WARNING | csv_filename not given | csv_update")
        else: print("WARNING | csv_filename not given | csv_update")
        return None
    csv_filename = str(csv_filename)
    if csv_filename[-4:] != ".csv":
        if log: logger.warning("WARNING | invalid file extension | csv_update")
        else: print("WARNING | invalid file extension | csv_update")
        return None
    location = str(location)
    location_type = str(location_type)
    if len(args) > 0:
        if log: logger.info("INFO | too many non-keyword arguements | csv_update")
        else: print("INFO | too many non-keyword arguements | csv_update")
    if len(kwargs) > 0:
        if log: logger.info("INFO | unexpected keyword arguments | csv_update")
        else: print("INFO | unexpected keyword arguments | csv_update")
    #verify given arguements


    if log: logger.debug("DEBUG | calling parse_csv_data | csv_update")
    else: print("DEBUG | calling parse_csv_data | csv_update")
    data = parse_csv_data(csv_filename)
    if data == None:
        if log: logger.error("ERROR | parse_csv_data failed | csv_update")
        else: print("ERROR | parse_csv_data failed")
        data = {}
    else:
        if log: logger.debug("DEBUG | parse_csv_data returned successfully | csv_update")
        else: print("DEBUG | parse_csv_data returned successfully | csv_update")
        if log: logger.debug("DEBUG | calling parse_csv_data2 | csv_update")
        else: print("DEBUG | calling parse_csv_data2 | csv_update")
        data = parse_csv_data2(data)
        if data == None:
            if log: logger.error("ERROR | parse_csv_data2 failed | csv_update")
            else: print("ERROR | parse_csv_data2 failed | csv_update")
            data = {}
        elif log: logger.debug("DEBUG | parse_csv_data2 returned successfully | csv_update")
        else: print("DEBUG | parse_csv_data2 returned successfully | csv_update")
    #obtain the current contents of the csv file
    if location not in list(data.keys()):
        if log: logger.info("INFO | no entries for location | csv_update")
        else: print("INFO | no entries for location | csv_update")
        data[location] = {}
    if log: logger.debug("DEBUG | calling process_covid_csv_data | csv_update")
    else: print("DEBUG | calling process_covid_csv_data | csv_update")
    data2 = process_covid_csv_data(data, targets = [{"header" : "cumDailyNsoDeathsByDeathDate", "mode" : "latestUpdate", "extra" : None}], areaName = location, csv = False)
    if data2 == None:
        if log: logger.error("ERROR | process_covid_csv_data failed | csv_update")
        else: print("ERROR | process_covid_csv_data failed | csv_update")
        if log: logger.debug("DEBUG | calling ovid_API_request_csv_data | csv_update")
        else: print("DEBUG | calling covid_API_request | csv_update")
        new_data = covid_API_request(location, location_type)
    else:
        date = data2["latestUpdate_cumDailyNsoDeathsByDeathDate"]
        if date == None:
            if log: logger.error("ERROR | cprocess_covid_csv_data failed | csv_update")
            else: print("ERROR | process_covid_csv_data failed | csv_update")
            if log: logger.debug("DEBUG | calling covid_API_request_csv_data | csv_update")
            else: print("DEBUG | calling covid_API_request | csv_update")
            new_data = covid_API_request(location, location_type)
        else:
            if log: logger.debug("DEBUG | process_covid_csv_data returned successfully | csv_update")
            else: print("DEBUG | process_covid_csv_data returned successfully | csv_update")
            if log: logger.debug("DEBUG | calling covid_API_request_csv_data | csv_update")
            else: print("DEBUG | calling covid_API_request | csv_update")
            new_data = covid_API_request(location, location_type, date = date)
    #attempt to find the latest date for which all values of data were known and specify this date in the covid_API_request to obtain any missing data from the uk_covid19 Cov19API
    if new_data == None:
        if log: logger.error("ERROR | covid_API_request failed | csv_update")
        else: print("ERROR | covid_API_request failed | csv_update")
        return None
    if log: logger.debug("DEBUG | covid_API_request returned successfully | csv_update")
    else: print("DEBUG | covid_API_request returned successfully | csv_update")
    for item in new_data[location]:
        data[location][item] = new_data[location][item]
    #place the new data into the old (replacing the old elements wherever a repeat key occurs - data from the uk_covid19 Cov19API is trusted to be more reliable
    new = {}
    try:
        for key in sorted(data[location], key = lambda item : int(datetime.strptime(item, "%Y-%m-%d").strftime("%Y%m%d")), reverse = True):
            new[key] = data[location][key]
        data[location] = new
        #sort the data by date
    except:
        if log: logger.warning('WARNING | invalid format for data["date"] as retrieved from uk_covid19 Cov19API or csv_file | csv_update')
        else: print('WARNING | invalid format for data["date"] as retrieved from uk_covid19 Cov19API or csv_file | csv_update')
        return None
    if log: logger.debug("DEBUG | calling csv_writeup | csv_update")
    else: print("DEBUG | calling csv_writeup | csv_update")
    if csv_writeup(csv_filename, data) == None:
        if log: logger.error("ERROR | csv_writeup failed | csv_update")
        else: print("ERROR | csv_writeup failed | csv_update")
        return None
    if log: logger.debug("DEBUG | csv_writeup returned successfully | csv_update")
    else: print("DEBUG | csv_writeup returned successfully | csv_update")
    #write the new data to the csv file
    if log: logger.debug("DEBUG | csv_update successfully completed | csv_update")
    else: print("DEBUG | csv_update successfully completed | csv_update")
    return True


def covid_update(update_name : str = None, log : bool = True, *args, **kwargs) -> None:
    '''a function to update covid data from uk_covid19 Cov19API'''

    if type(log) != bool:
        log = True
    if log:
        log = "logging" in globals() and "logger" in globals()
        if not log:
            print("WARNING | unable to log | covid_update")
    #verify if logging is enabled

    if log: logger.debug("DEBUG | covid_update called successfully | covid_update")
    else: print("DEBUG | covid_update called successfully | covid_update")

    global schedule_covid_updates
    global updates
    if "updates" not in globals():
        if log: logger.warning("WARNING | global updates not present | schedule_covid_updates")
        else: print("WARNING | global updates not present | schedule_covid_updates")
        updates = []
    if type(updates) != list:
        if log: logger.warning("WARNING | invalid type for global updates | schedule_covid_updates")
        else: print("WARNING | invalid type for global updates | schedule_covid_updates")
        updates = []
    for a in range(len(updates) -1 , -1, -1):
        if type(updates[a]) != dict:
            if log: logger.warning("WARNING | invalid type for element in updates | schedule_covid_updates")
            else: print("WARNING | invalid type for element in updates | schedule_covid_updates")
            updates.pop(a)
        elif list(updates[a].keys()) != ["time", "time2", "type", "title", "content", "event", "repeat"]:
            if log: logger.warning("WARNING | invalid format for element in updates | schedule_covid_updates")
            else: print("WARNING | invalid format for element in updates | schedule_covid_updates")
            updates.pop(a)
    #verify the contents of updates
    if update_name == None:
        if log: logger.warning("WARNING | update_name not given | news_API_request")
        else: print("WARNING | update_name not given | news_API_request")
    else:
        update_name = str(update_name)
        for a in range(len(updates) -1, -1, -1):
            if updates[a]["title"] == update_name and not updates[a]["type"]:
                if updates[a]["repeat"]:
                    if "schedule_covid_updates" not in globals():
                        if log: logger.warning("WARNING | schedule_covid_updates not imported | covid_update")
                        else: print("WARNING | schedule_covid_updates not imported | covid_update")
                        try:
                            from covid_data_handler import schedule_covid_updates
                        except:
                            if log: logger.critical("CRITICAL | covid_data_handler not in system path | covid_update")
                            else: print("CRITICAL | covid_data_handler not in system path | covid_update")
                            return None
                        #if the update that triggered this function is meant to repeat, reschedule the update
                    time = updates[a]["time2"]
                    updates.pop(a)
                    schedule_covid_updates(time, update_name, repeat = True)
                else:
                    updates.pop(a)
                break
    #if this function was triggered by an update, remove that update from updates

    csv = True
    global csv_update
    if "csv_update" not in globals():
        if log: logger.warning("WARNING | csv_update not imported | covid_update")
        else: print("WARNING | csv_update not imported | covid_update")
        try:
            from covid_data_handler import csv_update
        except:
            if log: logger.critical("CRITICAL | covid_data_handler not in system path | covid_update")
            else: print("CRITICAL | covid_data_handler not in system path | covid_update")
            csv = False
    global parse_csv_data
    if "parse_csv_data" not in globals():
        if log: logger.warning("WARNING | parse_csv_data not imported | covid_update")
        else: print("WARNING | parse_csv_data not imported | covid_update")
        try:
            from covid_data_handler import parse_csv_data
        except:
            if log: logger.critical("CRITICAL | covid_data_handler not in system path | covid_update")
            else: print("CRITICAL | covid_data_handler not in system path | covid_update")
            csv = False
    global parse_csv_data2
    if "parse_csv_data2" not in globals():
        if log: logger.warning("WARNING | parse_csv_data2 not imported | covid_update")
        else: print("WARNING | parse_csv_data2 not imported | covid_update")
        try:
            from covid_data_handler import parse_csv_data2
        except:
            if log: logger.critical("CRITICAL | covid_data_handler not in system path | covid_update")
            else: print("CRITICAL | covid_data_handler not in system path | covid_update")
            csv = False
    global covid_API_request
    if "covid_API_request" not in globals():
        if log: logger.warning("WARNING | covid_API_request not imported | covid_update")
        else: print("WARNING | covid_API_request not imported | covid_update")
        try:
            from covid_data_handler import covid_API_request
        except:
            if log: logger.critical("CRITICAL | covid_data_handler not in system path | covid_update")
            else: print("CRITICAL | covid_data_handler not in system path | covid_update")
            return None
    global process_covid_csv_data
    if "process_covid_csv_data" not in globals():
        if log: logger.warning("WARNING | process_covid_csv_data not imported | covid_update")
        else: print("WARNING | process_covid_csv_data not imported | covid_update")
        try:
            from covid_data_handler import process_covid_csv_data
        except:
            if log: logger.critical("CRITICAL | covid_data_handler not in system path | covid_update")
            else: print("CRITICAL | covid_data_handler not in system path | covid_update")
            return None
    #verify if necessary functions are present

    global csv_filename
    if "csv_filename" not in globals():
        if log: logger.warning("WARNING | global csv_filename not present | covid_update")
        else: print("WARNING | global csv_filename not present | covid_update")
        csv = False
    global local_7day_infections
    global national_7day_infections
    global hospital_cases
    global deaths_total
    global AreaName
    if "AreaName" not in globals():
        if log: logger.warning("WARNING | global AreaName not present | covid_update")
        else: print("WARNING | global AreaName not present | covid_update")
        AreaName = "Exeter"
    global AreaType
    if "AreaType" not in globals():
        if log: logger.warning("WARNING | global AreaType not present | covid_update")
        else: print("WARNING | global AreaType not present | covid_update")
        AreaType = "ltla"
    #verify necessary globals

    if len(args) > 0:
        if log: logger.info("INFO | too many non-keyword arguements | covid_update")
        else: print("INFO | too many non-keyword arguements | covid_update")
    if len(kwargs) > 0:
        if log: logger.info("INFO | unexpected keyword arguments | covid_update")
        else: print("INFO | unexpected keyword arguments | covid_update")
    #verify given arguements


    if csv:
        if log: logger.debug("DEBUG | calling csv_update | covid_update")
        else: print("DEBUG | calling csv_update | covid_update")
        check1 = csv_update(csv_filename)
        if check1 == None:
            if log: logger.error("ERROR | csv_update failed | covid_update")
            else: print("ERROR | csv_update failed | covid_update")
            csv = False
        elif log: logger.debug("DEBUG | csv_update returned successfully | covid_update")
        else: print("DEBUG | csv_update returned successfully | covid_update")
        if log: logger.debug("DEBUG | calling csv_update | covid_update")
        else: print("DEBUG | calling csv_update | covid_update")
        check2 = csv_update(csv_filename, AreaName, AreaType)
        if check2 == None:
            if log: logger.error("ERROR | csv_update failed | covid_update")
            else: print("ERROR | csv_update failed | covid_update")
            csv = False
        elif log: logger.debug("DEBUG | csv_update returned successfully | covid_update")
        else: print("DEBUG | csv_update returned successfully | covid_update")
    #attempt to update the local and national content of the csv file
    if csv:
        if log: logger.debug("DEBUG | calling parse_csv_data | covid_update")
        else: print("DEBUG | calling parse_csv_data | covid_update")
        data = parse_csv_data(csv_filename)
        if data == None:
            if log: logger.error("ERROR | parse_csv_data failed | covid_update")
            else: print("ERROR | parse_csv_data failed | covid_update")
            csv = False
        else:
            if log: logger.debug("DEBUG | parse_csv_data returned successfully | covid_update")
            else: print("DEBUG | parse_csv_data returned successfully | covid_update")
            if log: logger.debug("DEBUG | calling parse_csv_data2 | covid_update")
            else: print("DEBUG | calling parse_csv_data2 | covid_update")
            data = parse_csv_data2(data)
            if data == None:
                if log: logger.error("ERROR | parse_csv_data2 failed | covid_update")
                else: print("ERROR | parse_csv_data2 failed | covid_update")
                csv = False
            elif log: logger.debug("DEBUG | parse_csv_data2 returned successfully | covid_update")
            else: print("DEBUG | parse_csv_data2 returned successfully | covid_update")
    #if attempts to update the local and national content of the csv file were successful, take the contents of the csv file to be up to date covid statistics
    if not csv:
        if log: logger.debug("DEBUG | calling covid_API_request | covid_update")
        else: print("DEBUG | calling covid_API_request | covid_update")
        data = covid_API_request(location = AreaName, location_type = AreaType)
        if data == None:
            if log: logger.error("ERROR | covid_API_request failed | covid_update")
            else: print("ERROR | covid_API_request failed | covid_update")
            return None
        if log: logger.debug("DEBUG | covid_API_request returned successfully | covid_update")
        else: print("DEBUG | covid_API_request returned successfully | covid_update")
        if log: logger.debug("DEBUG | calling covid_API_request | covid_update")
        else: print("DEBUG | calling covid_API_request | covid_update")
        data2 = covid_API_request(location = "England", location_type = "Nation")
        if data2 == None:
            if log: logger.error("ERROR | covid_API_request failed | covid_update")
            else: print("ERROR | covid_API_request failed | covid_update")
            return None
        if log: logger.debug("DEBUG | covid_API_request returned successfully | covid_update")
        else: print("DEBUG | covid_API_request returned successfully | covid_update")
        data.update(data2)
    #if attempts to update the local and national content of the csv file were unsuccessful, obtain up to date covid statistics from the uk_covid19 Cov19API
    if log: logger.debug("DEBUG | calling process_covid_csv_data | covid_update")
    else: print("DEBUG | calling process_covid_csv_data | covid_update")
    temp = process_covid_csv_data(covid_csv_data = data, targets = [{"header" : "newCasesBySpecimenDate", "mode" : "sum", "extra" : 7}], areaName = AreaName, csv = False)
    if temp == None:
        if log: logger.error("ERROR | process_covid_csv_data failed | covid_update")
        else: print("ERROR | process_covid_csv_data failed | covid_update")
        return None
    if log: logger.debug("DEBUG | process_covid_csv_data returned successfully | covid_update")
    else: print("DEBUG | process_covid_csv_data returned successfully | covid_update")
    local_7day_infections = temp["sum_last7days_newCasesBySpecimenDate"]
    #calculate the value for the local 7 day infections from the covid data
    if log: logger.debug("DEBUG | calling process_covid_csv_data | covid_update")
    else: print("DEBUG | calling process_covid_csv_data | covid_update")
    temp = process_covid_csv_data(covid_csv_data = data, targets = [{"header" : "newCasesBySpecimenDate", "mode" : "sum", "extra" : 7}, {"header" : "hospitalCases", "mode" : "latest", "extra" : None}, {"header" : "cumDailyNsoDeathsByDeathDate", "mode" : "latest", "extra" : None}], csv = False)
#TARGETS SHOULD NOT BE NEEDED!!!
    if temp == None:
        if log: logger.error("ERROR | process_covid_csv_data failed | covid_update")
        else: print("ERROR | process_covid_csv_data failed | covid_update")
        return None
    if log: logger.debug("DEBUG | process_covid_csv_data returned successfully | covid_update")
    else: print("DEBUG | process_covid_csv_data returned successfully | covid_update")
    national_7day_infections = temp["sum_last7days_newCasesBySpecimenDate"]
    hospital_cases = temp["latest_hospitalCases"]
    deaths_total = temp["latest_cumDailyNsoDeathsByDeathDate"]
    #calculate or extract the remaining desired covid statistics from the covid data
    if log: logger.debug("DEBUG | covid_update successfully completed | covid_update")
    else: print("DEBUG | covid_update successfully completed | covid_update")
    return True


def schedule_covid_updates(update_interval : str = None, update_name : str = None, *args, repeat : bool = False, log : bool = True, **kwargs) -> None:
    '''a function to schedule updates to covid data'''

    if type(log) != bool:
        log = True
    if log:
        log = "logging" in globals() and "logger" in globals()
        if not log:
            print("WARNING | unable to log | schedule_covid_updates")
    #verify if logging is enabled

    if log: logger.debug("DEBUG | schedule_covid_updates called successfully | schedule_covid_updates")
    else: print("DEBUG | schedule_covid_updates called successfully | schedule_covid_updates")

    global sched
    if "sched" not in globals():
        if log: logger.warning("WARNING | sched not imported | schedule_covid_updates")
        else: print("WARNING | sched not imported | schedule_covid_updates")
        try:
            import sched
        except:
            if log: logger.critical("CRITICAL | sched not in system path | schedule_covid_updates")
            else: print("CRITICAL | sched not in system path | schedule_covid_updates")
            return None
    global time
    if "time" not in globals():
        if log: logger.warning("WARNING | time not imported | schedule_covid_updates")
        else: print("WARNING | time not imported | schedule_covid_updates")
        try:
            import time
        except:
            if log: logger.critical("CRITICAL | time not in system path | schedule_covid_updates")
            else: print("CRITICAL | time not in system path | schedule_covid_updates")
            return None
    global datetime
    if "datetime" not in globals():
        if log: logger.warning("WARNING | datetime not imported | schedule_covid_updates")
        else: print("WARNING | datetime not imported | schedule_covid_updates")
        try:
            from datetime import datetime
        except:
            if log: logger.critical("CRITICAL | datetime not in system path | schedule_covid_updates")
            else: print("CRITICAL | datetime not in system path | schedule_covid_updates")
            return None
    global covid_update
    if "covid_update" not in globals():
        if log: logger.warning("WARNING | covid_update not imported | schedule_covid_updates")
        else: print("WARNING | covid_update not imported | schedule_covid_updates")
        try:
            from covid_data_handler import covid_update
        except:
            if log: logger.critical("CRITICAL | covid_data_handler not in system path | schedule_covid_updates")
            else: print("CRITICAL | covid_data_handler not in system path | schedule_covid_updates")
            return None
    #verify if necessary functions are present

    global updates
    if "updates" not in globals():
        if log: logger.warning("WARNING | global updates not present | schedule_covid_updates")
        else: print("WARNING | global updates not present | schedule_covid_updates")
        updates = []
    if type(updates) != list:
        if log: logger.warning("WARNING | invalid type for global updates | schedule_covid_updates")
        else: print("WARNING | invalid type for global updates | schedule_covid_updates")
        updates = []
    for a in range(len(updates) -1 , -1, -1):
        if type(updates[a]) != dict:
            if log: logger.warning("WARNING | invalid type for element in updates | schedule_covid_updates")
            else: print("WARNING | invalid type for element in updates | schedule_covid_updates")
            updates.pop(a)
        elif list(updates[a].keys()) != ["time", "time2", "type", "title", "content", "event", "repeat"]:
            if log: logger.warning("WARNING | invalid format for element in updates | schedule_covid_updates")
            else: print("WARNING | invalid format for element in updates | schedule_covid_updates")
            updates.pop(a)
    global schedule
    if "schedule" not in globals():
        if log: logger.warning("WARNING | global schedule not present | schedule_covid_updates")
        else: print("WARNING | global schedule not present | schedule_covid_updates")
        schedule = sched.scheduler(time.time, time.sleep)
    if type(schedule) != type(sched.scheduler(time.time, time.sleep)):
        if log: logger.warning("WARNING | invalid type for global schedule | schedule_covid_updates")
        else: print("WARNING | invalid type for global schedule | schedule_covid_updates")
        schedule = sched.scheduler(time.time, time.sleep)
    #verify necessary globals

    if update_interval == None:
        if log: logger.warning("WARNING | update_interval not given | schedule_covid_updates")
        else: print("WARNING | update_interval not given | schedule_covid_updates")
        return None
    update_interval = str(update_interval).replace("%3A", ":")
    try:
        update_interval2 = datetime.strptime(update_interval, "%H:%M")
    except:
        if log: logger.warning("WARNING | invalid format for update_interval | schedule_covid_updates")
        else: print("WARNING | invalid format for update_interval | schedule_covid_updates")
        return None
    if update_name == None:
        if log: logger.warning("WARNING | update_name not given | schedule_covid_updates")
        else: print("WARNING | update_name not given")
        return None
    update_name2 = str(update_name)
    a = 1
    while True:
        check = True
        for update in updates:
            if update_name2 == update["title"]:
                check = False
        if check:
            break
        if log: logger.info("INFO | an update with this name already exists, " + update_name2 + " | schedule_covid_updates")
        else: print("INFO | an update with this name already exists, " + update_name2 + " | schedule_covid_updates")
        update_name2 = update_name + " (" + str(a) + ")"
        a += 1
    #ensure the update_name is unique
    if len(args) > 0:
        if log: logger.info("INFO | too many non-keyword arguements | schedule_covid_updates")
        else: print("INFO | too many non-keyword arguements | schedule_covid_updates")
    if type(repeat) != bool:
        if log: logger.warning("WARNING | invalid type for repeat | schedule_covid_updates")
        else: print("WARNING | invalid type for repeat | schedule_covid_updates")
        return None
    if len(kwargs) > 0:
        if log: logger.info("INFO | unexpected keyword arguments | schedule_covid_updates")
        else: print("INFO | unexpected keyword arguments | schedule_covid_updates")
    #verify given arguements


    update_interval2 = time.time() + ((update_interval2 - datetime(1900, 1, 1)).total_seconds() - (time.time() % (24 * 60 * 60))) % (24 * 60 * 60)
    #calculate the desired time from the update_interval
    event = schedule.enterabs(update_interval2, 1, covid_update, kwargs = {"update_name" : update_name})
    #schedule the calling of news_API_request
    updates.append({"time" : update_interval2, "time2" : update_interval, "type" : 0, "title" : update_name2, "content" : update_interval + ", Covid data", "event" : event, "repeat" : repeat})
    #add an appropriate update to updates
    if log: logger.info("INFO | covid data update set for " + str(update_interval2) + "(" + update_interval + ") | schedule_covid_updates")
    else: print("INFO | covid data update set for " + str(update_interval2) + " (" + update_interval + ") | schedule_covid_updates")
    if log: logger.debug("DEBUG | schedule_covid_updates successfully completed | schedule_covid_updates")
    else: print("DEBUG | schedule_covid_updates successfully completed | schedule_covid_updates")
    return True
