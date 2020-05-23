from time import strftime
import pandas as pd

class Planning_Alfredv1:

    def __init__(self):
        self.planning = pd.read_csv("planning.csv")

    def planning_day(self):

        date_of_day = strftime("%d:%m:%Y")
        get_day = self.planning.loc[self.planning["Date"] == date_of_day].shape[0]

        if (get_day == 0):
            return(get_day)
        else:
            return(get_day,"slt")

    def add_planning(self, categorie, get_day):
        hour_now = strftime("%H%M%s")
        cheked_emply = pd.isnull(self.planning.loc[get_day, categorie])

        if(cheked_emply == True):
            self.planning.loc[get_day, categorie] = "en court start:" + hour_now
            self.planning.to_csv("planning.csv")
        else:
            print("temp passe")

day = Planning_Alfredv1().planning_day()
print(day)

