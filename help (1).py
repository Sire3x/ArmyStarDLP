import os
import shutil
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Path to your dataset
train_data_dir = r'C:\Users\User\PycharmProjects\pythonProject\my_project\train'
test_data_dir = r'C:\Users\User\Downloads\test\test'

# Image size
img_width, img_height = 224, 224

# Batch size
batch_size = 32

# Number of epochs for fine-tuning
epochs = 10

# Confidence threshold for classification
confidence_threshold = .30Furm

# Load pre-trained ResNet50 model without top layers
base_model = ResNet50(weights='imagenet', include_top=False)

# Add custom classification layers
x = base_model.output
x = GlobalAveragePooling2D()(x)
predictions = Dense(1, activation='sigmoid')(x)

# Create the model
model = Model(inputs=base_model.input, outputs=predictions)

# Freeze initial layers
for layer in base_model.layers:
    layer.trainable = False

# Compile the model with the correct optimizer argument
model.compile(optimizer=SGD(learning_rate=0.001, momentum=0.9), loss='binary_crossentropy', metrics=['accuracy'])

# Data augmentation and normalization for training
train_datagen = ImageDataGenerator(
    rescale=1.0/255.0,
    rotation_range=20,  # Add rotation augmentation
    width_shift_range=0.2,  # Add width shift augmentation
    height_shift_range=0.2,  # Add height shift augmentation
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

# Generate training data
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary')

# Fine-tune the model
model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    epochs=epochs)

# Function to classify an image
def classify_image(image_path):
    img = image.load_img(image_path, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    preds = model.predict(x)
    class_label = 'tank' if preds[0][0] > confidence_threshold else 'no_tank'
    return class_label, preds[0][0]

# Classify images in the test folder and move them to appropriate folders
def classify_images_in_folder(folder_path, tank_folder, no_tank_folder):
    for filename in os.listdir(folder_path):
        if any(filename.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']):
            img_path = os.path.join(folder_path, filename)
            class_label, confidence = classify_image(img_path)
            if class_label == 'tank':
                shutil.copy(img_path, tank_folder)
            else:
                shutil.copy(img_path, no_tank_folder)

# Paths to folders for classification
tank_output_folder = 'tank_images'
no_tank_output_folder = 'no_tank_images'

# Create output folders if they don't exist
os.makedirs(tank_output_folder, exist_ok=True)
os.makedirs(no_tank_output_folder, exist_ok=True)

# Classify images in the test folder and move them to appropriate folders
classify_images_in_folder(test_data_dir, tank_output_folder, no_tank_output_folder)



print("Image classification and sorting completed.")

