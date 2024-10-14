import pandas as pd

# Load the batting data (update the path to the CSV file)
batting_data = pd.read_csv('C:\\Users\\Johan\\OneDrive\\Desktop\\TXST Baseball Analytics\\data\\2023 batting.csv')

# Display the first few rows of the data
print("Batting Data:")
print(batting_data.head())

# Calculate the batting average for each player
batting_data['BA'] = batting_data['BA'].astype(float)
batting_avg = batting_data[['Player', 'BA']]

# Sort by batting average
batting_avg_sorted = batting_avg.sort_values(by='BA', ascending=False)

# Display batting averages
print("\nBatting Averages:")
print(batting_avg_sorted)

# Save sorted batting averages to a new CSV
batting_avg_sorted.to_csv('batting_averages.csv', index=False)
print("\nBatting averages saved to 'batting_averages.csv'.")
