name = input("What is your name? ")
print ("Hello, " + name + "! Nice to meet you.")
print ("This is a Python file.")
print ("Python is a great programming language and is used for web development, data analysis, artificial intelligence, and more..")
userAnswer = input("Would you like to learn more about Python?")
if userAnswer.lower() == "yes":
    print ("Great! Python is a versatile language that is easy to learn and has a large community of developers. You can find many resources online to help you get started.");
else:    print ("No problem! If you ever change your mind, Python is a great language to learn and can open up many opportunities in the tech industry."); response = input(""); print ("Anytime!");
math1 = input("For example, python can perform a simple math problem. What is 5 + 3?")
if math1 == "8":
    print ("Correct! 5 + 3 is indeed 8.")
    print("This is just one of the many brilliant things about Python - it can be used for simple tasks like math problems, as well as complex applications like machine learning and data analysis.")
    print ("If you're interested in learning more about Python, there are many online resources available, including tutorials, courses, and forums where you can ask questions and get help from other Python developers. However I will provide some links to websites that can help you get started:")
    print ("1. Python.org - The official website for Python, where you can find documentation, tutorials, and downloads: https://www.python.org/")
    print ("2. Codecademy - An interactive platform that offers Python courses for beginners: https://www.codecademy.com/learn/learn-python-3")
    print ("3. Coursera - An online learning platform that offers Python courses from top universities and institutions: https://www.coursera.org/courses?query=python")
    print ("4. Stack Overflow - A popular forum where you can ask questions and get help from other Python developers: https://stackoverflow.com/questions/tagged/python")
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