name = input("What is your name? ")
print ("Hello, " + name + "! Nice to meet you.")
print ("This is a Python file.")
print ("Python is a great programming language and is used for web development, data analysis, artificial intelligence, and more..")
userAnswer = input("Would you like to learn more about Python?")
if userAnswer.lower() == "yes":
    print ("Great! Python is a versatile language that is easy to learn and has a large community of developers. You can find many resources online to help you get started.");
else:    print ("No problem! If you ever change your mind, Python is a great language to learn and can open up many opportunities in the tech industry."); response = input(""); print ("Anytime!");
math1 = input("Now, let's do a simple math problem. What is 5 + 3?")
if math1 == "8":
    print ("Correct! 5 + 3 is indeed 8.")
else:
    print ("That's not correct. The correct answer is 8. Do you want to try another math problem?")
    response1 = input("")
    if response1.lower() == "yes":
        print ("Great! Let's try another one. What is 10 - 4?")
        math2 = input("")
        if math2 == "6":
            print ("Correct! 10 - 4 is indeed 6.")
        else:
            print ("That's not correct. The correct answer is 6. Keep practicing and you'll get it!")
    else:
        print ("No problem! If you ever want to practice more math problems, just let me know.")