# Shipping Program
# A simple Shipping Price Calculation program. This project is a prompt from Codecacademy completed in Python by John Adam Gordon Whited on 3/31/2020.

# Variable declaration for the cost of Premium Ground Shipping
premium_ground = 125.00

# This function will determine the cost of ground shipping a package depending upon a user input of Weight
def cost_of_ground(weight):
  if weight <= 2.0:
    return (weight * 1.50) + 20.00
  elif weight > 2.0 and weight <= 6.00:
    return (weight * 3.00) + 20.00
  elif weight > 6.0 and weight <= 10.00:
    return (weight * 4.00) + 20.00
  else:
    return (weight * 4.75) + 20.00

# This function will determine the cost of drone shipping a package depending upon a user input of Weight
def cost_of_drone(weight):
  if weight <= 2.0:
    return (weight * 4.50)
  elif weight > 2.0 and weight <= 6.00:
    return (weight * 9.00)
  elif weight > 6.0 and weight <= 10.00:
    return (weight * 12.00)
  else:
    return (weight * 14.25)

# This function will determine the lowest cost of shipping a package and tell that to the user, as well as their price.
def lowest_cost(weight):
  if cost_of_ground(weight) < cost_of_drone(weight) and cost_of_ground(weight) < premium_ground:
    return "Ground shipping is the cheapest option. Here is your price: " + str(cost_of_ground(weight))
  elif cost_of_drone(weight) < cost_of_ground(weight) and cost_of_drone(weight) < premium_ground:
    return "Drone shipping is the cheapest option. Here is your price: " + str(cost_of_ground(weight))
  elif premium_ground < cost_of_drone(weight) and premium_ground < cost_of_ground(weight):
    return "Premium shipping is the cheapest option. Here is your price: " + str(premium_ground)
  
# Testing the lowest_cost() function with values of weight values 41.5, 4.8, and 2.
print(lowest_cost(41.5))
print(lowest_cost(4.8))
print(lowest_cost(2))

  
