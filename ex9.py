import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import tensorflow as tf
from tensorflow.keras import layers, models, datasets

# Load Dataset
(x_train_full, y_train_full), (x_test, y_test) = datasets.fashion_mnist.load_data()

# Preprocessing: Normalize and Reshape
x_train_full = x_train_full.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Reshape to include channel dimension (28, 28, 1)
x_train_full = x_train_full.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# Create Validation Set (10,000 samples)
x_val = x_train_full[:10000]
y_val = y_train_full[:10000]
x_train = x_train_full[10000:]
y_train = y_train_full[10000:]

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

model = models.Sequential([
    #28x28x1
    # Conv Layer 1
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)), #26x26x32
    layers.MaxPooling2D((2, 2)), #13x13x32
    layers.Dropout(0.25),
    # Conv Layer 2
    layers.Conv2D(64, (3, 3), activation='relu'),#11x11x64
    layers.MaxPooling2D((2, 2)), #5x5x64
    layers.Dropout(0.25),
    # Flatten & Dense Layer
    layers.Flatten(),   #10 1d outputs
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.50),
    # Output Layer
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the Model
history = model.fit(x_train, y_train, epochs=20,
                    validation_data=(x_val, y_val),
                    batch_size=64)

# Plot Accuracy and Loss Curves
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Accuracy Curve
ax1.plot(history.history['accuracy'], label='Train Accuracy')
ax1.plot(history.history['val_accuracy'], label='Val Accuracy')
ax1.set_title('Accuracy vs Epochs')
ax1.set_xlabel('Epochs')
ax1.set_ylabel('Accuracy')
ax1.legend()

# Loss Curve
ax2.plot(history.history['loss'], label='Train Loss')
ax2.plot(history.history['val_loss'], label='Val Loss')
ax2.set_title('Loss vs Epochs')
ax2.set_xlabel('Epochs')
ax2.set_ylabel('Loss')
ax2.legend()
plt.show()

# Confusion Matrix
y_pred = np.argmax(model.predict(x_test), axis=-1)
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Grays',
            xticklabels=class_names, yticklabels=class_names)

plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
