"""Conditions:

1) For each flight, `pricing_function` will be run once per (simulated) day to set that day's ticket price. 

2) The seats you don't sell today will be available to sell tomorrow, unless the flight leaves that day.

3) Your `pricing_function` is run for one flight at a time, and it takes following inputs:
    - **Number of days until the flight**
    - **Number of seats they have left to sell**
    - **A variable called `demand_level` that determines how many tickets you can sell at any given price. **

4) The quantity you sell at any price is:
                                quantity_sold = demand_level - price

5) Ticket quantities are capped at the number of seats available.

6) Your function will output the ticket price.

7) You learn the `demand_level` for each day at the time you need to make predictions for that day. 
    For all days in the future, you only know `demand_level` will be drawn from the uniform distribution between 100 and 200.  
    So, for any day in the future, it is equally likely to be each value between 100 and 200.

8) 
"""

from random import uniform
from math import floor
import numpy as np

history_price = []
history_tickets_sold = []
history_days_left = []
var_demand_level = 100 ** 2 / 12
exp_demand_level = 150

def get_demand_level():
    demand_level = uniform(100, 200)
    return demand_level


def pricing_function(days_left, tickets_left, demand_level):
    if len(history_days_left) == 0:
        gap = demand_level - floor(demand_level)
        p = int(floor(demand_level)) - var_demand_level/exp_demand_level - gap*5
        print(p)
        print(tickets_left)
        return int(p)
    elif days_left == 1 & tickets_left != 0:
        gap = demand_level - floor(demand_level)
        print(tickets_left)
        return 110 + var_demand_level/exp_demand_level + gap*5
    else:
        gap = demand_level - floor(demand_level)
        p = int(floor(demand_level)) - var_demand_level/exp_demand_level - gap*5
        quantity_demanded = floor(max(0, p - demand_level))
        q = min(quantity_demanded, tickets_left)
        price = get_price(p, q, history_price, history_tickets_sold, demand_level)
        print(price)
        print(demand_level)
        print(tickets_left)
        return int(price)
    

def get_price(p, q, x, y, demand_level):
    x_np = np.array(history_price)
    y_np = np.array(history_tickets_sold)
    prices = np.multiply(x_np, y_np)
    max_revenue = max(prices)
    if p * q >= max_revenue:
        return p
    else:
        place = np.where(prices == max_revenue)[0][0]
        max_price = x_np[place]
        quantity_demanded = floor(max(0, p - demand_level))
        if quantity_demanded == 0:
            return max_price
        else:
            return p
        

def store_history_data(days_left, price, tickets_sold):
    history_price.append(price)
    history_tickets_sold.append(tickets_sold)
    history_days_left.append(days_left)
    
def _tickets_sold(p, demand_level, max_qty):
        quantity_demanded = floor(max(0, p - demand_level))
        return min(quantity_demanded, max_qty)


def simulate_revenue(days_left, tickets_left, pricing_function, rev_to_date=0):
    if (days_left == 0) or (tickets_left == 0):
        return rev_to_date
    else:
        demand_level = get_demand_level()
        p = pricing_function(days_left, tickets_left, demand_level)
        q = _tickets_sold(demand_level, p, tickets_left)
        store_history_data(days_left, p, q)
        return simulate_revenue(days_left = days_left-1, 
                              tickets_left = tickets_left-q, 
                              pricing_function = pricing_function, 
                              rev_to_date = rev_to_date + p * q,
                             )

print(simulate_revenue(days_left=7, tickets_left=50, pricing_function=pricing_function))