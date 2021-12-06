'''a module for combining the covid_news_handling and covid_data_handler modules'''

def json_read(json_filename : str = "config.json", mode : bool = False, log = True, *args, **kwargs) -> dict:
    '''a function to read from a json file'''

    if type(log) != bool:
        log = True
    if log:
        log = "logging" in globals() and "logger" in globals()
        if not log:
            print("WARNING | unable to log | json_read")
    #verify if logging is enabled

    if log: logger.debug("DEBUG | json_read called successfully | json_read")
    else: print("DEBUG | json_read called successfully | json_read")

    global isfile
    if "isfile" not in globals():
        if log: logger.warning("WARNING | isfile not imported | json_read")
        else: print("WARNING | isfile not imported | json_read")
        try:
            from os.path import isfile
        except:
            if log: logger.critical("CRITICAL | os.path not in system path | json_read")
            else: print("CRITICAL | os.path not in system path | json_read")
            return None
    global json
    if "json" not in globals():
        if log: logger.warning("WARNING | json not imported | json_read")
        else: print("WARNING | json not imported | json_read")
        try:
            import json
        except:
            if log: logger.critical("CRITICAL | json not in system path | json_read")
            else: print("CRITICAL | json not in system path | json_read")
            return None
    #verify if necessary functions are present

    json_filename = str(json_filename)
    if json_filename[-5:] != ".json":
        if log: logger.warning("WARNING | invalid file extension | json_read")
        else: print("WARNING | invalid file extension | json_read")
        return None
    if not isfile(json_filename):
        if log: logger.warning("WARNING | config file does not exist | json_read")
        else: print("WARNING | config file does not exist | json_read")
        return None
    if type(mode) != bool:
        if log: logger.warning("WARNING | invalid type for mode | json_read")
        else: print("WARNING | invalid type for mode | json_read")
        return None
    if len(args) > 0:
        if log: logger.info("INFO | too many non-keyword arguements | json_read")
        else: print("INFO | too many non-keyword arguements | json_read")
    if len(kwargs) > 0:
        if log: logger.info("INFO | unexpected keyword arguments | json_read")
        else: print("INFO | unexpected keyword arguments | json_read")
    #verify given arguements

    with open(json_filename, "r") as f:
        data = f.read()
    #read data from file
    try:
        data = json.loads(data)
    except:
        if log: logger.warning("WARNING | invalid format for data | json_read")
        else: print("WARNING | invalid format for data | json_read")
        return None
    #attempt to convert data into a dictionary
    if list(data.keys()) != [["log_level", "csv_filename", "log_filename", "status_filename", "AreaName", "AreaType", "API_key"], ["local_7day_infections", "national_7day_infections", "hospital_cases", "deaths_total", "updates", "remove", "news"]][mode]:
        if log: logger.warning("WARNING | invalid format for data | json_read")
        else: print("WARNING | invalid format for data | json_read")
        return None
    #validate the keys of data
    for item in list(data.keys()):
        if (item == "remove" and type(data[item]) != dict) or (item in ["updates", "news"] and type(data[item]) != list) or (item not in ["updates", "remove", "news"] and type(data[item]) != str):
            if log: logger.warning('WARNING | invalid type for data["' + item + '"] | json_read')
            else: print('WARNING | invalid type for data["' + item + '"] | json_read')
            return None
    #validate the type of individual values of data
    if log: logger.debug("DEBUG | json_read successfully completed | json_read")
    else: print("DEBUG | json_read successfully completed | json_read")
    return data


def json_write(json_filename : str = "config.json", new_data : dict = {}, mode : bool = False, log : bool = True, *args, **kwargs) -> None:
    '''a function to write to a json file'''

    if type(log) != bool:
        log = True
    if log:
        log = "logging" in globals() and "logger" in globals()
        if not log:
            print("WARNING | unable to log | json_write")
    #verify if logging is enabled

    if log: logger.debug("DEBUG | json_write called successfully | json_write")
    else: print("DEBUG | json_write called successfully | json_write")

    global json
    if "json" not in globals():
        if log: logger.warning("WARNING | json not imported | json_write")
        else: print("WARNING | json not imported | json_write")
        try:
            import json
        except:
            if log: logger.critical("CRITICAL | json not in system path | json_write")
            else: print("CRITICAL | json not in system path | json_write")
            return None
    global json_read
    if "json_read" not in globals():
        if log: logger.warning("WARNING | json_read not imported | json_write")
        else: print("WARNING | json_read not imported | json_write")
        try:
            from startup import json_read
        except:
            if log: logger.critical("CRITICAL | startup not in system path | json_write")
            else: print("CRITICAL | startup not in system path | json_write")
            return None
    #verify if necessary functions are present

    json_filename = str(json_filename)
    if json_filename[-5:] != ".json":
        if log: logger.warning("WARNING | invalid file extension | json_write")
        else: print("WARNING | invalid file extension | json_write")
        return None
    if type(mode) != bool:
        if log: logger.warning("WARNING | invalid type for mode | json_write")
        else: print("WARNING | invalid type for mode | json_write")
        return None
    if type(new_data) != dict:
        if log: logger.warning("WARNING | invalid type for new_data | json_write")
        else: print("WARNING | invalid type for new_data | json_write")
        return None
    for item in list(new_data.keys()):
        if item not in [["log_level", "csv_filename", "log_filename", "status_filename", "AreaName", "AreaType", "API_key"], ["local_7day_infections", "national_7day_infections", "hospital_cases", "deaths_total", "updates", "remove", "news"]][mode]:
            if log: logger.warning("WARNING | invalid format for new_data | json_write")
            else: print("WARNING | invalid format for new_data | json_write")
            return None
        if (item == "remove" and type(new_data[item]) != dict) or (item in ["updates", "news"] and type(new_data[item]) != list) or (item not in ["updates", "remove", "news"] and type(new_data[item]) != str):
            if log: logger.warning('WARNING | invalid type for new_data["' + item + '"] | json_write')
            else: print('WARNING | invalid type for new_data["' + item + '"] | json_write')
            return None
    if len(args) > 0:
        if log: logger.info("INFO | too many non-keyword arguements | json_write")
        else: print("INFO | too many non-keyword arguements | json_write")
    if len(kwargs) > 0:
        if log: logger.info("INFO | unexpected keyword arguments | json_write")
        else: print("INFO | unexpected keyword arguments | json_write")
    #verify given arguements

    if log: logger.debug("DEBUG | calling json_read | json_write")
    else: print("DEBUG | calling json_read | json_write")
    data = json_read(json_filename, mode)
    #obtain data currently stored in file
    if data == None:
        if log: logger.error("ERROR | json_read failed | json_write")
        else: print("ERROR | json_read failed | json_write")
        if not mode:
            data = {"log_level" : "DEBUG", "csv_filename" : "covid.csv", "log_filename" : "sys.log", "status_filename" : "status.json", "AreaName" : "Exeter", "AreaType" : "ltla", "API_key" : ""}
        else:
            data = {"local_7day_infections" : "N/A", "national_7day_infections" : "N/A", "hospital_cases" : "N/A", "deaths_total" : "N/A", "updates" : [], "remove" : {}, "news" : []}
    #default data if unable to read from file
    elif log: logger.debug("DEBUG | json_read returned successfully | json_write")
    else: print("DEBUG | json_read returned successfully | json_write")
    data.update(new_data)
    #add the new data to the old
    data = json.dumps(data, indent = 4)
    with open(json_filename, "w") as f:
        f.write(data)
    #format this data and write it to a file
    if log: logger.debug("DEBUG | json_write successfully completed | json_write")
    else: print("DEBUG | json_write successfully completed | json_write")
    return True


