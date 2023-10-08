import pandas as pd


data = pd.read_csv("data/data.csv", sep=',')


def qualitative_characteristics(column):
    arr = [[0.0 for _ in range(0, 3)] for _ in range(0, 2)]
    for el in column:
        if el == "M":
            arr[0][0] += 1
        elif el == "F":
            arr[0][1] += 1
        else:
            arr[0][2] += 1
    for i in range(0, 3):
        arr[1][i] = round((arr[0][i] / len(column)) * 100, 3)
    return arr


def quantitative_characteristics():
    print("xd")


def main():
    col1 = data.iloc[:, 0]
    first = qualitative_characteristics(col1)
    print(first)


main()
