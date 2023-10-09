import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data/data.csv", sep=',')
colnames = ['Sex', 'Length [mm]', 'Diameter [mm]', 'Height [mm]', 'Whole weight [g]', 'Shucked weight [g]',
            'Viscera weight [g]', 'Shell weight [g]', 'Rings']


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
    for i, col in enumerate(data.columns):
        if data.columns.get_loc(col) != 0:
            result.append(
                [colnames[i], data[col].mean(), data[col].std(), data[col].min(), data[col].quantile(0.25),
                 data[col].median(), data[col].quantile(0.75), data[col].max()])
    return result


def point_3():
    qualitative = qualitative_characteristics()
    categories = ['M', 'F', 'I']
    plt.bar(categories, qualitative[0])
    plt.xlabel('Count')
    plt.ylabel('Categories')
    plt.title('Counts of occurrences')
    plt.show()


def point_4():
    fig, axs = plt.subplots(4, 2, figsize=(15, 15))
    fig.suptitle('Histograms')
    j = 0
    for i in range(len(data.columns[1:])):
        axs[j, i % 2].hist(data.iloc[:, i + 1], bins=10, edgecolor='black', log=True)
        axs[j, i % 2].set_title(colnames[i + 1])
        j += i % 2
    plt.show()


def point_5():  # nie dziala
    fig, axs = plt.subplots(14, 2, figsize=(12, 36))
    fig.suptitle('Scatter plots')
    for i in range(8):
        for j in range(i + 1, 8):
            axs[i, 0].scatter(data.iloc[:, i + 1], data.iloc[:, j + 1])
            axs[i, 0].set_title(colnames[i] + " - " + colnames[j])
    plt.show()


def point_6():
    data.columns = colnames
    print(data.corr())


def point_7():
    sns.heatmap(data.corr(), annot=True)
    plt.show()


def point_8():
    sns.regplot(x=data['Length [mm]'], y=data['Diameter [mm]'])
    plt.show()


def main():
    quantitative = quantitative_characteristics()
    for el in quantitative:
        print(el)

    # 3. Counts of occurrences of each category for the qualitative variable in the dataset.

    point_3()

    # 4. histogram of each quantitative variable in the dataset. All histograms should be placed in a single figure
    # spanning 4 rows and 2 columns.

    point_4()

    # 5. Using a package chosen among Matplotlib, Pandas, or Seaborn, create a scatter plot for each pair of the
    # quantitative variables in the dataset. All scatter plots should be placed in a single figure spanning 14 rows
    # and 2 columns.

    point_5()

    # 6. Table representing a linear correlation matrix of all quantitative variables in the dataset.

    point_6()

    # 7. heatmap representing a linear correlation matrix of all quantitative variables in the dataset.

    point_7()

    # 8. Linear regression plot with the two quantitative variables that are most strongly linearly correlated.

    point_8()


main()
