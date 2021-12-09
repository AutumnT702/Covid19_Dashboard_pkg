filename = "results.txt"
tests_csv = "tests.csv"
test_config_json = "test_config.json"
file = open(filename, "w")
file.close()

import covid_data_handler
from covid_data_handler import parse_csv_data
from covid_data_handler import parse_csv_data2
from covid_data_handler import subprocess_covid_csv_data
from covid_data_handler import process_covid_csv_data
from covid_data_handler import covid_API_request
from covid_data_handler import csv_writeup
from covid_data_handler import csv_update
from covid_data_handler import covid_update
from covid_data_handler import schedule_covid_updates

import covid_news_handling
from covid_news_handling import news_API_request
from covid_news_handling import update_news

import main
from main import json_read
from main import json_write
from main import reset_updates
from main import reset_news
from main import update_remove
from main import news_remove

def test_parse_csv_data():
    if "filename" not in globals():
        filename = "results.txt"
    with open(filename, "a") as file:
        file.write("test_parse_csv_data\n")

        try:
            assert parse_csv_data() == parse_csv_data(None, log = True)
            file.write("SUCCESS | parse_csv_data successfully defaults | test_parse_csv_data\n")
        except:
            file.write("FAILURE | parse_csv_data fails to default | test_parse_csv_data\n")

        data = parse_csv_data()
        try:
            assert data == None
            file.write("SUCCESS | parse_csv_data successfully returns None when given no arguments | test_parse_csv_data\n")
        except:
            file.write("FAILURE | parse_csv_data fails to return None when given no arguments | test_parse_csv_data\n")

        data = parse_csv_data("no file extension")
        try:
            assert data == None
            file.write("SUCCESS | parse_csv_data successfully returns None when given a csv_filename not ending in '.csv' | test_parse_csv_data\n")
        except:
            file.write("FAILURE | parse_csv_data fails to return None when given a csv_filename not ending in '.csv' | test_parse_csv_data\n")

        data = parse_csv_data("non_existant_file.csv")
        try:
            assert data == None
            file.write("SUCCESS | parse_csv_data successfully returns None when given a csv_filename that does not exist within the Covid19_Dashboard_pkg directory | test_parse_csv_data\n")
        except:
            file.write("FAILURE | parse_csv_data fails to return None when given a csv_filename that does not exist within the Covid19_Dashboard_pkg directory | test_parse_csv_data\n")

        data = parse_csv_data("nation_2021-10-28.csv")
        try:
            assert type(data) == list
            file.write("SUCCESS | parse_csv_data successfully returns a list when given valid arguments | test_parse_csv_data\n")
            try:
                assert len(data) == 639
                file.write("SUCCESS | parse_csv_data successfully returns an element for each line of the given csv file | test_parse_csv_data\n")
            except:
                file.write("FAILURE | parse_csv_data fails to return an element for each line of the given csv file | test_parse_csv_data\n")
            for a in range(len(data)):
                try:
                    assert len(data[a].split(",")) == 7
                    if a == len(data) - 1:
                        file.write("SUCCESS | parse_csv_data successfully returns each element such that each column forms its own comma seperated substring | test_parse_csv_data\n")
                except:
                    file.write("FAILURE | parse_csv_data fails to return each element such that each column forms its own comma seperated substring | test_parse_csv_data\n")
                    break
            try:
                assert data[20] == "E92000001,England,nation,2021-10-09,141109,4921,26560"
                file.write("SUCCESS | parse_csv_data successfully returns contents matching that of the given file | test_parse_csv_data\n")
            except:
                file.write("FAILURE | parse_csv_data fails to return contents matching that of the given file | test_parse_csv_data\n")
        except:
            file.write("FAILURE | parse_csv_data fails to return a list when given valid arguments | test_parse_csv_data\n")

        data2 = parse_csv_data("nation_2021-10-28.csv", "unnecessary_argument", ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | parse_csv_data is successfully unaffected by the addition of unnecessary arguments | test_parse_csv_data\n")
        except:
            file.write("FAILURE | parse_csv_data fails to be unaffected by the addition of unnecessary arguments | test_parse_csv_data\n")

        data2 = parse_csv_data("nation_2021-10-28.csv", argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument\n"])
        try:
            assert data2 == data
            file.write("SUCCESS | parse_csv_data is successfully unaffected by the addition of unnecessary keyword arguments | test_parse_csv_data\n")
        except:
            file.write("FAILURE | parse_csv_data fails to be unaffected by the addition of unnecessary keyword arguments | test_parse_csv_data\n")
    
        file.write("\n")


def test_parse_csv_data2():
    if "filename" not in globals():
        filename = "results.txt"
    with open(filename, "a") as file:
        file.write("test_parse_csv_data2\n")

        try:
            assert parse_csv_data2() == parse_csv_data2(None, log = True)
            file.write("SUCCESS | parse_csv_data2 successfully defaults | test_parse_csv_data2\n")
        except:
            file.write("FAILURE | parse_csv_data2 fails to default | test_parse_csv_data2\n")

        data = parse_csv_data2()
        try:
            assert data == None
            file.write("SUCCESS | parse_csv_data2 successfully returns None when given no arguments | test_parse_csv_data2\n")
        except:
            file.write("FAILURE | parse_csv_data2 fails to return None when given no arguments | test_parse_csv_data2\n")

        data = parse_csv_data2("this isn't a list")
        try:
            assert data == None
            file.write("SUCCESS | parse_csv_data2 successfully returns None when given covid_csv_data that is not a list | test_parse_csv_data2\n")
        except:
            file.write("FAILURE | parse_csv_data2 fails to return None when given covid_csv_data that is not a list | test_parse_csv_data2\n")

        data = parse_csv_data2(["this,list,does,not,have,all,elements,in,the,form,of,7,substrings,split,by,commas"])
        try:
            assert data == None
            file.write("SUCCESS | parse_csv_data2 successfully returns None when given covid_csv_data for which each element is not a string seperated into 7 substrings by commas | test_parse_csv_data2\n")
        except:
            file.write("FAILURE | parse_csv_data2 fails to return None when given covid_csv_data for which each element is not a string seperated into 7 substrings by commas | test_parse_csv_data2\n")

        data = parse_csv_data2(["unfortunately,element,1,has,repeating,headers,headers"])
        try:
            assert data == None
            file.write("SUCCESS | parse_csv_data2 successfully returns None when given covid_csv_data for which the first element has repeated substrings | test_parse_csv_data2\n")
        except:
            file.write("FAILURE | parse_csv_data2 fails to return None when given covid_csv_data for which the first element has repeated substrings | test_parse_csv_data2\n")

        data = parse_csv_data2(parse_csv_data("nation_2021-10-28.csv"))
        try:
            assert type(data) == dict
            file.write("SUCCESS | parse_csv_data2 successfully returns a dictionary when given valid arguments | test_parse_csv_data2\n")
            try:
                assert list(data.keys()) == ["England"]
                file.write("SUCCESS | parse_csv_data2 successfully returns a sub-dictionary for each unique areaName in the given covid_csv_data keyed to by that areaName | test_parse_csv_data2\n")
                try:
                    assert len(data["England"]) == 638
                    file.write("SUCCESS | parse_csv_data2 successfully returns an element for each element of the given covid_csv_data (excluding the first) | test_parse_csv_data2\n")
                except:
                    file.write("FAILURE | parse_csv_data2 fails to return an element for each element of the given covid_csv_data (excluding the first) | test_parse_csv_data2\n")
                for a in range(len(list(data["England"].keys()))):
                    try:
                        assert list(data["England"][list(data["England"].keys())[a]].keys()) == ["areaCode", "areaType", "cumDailyNsoDeathsByDeathDate", "hospitalCases", "newCasesBySpecimenDate"]
                        if a == len(list(data["England"].keys())) - 1:
                            file.write("SUCCESS | parse_csv_data2 successfully returns the values of the given covid_csv_data keyed to by the substring in the matching header index | test_parse_csv_data2\n")
                    except:
                        file.write("FAILURE | parse_csv_data2 fails to return the values of the given covid_csv_data keyed to by the substring in the matching header index | test_parse_csv_data2\n")
                try:
                    assert data["England"]["2021-10-08"] == {"areaCode" : "E92000001", "areaType" : "nation", "cumDailyNsoDeathsByDeathDate" : "141025", "hospitalCases" : "4975", "newCasesBySpecimenDate" : "29234"}
                    file.write("SUCCESS | parse_csv_data2 successfully returns contents matching that of the given covid_csv_data | test_parse_csv_data2\n")
                except:
                    file.write("FAILURE | parse_csv_data2 fails to return contents matching that of the given covid_csv_data | test_parse_csv_data2\n")
            except:
                file.write("FAILURE | parse_csv_data2 fails to return a sub-dictionary for each unique areaName in the given covid_csv_data keyed to by that areaName | test_parse_csv_data2\n")
        except:
            file.write("FAILUE | parse_csv_data2 fails to return a dictionary when given valid arguments | test_parse_csv_data2\n")

        data2 = parse_csv_data2(parse_csv_data("nation_2021-10-28.csv"), "unnecessary_argument", ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | parse_csv_data2 is successfully unaffected by the addition of unnecessary arguments | test_parse_csv_data2\n")
        except:
            file.write("FAILURE | parse_csv_data2 fails to be unaffected by the addition of unnecessary arguments | test_parse_csv_data2\n")

        data2 = parse_csv_data2(parse_csv_data("nation_2021-10-28.csv"), argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | parse_csv_data is successfully unaffected by the addition of unnecessary keyword arguments | test_parse_csv_data\n")
        except:
            file.write("FAILURE | parse_csv_data fails to be unaffected by the addition of unnecessary keyword arguments | test_parse_csv_data\n")

        file.write("\n")


def test_subprocess_covid_csv_data():
    if "filename" not in globals():
        filename = "results.txt"
    with open(filename, "a") as file:
        file.write("test_subprocess_covid_csv_data\n")

        try:
            assert subprocess_covid_csv_data() == subprocess_covid_csv_data(None, None, None, None, False, True)
            file.write("SUCCESS | subprocess_covid_csv_data successfully defaults | test_subprocess_covid_csv_data\n")
        except:
            file.write("FAILURE | subprocess_covid_csv_data fails to default | test_subprocess_covid_csv_data\n")

        data = (subprocess_covid_csv_data({"areaName" : { "date" : {"key" : "value"}}}, 0, "key", "areaName", None),
subprocess_covid_csv_data({"areaName" : { "date" : {"key" : "value"}}}, 0, "key", None, True),
subprocess_covid_csv_data({"areaName" : { "date" : {"key" : "value"}}}, 0, None, "areaName", True),
subprocess_covid_csv_data({"areaName" : { "date" : {"key" : "value"}}}, None, "key", "areaName", True),
subprocess_covid_csv_data(None, 0, "key", "areaName", True))
        try:
            assert data == (None, None, None, None, None)
            file.write("SUCCESS | subprocess_covid_csv_data successfully returns None when any of its arguments are missing | test_subprocess_covid_csv_data\n")
        except:
            file.write("FAILURE | subprocess_covid_csv_data fails to return None when any of its arguments are missing | test_subprocess_covid_csv_data\n")

        data = (subprocess_covid_csv_data({"areaName" : { "date" : {"key" : "value"}}}, 0, "key", "areaName", "not a boolean"),
subprocess_covid_csv_data({"areaName" : { "date" : {"key" : "value"}}}, "not an integer", "key", "areaName", True),
subprocess_covid_csv_data({"areaName" : {"not a dictionary"}}, 0, "key", "areaName", True),
subprocess_covid_csv_data({"not a dictionary"}, 0, "key", "areaName", True),
subprocess_covid_csv_data("not a dictionary", 0, "key", "areaName", True))
        try:
            assert data == (None, None, None, None, None)
            file.write("SUCCESS | subprocess_covid_csv_data successfully returns None when any of its arguments are of an invalid type | test_subprocess_covid_csv_data\n")
        except:
            file.write("FAILURE | subprocess_covid_csv_data fails to return None when any of its arguments are of an invalid type | test_subprocess_covid_csv_data\n")

        data = subprocess_covid_csv_data({"areaName" : { "date" : {"key" : "value"}}}, 0, "key", "invalid areaName", True)
        try:
            assert data == None
            file.write("SUCCESS | subprocess_covid_csv_data successfully returns None when given an areaName not present in the keys of data | test_subprocess_covid_csv_data\n")
        except:
            file.write("FAILURE | subprocess_covid_csv_data fails to return None when given an areaName not present in the keys of data | test_subprocess_covid_csv_data\n")

        data = subprocess_covid_csv_data({"areaName" : { "date" : {"key" : "value"}}}, 1, "key", "areaName", True)
        try:
            assert data == None
            file.write("SUCCESS | subprocess_covid_csv_data successfully returns None when given a row equalling or exceeding the length of data['areaName'] | test_subprocess_covid_csv_data\n")
        except:
            file.write("FAILURE | subprocess_covid_csv_data fails to return None when given a row equalling or exceeding the length of data['areaName'] | test_subprocess_covid_csv_data\n")

        data = subprocess_covid_csv_data({"areaName" : { "date" : {"key" : "value"}}}, 0, "invalid key", "areaName", True)
        try:
            assert data == None
            file.write("SUCCESS | subprocess_covid_csv_data successfully returns None when given a col not present in the keys of the dictionary for the key at index row in the keys of data['areaName'] | test_subprocess_covid_csv_data\n")
        except:
            file.write("FAILURE | subprocess_covid_csv_data fails to return None when given a col not present in the keys of the dictionary for the key at index row in the keys of data['areaName'] | test_subprocess_covid_csv_data\n")

        data = subprocess_covid_csv_data(parse_csv_data2(parse_csv_data("nation_2021-10-28.csv")), 17, "hospitalCases", "England", False)
        try:
            assert data == "5206"
            file.write("SUCCESS | subprocess_covid_csv_data successfully returns the value present for the key col in the dictionary for the key at index row in the keys of data['areaName'] | test_subprocess_covid_csv_data\n")
        except:
            file.write("FAILURE | subprocess_covid_csv_data fails to return the value present for the key col in the dictionary for the key at index row in the keys of data['areaName'] | test_subprocess_covid_csv_data\n")

        data1 = subprocess_covid_csv_data(parse_csv_data2(parse_csv_data("nation_2021-10-28.csv")), 3, "cumDailyNsoDeathsByDeathDate", "England", True)
        try:
            assert data1 == ""
            file.write("SUCCESS | subprocess_covid_csv_data successfully returns an empty string when asked to find the date for which a targetted value is present wherein the value itself is an empty string | test_subprocess_covid_csv_data\n")
        except:
            file.write("FAILURE | subprocess_covid_csv_data fails to return an empty string when asked to find the date for which a targetted value is present wherein the value itself is an empty string | test_subprocess_covid_csv_data\n")

        data2 = subprocess_covid_csv_data(parse_csv_data2(parse_csv_data("nation_2021-10-28.csv")), 32, "hospitalCases", "England", True)
        try:
            assert data2 == "2021-09-26"
            file.write("SUCCESS | subprocess_covid_csv_data successfully returns the key at index row in the keys of the dictionary data['areaName'] when latestUpdate is set to True and provided the value returned otherwise would not be an empty string | test_subprocess_covid_csv_data\n")
        except:
            file.write("FAILURE | subprocess_covid_csv_data fails to return the key at index row in the keys of the dictionary data['areaName'] when latestUpdate is set to True and provided the value returned otherwise would not be an empty string | test_subprocess_covid_csv_data\n")

        data3 = subprocess_covid_csv_data(parse_csv_data2(parse_csv_data("nation_2021-10-28.csv")), 17, "hospitalCases", "England", False, "unnecessary_argument", ["unnecessary_argument"])
        data4 = subprocess_covid_csv_data(parse_csv_data2(parse_csv_data("nation_2021-10-28.csv")), 3, "cumDailyNsoDeathsByDeathDate", "England", True, "unnecessary_argument", ["unnecessary_argument"])
        data5 = subprocess_covid_csv_data(parse_csv_data2(parse_csv_data("nation_2021-10-28.csv")), 32, "hospitalCases", "England", True, "unnecessary_argument", ["unnecessary_argument"])
        try:
            assert data3 == data
            assert data4 == data1
            assert data5 == data2
            file.write("SUCCESS | subprocess_covid_csv_data is successfully unaffected by the addition of unnecessary arguments | test_subprocess_covid_csv_data\n")
        except:
            file.write("FAILURE | subprocess_covid_csv_data fails to be unaffected by the addition of unnecessary arguments | test_subprocess_covid_csv_data\n")

        data3 = subprocess_covid_csv_data(parse_csv_data2(parse_csv_data("nation_2021-10-28.csv")), 17, "hospitalCases", "England", False, argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument"])
        data4 = subprocess_covid_csv_data(parse_csv_data2(parse_csv_data("nation_2021-10-28.csv")), 3, "cumDailyNsoDeathsByDeathDate", "England", True, argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument"])
        data5 = subprocess_covid_csv_data(parse_csv_data2(parse_csv_data("nation_2021-10-28.csv")), 32, "hospitalCases", "England", True, argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument"])
        try:
            assert data3 == data
            assert data4 == data1
            assert data5 == data2
            file.write("SUCCESS | subprocess_covid_csv_data is successfully unaffected by the addition of unnecessary keyword arguments | test_subprocess_covid_csv_data\n")
        except:
            file.write("FAILURE | subprocess_covid_csv_data fails to be unaffected by the addition of unnecessary keyword arguments | test_subprocess_covid_csv_data\n")

        file.write("\n")


def test_process_covid_csv_data():
    if "filename" not in globals():
        filename = "results.txt"
    with open(filename, "a") as file:
        file.write("test_process_covid_csv_data\n")

        try:
            assert process_covid_csv_data() == process_covid_csv_data(None, targets = [{"header" : "newCasesBySpecimenDate", "mode" : "sum", "extra" : 7}, {"header" : "hospitalCases", "mode" : "latest", "extra" : None}, {"header" : "cumDailyNsoDeathsByDeathDate", "mode" : "latest", "extra" : None}], areaName = "England", csv = True, log = True)
            file.write("SUCCESS | process_covid_csv_data successfully defaults | test_process_covid_csv_data\n")
        except:
            file.write("FAILURE | process_covid_csv_data fails to default | test_process_covid_csv_data\n")

        data = (process_covid_csv_data(["string"], targets = [{"header" : "string", "mode" : "latest", "extra" : None}], areaName = "string", csv = None),
process_covid_csv_data(["string"], targets = [{"header" : "string", "mode" : "latest", "extra" : None}], areaName = None, csv = True),
process_covid_csv_data(["string"], targets = None, areaName = "string", csv = True),
process_covid_csv_data(None, targets = [{"header" : "string", "mode" : "latest", "extra" : None}], areaName = "string", csv = True))
        try:
            assert data == (None, None, None, None)
            file.write("SUCCESS | process_covid_csv_data successfully returns None when any of its arguments are missing | test_process_covid_csv_data\n")
        except:
            file.write("FAILURE | process_covid_csv_data fails to return None when any of its arguments are missing | test_process_covid_csv_data\n")

        data = (process_covid_csv_data(["string"], targets = [{"header" : "string", "mode" : "latest", "extra" : None}], areaName = "string", csv = "not a boolean"),
process_covid_csv_data(["string"], targets = "not a list of dictionaries", areaName = "areaName", csv = True),
process_covid_csv_data("not a list of strings", targets = [{"header" : "string", "mode" : "latest", "extra" : None}], areaName = "string", csv = True),
process_covid_csv_data("not a dictionary", targets = [{"header" : "string", "mode" : "latest", "extra" : None}], areaName = "string", csv = False))
        try:
            assert data == (None, None, None, None)
            file.write("SUCCESS | process_covid_csv_data successfully returns None when any of its arguments are of an invalid type | test_process_covid_csv_data\n")
        except:
            file.write("FAILURE | process_covid_csv_data fails to return None when any of its arguments are of an invalid type | test_process_covid_csv_data\n")

        data = process_covid_csv_data(parse_csv_data("nation_2021-10-28.csv"), targets = [{"header" : "non-existant-header", "mode" : "latest", "extra" : None}, {"header" : "hospitalCases", "mode" : "sum", "extra" : 7}, {"header" : "newCasesBySpecimenDate", "mode" : "sum", "extra" : 7}, {"header" : "newCasesBySpecimenDate", "mode" : "rate", "extra" : 7}, {"header" : "hospitalCases", "mode" : "latest", "extra" : None}, {"header" : "cumDailyNsoDeathsByDeathDate", "mode" : "latest", "extra" : None}, {"header" : "cumDailyNsoDeathsByDeathDate", "mode" : "latestUpdate", "extra" : None}])
        try:
            assert type(data) == dict
            file.write("SUCCESS | process_covid_csv_data successfully returns a dictionay when given valid arguments | test_process_covid_csv_data\n")
            try:
                assert list(data.keys()) == ["latest_non-existant-header", "sum_last7days_hospitalCases", "sum_last7days_newCasesBySpecimenDate", "rate_last7days_newCasesBySpecimenDate", "latest_hospitalCases", "latest_cumDailyNsoDeathsByDeathDate", "latestUpdate_cumDailyNsoDeathsByDeathDate"]
                file.write("SUCCESS | process_covid_csv_data successfully returns a unique element for each unique target, keyed to by a string derived from the target | test_process_covid_csv_data\n")
            except:
                file.write("FAILURE | process_covid_csv_data fails to return a unique element for each unique target, keyed to by a string derived from the target | test_process_covid_csv_data\n")
            try:
                assert data["latest_non-existant-header"] == None
                file.write("SUCCESS | process_covid_csv_data successfully returns None for the value of a target that is of valid format but fails to produce any results | test_process_covid_csv_data\n")
            except:
                file.write("FAILURE | process_covid_csv_data fails to return None for the value of a target that is of valid format but fails to produce any results | test_process_covid_csv_data\n")
            try:
                assert data["latest_hospitalCases"] == "7019"
                file.write("SUCCESS | process_covid_csv_data successfully returns the correct value when asked to find the latest value for a given category | test_process_covid_csv_data\n")
            except:
                file.write("FAILURE | process_covid_csv_data fails to return the correct value when asked to find the latest value for a given category | test_process_covid_csv_data\n")
            try:
                assert data["latest_cumDailyNsoDeathsByDeathDate"] == "141544"
                file.write("SUCCESS | process_covid_csv_data successfully ignores any empty strings found in a search | test_process_covid_csv_data\n")
            except:
                file.write("FAILURE | process_covid_csv_data fails to ignore any empty strings found in a search | test_process_covid_csv_data\n")
            try:
                assert data["sum_last7days_hospitalCases"] == "46960"
                file.write("SUCCESS | process_covid_csv_data successfully returns the correct value when asked to sum the last n days of a given category | test_process_covid_csv_data\n")
            except:
                file.write("FAILURE | process_covid_csv_data fails to return the correct value when asked to sum the last n days of a given category | test_process_covid_csv_data\n")
            try:
                assert data["sum_last7days_newCasesBySpecimenDate"] == "240299"
                file.write("SUCCESS | process_covid_csv_data successfully ignores the first non empty element in any search targetting the category newCasesBySpecimenDate | test_process_covid_csv_data\n")
            except:
                file.write("FAILURE | process_covid_csv_data fails to ignore the first non empty element in any search targetting the category newCasesBySpecimenDate | test_process_covid_csv_data\n")
            try:
                assert data["rate_last7days_newCasesBySpecimenDate"] == str(240299 / 7)
                file.write("SUCCESS | process_covid_csv_data successfully returns the correct value when asked to find the rate of the last n days of a given category | test_process_covid_csv_data\n")
            except:
                file.write("FAILURE | process_covid_csv_data fails to return the correct value when asked to find the rate of the last n days of a given category | test_process_covid_csv_data\n")
            try:
                assert data["latestUpdate_cumDailyNsoDeathsByDeathDate"] == "2021-10-15"
                file.write("SUCCESS | process_covid_csv_data successfully returns the correct value when asked to find the date of the latest update to a given category | test_process_covid_csv_data\n")
            except:
                file.write("FAILURE | process_covid_csv_data fails to return the correct value when asked to find the date of the latest update to a given category | test_process_covid_csv_data\n")
        except:
            file.write("FAILURE | process_covid_csv_data fails to return a dictionay when given valid arguments | test_process_covid_csv_data\n")

        data2 = process_covid_csv_data(parse_csv_data2(parse_csv_data("nation_2021-10-28.csv")), targets = [{"header" : "non-existant-header", "mode" : "latest", "extra" : None}, {"header" : "hospitalCases", "mode" : "sum", "extra" : 7}, {"header" : "newCasesBySpecimenDate", "mode" : "sum", "extra" : 7}, {"header" : "newCasesBySpecimenDate", "mode" : "rate", "extra" : 7}, {"header" : "hospitalCases", "mode" : "latest", "extra" : None}, {"header" : "cumDailyNsoDeathsByDeathDate", "mode" : "latest", "extra" : None}, {"header" : "cumDailyNsoDeathsByDeathDate", "mode" : "latestUpdate", "extra" : None}], csv = False)
        try:
            assert data2 == data
            file.write("SUCCESS | process_covid_csv_data successfully takes covid_csv_data to be of a manner returned by parse_csv_data2 or parse_csv_data as determined by csv | test_process_covid_csv_data\n")
        except:
            file.write("FAILURE | process_covid_csv_data fails to take covid_csv_data to be of a manner returned by parse_csv_data2 or parse_csv_data as determined by csv | test_process_covid_csv_data\n")

        data2 = process_covid_csv_data(parse_csv_data("nation_2021-10-28.csv"), targets = ["invalid target", {"invalid target" : "invalid target"}, {"header" : "non-existant-header", "mode" : "latest", "extra" : None}, {"header" : "hospitalCases", "mode" : "sum", "extra" : 7}, {"header" : "newCasesBySpecimenDate", "mode" : "sum", "extra" : 7}, {"header" : "newCasesBySpecimenDate", "mode" : "rate", "extra" : 7}, {"header" : "hospitalCases", "mode" : "latest", "extra" : None}, {"header" : "cumDailyNsoDeathsByDeathDate", "mode" : "latest", "extra" : None}, {"header" : "cumDailyNsoDeathsByDeathDate", "mode" : "latestUpdate", "extra" : None}])
        try:
            assert data2 == data
            file.write("SUCCESS | process_covid_csv_data is successfully unaffected by the presence of any invalid elements of targets | test_process_covid_csv_data\n")
        except:
            file.write("FAILURE | process_covid_csv_data fails to be unaffected by the presence of any invalid elements of targets | test_process_covid_csv_data\n")

        data2 = process_covid_csv_data(parse_csv_data("nation_2021-10-28.csv"), "unnecessary_argument", ["unnecessary_argument"], targets = [{"header" : "non-existant-header", "mode" : "latest", "extra" : None}, {"header" : "hospitalCases", "mode" : "sum", "extra" : 7}, {"header" : "newCasesBySpecimenDate", "mode" : "sum", "extra" : 7}, {"header" : "newCasesBySpecimenDate", "mode" : "rate", "extra" : 7}, {"header" : "hospitalCases", "mode" : "latest", "extra" : None}, {"header" : "cumDailyNsoDeathsByDeathDate", "mode" : "latest", "extra" : None}, {"header" : "cumDailyNsoDeathsByDeathDate", "mode" : "latestUpdate", "extra" : None}])
        try:
            assert data2 == data
            file.write("SUCCESS | process_covid_csv_data is successfully unaffected by the addition of unnecessary arguments | test_process_covid_csv_data\n")
        except:
            file.write("FAILURE | process_covid_csv_data fails to be unaffected by the addition of unnecessary arguments | test_process_covid_csv_data\n")

        data2 = process_covid_csv_data(parse_csv_data("nation_2021-10-28.csv"), argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument"], targets = [{"header" : "non-existant-header", "mode" : "latest", "extra" : None}, {"header" : "hospitalCases", "mode" : "sum", "extra" : 7}, {"header" : "newCasesBySpecimenDate", "mode" : "sum", "extra" : 7}, {"header" : "newCasesBySpecimenDate", "mode" : "rate", "extra" : 7}, {"header" : "hospitalCases", "mode" : "latest", "extra" : None}, {"header" : "cumDailyNsoDeathsByDeathDate", "mode" : "latest", "extra" : None}, {"header" : "cumDailyNsoDeathsByDeathDate", "mode" : "latestUpdate", "extra" : None}])
        try:
            assert data2 == data
            file.write("SUCCESS | process_covid_csv_data is successfully unaffected by the addition of unnecessary keyword arguments | test_process_covid_csv_data\n")
        except:
            file.write("FAILURE | process_covid_csv_data fails to be unaffected by the addition of unnecessary keyword arguments | test_process_covid_csv_data\n")

        file.write("\n")


def test_covid_API_request():
    if "filename" not in globals():
        filename = "results.txt"
    with open(filename, "a") as file:
        file.write("test_covid_API_request\n")

        try:
            assert covid_API_request() == covid_API_request("Exeter", "ltla", date = "2020-01-30", structure = {"areaCode": "areaCode", "areaType": "areaType", "date": "date", "cumDailyNsoDeathsByDeathDate": "cumDailyNsoDeathsByDeathDate", "hospitalCases": "hospitalCases", "newCasesBySpecimenDate": "newCasesBySpecimenDate"}, log = True)
            file.write("SUCCESS | covid_API_request successfully defaults | test_covid_API_request\n")
        except:
            file.write("FAILURE | covid_API_request fails to default | test_covid_API_request\n")

        data = covid_API_request("England", "Nation", date = "2020-01-30", structure = None)
        try:
            assert data == None
            file.write("SUCCESS | process_covid_csv_data successfully returns None when structure is not given | test_covid_API_request\n")
        except:
            file.write("FAILURE | process_covid_csv_data fails to return None when structure is not given | test_covid_API_request\n")

        data = covid_API_request()
        try:
            assert type(data) == dict
            file.write("SUCCESS | covid_API_request successfully returns a dictionay when given valid arguments | test_covid_API_request\n")
            try:
                assert list(data.keys()) == ["Exeter"]
                file.write("SUCCESS | covid_API_request successfully returns a nested dictionary of the expected format when given valid arguments | test_covid_API_request\n")
                for a in range(len(list(data["Exeter"].keys()))):
                    try:
                        assert list(data["Exeter"][list(data["Exeter"].keys())[a]].keys()) == ["areaCode", "areaType", "cumDailyNsoDeathsByDeathDate", "hospitalCases", "newCasesBySpecimenDate"]
                        if a == len(list(data["Exeter"].keys())) - 1:
                            file.write("SUCCESS | covid_API_request successfully returns the values of the given covid_csv_data keyed to by the substring in the matching header index | covid_API_request\n")
                    except:
                        file.write("FAILURE | covid_API_request fails to return the values of the given covid_csv_data keyed to by the substring in the matching header index | covid_API_request\n")
            except:
                file.write("FAILURE | covid_API_request fails to return a nested dictionary of the expected format when given valid arguments | test_covid_API_request\n")
        except:
            file.write("FAILURE | covid_API_request fails to return a dictionay when given valid arguments | test_covid_API_request\n")

        data2 = covid_API_request("Exeter", "ltla", "unnecessary_argument", ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | covid_API_request is successfully unaffected by the addition of unnecessary arguments | test_covid_API_request\n")
        except:
            file.write("FAILURE | covid_API_request fails to be unaffected by the addition of unnecessary arguments | test_covid_API_request\n")

        data2 = covid_API_request("Exeter", "ltla", argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | covid_API_request is successfully unaffected by the addition of unnecessary keyword arguments | test_covid_API_request\n")
        except:
            file.write("FAILURE | covid_API_request fails to be unaffected by the addition of unnecessary keyword arguments | test_covid_API_request\n")

        file.write("\n")


def test_csv_writeup():
    if "filename" not in globals():
        filename = "results.txt"
    if "tests_csv" not in globals():
        tests_csv = "tests.csv"
    with open(filename, "a") as file:
        file.write("test_csv_writeup\n")

        try:
            assert csv_writeup() == csv_writeup(None, None, True)
            file.write("SUCCESS | csv_writeup successfully defaults | test_csv_writeup\n")
        except:
            file.write("FAILURE | csv_writeup fails to default | test_csv_writeup\n")

        data = (csv_writeup(tests_csv, None), csv_writeup(None, parse_csv_data2(parse_csv_data("nation_2021-10-28.csv"))))
        try:
            assert data == (None, None)
            file.write("SUCCESS | csv_writeup successfully returns None when any of its arguments are missing | test_csv_writeup\n")
        except:
            file.write("FAILURE | csv_writeup fails to return None when any of its arguments are missing | test_csv_writeup\n")

        data = (csv_writeup(tests_csv, {"areaName" : {"date" : {"invalid key" : "value"}}}),
csv_writeup(tests_csv, {"areaName" : {"date" : "not a dictionary"}}),
csv_writeup(tests_csv, {"areaName" : "not a dictionary"}),
csv_writeup("invalid extension", parse_csv_data2(parse_csv_data("nation_2021-10-28.csv"))))
        try:
            assert data == (None, None, None, None)
            file.write("SUCCESS | csv_writeup successfully returns None when any of its arguments are of an invalid type or format | test_csv_writeup\n")
        except:
            file.write("FAILURE | csv_writeup fails to return None when any of its arguments are of an invalid type or format | test_csv_writeup\n")

        data = csv_writeup(tests_csv, parse_csv_data2(parse_csv_data("nation_2021-10-28.csv")))
        try:
            assert data == True
            file.write("SUCCESS | csv_writeup successfully completes when given valid arguments | test_csv_writeup\n")
        except:
            file.write("FAILURE | csv_writeup fails to complete when given valid arguments | test_csv_writeup\n")

        data2 = csv_writeup(tests_csv, parse_csv_data2(parse_csv_data("nation_2021-10-28.csv")), "unnecessary_argument", ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | csv_writeup is successfully unaffected by the addition of unnecessary arguments | test_csv_writeup\n")
        except:
            file.write("FAILURE | csv_writeup fails to be unaffected by the addition of unnecessary arguments | test_csv_writeup\n")

        data2 = csv_writeup(tests_csv, parse_csv_data2(parse_csv_data("nation_2021-10-28.csv")), argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | csv_writeup is successfully unaffected by the addition of unnecessary keyword arguments | test_csv_writeup\n")
        except:
            file.write("FAILURE | csv_writeup fails to be unaffected by the addition of unnecessary keyword arguments | test_csv_writeup\n")

        data = parse_csv_data2(parse_csv_data("nation_2021-10-28.csv"))
        csv_writeup(tests_csv, data)
        data2 = parse_csv_data2(parse_csv_data(tests_csv))
        try:
            assert data2 == data
            file.write("SUCCESS | csv_writeup successfully writes to a csv file in a manner that can be interpretted by parse_csv_data and parse_csv_data2 | test_csv_writeup\n")
        except:
            file.write("FAILURE | csv_writeup fails to write to a csv file in a manner that can be interpretted by parse_csv_data and parse_csv_data2 | test_csv_writeup\n")

        file.write("\n")


def test_csv_update():
    if "filename" not in globals():
        filename = "results.txt"
    if "tests_csv" not in globals():
        tests_csv = "tests.csv"
    with open(filename, "a") as file:
        file.write("test_csv_update\n")

        try:
            assert csv_update() == csv_update(None, "England", "nation", True)
            file.write("SUCCESS | csv_update successfully defaults | test_csv_update\n")
        except:
            file.write("FAILURE | csv_update fails to default | test_csv_update\n")

        csv_writeup(tests_csv, parse_csv_data2(parse_csv_data("nation_2021-10-28.csv")))
        current = parse_csv_data(tests_csv)

        data = csv_update()
        try:
            assert data == None
            file.write("SUCCESS | csv_update successfully returns None when no arguments are given | test_csv_update\n")
        except:
            file.write("FAILURE | csv_update fails to return None when no arguments are given | test_csv_update\n")

        data = csv_update("no file extension")
        try:
            assert data == None
            file.write("SUCCESS | csv_update successfully returns None when given a csv_filename not ending in '.csv' | test_csv_update\n")
        except:
            file.write("FAILURE | csv_update fails to return None when given a csv_filename not ending in '.csv' | test_csv_update\n")

        data = csv_update(tests_csv)
        try:
            assert data == True
            file.write("SUCCESS | csv_update successfully completes when all arguments are given correctly | test_csv_update\n")
        except:
            file.write("FAILURE | csv_update fails to complete when all arguments are given correctly | test_csv_update\n")
        try:
            assert data != current
            file.write("SUCCESS | csv_update successfully rewrites the given csv file | test_csv_update\n")
        except:
            file.write("FAILURE | csv_update fails to rewrite the given csv file | test_csv_update\n")

        data2 = csv_update(tests_csv, "England", "nation", "unnecessary_argument", ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | csv_update is successfully unaffected by the addition of unnecessary arguments | test_csv_update\n")
        except:
            file.write("FAILURE | csv_update fails to be unaffected by the addition of unnecessary arguments | test_csv_update\n")

        data2 = csv_update(tests_csv, argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | csv_update is successfully unaffected by the addition of unnecessary keyword arguments | test_csv_update\n")
        except:
            file.write("FAILURE | csv_update fails to be unaffected by the addition of unnecessary keyword arguments | test_csv_update\n")

        file.write("\n")


def test_covid_update():
    if "filename" not in globals():
        filename = "results.txt"
    if "tests_csv" not in globals():
        tests_csv = "tests.csv"
    with open(filename, "a") as file:
        file.write("test_covid_update\n")

        csv_writeup(tests_csv, parse_csv_data2(parse_csv_data("nation_2021-10-28.csv")))
        current = parse_csv_data(tests_csv)

        covid_data_handler.local_7day_infections = "N/A"
        covid_data_handler.national_7day_infections = "N/A"
        covid_data_handler.hospital_cases = "N/A"
        covid_data_handler.deaths_total = "N/A"
        covid_data_handler.updates = [{"time" : 0, "time2" : "23:59", "type" : False, "title" : "update_name", "content" : "update content", "event" : None, "repeat" : False}]

        try:
            assert covid_update() == covid_update(None, True)
            file.write("SUCCESS | covid_update successfully defaults | test_covid_update\n")
        except:
            file.write("FAILURE | covid_update fails to default | test_covid_update\n")

        data = covid_update("update_name")
        try:
            assert covid_data_handler.updates == []
            file.write("SUCCESS | covid_update successfully removes its associated update from the global updates when called | test_covid_update\n")
        except:
            file.write("FAILURE | covid_update fails to remove its associated update from the global updates when called | test_covid_update\n")
        try:
            assert data == True
            file.write("SUCCESS | covid_update successfully completes when all arguments are given correctly | test_covid_update\n")
        except:
            file.write("FAILURE | covid_update fails to complete when all arguments are given correctly | test_covid_update\n")
        try:
            assert covid_data_handler.local_7day_infections != "N/A"
            assert covid_data_handler.national_7day_infections != "N/A"
            assert covid_data_handler.hospital_cases != "N/A"
            assert covid_data_handler.deaths_total != "N/A"
            file.write("SUCCESS | covid_update successfully updates the globally held covid statistics | test_covid_update\n")
        except:
            file.write("FAILURE | covid_update fails to update the globally held covid statistics | test_covid_update\n")

        data2 = covid_update("update_name", "unnecessary_argument", ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | covid_update is successfully unaffected by the addition of unnecessary arguments | test_covid_update\n")
        except:
            file.write("FAILURE | covid_update fails to be unaffected by the addition of unnecessary arguments | test_covid_update\n")

        data2 = covid_update("update_name", argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | covid_update is successfully unaffected by the addition of unnecessary keyword arguments | test_covid_update\n")
        except:
            file.write("FAILURE | covid_update fails to be unaffected by the addition of unnecessary keyword arguments | test_covid_update\n")

        covid_data_handler.updates = [{"time" : 0, "time2" : "23:59", "type" : False, "title" : "update_name", "content" : "update content", "event" : None, "repeat" : True}]
        data = covid_update("update_name")
        try:
            assert covid_data_handler.updates[0]["title"] == "update_name"
            file.write("SUCCESS | covid_update successfully reschedules itself if meant to repeat | test_covid_update\n")
            try:
                assert len(covid_data_handler.schedule.queue) != 0
                file.write("SUCCESS | covid_update successfully reschedules itself with the global schedule if meant to be repeat | test_covid_update\n")
                covid_data_handler.schedule.cancel(covid_data_handler.updates[0]["event"])
            except:
                file.write("FAILURE | covid_update fails to reschedule itself with the global schedule if meant to be repeat | test_covid_update\n")
        except:
            file.write("FAILURE | covid_update fails to reschedule itself if meant to repeat | test_covid_update\n")
        covid_data_handler.updates = []

        covid_data_handler.csv_filename = tests_csv
        covid_update()
        data = parse_csv_data(tests_csv)
        try:
            assert data != current
            file.write("SUCCESS | covid_update successfully rewrites the global csv file | test_covid_update\n")
        except:
            file.write("FAILURE | covid_update fails to rewrite the global csv file | test_covid_update\n")

        file.write("\n")


def test_schedule_covid_updates():
    if "filename" not in globals():
        filename = "results.txt"
    with open(filename, "a") as file:
        file.write("test_schedule_covid_updates\n")

        covid_data_handler.updates = []

        try:
            assert schedule_covid_updates() == schedule_covid_updates(None, None, repeat = False, log = True)
            file.write("SUCCESS | schedule_covid_updates successfully defaults | test_schedule_covid_updates\n")
        except:
            file.write("FAILURE | schedule_covid_updates fails to default | test_schedule_covid_updates\n")

        data = (schedule_covid_updates("23:59", "update_name", repeat = None), schedule_covid_updates("23:59", None), schedule_covid_updates(None, "update_name"))
        try:
            assert data == (None, None, None)
            file.write("SUCCESS | schedule_covid_updates successfully returns None when any of its arguments are missing | test_schedule_covid_updates\n")
        except:
            file.write("FAILURE | schedule_covid_updates fails to return None when any of its arguments are missing | test_schedule_covid_updates\n")

        data = schedule_covid_updates("invalid time", "update_name")
        try:
            assert data == None
            file.write("SUCCESS | schedule_covid_updates successfully returns None when time is given in an invalid format | test_schedule_covid_updates\n")
        except:
            file.write("FAILURE | schedule_covid_updates fails to return None when time is given in an invalid format | test_schedule_covid_updates\n")

        data = schedule_covid_updates("23:59", "update_name")
        try:
            assert data == True
            file.write("SUCCESS | schedule_covid_updates successfully completes when all arguments are given correctly | test_schedule_covid_updates\n")
            try:
                assert covid_data_handler.updates[0]["title"] == "update_name"
                file.write("SUCCESS | schedule_covid_updates successfully schedules covid_update to run | test_schedule_covid_updates\n")
                try:
                    assert len(covid_data_handler.schedule.queue) != 0
                    file.write("SUCCESS | schedule_covid_updates successfully schedules covid_update to run with the global schedule | test_schedule_covid_updates\n")
                    covid_data_handler.schedule.cancel(covid_data_handler.updates[0]["event"])
                except:
                    file.write("FAILURE | schedule_covid_updates fails to schedule covid_update to run with the global schedule | test_schedule_covid_updates\n")
            except:
                file.write("FAILURE | schedule_covid_updates fails to schedule covid_update to run | test_schedule_covid_updates\n")
        except:
            file.write("FAILURE | schedule_covid_updates fails to complete when all arguments are given correctly | test_schedule_covid_updates\n")

        covid_data_handler.updates = [{"time" : 0, "time2" : "23:59", "type" : False, "title" : "update_name", "content" : "update content", "event" : None, "repeat" : False}]
        data = schedule_covid_updates("23:59", "update_name")
        try:
            assert data == True
            file.write("SUCCESS | schedule_covid_updates successfully completes even when a repeat update_name is used | test_schedule_covid_updates\n")
            covid_data_handler.schedule.cancel(covid_data_handler.updates[1]["event"])
            try:
                assert covid_data_handler.updates[1]["title"] == "update_name (1)"
                file.write("SUCCESS | schedule_covid_updates successfully modifies update_name to ensure uniqueness | test_schedule_covid_updates\n")
            except:
                file.write("FAILURE | schedule_covid_updates fails to modify update_name to ensure uniqueness | test_schedule_covid_updates\n")
        except:
            file.write("FAILURE | schedule_covid_updates fails to complete when a repeat update_name is used | test_schedule_covid_updates\n")

        covid_data_handler.updates = []
        data2 = schedule_covid_updates("23:59", "update_name", "unnecessary_argument", ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | schedule_covid_updates is successfully unaffected by the addition of unnecessary arguments | test_schedule_covid_updates\n")
            covid_data_handler.schedule.cancel(covid_data_handler.updates[0]["event"])
        except:
            file.write("FAILURE | schedule_covid_updates fails to be unaffected by the addition of unnecessary arguments | test_schedule_covid_updates\n")

        covid_data_handler.updates = []
        data2 = schedule_covid_updates("23:59", "update_name", argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | schedule_covid_updates is successfully unaffected by the addition of unnecessary keyword arguments | test_schedule_covid_updates\n")
            covid_data_handler.schedule.cancel(covid_data_handler.updates[0]["event"])
        except:
            file.write("FAILURE | schedule_covid_updates fails to be unaffected by the addition of unnecessary keyword arguments | test_schedule_covid_updates\n")

        covid_data_handler.updates = []

        file.write("\n")
    

def test_news_API_request():
    if "filename" not in globals():
        filename = "results.txt"
    with open(filename, "a") as file:
        file.write("test_news_API_request\n")

        covid_news_handling.remove = {}
        covid_news_handling.news = []
        covid_news_handling.API_key = json_read()["API_key"]
        covid_news_handling.updates = [{"time" : 0, "time2" : "23:59", "type" : True, "title" : "update_name", "content" : "update content", "event" : None, "repeat" : False}]

        data = news_API_request()
        covid_news_handling.remove = {}
        data2 = news_API_request("Covid COVID-19 coronavirus", update_name = None, log = True)
        try:
            assert data == data2
            file.write("SUCCESS | news_API_request successfully defaults | test_news_API_request\n")
        except:
            file.write("FAILURE | news_API_request fails to default | test_news_API_request\n")

        covid_news_handling.remove = {}

        data = news_API_request(None)
        try:
            assert data == None
            file.write("SUCCESS | news_API_request successfully returns None when given no arguments | test_news_API_request\n")
        except:
            file.write("FAILURE | news_API_request fails to return None when given no arguments | test_news_API_request\n")

        covid_news_handling.remove = {}

        data = news_API_request(update_name = "update_name")
        try:
            assert covid_news_handling.updates == []
            file.write("SUCCESS | news_API_request successfully removes its associated update from the global updates when called | test_news_API_request\n")
        except:
            file.write("FAILURE | news_API_request fails to remove its associated update from the global updates when called | test_news_API_request\n")
        try:
            assert data == True
            file.write("SUCCESS | news_API_request successfully completes when all arguments are given correctly | test_news_API_request\n")
        except:
            file.write("FAILURE | news_API_request fails to complete when all arguments are given correctly | test_news_API_request\n")
        try:
            assert covid_news_handling.remove != {}
            assert covid_news_handling.news != []
            file.write("SUCCESS | news_API_request successfully updates the globally held news data | test_news_API_request\n")
        except:
            file.write("FAILURE | news_API_request fails to update the globally held news data | test_news_API_request\n")
    
        covid_news_handling.remove = {}
    
        data2 = news_API_request("Covid COVID-19 coronavirus", "update_name", "unnecessary_argument", ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | news_API_request is successfully unaffected by the addition of unnecessary arguments | test_news_API_request\n")
        except:
            file.write("FAILURE | news_API_request fails to be unaffected by the addition of unnecessary arguments | test_news_API_request\n")

        covid_news_handling.remove = {}

        data2 = news_API_request(update_name = "update_name", argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | news_API_request is successfully unaffected by the addition of unnecessary keyword arguments | test_news_API_request\n")
        except:
            file.write("FAILURE | news_API_request fails to be unaffected by the addition of unnecessary keyword arguments | test_news_API_request\n")

        covid_news_handling.remove = {}

        covid_news_handling.updates = [{"time" : 0, "time2" : "23:59", "type" : True, "title" : "update_name", "content" : "update content", "event" : None, "repeat" : True}]
        data = news_API_request(update_name = "update_name")
        try:
            assert covid_news_handling.updates[0]["title"] == "update_name"
            file.write("SUCCESS | news_API_request successfully reschedules itself if meant to repeat | test_news_API_request\n")
            try:
                assert len(covid_news_handling.schedule.queue) != 0
                file.write("SUCCESS | news_API_request successfully reschedules itself with the global schedule if meant to be repeat | test_news_API_request\n")
                covid_news_handling.schedule.cancel(covid_news_handling.updates[0]["event"])
            except:
                file.write("FAILURE | news_API_request fails to reschedule itself with the global schedule if meant to be repeat | test_news_API_request\n")
        except:
            file.write("FAILURE | news_API_request fails to reschedule itself if meant to repeat | test_news_API_request\n")
        covid_news_handling.updates = []
        covid_news_handling.remove = {}

        file.write("\n")


def test_update_news():
    if "filename" not in globals():
        filename = "results.txt"
    with open(filename, "a") as file:
        file.write("test_update_news\n")

        covid_news_handling.updates = []

        try:
            assert update_news() == update_news(None, None, repeat = False, log = True)
            file.write("SUCCESS | update_news successfully defaults | test_update_news\n")
        except:
            file.write("FAILURE | update_news fails to default | test_update_news\n")

        data = (update_news("23:59", "update_name", repeat = None), update_news("23:59", None), update_news(None, "update_name"))
        try:
            assert data == (None, None, None)
            file.write("SUCCESS | update_news successfully returns None when any of its arguments are missing | test_update_news\n")
        except:
            file.write("FAILURE | update_news fails to return None when any of its arguments are missing | test_update_news\n")

        data = update_news("invalid time", "update_name")
        try:
            assert data == None
            file.write("SUCCESS | update_news successfully returns None when time is given in an invalid format | test_update_news\n")
        except:
            file.write("FAILURE | update_news fails to return None when time is given in an invalid format | test_update_news\n")

        data = update_news("23:59", "update_name")
        try:
            assert data == True
            file.write("SUCCESS | update_news successfully completes when all arguments are given correctly | test_update_news\n")
            try:
                assert covid_news_handling.updates[0]["title"] == "update_name"
                file.write("SUCCESS | update_news successfully schedules news_API_request to run | test_update_news\n")
                try:
                    assert len(covid_news_handling.schedule.queue) != 0
                    file.write("SUCCESS | update_news successfully schedules news_API_request to run with the global schedule | test_update_news\n")
                    covid_news_handling.schedule.cancel(covid_news_handling.updates[0]["event"])
                except:
                    file.write("FAILURE | update_news fails to schedule news_API_request to run with the global schedule | test_update_news\n")
            except:
                file.write("FAILURE | update_news fails to schedule news_API_request to run | update_news\n")
        except:
            file.write("FAILURE | update_news fails to complete when all arguments are given correctly | test_update_news\n")

        covid_news_handling.updates = [{"time" : 0, "time2" : "23:59", "type" : True, "title" : "update_name", "content" : "update content", "event" : None, "repeat" : False}]
        data = update_news("23:59", "update_name")
        try:
            assert data == True
            file.write("SUCCESS | update_news successfully completes even when a repeat update_name is used | test_update_news\n")
            covid_news_handling.schedule.cancel(covid_news_handling.updates[1]["event"])
            try:
                assert covid_news_handling.updates[1]["title"] == "update_name (1)"
                file.write("SUCCESS | update_news successfully modifies update_name to ensure uniqueness | test_update_news\n")
            except:
                file.write("FAILURE | update_news fails to modify update_name to ensure uniqueness | test_update_news\n")
        except:
            file.write("FAILURE | update_news fails to complete when a repeat update_name is used | test_update_news\n")

        covid_news_handling.updates = []
        data2 = update_news("23:59", "update_name", "unnecessary_argument", ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | update_news is successfully unaffected by the addition of unnecessary arguments | test_update_news\n")
            covid_news_handling.schedule.cancel(covid_news_handling.updates[0]["event"])
        except:
            file.write("FAILURE | update_news fails to be unaffected by the addition of unnecessary arguments | test_update_news\n")

        covid_news_handling.updates = []
        data2 = update_news("23:59", "update_name", argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | update_news is successfully unaffected by the addition of unnecessary keyword arguments | test_update_news\n")
            covid_news_handling.schedule.cancel(covid_news_handling.updates[0]["event"])
        except:
            file.write("FAILURE | update_news fails to be unaffected by the addition of unnecessary keyword arguments | test_update_news\n")

        covid_news_handling.updates = []

        file.write("\n")


def test_json_read():
    if "filename" not in globals():
        filename = "results.txt"
    if "test_config_json" not in globals():
        test_config_json = "test_config.json"
    with open(filename, "a") as file:
        file.write("test_json_read\n")

        json_write(test_config_json, {"log_level" : "DEBUG", "csv_filename": "covid.csv", "log_filename": "sys.log", "status_filename" : "status.json", "AreaName": "Exeter", "AreaType": "ltla", "API_key": ""})

        try:
            assert json_read() == json_read("config.json", False, True)
            file.write("SUCCESS | json_read successfully defaults | test_json_read\n")
        except:
            file.write("FAILURE | json_read fails to default | test_json_read\n")

        data = (json_read("config.json", None), json_read(None, False))
        try:
            assert data == (None, None)
            file.write("SUCCESS | json_read successfully returns None when any of its arguments are missing | test_json_read\n")
        except:
            file.write("FAILURE | json_read fails to return None when any of its arguments are missing | test_json_read\n")

        data = json_read("no file extension")
        try:
            assert data == None
            file.write("SUCCESS | json_read successfully returns None when given a json_filename not ending in '.json' | test_json_read\n")
        except:
            file.write("FAILURE | json_read fails to return None when given a json_filename not ending in '.json' | test_json_read\n")

        data = json_read("non_existant_file.json")
        try:
            assert data == None
            file.write("SUCCESS | json_read successfully returns None when given a json_filename that does not exist within the Covid19_Dashboard_pkg directory | test_json_read\n")
        except:
            file.write("FAILURE | json_read fails to return None when given a json_filename that does not exist within the Covid19_Dashboard_pkg directory | test_json_read\n")

        data = json_read("status.json")
        try:
            assert data == None
            file.write("SUCCESS | json_read successfully returns None when the keys read don't match those that would be expected for the indicated mode | test_json_read\n")
        except:
            file.write("FAILURE | json_read fails to return None when the keys read don't match those that would be expected for the indicated mode | test_json_read\n")

        data = json_read(test_config_json)
        try:
            assert type(data) == dict
            file.write("SUCCESS | json_read successfully returns a dictionary when given valid arguments | test_json_read\n")
            try:
                assert data == {"log_level" : "DEBUG", "csv_filename": "covid.csv", "log_filename": "sys.log", "status_filename" : "status.json", "AreaName": "Exeter", "AreaType": "ltla", "API_key": ""}
                file.write("SUCCESS | json_read successfully returns the contents of the json file if its keys matches the keys indicated by mode | test_json_read\n")
            except:
                file.write("FAILURE | json_read fails to return the contents of the json file if its keys matches the keys indicated by mode | test_json_read\n")
        except:
            file.write("FAILURE | json_read fails to return a list when given valid arguments | test_json_read\n")

        data2 = json_read(test_config_json, False, True, "unnecessary_argument", ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | json_read is successfully unaffected by the addition of unnecessary arguments | test_json_read\n")
        except:
            file.write("FAILURE | json_read fails to be unaffected by the addition of unnecessary arguments | test_json_read\n")

        data2 = json_read(test_config_json, argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | json_read is successfully unaffected by the addition of unnecessary keyword arguments | test_json_read\n")
        except:
            file.write("FAILURE | json_read fails to be unaffected by the addition of unnecessary keyword arguments | test_json_read\n")

        file.write("\n")


def test_json_write():
    if "filename" not in globals():
        filename = "results.txt"
    if "test_config_json" not in globals():
        test_config_json = "test_config.json"
    with open(filename, "a") as file:
        file.write("test_json_write\n")

        try:
            assert json_write() == json_write("config.json", {}, False, True)
            file.write("SUCCESS | json_write successfully defaults | json_write\n")
        except:
            file.write("FAILURE | json_write fails to default | json_write\n")

        data = (json_write("config.json", {}, None), json_write("config.json", None, False), json_write(None, {}, False))
        try:
            assert data == (None, None, None)
            file.write("SUCCESS | json_write successfully returns None when any of its arguments are missing | test_json_write\n")
        except:
            file.write("FAILURE | json_write fails to return None when any of its arguments are missing | test_json_write\n")

        data = (json_write("invalid file extension"), json_write(new_data = "not a dictionary"), json_write(mode = "not a boolean"))
        try:
            assert data == (None, None, None)
            file.write("SUCCESS | json_write successfully returns None when any of its arguments are of an invalid type or format | test_json_write\n")
        except:
            file.write("FAILURE | json_write fails to return None when any of its arguments are of an invalid type or format | test_json_write\n")

        data = json_write(new_data = {"invalid key" : "value"})
        try:
            assert data == None
            file.write("SUCCESS | json_write successfully returns None when the keys of new_data don't match those that would be expected for the indicated mode | test_json_write\n")
        except:
            file.write("FAILURE | json_write fails to return None when the keys of new_data don't match those that would be expected for the indicated mode | test_json_write\n")

        data = json_write(test_config_json, {"API_key" : "this is new"})
        try:
            assert data == True
            file.write("SUCCESS | json_write successfully completes when the keys of new_data match those that would be expected for the indicated mode | test_json_write\n")
            try:
                assert list(json_read(test_config_json).keys()) == ["log_level", "csv_filename", "log_filename", "status_filename", "AreaName", "AreaType", "API_key"]
                file.write("SUCCESS | json_write successfully preserves the structure of the given json file | test_json_write\n")
            except:
                file.write("FAILURE | json_write fails to preserve the structure of the given json file | test_json_write\n")
            try:
                assert json_read(test_config_json)["API_key"] == "this is new"
                file.write("SUCCESS | json_write successfully updates the desired key values | test_json_write\n")
                json_write(test_config_json, {"API_key" : ""})
            except:
                file.write("FAILURE | json_write fails to update the desired key values | test_json_write\n")
        except:
            file.write("FAILURE | json_write fails to complete when the keys of new_data match those that would be expected for the indicated mode | test_json_write\n")

        data = json_write("config.json", {}, False)

        data2 = json_write("config.json", {}, False, "unnecessary_argument", ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | json_write is successfully unaffected by the addition of unnecessary arguments | test_json_write\n")
        except:
            file.write("FAILURE | json_write fails to be unaffected by the addition of unnecessary arguments | test_json_write\n")

        data2 = json_write(argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | json_write is successfully unaffected by the addition of unnecessary keyword arguments | test_json_write\n")
        except:
            file.write("FAILURE | json_write fails to be unaffected by the addition of unnecessary keyword arguments | test_json_write\n")

        file.write("\n")


def test_reset_updates():
    if "filename" not in globals():
        filename = "results.txt"
    with open(filename, "a") as file:
        file.write("test_reset_updates\n")

        covid_data_handler.updates = [{"time" : 0, "time2" : "23:59", "type" : False, "title" : "update_name1", "content" : "update content", "event" : None, "repeat" : False}]
        covid_news_handling.updates = [{"time" : 0, "time2" : "23:59", "type" : True, "title" : "update_name2", "content" : "update content", "event" : None, "repeat" : False}]
        main.updates = []

        data = reset_updates()
        try:
            assert data == reset_updates(True)
            file.write("SUCCESS | reset_updates successfully defaults | test_reset_updates\n")
        except:
            file.write("FAILURE | reset_updates fails to default | test_reset_updates\n")

        try:
            assert data == True
            file.write("SUCCESS | reset_updates successfully completes | test_reset_updates\n")
            try:
                assert main.updates == [{"time" : 0, "time2" : "23:59", "type" : False, "title" : "update_name1", "content" : "update content", "event" : None, "repeat" : False}, {"time" : 0, "time2" : "23:59", "type" : True, "title" : "update_name2", "content" : "update content", "event" : None, "repeat" : False}]
                file.write("SUCCESS | reset_updates successfully adds those elements present in covid_data_handler.updates or covid_news_handling.updates to main.updates | test_reset_updates\n")
            except:
                file.write("FAILURE | reset_updates fails to add those elements present in covid_data_handler.updates or covid_news_handling.updates to main.updates | test_reset_updates\n")
            main.updates.append({"time" : 0, "time2" : "23:59", "type" : False, "title" : "update_name3", "content" : "update content", "event" : None, "repeat" : False})
            data = reset_updates()
            try:
                assert {"time" : 0, "time2" : "23:59", "type" : False, "title" : "update_name3", "content" : "update content", "event" : None, "repeat" : False} not in main.updates
                file.write("SUCCESS | reset_updates successfully removes those elements in main.updates not present in covid_data_handler.updates or covid_news_handling.updates | test_reset_updates\n")
            except:
                file.write("FAILURE | reset_updates fails to remove those elements in main.updates not present in covid_data_handler.updates or covid_news_handling.updates | test_reset_updates\n")
        except:
            file.write("FAILURE | reset_updates fails to complete | test_reset_updates\n")

        data2 = reset_updates("unnecessary_argument", ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | reset_updates is successfully unaffected by the addition of unnecessary arguments | test_reset_updates\n")
        except:
            file.write("FAILURE | reset_updates fails to be unaffected by the addition of unnecessary arguments | test_reset_updates\n")

        data2 = reset_updates(argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument\n"])
        try:
            assert data2 == data
            file.write("SUCCESS | reset_updates is successfully unaffected by the addition of unnecessary keyword arguments | test_reset_updates\n")
        except:
            file.write("FAILURE | reset_updates fails to be unaffected by the addition of unnecessary keyword arguments | test_reset_updates\n")

        file.write("\n")


def test_reset_news():
    if "filename" not in globals():
        filename = "results.txt"
    with open(filename, "a") as file:
        file.write("test_reset_news\n")

        covid_news_handling.news = [{"title" : "title", "content" : "content"}]
        covid_news_handling.remove = {"title" : "date"}
        covid_news_handling.date = "2021-12-04"
        main.news = None
        main.remove = None
        main.date = None

        data = reset_news()
        try:
            assert data == reset_news(True)
            file.write("SUCCESS | reset_news successfully defaults | test_reset_news\n")
        except:
            file.write("FAILURE | reset_news fails to default | test_reset_news\n")

        try:
            assert data == True
            file.write("SUCCESS | reset_news successfully completes | test_reset_news\n")
            try:
                assert main.news == [{"title" : "title", "content" : "content"}]
                file.write("SUCCESS | reset_news successfully updates the news of main to match that of covid_news_handling | test_reset_news\n")
            except:
                file.write("FAILURE | reset_news fails to update the news of main to match that of covid_news_handling | test_reset_news\n")
            try:
                assert main.remove == {"title" : "date"}
                file.write("SUCCESS | reset_news successfully updates the remove of main to match that of covid_news_handling | test_reset_news\n")
            except:
                file.write("FAILURE | reset_news fails to update the remove of main to match that of covid_news_handling | test_reset_news\n")
            try:
                assert main.date == "2021-12-04"
                file.write("SUCCESS | reset_news successfully updates the date of main to match that of covid_news_handling | test_reset_news\n")
            except:
                file.write("FAILURE | reset_news fails to update the date of main to match that of covid_news_handling | test_reset_news\n")
        except:
            file.write("FAILURE | reset_news fails to complete | test_reset_news\n")

        data2 = reset_news("unnecessary_argument", ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | reset_news is successfully unaffected by the addition of unnecessary arguments | test_reset_news\n")
        except:
            file.write("FAILURE | reset_news fails to be unaffected by the addition of unnecessary arguments | test_reset_news\n")

        data2 = reset_news(argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument\n"])
        try:
            assert data2 == data
            file.write("SUCCESS | reset_news is successfully unaffected by the addition of unnecessary keyword arguments | test_reset_news\n")
        except:
            file.write("FAILURE | reset_news fails to be unaffected by the addition of unnecessary keyword arguments | test_reset_news\n")

        file.write("\n")


def test_update_remove():
    if "filename" not in globals():
        filename = "results.txt"
    with open(filename, "a") as file:
        file.write("test_update_remove\n")

        import sched
        import time
        main.schedule = sched.scheduler(time.time, time.sleep)
        covid_data_handler.schedule = main.schedule
        covid_news_handling.schedule = main.schedule
        main.updates = []
        covid_data_handler.updates = []
        covid_news_handling.updates = []

        try:
            assert update_remove() == update_remove(None, True)
            file.write("SUCCESS | update_remove successfully defaults | test_update_remove\n")
        except:
            file.write("FAILURE | update_remove fails to default | test_update_remove\n")

        data = update_remove(None)
        try:
            assert data == None
            file.write("SUCCESS | update_remove successfully returns None when no arguments are given | test_update_remove\n")
        except:
            file.write("FAILURE | update_remove fails to return None when no arguments are given | test_update_remove\n")

        schedule_covid_updates("23:59", "update_name1")
        update_news("23:59", "update_name2")
        print(main.schedule.queue)
        data = (update_remove("update_name1"), update_remove("update_name2"))
        try:
            assert data == (True, True)
            file.write("SUCCESS | update_remove successfully completes when given valid arguments | test_update_remove\n")
            try:
                assert covid_data_handler.updates == []
                file.write("SUCCESS | update_remove successfully removes the specified element from the updates of covid_data_handler | test_update_remove\n")
            except:
                file.write("FAILURE | update_remove fails to remove the specified element from the updates of covid_data_handler | test_update_remove\n")
            try:
                assert covid_news_handling.updates == []
                file.write("SUCCESS | update_remove successfully removes the specified element from the updates of covid_news_handling | test_update_remove\n")
            except:
                file.write("FAILURE | update_remove fails to remove the specified element from the updates of covid_news_handling | test_update_remove\n")
            try:
                assert main.updates == []
                file.write("SUCCESS | update_remove successfully removes the specified element from the updates of main | test_update_remove\n")
            except:
                file.write("FAILURE | update_remove fails to remove the specified element from the updates of main | test_update_remove\n")
            try:
                assert main.schedule.empty() == True
                file.write("SUCCESS | update_remove successfully cancels the scheduled update(s) | test_update_remove\n")
            except:
                file.write("FAILURE | update_remove fails to cancel the scheduled update(s) | test_update_remove\n")
        except:
            file.write("FAILURE | update_remove fails to complete when given valid arguments | test_update_remove\n")

        schedule_covid_updates("23:59", "update_name1")
        update_news("23:59", "update_name2")
        data2 = (update_remove("update_name1", "unnecessary_argument", ["unnecessary_argument"]), update_remove("update_name2", "unnecessary_argument", ["unnecessary_argument"]))
        try:
            assert data2 == data
            file.write("SUCCESS | update_remove is successfully unaffected by the addition of unnecessary arguments | test_update_remove\n")
        except:
            file.write("FAILURE | update_remove fails to be unaffected by the addition of unnecessary arguments | test_update_remove\n")

        schedule_covid_updates("23:59", "update_name1")
        update_news("23:59", "update_name2")
        data2 = (update_remove("update_name1", argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument"]), update_remove("update_name2", argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument"]))
        try:
            assert data2 == data
            file.write("SUCCESS | update_remove is successfully unaffected by the addition of unnecessary keyword arguments | test_update_remove\n")
        except:
            file.write("FAILURE | update_remove fails to be unaffected by the addition of unnecessary keyword arguments | test_update_remove\n")

        file.write("\n")


def test_news_remove():
    if "filename" not in globals():
        filename = "results.txt"
    with open(filename, "a") as file:
        file.write("test_news_remove\n")

        covid_news_handling.news = {"title" : "title", "content" : "content"}

        try:
            assert news_remove() == news_remove(None, True)
            file.write("SUCCESS | news_remove successfully defaults | test_news_remove\n")
        except:
            file.write("FAILURE | news_remove fails to default | test_news_remove\n")

        data = news_remove(None)
        try:
            assert data == None
            file.write("SUCCESS | news_remove successfully returns None when no arguments are given | test_news_remove\n")
        except:
            file.write("FAILURE | news_remove fails to return None when no arguments are given | test_news_remove\n")

        data = news_remove("title")
        try:
            assert data == True
            file.write("SUCCESS | news_remove successfully completes when given valid arguments | test_news_remove\n")
            try:
                assert main.news == []
                file.write("SUCCESS | news_remove successfully removes the specified element from the news of main | test_news_remove\n")
            except:
                file.write("FAILURE | news_remove fails to remove the specified element from the news of main | test_news_remove\n")
        except:
            file.write("FAILURE | news_remove fails to complete when given valid arguments | test_news_remove\n")

        covid_news_handling.news = {"title" : "title", "content" : "content"}
        data2 = news_remove("title", "unnecessary_argument", ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | news_remove is successfully unaffected by the addition of unnecessary arguments | test_news_remove\n")
        except:
            file.write("FAILURE | news_remove fails to be unaffected by the addition of unnecessary arguments | test_news_remove\n")

        covid_news_handling.news = {"title" : "title", "content" : "content"}
        data2 = news_remove("title", argument1 = "unnecessary_argument", argument2 = ["unnecessary_argument"])
        try:
            assert data2 == data
            file.write("SUCCESS | news_remove is successfully unaffected by the addition of unnecessary keyword arguments | test_news_remove\n")
        except:
            file.write("FAILURE | news_remove fails to be unaffected by the addition of unnecessary keyword arguments | test_news_remove\n")

        file.write("\n")


test_parse_csv_data()
test_parse_csv_data2()
test_subprocess_covid_csv_data()
test_process_covid_csv_data()
test_covid_API_request()
test_csv_writeup()
test_csv_update()
test_covid_update()
test_schedule_covid_updates()

test_news_API_request()
test_update_news()

test_json_read()
test_json_write()
test_reset_updates()
test_reset_news()
test_update_remove()
test_news_remove()
