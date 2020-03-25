#!/usr/bin/env python3

from pytube import Playlist

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def initialize_driver(args):
    driver_configuration = webdriver.ChromeOptions()
    driver_configuration.add_argument('--headless')
    if(args.d):
        prefs = {'download.default_directory' : args.d}
        driver_configuration.add_experimental_option('prefs', prefs)
    if(args.cdp):
        driver = webdriver.Chrome(executable_path = args.cdp, options = driver_configuration)
    else:
        """ Provide path here so you don't have to pass it every time you run the script. """
        driver = webdriver.Chrome(executable_path = r'd:\chromedriver_win32\chromedriver.exe', options = driver_configuration)
    return driver

def get_playlist_urls(args):
    return Playlist(args.playlist_url).parse_links()

def automate(driver, urls):
    prefix = 'https://www.youtube.com/'
    driver.get('https://ytmp3.cc/en12/')
    for i in range(len(urls) + 1):
        input_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "input")))
        input_element.send_keys(prefix + urls[i])
        start_conversion_button = driver.find_element_by_id("submit")
        start_conversion_button.click()
        main_window_redirect = driver.window_handles[0]
        download_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttons"]/a[1]')))
        download_button.click()
        driver.switch_to_window(main_window_redirect)
        convert_next_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttons"]/a[3]')))
        convert_next_button.click()

