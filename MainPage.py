import streamlit as st

# Set the page configuration with a title and an icon
st.set_page_config(
    page_title="Main Page",
    page_icon="👋",
)

# Display a welcome message on the main page
st.write("Grochem 👋")

# Display a success message on the sidebar prompting the user to select a page
st.sidebar.success("Select a page that you would like to view.")

# Add markdown content to the main page
st.markdown(
"""
Grochem, a cosmetic company that founded in 1900 years, started with air-freshener industry, 
then transform into household, thus comes. 
"""
)

def main():
    # Set the page configuration with a title and an icon
    st.set_page_config(page_title="Product Methodology", page_icon="💡")

    # Display the main header for the page
    st.write("# Product Methodology")
    
    # Display the header in the sidebar
    st.sidebar.header("Product Methodology")
    
    # Provide an introductory description of the page
    st.write(
        """This page explains how the product performs the defect detection by utilising object detection technique and image quality assessment."""
    )
    
    # Section header and image for PCB Defect Detection Process
    st.write("## PCB Defect Detection Process")
    
    
    # Detailed explanation of the PCB defect detection process
    st.write(
"""
### 1. Data Acquisition
- Images of PCB are taken by an Automated Optical Inspection(AOI) camera
- A collection of PCB images are then sent to us

### 2. Preprocessing
- Perform image annotation
- Perform augmentation to images

### 3. Model Training
- Prepare annotated dataset with labeled defect types
- Train a YOLOv8 deep learning model

### 4. Defect Detection 
- Model performs segmentation of PCB defects based on inputted image
"""        
    )  
    
    # Spacer for readability
    st.write("")
    
    # Section header and image for Deep Learning Model
    st.write("## Deep Learning Model")
    

    # Spacer for readability
    st.write("")
    
    # Section header and detailed explanation of the Pre-label Approach
    st.write("## Pre-label Approach")
    st.write(
"""
To address the “missing puzzle” of machine learning, which is the annotated printed circuit board, a pre-label approach is introduced. The labelling cost in PCBs area is relatively higher than other industries as there are required more professionals to identify. A pre-label approach has reduced the needs of professionals, and simplified the job of product owner by scanning through the result of pre-labeling, instead of manually labelling. A pre-label approach is completed via two steps. 

First, we start by manually labelling a small portion of the dataset, followed by training a model. In our experience, our team used 60~100 pcs of annotated images to train on YOLOv8-seg. The accuracy(mAP) varies from 93% to 98%. By implementing the simple model, we can annotate the remaining dataset with the simple model, and thus go through the result, validate the correctness of annotation, and adjust accordingly. 

Besides, in order to ensure the performance of a simple model on the unlabelled dataset, we can limit the number of predicted classes per entry, and adjust the confidence level, and even the Intersection of Union(IoU) to prevent overlapping. Not only that, image augmentation is also essential in this pre-labelled approach, as it can produce more training dataset in terms of multiplying. 

As the YOLOv8 is used and the Mosaic augmentation techniques are applied to YOLOv8 as well, it decreases the needs of large annotated dataset to reach the industry standard. 
"""
    )

    # Spacer for readability
    st.write("")
    
    # Section header and detailed explanation of the Over-rejection Test to Measure the Quality of Model
    st.write("## Over-rejection Test to Measure the Quality of Model")
    st.write(
"""
As the pixel by pixel approach performance results in a high false-positive rate, we introduced the deep learning approach. In order to prove to the industry that our deep learning model actually meets their requirements, a series of testing has been designed as a benchmark. 

Depending on the usage of object detection in other aspects, for example object tracking is more concerned on the mean average precision (mAP), as it could accept a false positive, and thus these false positives are handled when there is re-processing the data retrieved, by ignoring them. This approach is not applicable to the PCB manufacturing industry as the high volume of production, wastage of resources and in terms of cost effectiveness. In order to address that, we are not aiming to achieve high mAP, instead we aim to train a model that could pass the good unit test and over reject test. To train such a model, a series of null images is passed into the model, to better “understand” the targeting pattern that they should capture. A comparison on the same pre-trained model with and without null class is shown in the next section. 

Different from traditional models which aim to detect everything, by mixing the null class, it could more accurately capture, and reduce the false positives when only one class is inputted. Followed by the multiple classes annotation, the null class is actually impacting in reducing the false positives as well as the null class is a good one without any detection. Therefore, it trained the model to recognize such conditions should not be classified as defect.
"""
    )

# Run the main function when the script is executed
if __name__ == '__main__':
    main()
