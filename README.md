# yesss-scraper

This is a quick and dirty Python script that logs into the [Yesss! Kontomanager](https://www.yesss.at/kontomanager.at/) and downloads data from all the 'Einzelverbindungsnachweis' pages into a single convenient CSV file.

## Setup

 1. Install the required packages:
    ```
    pip install -r requirements.txt
    ```
 2. Enter your credentials in the `secret.py` file.
 3. Please note that this script uses Selenium to gather web data. You may need to [download the latest chromedriver.exe](https://googlechromelabs.github.io/chrome-for-testing/) and place it in this directory.
 4. Run `yes-scraper.py` with Python 3.


