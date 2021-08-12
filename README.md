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

Baseline Model
The baseline model was made from only images compressed from 150 pixels square to 75 pixels square. This model overfit the training data a lot so it was obvious that some regularization would be needed. Here is a plot of the training and validation accuracy:

Baseline Model Accuracies

The big difference between training and validation accuracy shows overfitting to the training data.

Final Model
Our final model used images that were compressed to 75 pixels square and had compressed color data. Here is an example of a before and after compressing:

Before Compressing

After Compressing

The final model has an accuracy of about 70% on the testing data that it has not seen before.

We also used LIME to visualize how the model makes decisions. Below is an example of an original image, the LIME explainer image, and the models predictions. The green on the LIME image shows parts of the image that positively affect the model accuracy and the red negatively affects the model.

Original

LIME Explainer

Predictions
