import pandas as pd

# Load the pitching data (update the path to the CSV file)
pitching_data = pd.read_csv('C:\\Users\\Johan\\OneDrive\\Desktop\\TXST Baseball Analytics\\data\\2023 pitching.csv')

# Display the first few rows of the data
print("Pitching Data:")
print(pitching_data.head())

# Calculate the ERA for each pitcher
pitching_data['ERA'] = pitching_data['ERA'].astype(float)

# Sort by ERA
era_sorted = pitching_data[['Player', 'ERA']].sort_values(by='ERA')

# Display ERA sorted data
print("\nERA Rankings:")
print(era_sorted)

# Save sorted ERA rankings to a new CSV
era_sorted.to_csv('era_rankings.csv', index=False)
print("\nERA rankings saved to 'era_rankings.csv'.")
