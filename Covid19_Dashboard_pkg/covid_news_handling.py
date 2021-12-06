'''a module for news data handling functionality'''

def news_API_request(covid_terms : str = "Covid COVID-19 coronavirus", *args, update_name : str = None, log : bool = True, **kwargs) -> None:
    '''a function to retrieve new live news articles from the newsAPI containing given terms and following a given date'''

    if type(log) != bool:
        log = True
    if log:
        log = "logging" in globals() and "logger" in globals()
        if not log:
            print("WARNING | unable to log | news_API_request")
    #verify if logging is enabled

    if log: logger.debug("DEBUG | news_API_request called successfully | news_API_request")
    else: print("DEBUG | news_API_request called successfully | news_API_request")

    global update_news
    global updates
    if "updates" not in globals():
        if log: logger.warning("WARNING | global updates not present | update_news")
        else: print("WARNING | global updates not present | update_news")
        updates = []
    if type(updates) != list:
        if log: logger.warning("WARNING | invalid type for global updates | update_news")
        else: print("WARNING | invalid type for global updates | update_news")
        updates = []
    for a in range(len(updates) -1, -1, -1):
        if type(updates[a]) != dict:
            if log: logger.warning("WARNING | invalid type for element in updates | update_news")
            else: print("WARNING | invalid type for element in updates | update_news")
            updates.pop(a)
        elif list(updates[a].keys()) != ["time", "time2", "type", "title", "content", "event", "repeat"]:
            if log: logger.warning("WARNING | invalid format for element in updates | update_news")
            else: print("WARNING | invalid format for element in updates | update_news")
            updates.pop(a)
    #verify the contents of updates
    if update_name == None:
        if log: logger.warning("WARNING | update_name not given | news_API_request")
        else: print("WARNING | update_name not given | news_API_request")
    else:
        update_name = str(update_name)
        for a in range(len(updates)):
            if updates[a]["title"] == update_name and updates[a]["type"]:
                if updates[a]["repeat"]:
                    if "update_news" not in globals():
                        if log: logger.warning("WARNING | update_news not imported | covid_update")
                        else: print("WARNING | update_news not imported | covid_update")
                        try:
                            from covid_news_handling import update_news
                        except:
                            if log: logger.critical("CRITICAL | covid_news_handling not in system path | covid_update")
                            else: print("CRITICAL | covid_news_handling not in system path | covid_update")
                        #if the update that triggered this function is meant to repeat, reschedule the update
                    time = updates[a]["time2"]
                    updates.pop(a)
                    update_news(time, update_name, repeat = True)
                else:
                    updates.pop(a)
                break
    #if this function was triggered by an update, remove that update from updates

    global datetime
    if "datetime" not in globals():
        if log: logger.warning("WARNING | datetime not imported | news_API_request")
        else: print("WARNING | datetime not imported | news_API_request")
        try:
            from datetime import datetime
        except:
            if log: logger.critical("CRITICAL | datetime not in system path | news_API_request")
            else: print("CRITICAL | datetime not in system path | news_API_request")
            return None
    global timedelta
    if "timedelta" not in globals():
        if log: logger.warning("WARNING | timedelta not imported | news_API_request")
        else: print("WARNING | timedelta not imported | news_API_request")
        try:
            from datetime import timedelta
        except:
            if log: logger.critical("CRITICAL | datetime not in system path | news_API_request")
            else: print("CRITICAL | datetime not in system path | news_API_request")
            return None
    global requests
    if "requests" not in globals():
        if log: logger.warning("WARNING | requests not imported | news_API_request")
        else: print("WARNING | requests not imported | news_API_request")
        try:
            import requests
        except:
            if log: logger.critical("CRITICAL | requests not in system path | news_API_request")
            else: print("CRITICAL | requests not in system path | news_API_request")
            return None
    global json
    if "json" not in globals():
        if log: logger.warning("WARNING | json not imported | news_API_request")
        else: print("WARNING | json not imported | news_API_request")
        try:
            import json
        except:
            if log: logger.critical("CRITICAL | json not in system path | news_API_request")
            else: print("CRITICAL | json not in system path | news_API_request")
            return None
    #verify if necessary functions are present

    global API_key
    if "API_key" not in globals():
        if log: logger.error("ERROR | global API_key not present | news_API_request")
        else: print("ERROR | global API_key not present | news_API_request")
        return None
    API_key = str(API_key)
    global remove
    if "remove" not in globals():
        if log: logger.warning("WARNING | global remove not present | news_API_request")
        else: print("WARNING | global remove not present | news_API_request")
        remove = {}
    if type(remove) != dict:
        if log: logger.warning("WARNING | invalid type for global remove | news_API_request")
        else: print("WARNING | invalid type for global remove | news_API_request")
        remove = {}
    for a in range(len(list(remove.keys())) - 1, -1, -1):
        try:
            datetime.strptime(remove[list(remove.keys())[a]], "%Y-%m-%d")
        except:
            if log: logger.warning("WARNING | invalid format for element of remove | news_API_request")
            else: print("WARNING | invalid format for element of remove | news_API_request")
            del remove[list(remove.keys())[a]]
    global news
    #verify necessary globals

    if covid_terms == None:
        if log: logger.warning("WARNING | covid_terms not given | news_API_request")
        else: print("WARNING | covid_terms not given | news_API_request")
        return None
    covid_terms = str(covid_terms)
    clear = []
    covid_terms = covid_terms.split()
    for a in range(len(covid_terms) - 1):
        for b in range(len(covid_terms) - 1, a, -1):
            if covid_terms[a] in covid_terms[b]:
                clear.append(b)
            if covid_terms[b] in covid_terms[a]:
                clear.append(a)
    clear = sorted(clear, reverse=True)
    for a in clear:
        if log: logger.info("INFO | unnecessary item in covid_terms, " + covid_terms[a] + " | news_API_request")
        else: print("INFO | unnecessary item in covid_terms, " + covid_terms[a] + " | news_API_request")
        covid_terms.pop(a)
    #remove repeat terms (including those that wholly contain another term)
    if len(args) > 0:
        if log: logger.info("INFO | too many non-keyword arguments | news_API_request")
        else: print("INFO | too many non-keyword arguments | news_API_request")
    if len(kwargs) > 0:
        if log: logger.info("INFO | unexpected keyword arguments | news_API_request")
        else: print("INFO | unexpected keyword arguments | news_API_request")
    #verify given arguements

    date = datetime.strftime(datetime.today() - timedelta(days=1), "%Y-%m-%d")
    temp_news = []
    page = 0
    checks = []
    for a in range(len(covid_terms)):
        checks.append(False)
    while len(temp_news) < 20 and False in checks:
        page += 1
        for a in range(len(covid_terms)):
            link = 'https://newsapi.org/v2/everything?sortBy=popularity&q="' + covid_terms[a] + '"&from=' + date + '&apiKey=' + API_key + '&page=' + str(page)
            #construct a valid link for the newsAPI
            if log: logger.debug("DEBUG | contacting newsapi with link, " + link + " | news_API_request")
            else: print("DEBUG | contacting newsapi with link, " + link + " | news_API_request")
            try:
                api = requests.get(link)
            except:
                if log: logger.critical("CRITICAL | failure to attempt contact with newsapi | news_API_request")
                else: print("CRITICAL | failure to attempt contact with newsapi | news_API_request")
                return None
            if api.status_code != 200:
                if log: logger.error("ERROR | failure with newsapi, status_code = " + str(api.status_code) + " | news_API_request")
                else: print("ERROR | failure with newsapi, status_code = " + str(api.status_code) + " | news_API_request")
                checks[a] = True
            #attempt to contact the newsAPI
            else:
                data = json.loads(api.text)
                checks[a] = data["totalResults"] - 100 * page <= 0
                #verify if there are additional results for this term
                for item in data["articles"]:
                    if item["title"] in list(remove.keys()):
                        if log: logger.info("INFO | article already seen, " + item["title"] + " | news_API_request")
                        else: print("INFO | article already seen, " + item["title"] + " | news_API_request")
                    #ignore articles that have already been seen (indicated by their presence in remove)
                    else:
                        description = item["description"].replace("<ol><li>", "").replace("</li><li>", "").replace("\r", "").replace("\n", "").replace("\xa0\xa0", " - ").replace(item["title"], "")
                        title = item["title"].replace(" -media", "").replace(" - Reuters Australia", "").replace(" - Reuters", "").replace(" - draft", "")
                        #format the title and content of each article
                        temp_news.append({"title" : title, "content" : description + " [" + item["url"] + "]"})
                        remove[item["title"]] = datetime.today().strftime("%Y-%m-%d")
                    #add a new article to news and remove
    if len(temp_news) == 0:
        if log: logger.error("ERROR | no success with any attempts to obtain more articles | news_API_request")
        else: print("ERROR | no success with any attempts to obtain more articles | news_API_request")
        return None
    news = temp_news
    date2 = (datetime.strptime(date, "%Y-%m-%d") - datetime(1900, 1, 1)).total_seconds()
    clear = []
    for item in remove:
        if (datetime.strptime(remove[item], "%Y-%m-%d") - datetime(1900, 1, 1)).total_seconds() < date2:
            if log: logger.info("INFO | removing outdated item from remove, " + item + " | news_API_request")
            else: print("INFO | removing outdated item from remove, " + item + " | news_API_request")
            clear.append(item)
    for item in clear:
        del remove[item]
    #remove elements of remove that are no longer relevant to the current date
    if log: logger.debug("DEBUG | news_API_request successfully completed | news_API_request")
    else: print("DEBUG | news_API_request successfully completed | news_API_request")
    return True


