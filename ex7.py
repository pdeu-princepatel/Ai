import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler #normalization
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

file_path="house_price_dataset (1).csv"
df=pd.read_csv(file_path)

encoder=LabelEncoder() # text data to integers

df['Location']=encoder.fit_transform(df['Location'])

df['House_Type']=encoder.fit_transform(df['House_Type'])

x=df.drop(columns='Price')

y=df['Price']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

scaler=StandardScaler()

X_train_scaled = scaler.fit_transform(x_train)

X_test_scaled = scaler.transform(x_test)

model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

test_loss = model.evaluate(X_test_scaled, y_test)

print(f'Test Loss (MSE): {test_loss}')

history = model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, validation_split=0.2)

# Get training and validation loss from history object

history_dict = history.history

loss_values = history_dict['loss']

val_loss_values = history_dict['val_loss']

epochs = range(1, len(loss_values) + 1)

plt.figure(figsize=(10, 6))
sns.lineplot(x=epochs, y=loss_values, label='Training Loss (MSE)')
sns.lineplot(x=epochs, y=val_loss_values, label='Validation Loss (MSE)')
plt.title('Training and Validation Loss (MSE) vs. Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss (MSE)')
plt.legend()
plt.grid(True)
plt.savefig("ex7")

