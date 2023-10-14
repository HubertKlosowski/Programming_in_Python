import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data/data.csv", sep=',')
unit_colnames = ['Sex', 'Length [mm]', 'Diameter [mm]', 'Height [mm]', 'Whole weight [g]', 'Shucked weight [g]',
                 'Viscera weight [g]', 'Shell weight [g]', 'Rings']
data.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight',
                'Shell weight', 'Rings']


def adjust_for_histrogram(column_data, bins):
    mininum = column_data.min()
    maximum = column_data.max()
    bin_size = (maximum - mininum) / bins
    return [mininum, maximum, bin_size]


def qualitative_characteristics():
    v1 = data['Sex'].value_counts().values
    percentages = [round(i / v1.sum() * 100, 3) for i in v1]
    return [v1, percentages]


def quantitative_characteristics():
    result = []
    for i in range(1, len(data.columns)):
        result.append(data.iloc[:, i].describe().drop('count').T)
    return result


def point_3():
    qualitative = qualitative_characteristics()
    categories = ['Male', 'Infant', 'Female']
    plt.bar(categories, qualitative[0], edgecolor='black')
    plt.ylabel('Count')
    plt.xlabel('Categories')
    plt.title('Counts of occurrences')
    plt.show()


def point_4():
    fig, axs = plt.subplots(4, 2, figsize=(15, 15))
    j = 0
    for i in range(1, len(data.columns)):
        axs[j, (i - 1) % 2].hist(data.iloc[:, i], bins=10, edgecolor='black', log=True)
        axs[j, (i - 1) % 2].set_xlabel(unit_colnames[i])
        arr = adjust_for_histrogram(data.iloc[:, i], 10)
        axs[j, (i - 1) % 2].set_xticks([round(arr[0] + arr[2] * i, 3) for i in range(11)])
        if i % 2 != 0:
            axs[j, (i - 1) % 2].set_ylabel('Count')
        j += (i - 1) % 2
    plt.show()


def point_5():
    fig, axs = plt.subplots(14, 2, figsize=(20, 65))
    plt.subplots_adjust(top=0.97, bottom=0.05, hspace=0.5, wspace=0.2)
    k, x = 0, 0
    for i in range(1, len(data.columns)):
        for j in range(i + 1, len(data.columns)):
            axs[x, k % 2].scatter(data.iloc[:, i], data.iloc[:, j])
            axs[x, k % 2].set_xlabel(unit_colnames[i])
            axs[x, k % 2].set_ylabel(unit_colnames[j])
            k += 1
            if k % 2 == 0:
                x += 1
    plt.show()


def point_6():
    print(data.iloc[:, 1:].corr())


def point_7():
    sns.heatmap(data.iloc[:, 1:].corr(), annot=True)
    plt.show()


def point_8():
    sns.regplot(x=data['Length'], y=data['Diameter'], line_kws={"color": "red"})
    plt.show()


def point_9():
    tmp = ['F', 'I', 'M']
    col1 = ['Female', 'Infant', 'Male']
    final = []
    for i, column in enumerate(data.columns[1:]):
        col0 = [data.columns[i + 1], '', '']
        for o, el in enumerate(tmp):
            stats = data[data['Sex'] == el][column].describe().drop('count').values
            stats = [round(i, 3) for i in stats]
            stats.insert(0, col1[o])
            stats.insert(0, col0[o])
            final.append(stats)
    return final


def group_data(colname, sex):
    result = []
    for element in sex:
        result.append(data[data['Sex'] == element][colname])
    return result


def point_10():
    titles = ['Female', 'Infant', 'Male']
    fig, axs = plt.subplots(4, 2, figsize=(30, 20))
    for i, col in enumerate(data.columns[1:]):
        axs[int(i / 2), i % 2].boxplot(group_data(col, ['F', 'I', 'M']), labels=titles)
        axs[int(i / 2), i % 2].set_title(col)
    plt.show()


def main():
    """
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

    # 9. Table with summary statistics for the quantitative variables in the dataset split by the categories of the
    # qualitative variable

    point_9()

    # 10. Boxplot of each quantitative variable in the dataset, grouping every one of them by the qualitative variable.
"""

    point_10()


main()
