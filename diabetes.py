import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/anbas061/Downloads/diabetes.csv")


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
print(df.describe())

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

#Distribution of Outcome
sns.countplot(x='Outcome', data=df)
plt.title('Distribution of Diabetes Outcome')
plt.xlabel('Outcome (0: No Diabetes, 1: Diabetes)')
plt.ylabel('Count')
plt.show()

#Scatter plots
selected_vars = ['Glucose', 'Insulin', 'Pregnancies']
sns.pairplot(df, hue='Outcome', vars=selected_vars, markers=["o", "s"])
plt.suptitle('Pairplot of Glucose, Insulin, and Pregnancies by Diabetes Outcome', y=1.02)
plt.show()

#Correlation matrix
correlation_matrix = df.corr().round(2)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

#Age vs. BMI
sns.lineplot(x='Age', y='BMI', data=df)
plt.title('Line Chart: Age vs. BMI')
plt.xlabel('Age')
plt.ylabel('BMI')
plt.show()