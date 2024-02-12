#Import Library
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json
from PIL import Image
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model 
import gdown

# URL model di Google Drive
model_url = 'https://drive.google.com/uc?id=1Pt_vxwxA5QkIKOx2BXQqy9P7jT1ZPEYz'

# Lokasi penyimpanan lokal
model_path = 'corn_model.h5'

# Unduh model
gdown.download(model_url, model_path, quiet=False)

# Load model
model_rf = load_model('corn_model.h5')


# Mapping class untuk tampilan prediction
class_labels = {0: 'Blight', 1: 'Common Rust', 2: 'Gray Leaf Spot', 3: 'Healthy'}

def run():
    '''
    Fungsi running file 
    '''
    
    #Header
    st.write('## Corn Leaf Picture')
    
    #Form Upload File
    uploaded_file = st.file_uploader("Upload a Picture", type=["jpeg", "jpg"])

    # Condition ketika data sudah di upload
    if uploaded_file is not None:
        
        # Menampilkan gambar yang di upload
        st.image(uploaded_file, caption='Uploaded Corn Leaf Picture', use_column_width=True)

        # proses gambar untuk prediction
        image = Image.open(uploaded_file)
        
        # Resize gambar sesuai dengan model
        image = image.resize((256, 256))
        
        # Convert gambar ke array
        img_array = np.asarray(image)
        
        #Expand dimensi untuk match model
        img_array = np.expand_dims(img_array, axis=0)

        # Prediksi dengan model
        prediction = model_rf.predict(img_array)
        
        #Match model dengan predict
        predicted_class = np.argmax(prediction)

        # Menampilkan hasil predict
        st.write('## Prediction Result:')
        st.write(f'### This corn has {class_labels[predicted_class]} disease')
        
        #Condition untuk menampilkan teks tambahan
        if predicted_class==0:
            
            #Membuat tulisan
            st.write(f'### What is Blight?')
            st.write(f'Anthracnose leaf blight of corn caused by the fungus Colletotrichum graminicola. The fungus overwinters on corn debris producing spores that infect the next year’s crop. Mild, wet conditions favor disease as spores are spread through rain splashing. Anthracnose leaf blight occurs early in the growing season affecting lower leaves initially with late season disease progression affecting the upper leaves.')
            st.write(f'### Symptoms')
            st.write(f'Early season symptoms appear as small, oval to elongate water soaked lesions on lower leaves. These semitransparent spots gradually enlarge to ¾ inch long and become tan at the center with red to reddish-brown or yellow-orange borders. The entire leaf may become blighted as the lesions coalesce and severely blighted leaves will yellow and die. During periods of wet weather, fungal fruiting bodies appearing as black specks may be found within the center of the lesions. In late season, symptoms may appear on upper leaves.')
            
        elif predicted_class==1:
            
            #Membuat tulisan
            st.write(f'### What is Common Rust?')
            st.write(f'Common rust is caused by the fungus Puccinia sorghi. Late occurring infections have limited impact on yield. The fungus overwinters on plants in southern states and airborne spores are wind-blown to northern states during the growing season. Disease development is favored by cool, moist weather (60 – 70◦ F).')
            st.write(f'### Symptoms')
            st.write(f'ymptoms of common rust often appear after silking. Small, round to elongate brown pustules form on both leaf surfaces and other above ground parts of the plant. As the pustules mature they become brown to black. If disease is severe, the leaves may yellow and die early.')
            
        elif predicted_class==2:
            
            #Membuat tulisan
            st.write(f'### What is Gray Leaf Spot?')
            st.write(f'Gray leaf spot is caused by the fungus Cercospora zeae-maydis. Epidemics of gray leaf spot have been observed in New York State in the Southern Tier and the Hudson River Valley. New hot spots of the disease have been reported in the Mohawk Valley and the Leatherstocking Region. Gray leaf spot is favored by wet humid weather as often found in valley microclimates. Additionally, it is favored in situations with reduced tillage and continuous corn. Airborne spores are spread locally and regionally from corn debris.')
            st.write(f'### Symptoms')
            st.write(f'Symptoms of gray leaf spot are usually first noticed in the lower leaves. Initially, lesions of gray leaf spot begin as a small dot with a yellow halo. Lesions will elongate over time running parallel to the veins becoming pale brown to gray and rectangular in shape with blunt ends. These lesions can be described as having the appearance of a “matchstick.” Lesions may eventually coalesce killing the leaves. Leaves appear grayish in color due to the presence of fungal spores.')
        else:
            
            #Membuat tulisan
            st.write(f'Congratulations! Your corn is healthy!!!!')
            st.write(f'The healthy corn leaf exhibits vibrant green coloration, firm texture, and absence of discoloration or irregularities, showcasing robust growth and optimal photosynthetic activity.')

        
# condition run
if __name__ == '__main__':
   run()