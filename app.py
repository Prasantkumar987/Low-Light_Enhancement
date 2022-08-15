import streamlit as st
import os
from PIL import Image

def load_image(image_file):
	img = Image.open(image_file)
	return img

def main():
    st.title("Low Light Enhancement Application")

    menu = ["Image","Dataset","DocumentFiles","About"]
    choice = st.sidebar.selectbox("Models",menu)

    if(choice == "Image"):
        st.subheader("Image")
    
    elif (choice == "Dataset"):
        st.subheader("Dataset")

    elif (choice == "DocumentFiles"):
        st.subheader("DocumentFiles")

  
  
    if(choice == "Image"):
        # st.subheader("Image")
        uploaded_files = st.file_uploader("Upload Images", type=["png","jpg","jpeg"], accept_multiple_files=True)

        if uploaded_files is not None:
                # TO See details
                for image_file in uploaded_files:
                    # file_details = {"filename":image_file.name,"filetype":image_file.type,
                    #                 "filesize":image_file.size}
                    # st.write(file_details)
                    st.image(load_image(image_file), width=350)
                
                #Saving upload
                    with open(os.path.join("./test_input_data",image_file.name),"wb") as f:
                        f.write((image_file).getbuffer())

                    with st.spinner('Wait for it...'):
                        # st.snow()   
                        os.system("python main.py --phase test --test_dir ./test_input_data --save_dir ./test_output_data")
                        # st.image(load_image(os.path.join("./test_output_data",image_file.name)), width=350)
                        image = [os.path.join("./test_input_data",image_file.name), os.path.join("./test_output_data",image_file.name)]
                        st.image(image, width=300)
                    
                    st.success('Done!')
                    
                    
if __name__ == '__main__':        
    main()