def reset_updates(log : bool = True, *args, **kwargs) -> None:
    '''a function to update the updates as stored in main'''

    if type(log) != bool:
        log = True
    if log:
        log = "logging" in globals() and "logger" in globals()
        if not log:
            print("WARNING | unable to log | reset_updates")
    #verify if logging is enabled

    if log: logger.debug("DEBUG | reset_updates called successfully | reset_updates")
    else: print("DEBUG | reset_updates called successfully | reset_updates")

    global sched
    if "sched" not in globals():
        print("WARNING | sched not imported | reset_updates")
        try:
            import sched
        except:
            print("CRITICAL | sched not in system path | reset_updates")
            return None
    global time
    if "time" not in globals():
        print("WARNING | time not imported | reset_updates")
        try:
            import time
        except:
            print("CRITICAL | time not in system path | reset_updates")
            return None
    global covid_data_handler
    if "covid_data_handler" not in globals():
        print("WARNING | covid_data_handler not imported | reset_updates")
        try:
            import covid_data_handler
        except:
            print("CRITICAL | covid_data_handler in system path | reset_updates")
            return None
    global covid_news_handling
    if "covid_news_handling" not in globals():
        print("WARNING | covid_news_handling not imported | reset_updates")
        try:
            import covid_news_handling
        except:
            print("CRITICAL | covid_news_handling in system path | reset_updates")
            return None
    #verify if necessary functions are present

    global schedule
    try:
        if covid_data_handler.schedule != covid_news_handling.schedule:
            if log: logger.warning("WARNING | global schedule not synced | reset_updates")
            else: print("WARNING | global schedule not synced | reset_updates")
            schedule = sched.scheduler(time.time, time.sleep)
            covid_data_handler.schedule = schedule
            covid_news_handling.schedule = schedule
        else:
            schedule = covid_data_handler.schedule
    except:
        if log: logger.warning("WARNING | global schedule not present in covid_data_handler or covid_news_handling | reset_updates")
        else: print("WARNING | global schedule not present in covid_data_handler or covid_news_handling | reset_updates")
        if "schedule" not in globals():
            if log: logger.warning("WARNING | global schedule not present | reset_updates")
            else: print("WARNING | global schedule not present | reset_updates")
            schedule = sched.scheduler(time.time, time.sleep)
        covid_data_handler.schedule = schedule
        covid_news_handling.schedule = schedule
    if type(covid_data_handler.schedule) != type(sched.scheduler(time.time, time.sleep)):
        if log: logger.warning("WARNING | invalid type for schedule | reset_updates")
        else: print("WARNING | invalid type for schedule | reset_updates")
        schedule = sched.scheduler(time.time, time.sleep)
    #verify necessary globals

    if len(args) > 0:
        if log: logger.info("INFO | too many non-keyword arguements | reset_updates")
        else: print("INFO | too many non-keyword arguements | reset_updates")
    if len(kwargs) > 0:
        if log: logger.info("INFO | unexpected keyword arguments | reset_updates")
        else: print("INFO | unexpected keyword arguments | reset_updates")
    #verify given arguements

    global updates
    for a in range(3):
        try:
            if type([updates, covid_data_handler.updates, covid_news_handling.updates][a]) != list:
                if log: logger.warning("WARNING | invalid type for updates | reset_updates")
                else: print("WARNING | invalid type for updates | reset_updates")
                [updates, covid_data_handler.updates, covid_news_handling.updates][a] = []
            for b in range(len([updates, covid_data_handler.updates, covid_news_handling.updates][a]) -1, -1, -1):
                if type([updates, covid_data_handler.updates, covid_news_handling.updates][a][b]) != dict:
                    if log: logger.warning("WARNING | invalid type for element in updates | reset_updates")
                    else: print("WARNING | invalid type for element in updates | reset_updates")
                    [updates, covid_data_handler.updates, covid_news_handling.updates][a].pop(b)
                elif list([updates, covid_data_handler.updates, covid_news_handling.updates][a][b].keys()) != ["time", "time2", "type", "title", "content", "event", "repeat"]:
                    if log: logger.warning("WARNING | invalid format for element in updates | reset_updates")
                    else: print("WARNING | invalid format for element in updates | reset_updates")
                    [updates, covid_data_handler.updates, covid_news_handling.updates][a].pop(b)
                #verify the updates (and contents therein) of main, covid_data_handler, and covid_news_handling
                elif a == 0:
                    if updates[b] not in [covid_data_handler.updates, covid_news_handling.updates][updates[b]["type"]]:
                        updates.pop(b)
                #remove elements of updates of main that aren't also present in the elements of covid_data_handler or covid_data_handling
                else:
                    if [updates, covid_data_handler.updates, covid_news_handling.updates][a][b] not in updates:
                        updates.append([updates, covid_data_handler.updates, covid_news_handling.updates][a][b])
                #add to the updates of main, those elements present in the updates of covid_data_handler and covid_data_handling
        except:
            if log: logger.warning("WARNING | global updates not present | reset_updates")
            else: print("WARNING | global updates not present | reset_updates")
            [updates, covid_data_handler.updates, covid_news_handling.updates][a] = []
        #default the value of updates if necessary

    if log: logger.debug("DEBUG | reset_updates successfully completed | reset_updates")
    else: print("DEBUG | reset_updates successfully completed | reset_updates")
    return True


