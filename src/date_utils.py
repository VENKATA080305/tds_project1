import datetime

def count_wednesdays():
    """Counts Wednesdays in the current month"""
    today = datetime.date.today()
    first_day = today.replace(day=1)
    wednesdays = sum(1 for i in range(31) if (first_day + datetime.timedelta(days=i)).weekday() == 2 and (first_day + datetime.timedelta(days=i)).month == today.month)
    
    return {"status": f"{wednesdays} Wednesdays counted"}, 200
