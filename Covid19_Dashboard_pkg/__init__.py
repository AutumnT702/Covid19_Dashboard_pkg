import main
from main import startup
#import essential functions

print("DEBUG | calling startup | init")
app = startup()
#ensure the program is initiated succesfully (all global variables and functions correctly set)

log = False
try:
    logging = main.logging
    logger = main.logger
    log = True
except:
    print("ERROR | logging framework not established | init")
#attempt to establish logging framework

if app == None:
    if log: logger.critical("CRITICAL | startup failed | init")
    else: print("CRITICAL | startup failed | init")
else:
    if log: logger.debug("DEBUG | startup successfully returned | init")
    else: print("DEBUG | startup successfully returned | init")
    #identify if startup completed successfully
    if log: logger.info("INFO | starting app on http://127.0.0.1:5000/index| init")
    print("INFO | starting app on http://127.0.0.1:5000/index | init")
    if __name__ == "__main__":
        app.run()
        #launch the covid dashboard
