#buylunch

#import things
import os

os.system("clear")
#Check whether the order is correct
def order_correct():
    print("Is this correct? (Wait for prompt) ")
    os.system("say Is this correct? True or False")
    correctorder = input("True or False: ")
    correctorder = correctorder.lower()
    if correctorder == "true" or correctorder == "yes" or correctorder == "t":
        orderresponse = "GLaD to hear it. Proceed to checkout."
        orderstatus = "Checkout"
    elif correctorder == "false" or correctorder == "no" or correctorder == "f":
        orderresponse = "Oh no! Sorry about that. Please try placing your order again."
        orderstatus = "Failed"
    else:
        orderresponse = "I don't know that response. Please respond 'True' or 'False'."
        orderstatus = "Failed"
    feedbackplacingorder = "You responded " + correctorder + ". " + orderresponse + " Your order status is: " + orderstatus + "."
    print(feedbackplacingorder)
    os.system("say " + feedbackplacingorder)

#Compose Lunch Order
def buy_lunch(main, side, drink):
    print("Your main course is " + main + ". You would like " + side + " on the side. And you would like " + drink + " to drink.")
    os.system("say " + "Your main course is " + main + ". You would like " + side + " on the side. And you would like " + drink + " to drink.")
    order_correct()

#Place the Order (code returns here if failed)
orderstatus = "Placing Order"
while(orderstatus == "Placing Order" or orderstatus == "Failed") and orderstatus != "Checkout" :
    buy_lunch (input("What would you like for your main course? "), input("What would you like for your side? "), input("What would you like to drink? "))

#Checkout - Get cost (WIP)
if(orderstatus == "Checkout"):
    print("Complete")
    exit()
