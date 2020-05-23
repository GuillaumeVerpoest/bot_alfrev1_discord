import pandas as pd 
import numpy as np 
from time import strftime 
planning = pd.read_csv("planning.csv")
def planning_day():
    date_du_jour = strftime("%d:%m:%Y")

    # ajoute une colone pour ouvrir la journée
    if (planning.loc[planning["Date"] == date_du_jour].shape[0] == 0):
        columns_day = planning.shape[0]
        planning.loc[columns_day, "Date"] = date_du_jour
        planning.to_csv("planning.csv")
        return(columns_day)
    # et si la journne est deja ouvert on ne la recree pas
    elif (planning.loc[planning["Date"] == date_du_jour].shape[0] == 1): 
        columns_day = planning.shape[0]
        return(columns_day-1)
    else:
        print("error bad create column_day")
    

def ajout_planning(categorie, columns_day):
    heure_actuelle = strftime("%H%M%S")
    # je verifie qu'elle est vide et je lui met le debut de la duree 
    if (pd.isnull(planning.loc[columns_day, categorie])) == True: 
        planning.loc[columns_day, categorie] = "en court start:" + heure_actuelle
        planning.to_csv("planning.csv")
    # si c'est pas le cas je recupere le debut debut de la duree 
    # et je le soutrait a l'heure actuelle
    elif (pd.isnull(planning.loc[columns_day, categorie])) == False:            
        index = planning.loc[columns_day, categorie]
        heure = index[15]+index[16]+index[17]+index[18]+index[19]+index[20]
        temp_passe = (int(heure_actuelle) - int(heure)) / 60
        return(temp_passe)

def stop(temps_passe, columns_day, categorie):
    planning.loc[columns_day, categorie] = temps_passe

temps_passe = ajout_planning("Code", planning_day())
stop(temps_passe, planning_day,"Code")


#planning.to_csv("planning.csv")
