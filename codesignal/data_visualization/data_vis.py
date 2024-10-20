import seaborn as sns
import pandas as pd


titanic_df = sns.load_dataset('titanic')

# Using value_counts()
print("value counts",titanic_df['sex'].value_counts())

# Count the unique entries in the 'embarked' column and list them
print("unique count",titanic_df['embarked'].nunique())
print("unique",titanic_df['embarked'].unique())

# DESCRIPTIVE STATISTIC
# Generate descriptive statistics
titanic_stats = titanic_df.describe()
print(titanic_stats)

# Generate descriptive statistics while including all column because by default they only look at columns containing numerical data
titanic_stats = titanic_df.describe(include='all')
print(titanic_stats)

# Calculate the numerical data range
age_range = titanic_df['age'].max() - titanic_df['age'].min()
print('Age Range:', age_range) # Age Range: 79.58

# Calculate the IQR
Q1 = titanic_df['age'].quantile(0.25)
Q3 = titanic_df['age'].quantile(0.75)
IQR = Q3 - Q1
print('Age IQR:', IQR) # Age IQR: 17.875

# Calculate the mean
mean_age = titanic_df['age'].mean()
print('Mean Age:', mean_age) # Mean Age: 29.69911764705882

# Calculate the median
median_age = titanic_df['age'].median()
print('Median Age:', median_age) # Median Age: 28.0