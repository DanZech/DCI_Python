from data_warehouse2 import stock
from datetime import datetime
import pytz


for i in stock:
    date_of_stock_datetime = datetime.strptime(
        date_of_stock, '%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.utc)
    current_datetime = get_current_utc_datetime()
    age_in_days = (current_datetime - date_of_stock_datetime).days
    #return age_in_days
    print(age_in_days)
    
    
