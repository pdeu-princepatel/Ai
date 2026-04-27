import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer #preprocessing steps to specific columns at once
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

df = pd.read_csv("heart_attack_data (1) (1).csv")

X =df.drop('target',axis=1)

Y =df['target']

num_cols = ['age','gender','cholesterol','blood_pressure','diabetes','smoking','obesity','exercise','family_history','stress_level','alcohol_consumption','heart_rate']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_cols)
    ], remainder='passthrough') # 'passthrough' keeps the 0/1 columns as they are

X_processed = preprocessor.fit_transform(X)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_processed, Y, test_size=0.2, random_state=42)

# 3. Build the Deep Learning Mod
model = keras.Sequential([
    keras.layers.Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dropout(0.2), # prevent overfiting
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid') # Sigmoid for 0 (No Disease) or 1 (Disease)
])

# 4. Compile
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# 5. Train
history = model.fit(
    X_train, y_train,
    epochs=100,
    batch_size=10,
    validation_data=(X_test, y_test),
    verbose=1
)

y_pred_prob = model.predict(X_test)

y_pred = (y_pred_prob > 0.5).astype(int)

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Grays', 
            xticklabels=['No Disease', 'Disease'], 
            yticklabels=['No Disease', 'Disease'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

print(classification_report(y_test, y_pred))
