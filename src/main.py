import pandas as pd 
from datetime import timedelta, datetime, date
import time


class Planning_Alfredv1:
    def __init__(self):
        self.planning = pd.read_csv("planning.csv", index_col = [0])
    
    def get_day(self):
        today = time.strftime("%d:%m:%Y")
        get_today = self.planning.loc[self.planning["date"] == today].shape[0]
        if(get_today != 0):
            colomns_today = self.planning["date"].shape[0] - 1
            return(colomns_today)
        else:
            colomns_today = self.planning["date"].shape[0]
            self.planning.loc[colomns_today, "date"] = today
            self.planning.to_csv("planning.csv")
            return(colomns_today)

    def add_activity(self, colomns_today, activity):
        i = 1
        while(True):
            activity_nbr = "activity" + str(i)
            heure_actuelle = time.strftime("%H:%M:%S")
            #verif si la colonne existe sinon on la crée
            if (activity_nbr not in self.planning.columns):
                self.planning.loc[colomns_today, activity_nbr] = None
            #si la colonne est vide on met l'activite est l'heure actuelle
            if pd.isnull(self.planning.iloc[colomns_today][activity_nbr]) == True:
                self.planning.loc[colomns_today, activity_nbr] = activity + "/" + heure_actuelle + "/"
                self.planning.to_csv("planning.csv")
                return(f"tu commence a {activity}")
            #si elle a deja commencer on affiche le chrono
            else:
                get_heure_activity = self.planning.iloc[colomns_today][activity_nbr].split("/")
                if (get_heure_activity[2] == ''):
                    array_planning = self.planning.iloc[colomns_today][activity_nbr].split("/")
                    array_planning = array_planning[1].split(":")
                    heure = timedelta(hours=int(array_planning[0]), minutes=int(array_planning[1]))
                    heure_actuelle = timedelta (hours = time.localtime().tm_hour, minutes = time.localtime().tm_min)
                    chrono = (heure_actuelle - heure)
                    return(chrono)
                i+= 1
    def stop_activity(self, colomns_today, activity):
        i = 1
        while(True):
            heure_actuelle = time.strftime("%H:%M:%S")
            activity_nbr = "activity" + str(i)

            if (activity_nbr not in self.planning.columns):
                return("aucune instance est en cour")
            if isinstance(self.planning.iloc[colomns_today][activity_nbr], float):
                return("aucune instance est en cour")
            get_heure_activity = self.planning.iloc[colomns_today][activity_nbr].split("/")
            if get_heure_activity[2] == '':
                get_heure_activity[2] = heure_actuelle
                get_heure_activity = "/".join(get_heure_activity)
                self.planning.loc[colomns_today, activity_nbr] = None
                self.planning.loc[colomns_today, activity_nbr] = get_heure_activity
                self.planning.to_csv("planning.csv")
                return(f"tu ne fais plus de {activity}")
            i+=1

