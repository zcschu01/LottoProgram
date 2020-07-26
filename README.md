# LottoProgram
Python program that downloads past Powerball and Mega Millions winning numbers in an easy to read excel format. This project uses the Open Data Socrata API.

## Getting Started
1. Install Dependencies
   * ```pip install pandas``` ```pip install sodapy```
     * [pandas](https://pandas.pydata.org/) is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
       built on top of the Python programming language.
     * [sodapy](https://github.com/xmunoz/sodapy) is a python client for the Socrata Open Data API.
2. Double click the python file to run the program
   * On the first prompt:
     * Enter 'y' or 'Y' to download latest numbers
     * Enter 'n' or 'N' to modify latest numbers for easier to read excel file
### (Optional) Get data you want
- Go to [sodapy](https://github.com/xmunoz/sodapy) to understand how to make API calls and modify this program to get the data you want
- If you plan to make changes, I would ***strongly*** recommend making your own [API token](https://opendata.socrata.com/login)
  - Go to developer profile and register your app
