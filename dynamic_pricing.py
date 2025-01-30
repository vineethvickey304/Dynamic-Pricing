import datetime
import random
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta

# Time-based Dynamic Pricing
def time_based_pricing(base_price):
    now = datetime.datetime.now()
    if 8 <= now.hour < 12:
        return base_price * 1.2  # Morning increase
    elif 12 <= now.hour < 18:
        return base_price * 1.5  # Afternoon increase
    return base_price

# Demand-based Dynamic Pricing
def demand_based_pricing(base_price, demand_factor):
    demand_multiplier = random.uniform(0.8, 1.2) * demand_factor
    return base_price * demand_multiplier

# Competitive-based Dynamic Pricing
def competitive_based_pricing(base_price, competitor_prices, max_increase=20):
    avg_competitor_price = np.mean(competitor_prices)
    dynamic_price = avg_competitor_price * (1 + (max_increase / 100))
    return min(dynamic_price, base_price * (1 + max_increase / 100))

# Surge Pricing
def surge_pricing(base_price, demand_factor):
    if demand_factor < 1.0:
        surge_multiplier = 1.0
    elif 1.0 <= demand_factor < 1.5:
        surge_multiplier = 1.5
    else:
        surge_multiplier = 2.0
    return base_price * surge_multiplier

if __name__ == "__main__":
    base_price = 100
    competitor_prices = [95, 98, 105, 100, 102]
    demand_factor = 1.2
    
    print("Time-Based Pricing:", time_based_pricing(base_price))
    print("Demand-Based Pricing:", demand_based_pricing(base_price, demand_factor))
    print("Competitive-Based Pricing:", competitive_based_pricing(base_price, competitor_prices))
    print("Surge Pricing:", surge_pricing(base_price, demand_factor))