def reset_news(log : bool = True, *args, **kwargs) -> None:
    '''a function to update the news as stored in main'''

    if type(log) != bool:
        log = True
    if log:
        log = "logging" in globals() and "logger" in globals()
        if not log:
            print("WARNING | unable to log | reset_news")
    #verify if logging is enabled

    if log: logger.debug("DEBUG | reset_news called successfully | reset_news")
    else: print("DEBUG | reset_news called successfully | reset_news")

    global covid_news_handling
    if "covid_news_handling" not in globals():
        print("WARNING | covid_news_handling not imported | reset_news")
        try:
            import covid_news_handling
        except:
            print("CRITICAL | covid_news_handling in system path | reset_news")
            return None
    global datetime
    if "datetime" not in globals():
        if log: logger.warning("WARNING | datetime not imported | reset_news")
        else: print("WARNING | datetime not imported | reset_news")
        try:
            from datetime import datetime
        except:
            if log: logger.critical("CRITICAL | datetime not in system path | reset_news")
            else: print("CRITICAL | datetime not in system path | reset_news")
            return None
    global timedelta
    if "timedelta" not in globals():
        if log: logger.warning("WARNING | timedelta not imported | reset_news")
        else: print("WARNING | timedelta not imported | reset_news")
        try:
            from datetime import timedelta
        except:
            if log: logger.critical("CRITICAL | datetime not in system path | reset_news")
            else: print("CRITICAL | datetime not in system path | reset_news")
            return None
    #verify if necessary functions are present

    if len(args) > 0:
        if log: logger.info("INFO | too many non-keyword arguements | reset_news")
        else: print("INFO | too many non-keyword arguements | reset_news")
    if len(kwargs) > 0:
        if log: logger.info("INFO | unexpected keyword arguments | reset_news")
        else: print("INFO | unexpected keyword arguments | reset_news")
    #verify given arguements

    global news
    try:
        news = covid_news_handling.news
        #attempt to update main.news to match covid_news_handling.news
    except:
        if log: logger.warning("WARNING | global news not present in covid_news_handling | reset_news")
        else: print("WARNING | global news not present in covid_news_handling | reset_news")
        if "news" not in globals():
            if log: logger.warning("WARNING | global news not presentg | reset_news")
            else: print("WARNING | global news not present | reset_news")
            news = []
        covid_news_handling.news = news
    if type(news) != list:
        if log: logger.warning("WARNING | invalid type for global news | reset_news")
        else: print("WARNING | invalid type for global news | reset_news")
        news = []
    #validate and, if necessary, default news
    else:
        for a in range(len(news) - 1, -1, -1):
            if type(news[a]) != dict:
                if log: logger.warning("WARNING | invalid type for element in news | reset_news")
                else: print("WARNING | invalid type for element in news | reset_news")
                news.pop(a)
            elif list(news[a].keys()) != ["title", "content"]:
                print(updates[a].keys())
                if log: logger.warning("WARNING | invalid format for element in news, " + str(news[a]) + " | reset_news")
                else: print("WARNING | invalid format for element in news, " + str(news[a]) + " | reset_news")
                news.pop(a)
        #validate elements of news
    global remove
    try:
        remove = covid_news_handling.remove
        #attempt to update main.remove to match covid_news_handling.remove
    except:
        if log: logger.warning("WARNING | global remove not present in covid_news_handling | reset_news")
        else: print("WARNING | global remove not present in covid_news_handling | reset_news")
        if "remove" not in globals():
            if log: logger.warning("WARNING | global remove not present | reset_news")
            else: print("WARNING | global remove not present | reset_news")
            remove = {}
        covid_news_handling.remove = remove
    if type(remove) != dict:
        if log: logger.warning("WARNING | invalid type for global remove | reset_news")
        else: print("WARNING | invalid type for global remove | reset_news")
        remove = {}
    #validate and, if necessary, default remove

    if log: logger.debug("DEBUG | reset_news successfully completed | reset_news")
    else: print("DEBUG | reset_news successfully completed | reset_news")
    return True


