# streamlit run app.py 
import streamlit as st 
from PIL import Image 
import time 

st.title("Machine Learning Model Deployment at streamlit Server")


st.header("Introduction")

st.subheader("This is Subheader")


st.text("This is text")

# Read Input from the used
input_text = st.text_input("Enter Text : ", "type here...")

 
st.text(input_text)

input_text = st.text_area("Enter here : " , "this is large text area ")

st.markdown("This text is ___really important___")
st.markdown("# This is Heading")
st.markdown("## This is Sub Heading")
# 2 spaces 
st.markdown("""1.  line one 
2.  line two   
3.  line three
""")

# button 
button = st.button("Click Me")
if button : 
    st.text("I am clicked")
    st.info("I am clicked. Snap me fast")
    st.toast("I will dissapear")
    st.warning("This is Warning")
    st.error("This is error")


# Image 
st.image("https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg?cs=srgb&dl=pexels-anjana-c-169994-674010.jpg" , width = 200)

img = Image.open("panda-1236875_640.jpg")
st.image(img,width=200)

# CheckBox 

flag = st.checkbox("Select Me")
if flag : 
    img = Image.open("panda-1236875_640.jpg")
    st.image(img,width=200)


# Radio Button 
selection = st.radio("Choose Model " , ["NLP" , "Image" , "Audio"])
st.text(selection)

# select box drop downarrow thing 
selection = st.selectbox("Choose Model " , ["NLP" , "Image" , "Audio"])
st.text(selection)

#  multi select 
selection = st.multiselect("Choose Model " , ["NLP" , "Image" , "Audio"])
st.text(selection)

with st.spinner("Downloadng") : 
    st.write("Dowload your model here")
    time.sleep(10)

# slider : select numerical value from the given list
# TH = 0.5 , large TH -> high precision , small TH -> high recall 
selection = st.slider("Set Threshold" , 0 , 100 , step = 5)
st.text(selection)


