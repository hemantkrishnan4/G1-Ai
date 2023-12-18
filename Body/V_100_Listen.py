#Import Necessary Packages
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.by import By
import warnings
from selenium.webdriver.service import Service

#Ignore unnecessary warnings
warnings.simplefilter("ignore")

try:
    #Define the URL
    url = "https://dictation.io/speech"

    #Set up Chrome options
    chrome_driver_path = 'C:\\webdrivers\\chromedriver.exe'
    chrome_options = Options()
    