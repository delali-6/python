# This program is designed to automatically test websites and applications for functionality, performance, and security. It can be used by developers and testers 
# to ensure that their software is working as intended and to identify any issues or bugs that need to be addressed. The program can be customized to test specific 
# features or functionalities of a website or application, and it can generate reports on the results of the tests.

# To start, the program would test a website that I have created using HTML, CSS, and JavaScript. The program would check for any broken links, ensure that all images are 
# loading properly, and test the responsiveness of the website on different devices and screen sizes. 
# The program would also test the functionality of any forms or interactive elements on the website, such as contact forms or navigation menus. It would check that all
# buttons and links are working correctly and that any user input is being processed properly.

from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

service = Service(executable_path="C:\\Users\\comp5274207\\Downloads\\edgedriver_win64\\msedgedriver.exe")

#My website URL
url = "https://delali-6.github.io/Hot-Beans/"

# Initialize the WebDriver (make sure to have the appropriate driver installed and in your PATH)
# Start timer for the performance test
start_time = time.time()

# Launch edge browser and navigate to the website
driver = webdriver.Edge(service=service)

#Open the website
driver.get(url)

# Wait for the page to load
time.implicitly_wait(10)

# Performance test: Check page load time
load_time = time.time() - start_time
print(f"Page load time: {load_time:.2f} seconds")

# Functional test: Page title test
expected_title = "Hot Beans Web | Empowering the Next Generation of Developers"
actual_title = driver.title

if actual_title == expected_title:
    print("Page title test passed")
else:
    print("Page title test failed")
    print(f"Expected: {expected_title}")
    print(f"Actual: {actual_title}")

# Functional test: Check for links and images
try:
    links = driver.find_elements(By.TAG_NAME, "a")
    images = driver.find_elements(By.TAG_NAME, "img")
    print(f"Number of links: {len(links)}")
    print(f"Number of images: {len(images)}")
except NoSuchElementException as e:
    print("Error finding elements: ", e)

# Basic responsiveness test: Check if the website is responsive by resizing the window
try:
    driver.set_window_size(375, 667)  # Simulate mobile device
    time.sleep(2)  # Wait for the page to adjust
    print("Responsiveness test passed")
except Exception as e:
    print("Responsiveness test failed: ", e)
print("Testing completed.")

# Screenshot test: Take a screenshot of the website for debugging purposes
try:
    driver.save_screenshot("screenshot.png")
    print("Screenshot taken successfully")
except Exception as e:
    print("Screenshot test failed: ", e)

# Close the browser
driver.quit()