from time import strftime, localtime
from datetime import timedelta
from datetime import datetime
import time
import pandas as pd

def get_hour_in_planning(index):
    array = index.split(':')
    delta = timedelta(hours = int(array[0]), minutes = int(array[1]))
    return(delta)



class Planning_Alfredv1:

    def __init__(self):
        self.planning = pd.read_csv("planning.csv", index_col = [0])

    def get_planning_day(self):

        date_of_day = strftime("%d:%m:%Y")
        get_day = self.planning.loc[self.planning["Date"] == date_of_day].shape[0]
        line_today = self.planning.shape[0]

        if (get_day == 0):
            self.planning.loc[line_today, "Date"] = date_of_day
            self.planning.to_csv("planning.csv")
            return(line_today)
        else:
            return(line_today-1)

    def add_planning(self, day_planning, categorie):
        hour_of_start = timedelta (hours = time.localtime().tm_hour, minutes = time.localtime().tm_min)

        if(pd.isnull(self.planning.loc[day_planning, categorie]) == True):
            self.planning.loc[day_planning, categorie] = hour_of_start
            self.planning.to_csv("planning.csv")
            return("initialisation du chrono")
        else:
            hour = get_hour_in_planning(self.planning.loc[day_planning, categorie])
            return(hour_of_start - hour)

    def stop(self, day_planning, categorie, time):
        get_hour = timedelta(hours= 0, minutes=0)
        if(pd.isnull(self.planning.loc[day_planning, "temp "+ categorie]) == False):
            get_hour = get_hour_in_planning(self.planning.loc[day_planning,"temp " + categorie])
        self.planning.loc[day_planning,"temp "+ categorie] =  get_hour + time
        self.planning.loc[day_planning, categorie] = None
        self.planning.to_csv("planning.csv")




