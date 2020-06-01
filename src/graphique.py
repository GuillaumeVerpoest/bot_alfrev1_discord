import pandas as pd 
from datetime import timedelta, datetime, date
import time
import matplotlib.pyplot as plt
from func import trans_str_to_delta_time

class Graphique_Alfredv1:
    def __init__(self):
        self.planning = pd.read_csv("planning.csv", index_col = [0])
    
    def journalier(self):
        today = time.strftime("%d:%m:%Y")
        get_day = self.planning.loc[self.planning["date"] == today].shape[0]-1
        i = 1
        array_labels = []
        array_sizes = []
        while(True):
            activity_nbr = "activity" + str(i)
            if (activity_nbr not in self.planning.columns):
                break
            array_activity = self.planning.loc[get_day, activity_nbr].split("/")
            array_labels.append(f"{array_activity[0]} => \n{array_activity[1]}\n{array_activity[2]}")
            hours_start = trans_str_to_delta_time(array_activity[1])
            hours_end = trans_str_to_delta_time(array_activity[2])
            chrono = str(hours_end - hours_start)
            print(chrono)
            chrono = chrono[:4].replace(':','.')
            chrono = float(chrono)/24
            array_sizes.append(chrono)
            i+=1
        add=0
        for x in array_sizes:
            add+= x 
        add = 1 - add
        array_sizes.append(add)
        array_labels.append("24H")
           
        labels = tuple(array_labels)
        sizes = array_sizes
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', counterclock=False, startangle=90)
        ax1.axis('equal')
        plt.show()

Graphique_Alfredv1().journalier()