import csv
import numpy as np


def getDataSource(dataPath):
    marks = []
    daysPresent = []
    with open(dataPath) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            marks.append(float(row["Marks In Percentage"]))
            daysPresent.append(int(row["Days Present"]))
    return {
        "x": marks, "y": daysPresent
    }


def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation bertween Marks & Days Present :\t", correlation[0, 1])


def main():
    dataPath = "./data2.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)


main()
