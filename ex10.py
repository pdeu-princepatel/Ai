import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

# Configuration
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32

DATASET_DIR = 'C:/Users/Prince Patel/Desktop/sem 6/ai lab/COVID-19_Radiography_Dataset'

# Data Generator
train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    zoom_range=0.15,
    horizontal_flip=True
)

train_generator = train_datagen.flow_from_directory(
    DATASET_DIR,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)

val_generator = train_datagen.flow_from_directory(
    DATASET_DIR,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

print("Classes:", train_generator.class_indices)

# ================= RESNET MODEL =================
def build_resnet50():
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    
    for layer in base_model.layers:
        layer.trainable = False

    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(512, activation='relu')(x)
    x = Dropout(0.5)(x)
    
    predictions = Dense(4, activation='softmax')(x)

    model = Model(inputs=base_model.input, outputs=predictions)

    model.compile(
        optimizer=Adam(learning_rate=0.0001),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    return model
# ================= CUSTOM CNN =================
def build_custom_cnn():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        MaxPooling2D(2, 2),

        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),

        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),

        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(4, activation='softmax')  # 4 classes
    ])

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

model_scratch = build_custom_cnn()

history_scratch = model_scratch.fit(
    train_generator,
    validation_data=val_generator,
    epochs=10
)
def plot_comparison(history_resnet, history_scratch):
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))

    # Accuracy Plot
    axs[0].plot(history_resnet.history['accuracy'], label='ResNet Train')
    axs[0].plot(history_resnet.history['val_accuracy'], label='ResNet Val')
    axs[0].plot(history_scratch.history['accuracy'], label='Scratch Train')
    axs[0].plot(history_scratch.history['val_accuracy'], label='Scratch Val')
    axs[0].set_title('Accuracy Comparison')
    axs[0].set_xlabel('Epochs')
    axs[0].set_ylabel('Accuracy')
    axs[0].legend()

    # Loss Plot
    axs[1].plot(history_resnet.history['loss'], label='ResNet Train')
    axs[1].plot(history_resnet.history['val_loss'], label='ResNet Val')
    axs[1].plot(history_scratch.history['loss'], label='Scratch Train')
    axs[1].plot(history_scratch.history['val_loss'], label='Scratch Val')
    axs[1].set_title('Loss Comparison')
    axs[1].set_xlabel('Epochs')
    axs[1].set_ylabel('Loss')
    axs[1].legend()

    # SAVE THE IMAGE
    # Use bbox_inches='tight' to ensure labels aren't cut off
    plt.savefig('model_comparison_results.png', dpi=300, bbox_inches='tight')
    print("Comparison plot saved as 'model_comparison_results.png'")
    
    plt.show()

model_resnet = build_resnet50()
history_resnet = model_resnet.fit(
    train_generator,
    validation_data=val_generator,
    epochs=10
)
plot_comparison(history_resnet, history_scratch)