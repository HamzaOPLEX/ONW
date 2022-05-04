from configs.config_vars import *

def GenrateAppID(type):
    id = APP_TYPE[type].objects.all().last().id + 1
    return APP_ID_NAME[type] + str(id).zfill(4)