from datetime import datetime, date, time

def get_date_time_own_format():    
    """ 
    Get the current date with a specific Format


    Args:


    Returns:
        date_time(string): String with the date time to in a own specific format.
    """


    dte = 'Date:'
    now = datetime.now()
    yr = str(now.year) + '-'
    mth =  str(now.month) + '-'
    dy = str(now.day) + '-'
    tme = 'Time:'
    hr = str(now.hour) + ':' 
    mt = str(now.minute) + ':'
    scs = str(now.second)
    date_time = dte + yr + mth + dy + tme + hr + mt + scs
    return date_time


def get_date_time_hm():    
    """ 
    Get the current date with a specific Format


    Args:


    Returns:
        date_time(string): String with the date time to in a own specific format.
    """


    dte = 'Date:'
    now = datetime.now()
    yr = str(now.year) + '-'
    mth =  str(now.month) + '-'
    dy = str(now.day) + '-'
    tme = 'Time:'
    hr = str(now.hour) + ':' 
    mt = str(now.minute) 
    date_time = dte + yr + mth + dy + tme + hr + mt
    return date_time



def get_date_and_hour_own_format():
    """ 
    Get the current date and hour with a specific Format


    Args:


    Returns:
        date_time(string): String with the date time to in a own specific format.
    """


    dte = 'Date:'
    now = datetime.now()
    yr = str(now.year) + '-'
    mth =  str(now.month) + '-'
    dy = str(now.day) + '-'
    tme = 'Time:'
    hr = str(now.hour)     
    date_time = dte + yr + mth + dy + tme + hr
    return date_time

if __name__ == "__main__":
    print(get_date_time_own_format())
        

