#DATIME MODULE

def date():
    import datetime
    now=datetime.datetime.now
    return (now().date())

def time():
    import datetime
    now=datetime.datetime.now
    return (now().time())

    


