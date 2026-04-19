## Web Scraping Projects Collection
# Hello! Thank you for visiting my README 😊

**This repository is a collection of my web scraping projects built using Python and BeautifulSoup.**

# 1. Quotes to Scrape - Web Scraping Project


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

# 2. Hacker News Scraper - Web Scraping Project

##  Description

This project is a Python-based web scraper that extracts articles, upvotes, authors, comments, and posting time from Hacker News.
It demonstrates how to scrape real-time tech news data and convert it into a structured dataset.

## Features

* Extracts article titles and links
* Collects upvotes (points) for each article
* Retrieves author names
* Captures posting time
* Extracts number of comments
* Handles missing data using exception handling
* Stores data in CSV format

## Tech Stack

* Python
* Requests
* BeautifulSoup
* Pandas

##  How It Works

* Sends an HTTP request to the Hacker News homepage
* Parses HTML using BeautifulSoup
* Extracts article details using class selectors
* Handles missing values using try-except blocks
* Stores data in a list of dictionaries
* Converts data into a Pandas DataFrame
* Exports the dataset to a CSV file

##  Output

The script generates a file named **articles_list.csv** containing:

* Article Name
* Link
* Upvotes
* Author
* Time Posted
* Comments Count


# 3. Fake Jobs Scraper - Web Scraping Project

##  Description

This project is a Python-based web scraper that extracts job listings from Real Python Fake Jobs.
It collects structured job data for analysis and practice purposes.

##  Features

* Extracts job titles
* Collects company names
* Retrieves job locations
* Captures posting time
* Extracts footer details and links
* Handles missing data using exception handling
* Stores data in CSV format

##  Tech Stack

* Python
* Requests
* BeautifulSoup
* Pandas

##  How It Works

* Sends an HTTP request to the website
* Parses HTML using BeautifulSoup
* Extracts job-related information using class selectors
* Handles missing values using try-except blocks
* Stores extracted data in a list of dictionaries
* Converts it into a Pandas DataFrame
* Saves the data into a CSV file

##  Output

The generated dataset contains:

* Title
* Company
* Location
* Time
* Footer
* Footer Link

# 4. Books to Scrape - Web Scraping Project

##  Description

This project is a Python-based web scraper that extracts book details such as name, price, and product links from Books to Scrape.
It is designed to practice scraping structured product data from an e-commerce-style website.

##  Features

* Extracts book names
* Collects product links
* Retrieves book prices
* Handles multiple items from the page
* Stores data in CSV format

##  Tech Stack

* Python
* Requests
* BeautifulSoup
* Pandas

##  How It Works

* Sends an HTTP request to the website
* Parses HTML using BeautifulSoup
* Extracts book details using class selectors
* Stores data in a list of dictionaries
* Converts data into a Pandas DataFrame
* Exports the data into a CSV file

##  Output

The generated dataset contains:

* Name
* Link
* Price

# 5. Love & Flair Scraper - Web Scraping Project
![Love & Flair](images/image5.png)

##  Description

This project is a Python-based web scraper that extracts product data from Love & Flair.
It collects detailed information about activewear products including pricing, availability, colors, sizes, and materials.

##  Features

* Scrapes product links from multiple pages (pagination)
* Extracts product names and prices
* Retrieves stock availability
* Collects available colors and sizes
* Extracts product material information
* Handles missing data using conditional logic
* Stores structured data in CSV format

##  Tech Stack

* Python
* Requests
* BeautifulSoup
* Pandas

##  How It Works

* Sends HTTP requests to multiple product listing pages
* Extracts product links using HTML class selectors
* Removes duplicate links using set()
* Visits each product page individually
* Scrapes detailed product information
* Cleans and structures data (colors, sizes, etc.)
* Stores data in a list of dictionaries
* Converts it into a Pandas DataFrame
* Exports the dataset into a CSV file

##  Output

The generated dataset contains:

* Name
* Price
* Stock
* Color
* Size
* Material
* Product Link

## Author

**Divya Upadhyay 😊😊**








