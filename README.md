# Landscape Image Classification
## Using convolutional neural networks to classify images into their respective category.

## Table of Contents
* Goal
* Data
* Models
## Goal
The goal of this project is to be able to input a landscape image into a model and have it predict if the image contains:

* Buildings
* Forests
* Glaciers
* Mountains
* Seas
* Streets
To do this we implement a convolutional neural network that looks for patterns in the images.

A Convolutional Neural Network is a Deep Learning algorithm which can take in an input image, assign importance through learnable weights and biases to various aspects of an image and be able to differentiate one from the other. Each image had a pixel structure of 150 x 150 x 3. Pixels split into 3 rgb layers, so 17,000 images with 150x150 pixels x 3 layers is a lot of pixels. CNNs help to reduce the images into a form which is easier to process, without losing features that are critical to getting a good prediction. Image matices are passed through a filter to extract the important feature. The new values then go through a pooling layer to reduce dimensionality. The matrices are then flattened and passed into a normal neural network. Finally, with back propagation, the filter values are adjusted to minimize the cost function. This process is repeated for each epoch.

## Data
The data for this project consists of 17,034 images of different landscapes split into training and testing sets.

The dataset can be found on kaggle here.

## Models
We tried making many different models using images of different sizes and color compression.

### Baseline Model
The baseline model was made from only images compressed from 150 pixels square to 75 pixels square. This model overfit the training data a lot so it was obvious that some regularization would be needed. Here is a plot of the training and validation accuracy:

![Baseline_accuracy](https://user-images.githubusercontent.com/84738906/129249087-4c680cfd-9846-426a-bc92-4f7e676b8606.png)


The big difference between training and validation accuracy shows overfitting to the training data.

### Final Model
The final model I made adds l2 regularization and dropout layers to prevent overfitting. I also tune the learning rate to try to prevent the accuracy from fluctuating every 4 or so epochs. The model ended up with about a 78 train accuracy score and a 76 validation accuracy score. [Here](https://github.com/Joshua-Hill-Science/Landscapes/blob/ross/Project_4_Ross.ipynb) is a link to my collab notebook.

## Lime
We also used LIME to visualize how the model makes decisions. Below is an example of an original image, the LIME explainer image, and the models predictions. The green on the LIME image shows parts of the image that positively affect the model accuracy and the red negatively affects the model.

#### Original:

![test_1777-mountain-preds-1](https://user-images.githubusercontent.com/84738906/129249355-a0b4acfa-77ff-430c-abb4-b28e13491e7b.jpg)

#### LIME Explainer:

![test_1777-mountain](https://user-images.githubusercontent.com/84738906/129249278-2f531925-484a-46d0-b243-a8b3ffeb0043.jpg)

#### Predictions:

![unnamed](https://user-images.githubusercontent.com/84738906/129249900-da956caf-c676-4681-a28b-c3f6eeaf20b1.png)
