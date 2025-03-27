import streamlit as st
from stegano import lsb
from PIL import Image
import os

# Ensure output directory exists
output_dir = "output_images"
os.makedirs(output_dir, exist_ok=True)

st.title("Steganography App - Hide & Reveal Messages in Images")

# Upload Image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Select Mode: Hide or Reveal
mode = st.radio("Choose an action:", ["Hide a Message", "Reveal a Message"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    if mode == "Hide a Message":
        secret_message = st.text_area("Enter the message to hide:")
        output_filename = st.text_input("Enter output filename (without extension):", "stego_image")
        
        if st.button("Hide Message"):
            if secret_message:
                output_path = os.path.join(output_dir, f"{output_filename}.png")
                secret_img = lsb.hide(uploaded_file, secret_message)
                secret_img.save(output_path)
                st.success(f"Message hidden successfully! File saved as {output_path}")

                with open(output_path, "rb") as file:
                    st.download_button("Download Stego Image", file, file_name=f"{output_filename}.png")
            else:
                st.error("Please enter a message to hide.")

    elif mode == "Reveal a Message":
        if st.button("Reveal Message"):
            message = lsb.reveal(uploaded_file)
            if message:
                st.success(f"Hidden message: {message}")
            else:
                st.warning("No hidden message found.")