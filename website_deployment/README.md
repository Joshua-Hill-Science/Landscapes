# Website running instructions.
Here are the files, minus the model for deploying our website. Given the size of the model file, it is kept locally.

## Requirements:
All python packages can be found in the requirements.txt file.<br>
To create a new conda environment to use this repo, run:<br><br>
conda create --name {name}-env pip<br>
conda activate {name}-env<br>
pip install -r requirements.txt<br>
Note that this environment does not include Jupyter Notebook, it only includes the requirements for the Streamlit app.<br>

## Starting the Website:
Once installed run the following line within terminal.<br><br>
conda activate {name}-env<br>
streamlit run Landscape_Prediction_Website.py

## Loading the images:
To import an image the code is written to run examples from the Kaggle Dataset, we did not test running other images with different aspect ratios. Please commit on this Repo if you attempt this, we would like to know the result.
