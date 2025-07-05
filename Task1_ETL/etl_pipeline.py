# Import Libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# Load Data
df = pd.read_csv("Iris.csv")  # make sure file name is correct
print("Dataset Preview:\n", df.head())

# Drop unnecessary column if exists
df = df.drop(columns="Id", errors='ignore')

# Check for missing values
print("Missing Values:\n", df.isnull().sum())

# Label Encode Species column
le = LabelEncoder()
df['Species'] = le.fit_transform(df['Species'])

# Feature Scaling
features = df.drop('Species', axis=1)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Create feature and target variables
X = pd.DataFrame(scaled_features, columns=features.columns)
y = df['Species']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Export Cleaned Data to CSV
X_train.to_csv("X_train.csv", index=False)
y_train.to_csv("y_train.csv", index=False)

print("ETL Pipeline Complete ✅")
