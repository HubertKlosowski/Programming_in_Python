import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data/data.csv", sep=',')
colnames = ['Sex', 'Length [mm]', 'Diameter [mm]', 'Height [mm]', 'Whole weight [g]', 'Shucked weight [g]',
            'Viscera weight [g]', 'Shell weight [g]', 'Rings']
df = data.select_dtypes(include=['number'])  # wybieramy tylko kolumny posiadajace wartosci numeryczne


def adjust_for_histrogram(column, bins):
    mininum = column.min()
    maximum = column.max()
    bin_size = (maximum - mininum) / bins
    return [mininum, maximum, bin_size]


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
    for i, col in enumerate(df.columns):
        result.append([colnames[i + 1], df[col].mean(), df[col].std(), df[col].min(), df[col].quantile(0.25),
                       df[col].median(), df[col].quantile(0.75), df[col].max()])
    return result


def point_3():
    qualitative = qualitative_characteristics()
    categories = ['M', 'F', 'I']
    plt.bar(categories, qualitative[0], edgecolor='black')
    plt.xlabel('Count')
    plt.ylabel('Categories')
    plt.title('Counts of occurrences')
    plt.show()


def point_4():
    fig, axs = plt.subplots(4, 2, figsize=(15, 15))
    fig.suptitle('Histograms')
    j = 0
    for i in range(len(df.columns)):
        axs[j, i % 2].hist(df.iloc[:, i], bins=10, edgecolor='black', log=True)
        axs[j, i % 2].set_xlabel(colnames[i + 1])
        arr = adjust_for_histrogram(df.iloc[:, i], 10)
        axs[j, i % 2].set_xticks([round(arr[0] + arr[2] * i, 2) for i in range(11)])
        j += i % 2
    plt.show()


def point_5():
    fig, axs = plt.subplots(14, 2, figsize=(20, 70))
    fig.suptitle('Scatter plots')
    k, x = 0, 0
    for i in range(8):
        for j in range(i + 1, 8):
            axs[x, k % 2].scatter(df.iloc[:, i], df.iloc[:, j])
            axs[x, k % 2].set_xlabel(colnames[i + 1])
            axs[x, k % 2].set_ylabel(colnames[j + 1])
            k += 1
            if k % 2 == 0:
                x += 1
    plt.show()


def point_6():
    df.columns = colnames[1:]
    print(df.corr())


def point_7():
    sns.heatmap(df.corr(), annot=True)
    plt.show()


def point_8():
    sns.regplot(x=df['Length [mm]'], y=df['Diameter [mm]'])
    plt.show()


def main():
    qualitative = qualitative_characteristics()
    for el in qualitative:
        print(el)
    quantitative = quantitative_characteristics()
    for el in quantitative:
        print(el)

    # 3. Counts of occurrences of each category for the qualitative variable in the dataset.

    point_3()

    # 4. histogram of each quantitative variable in the dataset. All histograms should be placed in a single figure
    # spanning 4 rows and 2 columns.

    point_4()

    # 5. Scatter plot for each pair of the quantitative variables in the dataset. All scatter plots should be placed
    # in a single figure spanning 14 rows and 2 columns.

    point_5()

    # 6. Table representing a linear correlation matrix of all quantitative variables in the dataset.

    point_6()

    # 7. heatmap representing a linear correlation matrix of all quantitative variables in the dataset.

    point_7()

    # 8. Linear regression plot with the two quantitative variables that are most strongly linearly correlated.

    point_8()


main()
