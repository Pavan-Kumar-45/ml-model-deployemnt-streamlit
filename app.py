import streamlit as st 
import os 
import boto3
bucket_name = "mlopsudemy"
s3 = boto3.client('s3')

st.header("Machine Learning Model Deployment at Streamlit Server")
paginator = s3.get_paginator('list_objects_v2')
local_path = 'tinybert-sentiment-analysis'        # Local destination folder
s3_path = 'ml_models/tinybert-sentiment-analysis/'             # S3 prefix (acts like a folder)

def download_directory(local_path, s3_prefix):
    # Paginator handles large numbers of objects (splits into pages)
    for result in paginator.paginate(Bucket=bucket_name, Prefix=s3_prefix):
        if 'Contents' in result:     # Check if this page has any objects
            for key in result['Contents']:  # Loop through each object
                s3_key = key['Key']  # Get the full S3 key (path)
                
                # Build local file path
                local_file = os.path.join(local_path, os.path.relpath(s3_key, s3_path)).replace('\\','/')
                
                # Create directories if they don't exist
                os.makedirs(os.path.dirname(local_file), exist_ok=True)
                
                # Download the file
                s3.download_file(bucket_name, s3_key, local_file)


 

flag = st.button("Download Model")

if flag:
    with st.spinner("Downloading..."):
        download_directory(local_path, s3_path)
    st.success(f"Model downloaded to {local_path}")


text = st.text_area("Enter Your Review : " , "Type...") 

predict = st.button("Predict") 

if predict : 
    with st.spinner("Predicting...") : 
        from transformers import pipeline 
        import torch 

        device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        classifier = pipeline('text-classification' , model = 'tinybert-sentiment-analysis' , device=device)

        output = classifier(text)

        st.write(output)
        # st.info(output)

        