def update_news(update_interval : str = None, update_name : str = None, *args, repeat : bool = False, log : bool = True, **kwargs) -> None:
    '''a function to schedule updates to news articles'''

    if type(log) != bool:
        log = True
    if log:
        log = "logging" in globals() and "logger" in globals()
        if not log:
            print("WARNING | unable to log | update_news")
    #verify if logging is enabled

    if log: logger.debug("DEBUG | update_news called successfully | update_news")
    else: print("DEBUG | update_news called successfully | update_news")

    global sched
    if "sched" not in globals():
        if log: logger.warning("WARNING | sched not imported | update_news")
        else: print("WARNING | sched not imported | update_news")
        try:
            import sched
        except:
            if log: logger.critical("CRITICAL | sched not in system path | update_news")
            else: print("CRITICAL | sched not in system path | update_news")
            return None
    global time
    if "time" not in globals():
        if log: logger.warning("WARNING | time not imported | update_news")
        else: print("WARNING | time not imported | update_news")
        try:
            import time
        except:
            if log: logger.critical("CRITICAL | time not in system path | update_news")
            else: print("CRITICAL | time not in system path | update_news")
            return None
    global datetime
    if "datetime" not in globals():
        if log: logger.warning("WARNING | datetime not imported | update_news")
        else: print("WARNING | datetime not imported | update_news")
        try:
            from datetime import datetime
        except:
            if log: logger.critical("CRITICAL | datetime not in system path | update_news")
            else: print("CRITICAL | datetime not in system path | update_news")
            return None
    global news_API_request
    if "news_API_request" not in globals():
        if log: logger.warning("WARNING | covid_update not imported | update_news")
        else: print("WARNING | covid_update not imported | update_news")
        try:
            from covid_news_handling import news_API_request
        except:
            if log: logger.critical("CRITICAL | covid_news_handling not in system path | update_news")
            else: print("CRITICAL | covid_news_handling not in system path | update_news")
            return None
    #verify if necessary functions are present

    global updates
    if "updates" not in globals():
        if log: logger.warning("WARNING | global updates not present | update_news")
        else: print("WARNING | global updates not present | update_news")
        updates = []
    if type(updates) != list:
        if log: logger.warning("WARNING | invalid type for global updates | update_news")
        else: print("WARNING | invalid type for global updates | update_news")
        updates = []
    for a in range(len(updates) -1, -1, -1):
        if type(updates[a]) != dict:
            if log: logger.warning("WARNING | invalid type for element in updates | update_news")
            else: print("WARNING | invalid type for element in updates | update_news")
            updates.pop(a)
        elif list(updates[a].keys()) != ["time", "time2", "type", "title", "content", "event", "repeat"]:
            if log: logger.warning("WARNING | invalid format for element in updates | update_news")
            else: print("WARNING | invalid format for element in updates | update_news")
            updates.pop(a)
    global schedule
    if "schedule" not in globals():
        if log: logger.warning("WARNING | global schedule not present | update_news")
        else: print("WARNING | global schedule not present | update_news")
        schedule = sched.scheduler(time.time, time.sleep)
    elif type(schedule) != type(sched.scheduler(time.time, time.sleep)):
        if log: logger.warning("WARNING | invalid type for global schedule | update_news")
        else: print("WARNING | invalid type for global schedule | update_news")
        schedules = sched.scheduler(time.time, time.sleep)
    #verify necessary globals

    if update_interval == None:
        if log: logger.warning("WARNING | update_interval not given | update_news")
        else: print("WARNING | update_interval not given | update_news")
        return None
    update_interval = str(update_interval).replace("%3A", ":")
    try:
        update_interval2 = datetime.strptime(update_interval, "%H:%M")
    except:
        if log: logger.warning("WARNING | invalid format for update_interval | update_news")
        else: print("WARNING | invalid format for update_interval | update_news")
        return None
    if update_name == None:
        if log: logger.warning("WARNING | update_name not given | update_news")
        else: print("WARNING | update_name not given | update_news")
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
        if log: logger.info("INFO | an update with this name already exists, " + update_name2 + " | update_news")
        else: print("INFO | an update with this name already exists, " + update_name2 + " | update_news")
        update_name2 = update_name + " (" + str(a) + ")"
        a += 1
    #ensure the update_name is unique
    if len(args) > 0:
        if log: logger.info("INFO | too many non-keyword arguements | update_news")
        else: print("INFO | too many non-keyword arguements | update_news")
    if type(repeat) != bool:
        if log: logger.warning("WARNING | invalid type for repeat | update_news")
        else: print("WARNING | invalid type for repeat | update_news")
        return None
    if len(kwargs) > 0:
        if log: logger.info("INFO | unexpected keyword arguments | update_news")
        else: print("INFO | unexpected keyword arguments | update_news")
    #verify given arguements


    update_interval2 = time.time() + ((update_interval2 - datetime(1900, 1, 1)).total_seconds() - (time.time() % (24 * 60 * 60))) % (24 * 60 * 60)
    #calculate the desired time from the update_interval
    event = schedule.enterabs(update_interval2, 1, news_API_request, kwargs = {"update_name" : update_name2})
    #schedule the calling of news_API_request
    updates.append({"time" : update_interval2, "time2" : update_interval, "type" : 1, "title" : update_name2, "content" : update_interval + ", news articles", "event" : event, "repeat" : repeat})
    #add an appropriate update to updates
    if log: logger.info("INFO | news article update set for " + str(update_interval2) + "(" + update_interval + ") | update_news")
    else: print("INFO | news article update set for " + str(update_interval2) + " (" + update_interval + ") | update_news")
    if log: logger.debug("DEBUG | update_news successfully completed | update_news")
    else: print("DEBUG | update_news successfully completed | update_news")
    return True
