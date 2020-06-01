from datetime import timedelta, datetime, date


def trans_str_to_delta_time(index):
    index = index.split(":")
    delta = timedelta (hours = int(index[0]), minutes=int(index[1]))
    return(delta)

