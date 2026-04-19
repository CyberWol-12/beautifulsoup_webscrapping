## Web Scraping Projects Collection
# Hello! Thank you for visiting my README 😊

**This repository is a collection of my web scraping projects built using Python and BeautifulSoup.**

#  Quotes to Scrape - Web Scraping Project

## Description

This project is a Python-based web scraper that extracts quotes, authors, tags, and author profile links from Quotes to Scrape.
It demonstrates how to scrape multi-page data and store it in a structured format for analysis.

## Features

* Scrapes quotes from multiple pages (1–10)
* Extracts quote text and author names
* Collects tags associated with each quote
* Retrieves author profile links
* Stores data in CSV format

##  Tech Stack

* Python
* Requests
* BeautifulSoup
* Pandas

##  How It Works

* Sends HTTP requests to each page of the website
* Parses HTML using BeautifulSoup
* Extracts data using class selectors
* Uses a loop to handle pagination
* Stores extracted data in a list
* Converts data into a Pandas DataFrame
* Exports the data to a CSV file




##  Output

The script generates a file named **quotes.csv** containing:

* Quotes
* Author
* Author_link
* Tags
