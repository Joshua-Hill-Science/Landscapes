import numpy as np
import streamlit as st
from PIL import Image, ImageOps
import tensorflow
from sklearn.cluster import MiniBatchKMeans
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import cv2
from lime import lime_image
from skimage.segmentation import mark_boundaries

def color_compress_KNN(image, KNN=4):
    import warnings; warnings.simplefilter('ignore') 
    Kmeans_images = []
    rescaled_image = np.array(image) / 255.0 # use 0...1 scale
    preprocessed_image = rescaled_image.reshape(150 * 150, 3)
    kmeans = MiniBatchKMeans(KNN)
    kmeans.fit(preprocessed_image)
    new_colors = kmeans.cluster_centers_[kmeans.predict(preprocessed_image)]
    color_compressed_image = new_colors.reshape(np.array(image).shape)
    #Changed to predict in Warren's Model
    reshaped_cci = cv2.resize(color_compressed_image, (75,75)).reshape(1,75,75,3)
    return reshaped_cci

def import_and_predict(image_data, model):
    
        img_output = color_compress_KNN(image_data)
        prediction = model.predict(img_output)[0]
        
        return prediction, img_output


def image_expl(model,image_array):
    '''
    Takes a model, single image array, name string of the model, and the true label of the image.
    Uses LIME to get an image explainer and plots the image and explaination.
    '''
    
    explained_image, ax = plt.subplots()
    #instantiate explainer
    explainer = lime_image.LimeImageExplainer(random_state=1)
    #explain an image caste to double bc updated keras version, pass predictor 
    explanation = explainer.explain_instance(image_array[0].astype('double'), model.predict)
    #show the image
    ax = plt.imshow(image_array[0])
    #get the mask for the prediction
    temp, mask = explanation.get_image_and_mask(model.predict(image_array.reshape((1,75,75,3))).argmax(axis=1)[0], positive_only=False, hide_rest=False)
    #show image and mask together
    ax = plt.title("Best Explaination of What Our Model is Seeing.")
    ax = plt.imshow(mark_boundaries(temp, mask))
    plt.axis("off")
    return explained_image
    
    
class_names=['mountain', 'street', 'glacier', 'buildings', 'sea', 'forest']
def pick_a_graph(model, image, color_coder, graph_type="bar"):
    if graph_type == "bar":
        fig_bar, ax = plt.subplots()
        ax = plt.bar([0,1,2,3,4,5], model.predict(image)[0])
        for i in color_coder:
            if color_coder[i] == model.predict(image)[0].max():
                ax[i].set_color("r")
                Best_guess = mpatches.Patch(color='red', label=round(color_coder[i],2))
            else:
                ax[i].set_color("b")
        plt.legend(handles=[Best_guess])
        plt.title("Model's Confidence as a Bar Plot")
        plt.ylabel("Model Confidence")
        plt.xlabel("Classes")
        ax = plt.xticks(ticks=[0,1,2,3,4,5],labels=[x.title() for x in class_names], size=10)
        return fig_bar
    elif graph_type == "donut":
        fig_pie, ax = plt.subplots(subplot_kw=dict(aspect="equal"))
        recipe = color_coder
        data = color_coder.values()
        wedges, texts = plt.pie(color_coder.values(), wedgeprops=dict(width=0.5), startangle=-40)
        bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

        ax.legend(wedges, [x.title() for x in class_names], title="Classes")
        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            ax.annotate(round(color_coder[i],2), xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                        horizontalalignment=horizontalalignment, **kw)
        ax.set_title("Model's Confidence as a Pie Chart")
        return fig_pie
    elif graph_type == "lollipop":
        # creating an empty chart
        fig_lollipop, ax = plt.subplots()
        # plotting using plt.stem
        ax = plt.stem([0,1,2,3,4,5], model.predict(image)[0]
                  ,use_line_collection=True, basefmt=' ')
        plt.title("Model's Confidence as a Lollipop Graph")
        plt.ylabel("Model Confidence")
        plt.xlabel("Classes")
        ax = plt.xticks(ticks=[0,1,2,3,4,5],labels=[x.title() for x in class_names])
        return fig_lollipop
    elif graph_type == "scatter":
        fig_scatter= plt.figure()
        ax1=fig_scatter.add_subplot(111)
        X=[0,1,2,3,4,5]
        y=model.predict(image)[0]
        for i in color_coder:
            if color_coder[i] == y.max():
                ax1.scatter([i], y[i], c ='r', marker="*", s=750)
                ax1.scatter(np.delete(X,i), np.delete(y,i))
                Best_guess = mpatches.Patch(color='red', label=round(color_coder[i],2))
        plt.legend(handles=[Best_guess])
        plt.title("Model's Confidence as a Scatter Plot")
        plt.ylabel("Model Confidence")
        plt.xlabel("Classes")
        ax1= plt.xticks(ticks=X,labels=[x.title() for x in class_names])
        return fig_scatter
    
    
    
