def message_to_hq(location, food_location, order_number,restaurant):
  print(f"Hello, someone needs to be sent to {food_location}, take that to {location}. The restaurant is {restaurant} and the order number is {order_number}")
def lost_food():
  location = input("Where are you located?")
  restaurant = input("From which of our many restaurants did you order from?")
  order_number = input("What is your order number?")
  print("Finding food...")
  food_location = "here"
  print("Food found!")
  print("Creating route...")
  message_to_hq(location, food_location, order_number, restaurant)
  print("Route made and your food should be on your way shortly!")

def wrong_order():
  location = input("Where are you located?")
  while True:
    order_number = input("What was your order number?")
    wrong_order_number = input("What was the order number you recieved?")
  
    if wrong_order_number != order_number:
      print("Sorry for the mix up! Order is being sent now.")
      break
    else:
      print("It looks like you put in the same order number, is everything alright?")
      continue
def food_delievery_issue():
  name = input('Hi there!, what is your name? ')
  while True:
    problem = input(f'What is the issue {name}, choose from the following options \n1. Lost food \n2.Appearing as Delievered on the app but it is not \n3. Order came wrong \n' )
    if problem == "1" or problem == "2":
    
      #we want to make a fake little section for like scanning the food right? It won't be actually scanning for it but the code will act like it is. 
      lost_food()
      break
  
    elif problem == "3":
      wrong_order()
      break
    else:
      print("I'm sorry that isn't one of the options. ")
      continue

food_delievery_issue()
