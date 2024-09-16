import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import io

# Load the Stable Diffusion model
@st.cache_resource
def load_model():
    model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token=True)
    model.to("cuda" if torch.cuda.is_available() else "cpu")
    return model

model = load_model()

def generate_image(prompt):
    # Generate the image using the model
    generator = torch.manual_seed(42)  # Optional: For reproducibility
    image = model(prompt).images[0]
    return image

def save_image(image, file_name):
    image.save(file_name)

def main():
    st.title("Stable Diffusion Text-to-Image Generator")
    
    # Input from the user
    text_prompt = st.text_area("Enter your text prompt:", "A serene beach at sunset")

    if st.button("Generate Image"):
        with st.spinner("Generating image..."):
            # Generate image
            image = generate_image(text_prompt)
            
            # Convert image to bytes for download
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_str = buffered.getvalue()
            
            # Display the image
            st.image(image, caption="Generated Image", use_column_width=True)

            # Provide a download button
            st.download_button(
                label="Download Image",
                data=img_str,
                file_name="generated_image.png",
                mime="image/png"
            )

if __name__ == "__main__":
    main()
