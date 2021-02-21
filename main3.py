import csv
import numpy as np


def getDataSource(dataPath):
    cups_of_coffee = []
    hours_of_sleep = []
    with open(dataPath) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            cups_of_coffee.append(float(row["Coffee in ml"]))
            hours_of_sleep.append(int(row["sleep in hours"]))
    return {
        "x": cups_of_coffee, "y": hours_of_sleep
    }


def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between Cups of Coffee & Hours of Sleep :\t",
          correlation[0, 1])


def main():
    dataPath = "./data3.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)


main()
