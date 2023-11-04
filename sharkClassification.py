# needed libraries:
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow import keras
from tensorflow import layers
from tensorflow import Sequential

# creating dataset:
batch_size = 64
img_height = 180
img_width = 180

train_ds = tf.keras.utils.image_dataset_from_directory(
    "sharkPhotos",
    validation_split=0.2,
    subset="training",
    seed=10,
    image_size=(img_height, img_width),
    batch_size=batch_size)

val_ds = tf.keras.utils.image_dataset_from_directory(
    "sharkPhotos",
    validation_split=0.2,
    subset="validation",
    seed=10,
    image_size=(img_height, img_width),
    batch_size=batch_size)

sharkNames = train_ds.class_names

# visualize data:
plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(int(labels[i]))
        plt.axis("off")

# augment data:
data_augmentation = keras.Sequential(
    [
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.1),
        layers.RandomZoom(0.1),
    ]
)

# standardize data:
normalization_layer = layers.Rescaling(1./255)

# create model:
num_classes = len(sharkNames)

model = Sequential([
  layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
  layers.Conv2D(16, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(128, activation='relu'),
  layers.Dense(num_classes)
])

model.compile(optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy'])

# train model:
epochs = 25

history = model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=epochs
)