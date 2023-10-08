import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/data.csv", sep=',')


def qualitative_characteristics():
    column = data.iloc[:, 0]
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
    result = []
    col_names = ['Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight',
                 'Rings']
    for i, col in enumerate(data.columns):
        if data.columns.get_loc(col) != 0:
            result.append([i, data[col].mean(), data[col].std(), data[col].min(), data[col].quantile(0.25),
                           data[col].median(), data[col].quantile(0.75), data[col].max()])
    return result


def main():
    qualitative = qualitative_characteristics()
    quantitative = quantitative_characteristics()

    print(quantitative)

    # 3. Counts of occurrences of each category for the qualitative variable in the dataset.

    categories = ['M', 'F', 'I']
    plt.bar(categories, qualitative[0])
    plt.xlabel('Count')
    plt.ylabel('Categories')
    plt.title('Counts of occurrences')
    plt.show()

    # 4. histogram of each quantitative variable in the dataset. All histograms should be placed in a single figure
    # spanning 4 rows and 2 columns.

    fig, axs = plt.subplots(4, 2)
    fig.suptitle('Histograms')

    plt.show()


main()
