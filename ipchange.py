# This program is created to change the IP address of the computer using a VPN service. It can be used to enhance privacy and security while browsing the internet, as well as to 
# access geo-restricted content. The program will connect to a VPN server and change the IP address of the computer to one provided by the VPN service.
import subprocess
import time
import os
import sys
import platform
import socket
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options

# Configure logging
logging.basicConfig(filename='ipchange.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')