import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():
    #Menampilkan gambar header
    image = Image.open('header.jpg')
    st.image(image)
    #Membuat title
    st.title('Corn Leaf Disease Prediction') 

    #Menampilkan gambar
    image = Image.open('corn.jpg')
    st.image(image, caption = 'Corn Plant')

    
    #Membuat garis
    st.markdown('----')
    
    #Membuat subheader
    st.subheader('What is corn disease?', divider='blue')
    
    #Membuat tulisan
    st.write('Corn, or maze, is a worldwide mass-produced agricultural crop. In addition to being consumed directly as food, it forms the basis for many other products such as cooking oil, starch, flour, sugar, biofuel, alcohol, and animal feed. Corn grows in varying environmental conditions and it is considered one of the most important crops characterized by high genetic diversity and production potential, along with rice and wheat [9]. The global corn production reached 1.15 billion tons in 2020 [10]. It is naturally exposed to many diseases that can attack various parts of the plant including the leaves, trunk, and fruit at all growth stages. This has a direct impact on the yield of corn harvest and consequently can lead to great financial loss. On a global scale, depleted agricultural production of staple crops such as corn can lead to food shortages, hunger, or even famine [11]. Diseases that infect corn leaves during the growth process are the most dangerous of these maladies. Hence, this work considers three common leaf diseases [12]: Cercospora leaf spot, common rust, and northern leaf blight.')
    
    #Membuat garis
    st.markdown('----')
    
    #Header for sleep disorder
    st.subheader('List Of Corn Disease', divider='blue')
    
    #Membuat tampilan coloumn
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        #Header column
        st.header("Blight Disease")

        #Menampilkan gambar
        st.image("https://cals.cornell.edu/sites/default/files/styles/three_card_callout/public/2021-02/anthracnose02-400x267.jpg?h=a61266fd&itok=e36ASkdw")
        
        #Membuat tulisan
        st.write("Anthracnose leaf blight of corn caused by the fungus Colletotrichum graminicola. The fungus overwinters on corn debris producing spores that infect the next year’s crop. Mild, wet conditions favor disease as spores are spread through rain splashing. Anthracnose leaf blight occurs early in the growing season affecting lower leaves initially with late season disease progression affecting the upper leaves.")
    with col2:
        #Header column
        st.header("Common Rust")

        #Menampilkan gambar
        st.image("https://cals.cornell.edu/sites/default/files/styles/three_card_callout/public/2021-02/commrust2-9-400x267.gif?h=a61266fd&itok=6PGKkhmQ")
        
        #Membuat tulisan
        st.write("Common rust is caused by the fungus Puccinia sorghi. Late occurring infections have limited impact on yield. The fungus overwinters on plants in southern states and airborne spores are wind-blown to northern states during the growing season. Disease development is favored by cool, moist weather (60 – 70◦ F).")        
        
    with col3:
        #Header column
        st.header("Gray Leaf Spot")
        
        #Menampilkan gambar
        st.image("https://cals.cornell.edu/sites/default/files/styles/three_card_callout/public/2021-02/gray-leaf-spot-on-corn-07282020-chemung-ny-5744-web.jpg?h=bc58accd&itok=Csddl9J0")
        
        #Membuat tulisan
        st.write("Gray leaf spot is caused by the fungus Cercospora zeae-maydis. Epidemics of gray leaf spot have been observed in New York State in the Southern Tier and the Hudson River Valley. New hot spots of the disease have been reported in the Mohawk Valley and the Leatherstocking Region. Gray leaf spot is favored by wet humid weather as often found in valley microclimates. Additionally, it is favored in situations with reduced tillage and continuous corn. Airborne spores are spread locally and regionally from corn debris.")
    
    with col4:
        #Header column
        st.header("Healthy Leaf")

        #Menampilkan gambar
        st.image("https://www.garden.eco/wp-content/uploads/2018/04/corn-leaves.jpg")
        
        #Membuat tulisan
        st.write("The healthy corn leaf exhibits vibrant green coloration, firm texture, and absence of discoloration or irregularities, showcasing robust growth and optimal photosynthetic activity.")
    
    #Menampilkan tulisan
    st.write('Copyright by Susantohamzah')

#condition untuk run file
if __name__ == '__main__':
    run()