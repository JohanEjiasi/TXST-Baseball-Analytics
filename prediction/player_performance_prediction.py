import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the batting data (update the path to the CSV file)
batting_data = pd.read_csv('C:\\Users\\Johan\\OneDrive\\Desktop\\TXST Baseball Analytics\\data\\2023 batting.csv')

# Display the first few rows of the data
print("Batting Data:")
print(batting_data.head())

# Prepare the data for prediction
features = batting_data[['OBP', 'SLG', 'RBI', 'HBP', 'BB', 'K', 'SB', 'CS']]  # Example feature columns
target = batting_data['BA']  # Target column

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")

# Display predictions vs actual
predictions_df = pd.DataFrame({'Actual BA': y_test, 'Predicted BA': predictions})
print("\nPredictions vs Actual:")
print(predictions_df)

# Create predictions folder if it doesn't exist
predictions_folder = 'C:\\Users\\Johan\\OneDrive\\Desktop\\TXST Baseball Analytics\\predictions'
os.makedirs(predictions_folder, exist_ok=True)

# Save predictions to a new CSV
predictions_file_path = os.path.join(predictions_folder, 'predictions.csv')
predictions_df.to_csv(predictions_file_path, index=False)
print(f"\nPredictions saved to '{predictions_file_path}'.")

# Save sorted batting averages to a new CSV
batting_avg_sorted = batting_data[['Player', 'BA']].sort_values(by='BA', ascending=False)
batting_avg_sorted_file_path = os.path.join(predictions_folder, 'batting_averages.csv')
batting_avg_sorted.to_csv(batting_avg_sorted_file_path, index=False)
print(f"\nBatting averages saved to '{batting_avg_sorted_file_path}'.")
