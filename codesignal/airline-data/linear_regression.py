import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

flights_data = sns.load_dataset("flights")
flights_data['year'] = pd.to_datetime(flights_data['year'], format='%Y')
flights_pivot = pd.pivot_table(data=flights_data, values='passengers', index='year', aggfunc='sum').reset_index()


# Extracting the year from the date and converting it into the appropriate format
flights_pivot['year'] = flights_pivot['year'].dt.year

X = np.array(flights_pivot['year']).reshape(-1,1)
y = flights_pivot['passengers']

reg = LinearRegression().fit(X, y)

plt.scatter(X, y, color = "m", marker = "o", s = 30)

Y_pred = reg.predict(X)
plt.plot(X, Y_pred, color = "g")

plt.xlabel('Year')
plt.ylabel('Passengers')
plt.title('Linear Regression: Passengers Over Time')
plt.show()


# In the above code example, we load the Flights dataset and pivot it to get the total passenger count for each year. Next, we create our Linear Regression model and fit it to the data (years and passenger counts). We use a scatter plot to visualize the data points, while the line plot indicates our fitted regression line.

# The purple dots represent the actual number of passengers for each year from 1949 to 1960, plotted against the year. The green line represents the line of best fit generated by linear regression. This line aims to minimize the total distance between itself and each point (which signifies the error or residual). It represents our model's best guess for the passenger count given a particular year.

print ("R-squared statistic: ", reg.score(X, y))

# Forecast for the next 10 years
new_years = np.array(range(1961, 1971)).reshape(-1,1)
new_passenger_numbers = reg.predict(new_years)
print("Year, Predicted Passengers")
for year, passengers in zip(new_years, new_passenger_numbers):
    print(f"{year[0]}, {int(passengers)}")

# Above, we're predicting passenger counts for the years 1961 to 1971. 
# The LinearRegression.predict function is used to perform the predictions. 
# It generates the dependent variable's predicted values based on the linear regression model.

