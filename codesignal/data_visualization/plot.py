import matplotlib.pyplot as plt

import seaborn as sns

# Load the dataset
titanic_df = sns.load_dataset('titanic')

# Count total males and females
gender_data = titanic_df['sex'].value_counts()

# Create a bar chart
gender_data.plot(kind ='bar', title='Sex Distribution')
plt.show()

# Enhancing your plot
gender_data = titanic_df['sex'].value_counts()

gender_data.plot(kind ='bar')
plt.xlabel("Sex")
plt.ylabel("Count")
plt.title("Sex Distribution")
plt.show()

# Embarkation point distribution
embark_data = titanic_df['embarked'].value_counts()
embark_data.plot(kind='bar')
plt.xlabel("Embarkation Point")
plt.ylabel("Count")
plt.title("Embarkation Point Distribution")
plt.show()

# Using Seaborn
sns.set(style="whitegrid")

# set the palette to Blues, the font to Serif and scale it up 1.2 times
sns.set(style="whitegrid", palette="Blues", font="Serif", font_scale=1.2)



# Set plot styling
sns.set(style="whitegrid", palette="Blues", font="Serif", font_scale=1.2)

# Create a plot
sns.countplot(x='pclass', data=titanic_df)
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='pclass', data=titanic_df, palette='coolwarm')
plt.show()

# Using legend
plt.figure(figsize=(12, 6))
sns.countplot(x='pclass', data=titanic_df, palette='coolwarm')
plt.title('Passenger Class Count')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.legend(title='Passenger Class')
plt.show()

# rotation
plt.figure(figsize=(12, 6))
sns.countplot(x='pclass', data=titanic_df, palette='coolwarm')
plt.title('Passenger Class Count')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.legend(title='Passenger Class')
plt.xticks(rotation=45)
plt.show()

# Histogram

# and the kde=True part is there also to draw a curve of Kernel Density Estimation (KDE) that estimates the probability density function of the variable
sns.histplot(data=titanic_df, x='age', kde=True)

# Increase the number of bins to 30 (default is 10)
sns.histplot(data=titanic_df, x='age', bins=30, kde=True)

# Give your plot a comprehensive title
plt.title('Age Distribution Among Titanic Passengers')

# Label your axes
plt.xlabel('Age')
plt.ylabel('Number of Passengers')
plt.show()

# A histogram using 'hue', 'multiple', and 'palette'
sns.histplot(data=titanic_df, x='age', hue="sex", multiple="stack", palette="pastel")

# A histogram using 'binwidth' and 'element'
sns.histplot(data=titanic_df, x="age", binwidth=1, element="step", color="purple")


# Applying a blue color palette
sns.set_palette("Blues")

# Bar plot for the 'sex' variable with title
sns.countplot(x='sex', data=titanic_df).set_title('Sex Distribution')

# Color-coded bar plot representing 'sex' and survival ('survived')
sns.countplot(x='sex', hue='survived', data=titanic_df, color="cyan", order=["female", "male"], orient='v').set_title('Sex and Survival Rates')

# Comparing the 'sex' variable with 'survived'
sns.countplot(x='sex', hue='survived', data=titanic_df)

# Comparing the 'pclass' variable with 'survived'
sns.countplot(x='pclass', hue='survived', data=titanic_df)

# Comparing the 'embarked' variable with 'survived'
sns.countplot(x='embarked', hue='survived', data=titanic_df)

# Display Scatter Plot of Age vs Fare
sns.scatterplot(x='age', y='fare', data=titanic_df)
plt.title("Age vs Fare")
plt.show()

sns.scatterplot(x='age', y='fare', hue='pclass', data=titanic_df)
plt.title("Age vs Fare (Separate colors for Passenger Class)")
plt.show()

sns.scatterplot(x='age', y='fare', hue='pclass', style='sex', size='fare', sizes=(20, 200), data=titanic_df)
plt.title("Age vs Fare (Separate markers for Sex and Sizes for Fare)")
plt.show()

# Correlation of all numeric variables in the Titanic dataset
corr_vals = titanic_df.corr(numeric_only=True)
print(corr_vals)

# Create a box plot
sns.boxplot(x='pclass', y='fare', data=titanic_df)
plt.title('Fares vs Passenger Classes')
plt.show()

sns.boxplot(x='pclass', y='fare', hue='survived', data=titanic_df)
plt.title('Fares vs Passenger Classes Differentiated by Survival')
plt.show()

sns.boxplot(
    x='pclass', y='fare',
    hue='survived',
    data=titanic_df,
    palette='Set3', linewidth=1.5,
    order=[3,1,2], hue_order=[1,0],
    color='skyblue', saturation=0.7,
    dodge=True, fliersize=5
)
plt.title('Fares vs Passenger Classes Differentiated by Survival')
plt.show()

sns.boxplot(
    x='pclass', y='fare',
    hue='survived',
    data=titanic_df,
    palette='Set3', linewidth=1.5,
    order=[3,1,2], hue_order=[1,0],
    color='skyblue', saturation=0.7,
    dodge=True, fliersize=5
)
plt.title('Fares vs Passenger Classes Differentiated by Survival')
plt.show()

# Calculate correlation matrix
correlation_matrix = titanic_df.corr(numeric_only=True)

# Create a heatmap
sns.heatmap(correlation_matrix, annot=True)

# Show plot
plt.show()

# Create a heatmap
sns.heatmap(correlation_matrix, annot=True, cbar=True, vmin=-1, vmax=1)

# Show plot
plt.show()

# Create a heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

plt.show()

# Building a color map 
color_map = sns.diverging_palette(220, 20, as_cmap=True)
sns.heatmap(correlation_matrix, annot=True, cmap=color_map)

plt.show()