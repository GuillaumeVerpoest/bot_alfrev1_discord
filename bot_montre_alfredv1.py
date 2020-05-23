from time import gmtime, strftime, sleep
import time
 
def sa_montre(): #affiche l'heure reele
    print(strftime("%H:%M:%S"))
    sleep(1)
    sa_montre()
    