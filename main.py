#!/usr/bin/env python3

import argparse
import selenium_automation_script as sas

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('playlist_url', help = "Provide a valid youtube playlist URL.")
    parser.add_argument('-d', metavar = 'DESTINATION', help = "Downloads directory. If not provided downloads will be placed in folder set by automated chrome.")
    parser.add_argument('-cdp', metavar = 'PATH', help = "ChromeDriver system path.")
    return parser.parse_args()

def main():
    args = parse_arguments()
    driver = sas.initialize_driver(args)
    urls = sas.get_playlist_urls(args)
    sas.automate(driver, urls)

if __name__ == '__main__':
    main()
        
    