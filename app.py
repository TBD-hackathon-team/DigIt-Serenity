import json
# import Queue

import pandas as pd
# import matplotlib.pyplot as plt
from urllib2 import Request, urlopen, URLError
import requests


def main():
    print "this is main"

    url = "https://globalcurrencies.xignite.com/xGlobalCurrencies.json/GetHistoricalRatesRange?Symbol=BTCUSD&PriceType=Mid&StartDate=10/20/2017&EndDate=10/27/2017&PeriodType=Daily&FixingTime=22:00&_token=AE4A02E0271A4E77B78B314AEE9A132D"

    response = requests.get(url).json()
    # print response
    print json.dumps(response, indent=4)



if __name__ == '__main__':
    main()