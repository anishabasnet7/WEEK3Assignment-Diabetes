import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("..//WEEK3Assignment Diabetes//diabetes.csv")
print("First few rows of the dataframe")
print(df.head())
print("Missing Values")
print(df.isnull().sum())
df_cleaned = df.dropna()
print("\nDuplicate Rows")
print(df_cleaned.duplicated().sum())
df_cleaned = df_cleaned.drop_duplicates()
print("\nCleaned dataset Information")
print(df_cleaned.info())
print("\nCleaned dataset  ")
print(df_cleaned.head())

# Overall Stats
print("Summary Statistics")
summary_statistics = df.describe()
print(summary_statistics)
excel_file_path = "..//WEEK3Assignment Diabetes//summary_statistics.xlsx"
summary_statistics.to_excel(excel_file_path, index=True)

#Mean
means = df.mean().round(4)
print("\nMean")
print(means)

#Median 
medians = df.median().round(4)
print("\nMedian")
print(medians)

#Mode
modes = df.mode().iloc[0]
print("\nMode")
print(modes)

#Standard Deviation
std_devs = df.std().round(4)
print("\nStandard Deviation")
print(std_devs)

#Correlation Matrix
correlation_matrix = df.corr().round(4)
print("\nCorrelation Matrix")
print(correlation_matrix)
excel_file_path = "..//WEEK3Assignment Diabetes//correlation.xlsx"
correlation_matrix.to_excel(excel_file_path, index=True)

#Bar Graph
sns.countplot(x='Outcome', data=df)
plt.title('Bargraph of Diabetes vs Non Diabetes')
plt.xlabel('Outcome (0: No Diabetes, 1: Diabetes)')
plt.ylabel('Count')
plt.show()

#Histogram
selected_vars = ['Glucose', 'Insulin', 'Pregnancies']
sns.set(style="ticks")
pair_plot = sns.pairplot(df, hue='Outcome', vars=selected_vars, markers=["o", "s"], diag_kind='hist')
labels = {'Glucose': 'Glucose Level', 'Insulin': 'Insulin Level', 'Pregnancies': 'Number of Pregnancies'}
for i in range(len(selected_vars)):
    for j in range(len(selected_vars)):
        if i == len(selected_vars) - 1:
            pair_plot.axes[i, j].set_xlabel(labels[selected_vars[j]])
        if j == 0:
            pair_plot.axes[i, j].set_ylabel(labels[selected_vars[i]])
plt.suptitle('Histogram of Glucose, Insulin, and Pregnancies by Diabetes Outcome', y=1.02)
plt.show()

#Heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='Oranges', linewidths=0.5)
plt.title('Heatmap')
plt.show()

# Density Plot
plt.figure(figsize=(12, 8))
sns.kdeplot(df['Glucose'], label='Glucose', fill=True)
sns.kdeplot(df['BMI'], label='BMI', fill=True)
sns.kdeplot(df['Age'], label='Age', fill=True)
plt.title('Density Plot')
plt.xlabel('Variables')
plt.ylabel('Density')
plt.legend()
plt.show()