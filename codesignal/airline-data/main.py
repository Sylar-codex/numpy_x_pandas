import matplotlib.pyplot as plt
import seaborn as sns

flights_df = sns.load_dataset('flights')

# Pivot the DataFrame to get the month as the index
flights_df_pivot = flights_df.pivot(index="month", columns="year", values="passengers")

# Plot the passenger count for each month over each year
flights_df_pivot.plot(title='Passenger Counts (1949 - 1960)')
plt.ylabel("Passenger Count")
plt.show()

flights_df_pivot.plot(grid=True, figsize=(10,5), linestyle='--')
plt.title("Passenger Counts (1949 - 1960)")
plt.ylabel("Passenger Count")
plt.show()



import matplotlib.pyplot as plt
import seaborn as sns

# Load the flights dataset
flights_data = sns.load_dataset('flights')

# Aggregate passengers' count for each month
month_wise_data = flights_data.groupby('month')['passengers'].sum().reset_index()

# Create line plots
plt.figure(figsize=(14, 8))
plt.plot(month_wise_data['month'], month_wise_data['passengers'], marker='o')
plt.grid(True)
plt.title('Month-wise Number of Passengers (1949 - 1960)', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Passengers', fontsize=12)
plt.show()

# Year-wise passenger distribution
year_wise_data = flights_data.groupby('year')['passengers'].sum()

year_wise_data.plot(kind='line', marker='o')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Number of Passengers", fontsize=12)
plt.title("Year-wise Number of Passengers (1949 - 1960)", fontsize=14)
plt.grid(True)
plt.show()

year_wise_data.plot(kind='line', marker='o', color='skyblue', alpha=0.7, grid=True)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Number of Passengers", fontsize=12)
plt.title("Year-wise Number of Passengers (1949 - 1960)", fontsize=14)
plt.show()

# Pivot the dataset
flights_pivot = flights_df.pivot(index="month", columns="year", values="passengers")
print(flights_pivot)

# Detailed heat map
sns.heatmap(flights_pivot, 
            cmap='YlGnBu', # choosing a yellow-green-blue colormap
            annot=True, # Turning on annotations
            fmt="d", # displaying annotations as integer
            linewidths=.5, # Add gridlines with width 0.5
            cbar=True, # Include color bar
            center = flights_pivot.loc["Jan", 1955] # Center colormap at the value of passengers in January 1955
)
plt.show()