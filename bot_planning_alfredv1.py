from time import strftime
from datetime import timedelta
from datetime import datetime
import time
import pandas as pd

class Planning_Alfredv1:

    def __init__(self):
        self.planning = pd.read_csv("planning.csv", index_col = [0])

    def planning_day(self):

        date_of_day = strftime("%d:%m:%Y")
        get_day = self.planning.loc[self.planning["Date"] == date_of_day].shape[0]
        line_today = self.planning.shape[0]

        if (get_day == 0):
            self.planning.loc[line_today, "Date"] = date_of_day
            self.planning.to_csv("planning.csv")
            return(line_today)
        else:
            return(line_today-1)

    def add_planning(self, categorie, day):
        hour_now = timedelta (hours = time.localtime().tm_hour, minutes = time.localtime().tm_min)
        cheked_emply = pd.isnull(self.planning.loc[day, categorie])

        if(cheked_emply == True):
            self.planning.loc[day, categorie] = hour_now
            self.planning.to_csv("planning.csv")
        else:
            get_hour_in_planning = self.planning.loc[day, categorie].split(':')
            hour = timedelta (hours = int(get_hour_in_planning[0]), minutes = int(get_hour_in_planning[1]))
            return(hour_now - hour)

    def stop(self, day, categorie, time):
        cheked_emply = pd.isnull(self.planning.loc[day, categorie])
        hour2 = timedelta(hours= 0, minutes=0)
        if(cheked_emply == False):
            get_hour_in_planning2 = self.planning.loc[day,"temp " + categorie].split(':')
            hour2 = timedelta (hours = int(get_hour_in_planning2[0]), minutes = int(get_hour_in_planning2[1]))
        print(hour2)
        self.planning.loc[day,"temp "+ categorie] =  hour2 + time
        self.planning.loc[day, categorie] = None
        self.planning.to_csv("planning.csv")

alfred = Planning_Alfredv1()
day = alfred.planning_day()
time = alfred.add_planning("Code", day)
print(time)
alfred.stop(day, "Code", time)