def update_remove(remove_update : str = None, log : bool = True, *args, **kwargs) -> None:
    '''a function to remove an update'''

    if type(log) != bool:
        log = True
    if log:
        log = "logging" in globals() and "logger" in globals()
        if not log:
            print("WARNING | unable to log | update_remove")
    #verify if logging is enabled

    if log: logger.debug("DEBUG | update_remove called successfully | update_remove")
    else: print("DEBUG | update_remove called successfully | update_remove")


    global sched
    if "sched" not in globals():
        print("WARNING | sched not imported | update_remove")
        try:
            import sched
        except:
            print("CRITICAL | sched not in system path | update_remove")
            return None
    global time
    if "time" not in globals():
        print("WARNING | time not imported | update_remove")
        try:
            import time
        except:
            print("CRITICAL | time not in system path | update_remove")
            return None
    global covid_data_handler
    if "covid_data_handler" not in globals():
        if log: logger.warning("WARNING | covid_data_handler not imported | update_remove")
        else: print("WARNING | covid_data_handler not imported | update_remove")
        try:
            import covid_data_handler
        except:
            if log: logger.critical("CRITICAL | covid_data_handler not in system path | update_remove")
            else: print("CRITICAL | covid_data_handler not in system path | update_remove")
            return None
    global covid_news_handling
    if "covid_news_handling" not in globals():
        if log: logger.warning("WARNING | covid_news_handling not imported | update_remove")
        else: print("WARNING | covid_news_handling not imported | update_remove")
        try:
            import covid_news_handling
        except:
            if log: logger.critical("CRITICAL | covid_news_handling not in system path | update_remove")
            else: print("CRITICAL | covid_news_handling not in system path | update_remove")
            return None
    global reset_updates
    if "reset_updates" not in globals():
        if log: logger.warning("WARNING | reset_updates not imported | update_remove")
        else: print("WARNING | reset_updates not imported | update_remove")
        try:
            from main import reset_updates
        except:
            if log:logger.critical("CRITICAL | main not in system path | update_remove")
            else: print("CRITICAL | main not in system path | update_remove")
            return None
    #verify if necessary functions are present

    global schedule
    try:
        if covid_data_handler.schedule != covid_news_handling.schedule:
            if log: logger.warning("WARNING | global schedule not synced | update_remove")
            else: print("WARNING | global schedule not synced | update_remove")
            schedule = sched.scheduler(time.time, time.sleep)
            covid_data_handler.schedule = schedule
            covid_news_handling.schedule = schedule
        else:
            schedule = covid_data_handler.schedule
    except:
        if log: logger.warning("WARNING | global schedule not present in covid_data_handler or covid_news_handling | update_remove")
        else: print("WARNING | global schedule not present in covid_data_handler or covid_news_handling | update_remove")
        if "schedule" not in globals():
            if log: logger.warning("WARNING | global schedule not present | update_remove")
            else: print("WARNING | global schedule not present | update_remove")
            schedule = sched.scheduler(time.time, time.sleep)
        covid_data_handler.schedule = schedule
        covid_news_handling.schedule = schedule
    if type(covid_data_handler.schedule) != type(sched.scheduler(time.time, time.sleep)):
        if log: logger.warning("WARNING | invalid type for schedule | update_remove")
        else: print("WARNING | invalid type for schedule | update_remove")
        schedule = sched.scheduler(time.time, time.sleep)
    global updates
    #verify necessary globals

    if remove_update == None:
        if log: logger.warning("WARNING | remove_update not given | update_remove")
        else: print("WARNING | remove_update not given | update_remove")
        return None
    remove_update = str(remove_update)
    #verify given arguements

    if log: logger.debug("DEBUG | calling reset_updates | update_remove")
    else: print("DEBUG | calling reset_updates | update_remove")
    if reset_updates() == None:
        if log: logger.error("ERROR | reset_updates failed | update_remove")
        else: print("ERROR | reset_updates failed | update_remove")
        return None
    #attempt to ensure updates of all relevant functions are up to date and in sync
    elif log: logger.debug("DEBUG | reset_updates successfully returned | update_remove")
    else: print("DEBUG | reset_updates successfully returned | update_remove")
    for a in range(len(updates) - 1, -1, -1):
        if updates[a]["title"] == remove_update:
            if log: logger.debug("DEBUG | removing update, " + remove_update + " | update_remove")
            else: print("DEBUG | removing update, " + remove_update + " | update_remove")
            schedule.cancel(updates[a]["event"])
            #cancel the update with the scheduler
            [covid_data_handler.updates, covid_news_handling.updates][updates[a]["type"]].pop([covid_data_handler.updates, covid_news_handling.updates][updates[a]["type"]].index(updates[a]))
            #remove the update from the updates of the module that spawned it
            updates.pop(a)
            #remove the update from main.updates

    if log: logger.debug("DEBUG | update_remove successfully completed | update_remove")
    else: print("DEBUG | update_remove successfully completed | update_remove")
    return True


def news_remove(remove_news : str = None, log : bool = True, *args, **kwargs) -> None:
    '''a function to remove a news article'''

    if type(log) != bool:
        log = True
    if log:
        log = "logging" in globals() and "logger" in globals()
        if not log:
            print("WARNING | unable to log | news_remove")
    #verify if logging is enabled

    if log: logger.debug("DEBUG | news_remove called successfully | news_remove")
    else: print("DEBUG | news_remove called successfully | news_remove")

    global reset_news
    if "reset_news" not in globals():
        if log: logger.warning("WARNING | reset_news not imported | news_remove")
        else: print("WARNING | reset_news not imported | news_remove")
        try:
            from main import reset_news
        except:
            if log:logger.critical("CRITICAL | main not in system path | news_remove")
            else: print("CRITICAL | main not in system path | news_remove")
            return None
    #verify if necessary functions are present

    global news

    if remove_news == None:
        if log: logger.warning("WARNING | remove_news not given | news_remove")
        else: print("WARNING | remove_news not given | news_remove")
        return None
    remove_news = str(remove_news)
    #verify given arguements

    if log: logger.debug("DEBUG | calling reset_news | news_remove")
    else: print("DEBUG | calling reset_news | news_remove")
    if reset_news() == None:
        if log: logger.error("ERROR | reset_news failed | news_remove")
        else: print("ERROR | reset_news failed | news_remove")
        return None
    #attempt to ensure the news of main is in sync with the news of covid_news_handling
    elif log: logger.debug("DEBUG | reset_news successfully returned | news_remove")
    else: print("DEBUG | reset_news successfully returned | news_remove")
    for a in range(len(news) - 1, -1, -1):
        if news[a]["title"] == remove_news:
            if log: logger.debug("DEBUG | removing article, " + remove_news + " | news_remove")
            else: print("DEBUG | removing article, " + remove_news + " | news_remove")
            news.pop(a)
    #remove the relevant news article from news

    if log: logger.debug("DEBUG | news_remove successfully completed | news_remove")
    else: print("DEBUG | news_remove successfully completed | news_remove")
    return True


