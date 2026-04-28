import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.metrics import mean_absolute_error, r2_score,accuracy_score ,confusion_matrix,classification_report
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report, confusion_matrix

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Load your dataset
df = pd.read_csv('house_price_dataset (1).csv') 

# Remove any accidental leading or trailing spaces from column names
df.columns = df.columns.str.strip()

# 2. Data Preprocessing (Handling missing values, encoding, and normalization)
# Let's assume we fill missing numerical values with the mean
X = df.drop('Price', axis=1)
y = df['Price']
# Identify column types automatically
# This selects all continuous numeric columns
numerical_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()

# This selects all text/object columns
categorical_features = X.select_dtypes(include=['object', 'category']).columns.tolist()

print("Detected Numerical Columns:", numerical_features)
print("Detected Categorical Columns:", categorical_features)

# Apply Normalization to numerical and One-Hot Encoding to categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

# Fit and transform safely
X_processed = preprocessor.fit_transform(X)

# 1. Split the dataset (60% Train, 20% Validation, 20% Test)
X_train, X_temp, y_train, y_temp = train_test_split(X_processed, y, test_size=0.4, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# 3. Build Neural Network with 10% Dropout after each hidden layer
model = Sequential([
    # Input layer and First hidden layer
    Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.10), # 10% dropout
    
    # Second hidden layer
    Dense(16, activation='relu'),
    Dropout(0.10), # 10% dropout
    
    # Output layer (Binary Classification)
    Dense(1)
])

model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

# Train the model using training and validation sets
history = model.fit(
    X_train, y_train, 
    validation_data=(X_val, y_val), 
    epochs=50, 
    batch_size=32, 
    verbose=1
)

# 4. Print Confusion Matrix and Classification Report based on Test Set
y_pred = model.predict(X_test)

print("\n--- Model Evaluation ---")
print(f"Mean Absolute Error: {mean_absolute_error(y_test, y_pred)}")
print(f"R2 Score: {r2_score(y_test, y_pred)}")

# 5. Plot Loss and Accuracy Curves
fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# Plot Loss
axs[0].plot(history.history['loss'], label='Training Loss', color='blue')
axs[0].plot(history.history['val_loss'], label='Validation Loss', color='orange')
axs[0].set_title('Training and Validation Loss')
axs[0].set_xlabel('Epochs')
axs[0].set_ylabel('Loss')
axs[0].legend()
axs[0].grid(True)

# Plot Accuracy
axs[1].plot(history.history['accuracy'], label='Training Accuracy', color='blue')
axs[1].plot(history.history['val_accuracy'], label='Validation Accuracy', color='orange')
axs[1].set_title('Training and Validation Accuracy')
axs[1].set_xlabel('Epochs')
axs[1].set_ylabel('Accuracy')
axs[1].legend()
axs[1].grid(True)

plt.show()
