#This is a program that allows customers to build their own pizza by answering a series of questions about their preferences. 
# The program will then generate a summary of the customer's pizza order based on their answers and calculate the total cost.
price = 0 #This variable will keep track of the total cost of the pizza order.
print("Hello customer")
print ("Complete the form to make and order your pizza")
size = input("""What size pizza would you like? 
             - small 
             - medium 
             - large) """)
while size.lower() not in ["small", "medium", "large"]:
    print ("Invalid input. Please enter 'small', 'medium', or 'large'.")
    size = input("""What size pizza would you like? 
             - small 
             - medium 
             - large) """)
if size.lower() == "small":
    price += 6
elif size.lower() == "medium":
    price += 8
else:    price += 10
base = input("""Choose your base: 
             - Classic crust....+ £0
             - Thin & crispy....+ £1
             - Deep pan....+ £2) """)
while base.lower() not in ["classic crust", "thin & crispy", "deep pan"]:
    print ("Invalid input. Please enter 'classic crust', 'thin & crispy', or 'deep pan'.")
    base = input("""Choose your base: 
             - Classic crust....+ £0
             - Thin & crispy....+ £1
             - Deep pan....+ £2) """)
if base.lower() == "classic crust":
    price += 0
elif base.lower() == "thin & crispy":
    price += 1
else:    price += 2
toppings = input("How many toppings would you like? Each topping is + £1.50 ")
price += int(toppings) * 1.5
eatinOrTakeaway = input("""Would you like to eat in or take away? 
                        - Eat in....+ £2 Service
                        - Take away....+ £0) """)
while eatinOrTakeaway.lower() not in ["eat in", "take away"]:
    print ("Invalid input. Please enter 'eat in' or 'take away'.")
    eatinOrTakeaway = input("""Would you like to eat in or take away? 
                        - Eat in....+ £2 Service
                        - Take away....+ £0) """)
if eatinOrTakeaway.lower() == "eat in":
    price += 2
else:    price += 0
print ("""Thank you for your order! Here is a summary of your pizza order:
    - Size: """ + size
    + "\n- Base: " + base
    + "\n- Toppings: " + toppings
    + "\n- Eat in or Takeaway: " + eatinOrTakeaway
    + "\n- Total Price: £" + str(price)
       )
discount = input("Do you have a discount code? (yes or no) ")
if discount.lower() == "yes":
    code = input("Please enter your discount code: ")
    if code == "PIZZA10":
        price = price - price*0.2
        print ("Congratulations! You have received a 20% discount. Your new total price is: £" + str(price))
    else:
        print ("Sorry, that discount code is not valid.")
if eatinOrTakeaway.lower() == "eat in":
    print ("Your order will be ready shortly. Please wait at your table and a server will bring it to you.")
else:
    print ("Your order will be ready for pickup in 15 minutes. Please come to the counter to collect your pizza.")