def dashboard_setup(log : bool = True, *args, **kwargs):
    '''a function to setup the covid dashboard'''

    if type(log) != bool:
        log = True
    if log:
        log = "logging" in globals() and "logger" in globals()
        if not log:
            print("WARNING | unable to log | dashboard_setup")
    #verify if logging is enabled

    if log: logger.debug("DEBUG | dashboard_setup called successfully | dashboard_setup")
    else: print("DEBUG | dashboard_setup called successfully | dashboard_setup")

    global Flask
    if "Flask" not in globals():
        if log: logger.warning("WARNING | Flask not imported | dashboard_setup")
        else: print("WARNING | Flask not imported | dashboard_setup")
        try:
            from flask import Flask
        except:
            if log: logger.critical("CRITICAL | flask not in system path | dashboard_setup")
            else: print("CRITICAL | flask not in system path | dashboard_setup")
            return None
    #verify if necessary functions are present

    if len(args) > 0:
        if log: logger.info("INFO | too many non-keyword arguements | dashboard_setup")
        else: print("INFO | too many non-keyword arguements | dashboard_setup")
    if len(kwargs) > 0:
        if log: logger.info("INFO | unexpected keyword arguments | dashboard_setup")
        else: print("INFO | unexpected keyword arguments | dashboard_setup")
    #verify given arguements


    app = Flask(__name__)
    import os
    import logging
    logging.getLogger('werkzeug').disabled = True
    os.environ['WERKZEUG_RUN_MAIN'] = 'true'
    #prevent flask from making its own logs


    @app.route("/index")
    def dashboard():
        '''a function to serve the covid dashboard'''

        global log
        if "log" not in globals():
            log = True
        if log:
            log = "logging" in globals() and "logger" in globals()
            if not log:
                print("WARNING | unable to log | dashboard")
        #verify if logging is enabled

        global sched
        if "sched" not in globals():
            print("WARNING | sched not imported | dashboard")
            try:
                import sched
            except:
                print("CRITICAL | sched not in system path | dashboard")
                return None
        global time
        if "time" not in globals():
            print("WARNING | time not imported | dashboard")
            try:
                import time
            except:
                print("CRITICAL | time not in system path | dashboard")
                return None
        global request
        if "request" not in globals():
            if log: logger.warning("WARNING | request not imported | dashboard")
            else: print("WARNING | request not imported | dashboard")
            try:
                from flask import request
            except:
                if log: logger.critical("CRITICAL | flask not in system path | dashboard")
                else: print("CRITICAL | flask not in system path | dashboard")
                return None
        global render_template
        if "render_template" not in globals():
            if log: logger.warning("WARNING | render_template not imported | dashboard")
            else: print("WARNING | render_template not imported | dashboard")
            try:
                from flask import render_template
            except:
                if log: logger.critical("CRITICAL | flask not in system path | dashboard")
                else: print("CRITICAL | flask not in system path | dashboard")
                return None
        global covid_data_handler
        if "covid_data_handler" not in globals():
            if log: logger.warning("WARNING | covid_data_handler not imported | dashboard")
            else: print("WARNING | covid_data_handler not imported | dashboard")
            try:
                import covid_data_handler
            except:
                if log: logger.critical("CRITICAL | covid_data_handler not in system path | dashboard")
                else: print("CRITICAL | covid_data_handler not in system path | dashboard")
                return None
        global covid_news_handling
        if "covid_news_handling" not in globals():
            if log: logger.warning("WARNING | covid_news_handling not imported | dashboard")
            else: print("WARNING | covid_news_handling not imported | dashboard")
            try:
                import covid_news_handling
            except:
                if log: logger.critical("CRITICAL | covid_news_handling not in system path | dashboard")
                else: print("CRITICAL | covid_news_handling not in system path | dashboard")
                return None
        global schedule_covid_updates
        schedule_covid_updates = covid_data_handler.schedule_covid_updates
        global update_news
        update_news = covid_news_handling.update_news
        global json_write
        if "json_write" not in globals():
            if log: logger.warning("WARNING | json_write not imported | dashboard")
            else: print("WARNING | json_write not imported | dashboard")
            try:
                from main import json_write
            except:
                if log:logger.critical("CRITICAL | main not in system path | dashboard")
                else: print("CRITICAL | main not in system path | dashboard")
                return None
        global reset_updates
        if "reset_updates" not in globals():
            if log: logger.warning("WARNING | reset_updates not imported | dashboard")
            else: print("WARNING | reset_updates not imported | dashboard")
            try:
                from main import reset_updates
            except:
                if log:logger.critical("CRITICAL | main not in system path | dashboard")
                else: print("CRITICAL | main not in system path | dashboard")
                return None
        global reset_news
        if "reset_news" not in globals():
            if log: logger.warning("WARNING | reset_news not imported | dashboard")
            else: print("WARNING | reset_news not imported | dashboard")
            try:
                from main import reset_news
            except:
                if log:logger.critical("CRITICAL | main not in system path | dashboard")
                else: print("CRITICAL | main not in system path | dashboard")
                return None
        global update_remove
        if "update_remove" not in globals():
            if log: logger.warning("WARNING | updates_remove not imported | dashboard")
            else: print("WARNING | updates_remove not imported | dashboard")
            try:
                from main import updates_remove
            except:
                if log:logger.critical("CRITICAL | main not in system path | dashboard")
                else: print("CRITICAL | main not in system path | dashboard")
                return None
        global news_remove
        if "news_remove" not in globals():
            if log: logger.warning("WARNING | news_remove not imported | dashboard")
            else: print("WARNING | news_remove not imported | dashboard")
            try:
                from main import news_remove
            except:
                if log:logger.critical("CRITICAL | main not in system path | dashboard")
                else: print("CRITICAL | main not in system path | dashboard")
                return None
        #verify if necessary functions are present


        global status_filename
        if "status_filename" not in globals():
            if log: logger.warning("WARNING | global status_filename not present | dashboard")
            else: print("WARNING | global status_filename not present | dashboard")
            status_filename = "status.json"
        status_filename = str(status_filename)
        if status_filename[-5:] != ".json":
            if log: logger.warning("WARNING | invalid file extension for status_filename | dashboard")
            print("WARNING | invalid file extension for status_filename | dashboard")
            status_filename = "status.json"
        global schedule
        try:
            if covid_data_handler.schedule != covid_news_handling.schedule:
                if log: logger.warning("WARNING | global schedule not synced | dashboard")
                else: print("WARNING | global schedule not synced | dashboard")
                schedule = sched.scheduler(time.time, time.sleep)
                covid_data_handler.schedule = schedule
                covid_news_handling.schedule = schedule
            else:
                schedule = covid_data_handler.schedule
        except:
            if log: logger.warning("WARNING | global schedule not present in covid_data_handler or covid_news_handling | dashboard")
            else: print("WARNING | global schedule not present in covid_data_handler or covid_news_handling | dashboard")
            if "schedule" not in globals():
                if log: logger.warning("WARNING | global schedule not present | dashboard")
                else: print("WARNING | global schedule not present | dashboard")
                schedule = sched.scheduler(time.time, time.sleep)
            covid_data_handler.schedule = schedule
            covid_news_handling.schedule = schedule
        if type(covid_data_handler.schedule) != type(sched.scheduler(time.time, time.sleep)):
            if log: logger.warning("WARNING | invalid type for schedule | dashboard")
            else: print("WARNING | invalid type for schedule | dashboard")
            schedule = sched.scheduler(time.time, time.sleep)
        global updates
        global news
        global remove
        global date
        global local_7day_infections
        global national_7day_infections
        global hospital_cases
        global deaths_total
        #verify necessary globals


        remove_update = request.args.get("update_item")
        remove_news = request.args.get("notif")
        if remove_update != None:
            if log: logger.debug("DEBUG | calling update_remove | dashboard")
            else: print("DEBUG | calling update_remove | dashboard")
            if update_remove(remove_update) == None:
                if log: logger.error("ERROR | update_remove failed | dashboard")
                else: print("ERROR | update_remove failed | dashboard")
                return None
            if log: logger.debug("DEBUG | update_remove successfully returned")
            else: print("DEBUG | update_remove successfully returned")
        #remove elements up updates as requested
        elif remove_news != None:
            if log: logger.debug("DEBUG | calling news_remove | dashboard")
            else: print("DEBUG | calling news_remove | dashboard")
            if news_remove(remove_news) == None:
                if log: logger.error("ERROR | news_remove failed | dashboard")
                else: print("ERROR | news_remove failed | dashboard")
                return None
            if log: logger.debug("DEBUG | news_remove successfully returned")
            else: print("DEBUG | news_remove successfully returned")
        #remove elements of news as requested

        if log: logger.debug("DEBUG | running schedule | dashboard")
        else: print("DEBUG | running schedule | dashboard")
        schedule.run(blocking = False)
        #allow any functions currently intended to run to do so
        
        if log: logger.debug("DEBUG | calling reset_updates | dashboard")
        else: print("DEBUG | calling reset_updates | dashboard")
        if reset_updates() == None:
            if log: logger.error("ERROR | reset_updates failed | dashboard")
            else: print("ERROR | reset_updates failed | dashboard")
        elif log: logger.debug("DEBUG | reset_updates successfully returned | dashboard")
        else: print("DEBUG | reset_updates successfully returned | dashboard")
        if log: logger.debug("DEBUG | calling reset_news | dashboard")
        else: print("DEBUG | calling reset_news | dashboard")
        if reset_news() == None:
            if log: logger.error("ERROR | reset_news failed | dashboard")
            else: print("ERROR | reset_news failed | dashboard")
        elif log: logger.debug("DEBUG | reset_news successfully returned | dashboard")
        else: print("DEBUG | reset_news successfully returned | dashboard")
        #update the contents of updates and news

        update_name = request.args.get("two")
        update_interval = request.args.get("update")
        repeat = request.args.get("repeat") != None
        covid_update = request.args.get("covid-data") != None
        news_update = request.args.get("news") != None
        if update_name != None and update_interval != None and (covid_update or news_update):
            update_name2 = update_name
            a = 1
            while True:
                check = True
                for update in updates:
                    if update_name2 == update["title"]:
                        check = False
                if check:
                    break
                if log: logger.info("INFO | an update with this name already exists, " + update_name2 + " | dashboard")
                else: print("INFO | an update with this name already exists, " + update_name2 + " | dashboard")
                update_name2 = update_name + " (" + str(a) + ")"
                a += 1
            #ensure the title of a new update is unique
            if covid_update:
                if log: logger.debug("DEBUG | calling schedule_covid_updates | dashboard")
                else: print("DEBUG | calling schedule_covid_updates | dashboard")
                if schedule_covid_updates(update_interval, update_name2, repeat = repeat) == None:
                    if log: logger.error("ERROR | schedule_covid_updates failed | dashboard")
                    else: print("ERROR | schedule_covid_updates failed | dashboard")
                elif log: logger.debug("DEBUG | schedule_covid_updates successfully returned | dashboard")
                else: print("DEBUG | schedule_covid_updates successfully returned | dashboard")
            #schedule a covid update if desired
            if news_update:
                if log: logger.debug("DEBUG | calling update_news | dashboard")
                else: print("DEBUG | calling update_news | dashboard")
                if update_news(update_interval, update_name2, repeat = repeat) == None:
                    if log: logger.error("ERROR | update_news failed | dashboard")
                    else: print("ERROR | update_news failed | dashboard")
                elif log: logger.debug("DEBUG | update_news successfully returned | dashboard")
                else: print("DEBUG | update_news successfully returned | dashboard")
            #schedule a news update if required

            if log: logger.debug("DEBUG | calling reset_updates | dashboard")
            else: print("DEBUG | calling reset_updates | dashboard")
            if reset_updates() == None:
                if log: logger.error("ERROR | reset_updates failed | dashboard")
                else: print("ERROR | reset_updates failed | dashboard")
            elif log: logger.debug("DEBUG | reset_updates successfully returned | dashboard")
            else: print("DEBUG | reset_updates successfully returned | dashboard")
            #update the contents of updates

        try:
            local_7day_infections = str(covid_data_handler.local_7day_infections)
        except:
            if log: logger.warning("WARNING | global local_7day_infections not present in covid_data_handler | dashboard")
            else: print("WARNING | global local_7day_infections not present in covid_data_handler | dashboard")
            if "local_7day_infection" not in globals():
                if log: logger.warning("WARNING | global local_7day_infections not present | dashboard")
                else: print("WARNING | global local_7day_infections not present | dashboard")
                local_7day_infection = "N/A"
        try:
            national_7day_infections = str(covid_data_handler.national_7day_infections)
        except:
            if log: logger.warning("WARNING | global national_7day_infections not present in covid_data_handler | dashboard")
            else: print("WARNING | global national_7day_infections not present in covid_data_handler | dashboard")
            if "national_7day_infection" not in globals():
                if log: logger.warning("WARNING | global national_7day_infections not present | dashboard")
                else: print("WARNING | global national_7day_infections not present | dashboard")
                national_7day_infection = "N/A"
        try:
            hospital_cases = str(covid_data_handler.hospital_cases)
        except:
            if log: logger.warning("WARNING | global hospital_cases not present in covid_data_handler | dashboard")
            else: print("WARNING | hospital_cases not present in covid_data_handler | dashboard")
            if "hospital_cases" not in globals():
                if log: logger.warning("WARNING | global hospital_cases not present | dashboard")
                else: print("WARNING | global hospital_cases not present | dashboard")
                hospital_cases = "N/A"
        try:
            deaths_total = str(covid_data_handler.deaths_total)
        except:
            if log: logger.warning("WARNING | global deaths_total not present in covid_data_handler | dashboard")
            else: print("WARNING | deaths_total not present in covid_data_handler | dashboard")
            if "deaths_total" not in globals():
                if log: logger.warning("WARNING | global deaths_total not present | dashboard")
                else: print("WARNING | global deaths_total not present | dashboard")
                local_7day_infection = "N/A"
        #update covid statistics

        new_updates = []
        for update in updates:
            new_updates.append({"time" : update["time"], "time2" : update["time2"], "type" : update["type"], "title" : update["title"], "content" : update["content"], "repeat" : update["repeat"]})
        #create a copy of updates that can be saved to a file
        if log: logger.debug("DEBUG | calling json_write | dashboard")
        else: print("DEBUG | calling json_write | dashboard")
        if json_write(status_filename, {"local_7day_infections" : local_7day_infections, "national_7day_infections" : national_7day_infections, "hospital_cases" : hospital_cases, "deaths_total" : deaths_total, "updates" : new_updates, "remove" : remove, "news" : news}, True) == None:
            if log: logger.error("ERROR | json_write failed | dashboard")
            else: print("ERROR | json_write failed | dashboard")
        elif log: logger.debug("DEBUG | json_write successfully returned | dashboard")
        else: print("DEBUG | json_read successfully returned | dashboard")
        #update the status file with up to date values

        return render_template("index.html", title = "Covid Dashboard", location = "Exeter", local_7day_infections = local_7day_infections, nation_location = "England", national_7day_infections = national_7day_infections, hospital_cases = hospital_cases, deaths_total = deaths_total, updates = updates, news_articles = news)


    if log: logger.debug("DEBUG | dashboard_setup successfully completed | dashboard")
    else: print("DEBUG | dashboard_setup successfully completed | dashboard")
    return app