# Start of the website
# Loading in the Model
model = tensorflow.keras.models.load_model("Models/3rd-color_comp_model.h5")
page_image=("Sample_Pictures/Icon.jpg")
st.set_page_config(page_title="Image Classification",page_icon=page_image,layout="wide")
# Creating a centered layout
_, center_,_ = st.columns([1,2,1])
with center_:
    st.markdown("""
             # Intel Nature Image Predictor
             """
             )
    st.markdown(" ## **Data found on Kaggle**:")
    st.caption("https://www.kaggle.com/puneet6060/intel-image-classification")

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    st.image("Sample_Pictures/Buildings_Image.jpg", caption="Building Example", width= 250)
with col2:
    st.image("Sample_Pictures/Forest_Image.jpg", caption="Forest Example", width= 250)
with col3:
    st.image("Sample_Pictures/Glacier_Image.jpg", caption="Glacier Example", width= 250)
with col4:
    st.image("Sample_Pictures/Mountain_Image.jpg", caption="Mountain Example", width= 250)
with col5:
    st.image("Sample_Pictures/Sea_Image.jpg", caption="Sea Example", width= 250)
with col6:
    st.image("Sample_Pictures/Street_Image.jpg", caption="Street Example", width= 250)

st.markdown("## This image classifier web app will predict which of 6 classes your uploaded Image should be.")
st.markdown("## Today we will be showing you how this Image performs in our model.")

file = st.file_uploader("Please upload an image file", type=["jpg","png"])
#
if file is None:
    st.text("Please select an Image from the Kaggle Dataset to be classified")
else:
    image = Image.open(file)
    prediction, new_image = import_and_predict(image, model)
    explained_image=image_expl(model, new_image)
    color_coder=dict(enumerate(prediction,0))
    
    fig_bar, ax = plt.subplots()
    plt.title("Model's Probablity for Class of Given Image")
    ax=plt.bar([0,1,2,3,4,5], prediction, edgecolor='black')
    for i in color_coder:
        if color_coder[i] == prediction.max():
            ax[i].set_color("r")
            Best_guess = mpatches.Patch(color='red', label=round(color_coder[i],2))
        else:
            ax[i].set_color("b")
    plt.legend(handles=[Best_guess])
    ax=plt.xticks(ticks=[0,1,2,3,4,5],labels=['mountain', 'street', 'glacier', 'buildings', 'sea', 'forest'])
    cola , colb, colc = st.columns([1,1,1])
    with cola:
        st.image(image,caption="Original Image", width=500)
    with colb:
        st.image(new_image,caption="Color Compressed Image", width=500)
    with colc:
        choice = st.selectbox("Graph Selector", ["Bar", "Donut", "Lollipop", "Scatter"])
        result_fig=pick_a_graph(model, new_image, color_coder, choice.lower())
        st.pyplot(result_fig)
        
# Lime required Section
    _,final,_ =st.columns([1,2,1])
    with final: 
        if st.button('How did the Model do that!?!',  help="Click Me to Find out!"):
            st.pyplot(explained_image)