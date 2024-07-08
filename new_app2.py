import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import Image
import base64

# Load the saved model

model = load_model('glaucoma_model6.keras')
class_dict = np.load("class_names.npy") #labels file we have saved as array

def predict(image):
    IMG_SIZE = (1, 224, 224, 3)

    img = image.resize(IMG_SIZE[1:-1])
    img_arr = np.array(img)
    img_arr = img_arr.reshape(IMG_SIZE)

    pred_proba = model.predict(img_arr)
    pred = np.argmax(pred_proba)
    return pred

def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        base64_img = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{base64_img}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
contnt = "<p>Herbal medicines are preferred in both developing and developed countries as an alternative to " \
         "synthetic drugs mainly because of no side effects. Recognition of these plants by human sight will be " \
         "tedious, time-consuming, and inaccurate.</p> " \
         "<p>Applications of image processing and computer vision " \
         "techniques for the identification of the medicinal plants are very crucial as many of them are under " \
         "extinction as per the IUCN records. Hence, the digitization of useful medicinal plants is crucial " \
         "for the conservation of biodiversity.</p>"

if __name__ == '__main__':
    add_bg_from_local("Background5.webp")
    new_title = '<p style="font-family:sans-serif; color:maroon; font-size: 50px;">Glaucoma Stages Detection</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    contnt = '<p style="font-family:sans-serif; color:Navy; font-size: 30px;">Glaucoma Identification</p>'
    st.markdown(contnt,unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        img = img.resize((300, 300))
        st.image(img)
        if st.button("Predict"):
            pred = predict(img)
            name = class_dict[pred]
            result = f'<p style="font-family:sans-serif; color:Red; font-size: 36px;">The given image is {name}</p>'
            st.markdown(result, unsafe_allow_html=True)
            if name=='Glaucoma_advanced':
               k = f'<p style="font-family:sans-serif; color:Blue; font-size: 32px;">Preventive measure: Frequent and close monitoring by your eye care specialist</p>'
               st.markdown(k, unsafe_allow_html=True)
            elif name=='Glaucoma_early':
                k = f'<p style="font-family:sans-serif; color:Blue; font-size: 32px;">Preventive measure: Schedule comprehensive eye exams at least every 1-2 years, especially if you are at risk or over 40.</p>'
                st.markdown(k, unsafe_allow_html=True)
            elif name=='Glaucoma_moderate':
                k = f'<p style="font-family:sans-serif; color:Blue; font-size: 32px;">Preventive measure: Increase the frequency of eye exams to monitor progression and adjust treatment as needed.</p>'
                st.markdown(k, unsafe_allow_html=True)
            else:
                k = f'<p style="font-family:sans-serif; color:Blue; font-size: 32px;">Preventive measure: Frequently check your eyes so that you are not effected by glaucoma.</p>'
                st.markdown(k, unsafe_allow_html=True)