def startup(*args, **kwargs):
    '''a function to setup and start the program'''

    global covid_data_handler
    if "covid_data_handler" not in globals():
        print("WARNING | covid_data_handler not imported | startup")
        try:
            import covid_data_handler
        except:
            print("CRITICAL | covid_data_handler not in system path | startup")
            return None
    global covid_news_handling
    if "covid_news_handling" not in globals():
        print("WARNING | covid_news_handling not imported | startup")
        try:
            import covid_news_handling
        except:
            print("CRITICAL | covid_news_handling not in system path | startup")
            return None
    global schedule_covid_updates
    schedule_covid_updates = covid_data_handler.schedule_covid_updates
    global covid_update
    covid_update = covid_data_handler.covid_update
    global update_news
    update_news = covid_news_handling.update_news
    global news_API_request
    news_API_request = covid_news_handling.news_API_request

    global isfile
    if "isfile" not in globals():
        print("WARNING | isfile not imported | startup")
        try:
            from os.path import isfile
        except:
            print("CRITICAL | os.path not in system path | startup")
            return None
    covid_data_handler.isfile = isfile
    covid_news_handling.isfile = isfile
    global datetime
    if "datetime" not in globals():
        print("WARNING | datetime not imported | startup")
        try:
            from datetime import datetime
        except:
            print("CRITICAL | datetime not in system path | startup")
            return None
    covid_data_handler.datetime = datetime
    covid_news_handling.datetime = datetime
    global logging
    if "logging" not in globals():
        print("WARNING | logging not imported | startup")
        try:
            import logging
        except:
            print("CRITICAL | logging not in system path | startup")
            return None
    covid_data_handler.logging = logging
    covid_news_handling.logging = logging
    global sched
    if "sched" not in globals():
        print("WARNING | sched not imported | startup")
        try:
            import sched
        except:
            print("CRITICAL | sched not in system path | startup")
            return None
    covid_data_handler.sched = sched
    covid_news_handling.sched = sched
    global time
    if "time" not in globals():
        print("WARNING | time not imported | startup")
        try:
            import time
        except:
            print("CRITICAL | time not in system path | startup")
            return None
    covid_data_handler.time = time
    covid_news_handling.time = time
    global json_read
    if "json_read" not in globals():
        print("WARNING | json_read not imported | startup")
        try:
            from main import json_read
        except:
            print("CRITICAL | main not in system path | startup")
            return None
    global json_write
    if "json_write" not in globals():
        print("WARNING | json_write not imported | startup")
        try:
            from main import json_write
        except:
            print("CRITICAL | main not in system path | startup")
            return None
    global dashboard_setup
    if "dashboard_setup" not in globals():
        print("WARNING | dashboard_setup not imported | startup")
        try:
            from main import dashboard_setup
        except:
            print("CRITICAL | main not in system path | startup")
            return None
    #verify if necessary functions are present

    global status_filename
    global logger
    global schedule
    global local_7day_infections
    global national_7day_infections
    global hospital_cases
    global deaths_total
    global updates
    global remove
    global news
    #verify necessary globals

    if len(args) > 0:
        print("INFO | too many non-keyword arguements | startup")
    if len(kwargs) > 0:
        print("INFO | unexpected keyword arguments | startup")
    #verify given arguements

    print("DEBUG | calling json_read | startup")
    data = json_read()
    while data == None:
        print("ERROR | json_read failed | startup")
        print("DEBUG | calling json_write | startup")
        if json_write() == None:
            print("ERROR | json_write failed | startup")
            status_filename = "status.json"
            break
        #if failing to extract the contents of the config file, try resetting the config file to its default contents
        print("DEBUG | json_write successfully returned | startup")
        print("DEBUG | calling json_read | startup")
        data = json_read()
    if data != None:
        print("DEBUG | json_read successfully returned | startup")
    #attempt to extract the contents of the config file

    log_filename = None
    log_level = None
    if data != None:
        if data["log_filename"][-4:] == ".log":
            log_filename = data["log_filename"]
            if "isfile" in globals():
                if not isfile(log_filename):
                    print("WARNING log file does not exist | startup")
                else:
                    with open(log_filename, "r") as f:
                        logs = f.read().split("\n")
                    logs.pop()
                    for a in range(len(logs) - 1, -1, -1):
                        line = logs[a].split(" | ")
                        if len(line) == 4:
                            if line[1] not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
                                print("WARNING | invalid content for log | startup")
                                logs.pop(a)
                                continue
                            if "datetime in globals":
                                try:
                                    datetime.strptime(line[0], "%Y-%m-%d %H:%M:%S,%f")
                                except:
                                    print("WARNING | invalid format for log, " + logs[a] + " | startup")
                                    logs.pop(a)
                                continue
                            else:
                                print("WARNING | unable to validate format for log, " + logs[a] + " | startup")
                        print("WARNING | invalid format for log, " + logs[a] + " | startup")
                        logs.pop(a)
                    with open(log_filename, "w") as f:
                        f.write("\n".join(logs) + "\n")
        log_level = data["log_level"]
    if log_filename == None:
        print("ERROR | log_filename not given, defaulting | startup")
        if "isfile" in globals():
            log_filename = "sys.log"
            log_filename2 = "sys.log"
            a = 1
            while True:
                check = True
                if isfile(log_filename):
                    check = False
                if check:
                    break
                print("INFO | a log file with this name already exists, " + log_filename + " | startup")
                log_filename = log_filename2 + " (" + str(a) + ")"
                a += 1
        print("DEBUG | calling json_write | startup")
        if json_write(new_data = {"log_filename" : log_filename}) == None:
            print("ERROR | json_write failed | startup")
        print("DEBUG | json_write successfully returned | startup")
    if log_level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        print("ERROR | log_level not given, defaulting | startup")
        log_level = "DEBUG"
    logging.basicConfig(level=[logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL][["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"].index(log_level)], filename=log_filename, encoding="utf-8", format="%(asctime)s | %(message)s")
    logger = logging.getLogger(__name__)
    covid_data_handler.logger = logger
    covid_news_handling.logger = logger
    logger.debug("DEBUG | beginning logging | startup")
    #setup logging framework

    schedule = sched.scheduler(time.time, time.sleep)
    covid_data_handler.schedule = schedule
    covid_news_handling.schedule = schedule
    #setup scheduling framework

    if data != None:
        covid_data_handler.csv_filename = str(data["csv_filename"])
        covid_data_handler.AreaName = str(data["AreaName"])
        covid_data_handler.AreaType = str(data["AreaType"])
        covid_news_handling.API_key = str(data["API_key"])
        status_filename = str(data["status_filename"])
    #extract data read from the config file

    print("DEBUG | calling json_read | startup")
    data = json_read(status_filename, True)
    while data == None:
        print("ERROR | json_read failed | startup")
        print("DEBUG | calling json_write | startup")
        if json_write(status_filename, mode = True) == None:
            print("ERROR | json_write failed | startup")
            covid_data_handler.local_7day_infections = "N/A"
            covid_data_handler.national_7day_infections = "N/A"
            covid_data_handler.hospital_cases = "N/A"
            covid_data_handler.deaths_total = "N/A"
            updates = []
            covid_data_handler.updates = []
            covid_news_handling.updates = []
            covid_news_handling.news = []
            covid_news_handling.remove = {}
            break
            #if failing to reset the status file to its default contents, default the data that would be read from it
        #if failing to extract the contents of the config file, try resetting the status file to its default contents
        print("DEBUG | json_write successfully returned | startup")
        print("DEBUG | calling json_read | startup")
        data = json_read(status_filename, 1)
    #attempt to extract the contents of the status file

    if data != None:
        print("DEBUG | json_read successfully returned | startup")

        local_7day_infections = str(data["local_7day_infections"])
        covid_data_handler.local_7day_infections = local_7day_infections
        national_7day_infections = str(data["national_7day_infections"])
        covid_data_handler.national_7day_infections = national_7day_infections
        hospital_cases = str(data["hospital_cases"])
        covid_data_handler.hospital_cases = hospital_cases
        deaths_total = str(data["deaths_total"])
        covid_data_handler.deaths_total = deaths_total
        remove = data["remove"]
        if type(remove) != dict:
            logger.warning("WARNING | invalid type for remove | startup")
            remove = {}
        covid_news_handling.remove = remove
        news = data["news"]
        if type(news) != list:
            logger.warning("WARNING | invalid type for news | startup")
            news = []
        covid_news_handling.news = news
        #extract and verify data read from the status file

        updates = data["updates"]
        covid_data_handler.updates = []
        covid_news_handling.updates = []
        if type(updates) != list:
            logger.warning("WARNING | invalid type for updates | startup")
            updates = []
        checks = [1, 1]
        for a in range(len(updates) - 1, -1, -1):
            if type(updates[a]) != dict:
                logger.warning("WARNING | invalid type for element of updates | startup")
            elif list(updates[a].keys()) != ["time", "time2", "type", "title", "content", "repeat"]:
                logger.warning("WARNING | invalid format for element of updates | startup")
            elif updates[a]["type"] not in [0, 1] or updates[a]["repeat"] not in [0, 1]:
                logger.warning('WARNING | invalid type for "type" in element of updates | startup')
            #verify the elements of updates
            elif updates[a]["time"] > time.time() or updates[a]["repeat"]:
                logger.info("INFO | suitable update found | startup")
                if updates[a]["type"]:
                    update_news(updates[a]["time2"], updates[a]["title"], repeat = updates[a]["repeat"])
                else:
                    schedule_covid_updates(updates[a]["time2"], updates[a]["title"], repeat = updates[a]["repeat"])
                #if any updates should have occurred between the last time the program was run and now, inact them immediately
            elif checks[updates[a]["type"]] and updates[a]["time"] <= time.time():
                if updates[a]["type"]:
                    news_API_request()
                else:
                    covid_update()
            #if any updates were scheduled in the last run of the program and have yet to come to past, schedule them again
            updates.pop(a)

    logger.debug("DEBUG | calling dashboard_setup | startup")
    app = dashboard_setup()
    #obtain the framework for the covid dashboard
    if app == None:
        logger.critical("CRITICAL | dashboard_setup failed | startup")
        return None
    else:
        logger.debug("DEBUG | dashboard_setup successfully returned | startup")
        logger.debug("DEBUG | startup successfully completed | startup")
        return app
