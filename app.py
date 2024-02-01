import streamlit as st
import google.generativeai as genai
import os
from PIL import Image
#To load all environment variable
from dotenv import load_dotenv
load_dotenv()
#Gemini Configuration
genai.configure(api_key="AIzaSyB2hmhEUf9PlZapwRzkjLZChXvKADDYDMo")

#To write a response from image
def get_response(ip_prompt,img):
    model=genai.GenerativeModel("gemini-pro-vision")
    response=model.generate_content(ip_prompt,img)
    return response.text

#Default Image format for Google Gemini
def image_format(img):
    byte_data=img.getvalue()
    image_set=[{"mime/type":img.type,"data":byte_data }]
    return image_set

#With streamlit
st.set_page_config("Calories Advisor")
st.header("Check here before you have!")
uploadfile=st.file_uploader("Choose a image", type=["JPEG","JPG","png"])
img=""
if uploadfile is not None:
    img=Image.open(img)
    st.image(img,caption="Uploaded Image.",use_column_width=True)
submit=st.button("Help me to unlock the calorie details!")

ip_prompt="""You are the nutritionist where you need to see the image and calculate the calories and need
            to provide the calories details  in below format
                1. Item 1 - no.of calories 
                2. Item 2- no.of calories
                _____
                _____
                Finally you need to mention the healthy and junk percentage of that food, and also mention the 
                percentage split of carbohydrate,protein,fat and fiber and also please recommand which type of health problem
                people can intake this food."""

#Main
if submit:
    if uploadfile is not None:
        image_data=image_format(uploadfile)
        response_gemini=get_response(ip_prompt,image_data)
        st.header("Here is the calories details ...")
        st.write(response_gemini)
    else:
        FileNotFoundError("Kindly upload a image to check calories")

