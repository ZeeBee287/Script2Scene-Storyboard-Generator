%%writefile app.py
import streamlit as st
from utils import split_into_scenes, generate_image_from_prompt
import time

st.set_page_config(page_title="Script2Scene", layout="wide")
st.title("🎬 Script2Scene - AI Storyboard Generator")

st.markdown("Paste your story and get storyboard scenes generated using AI.")

with st.form("script_form"):
    story_text = st.text_area("Paste your story or script here:", height=300)
    num_scenes = st.slider("How many scenes to generate?", min_value=1, max_value=10, value=5)

    style = st.selectbox("Choose image style:", ["Realistic", "Cartoon", "Anime", "Pixel Art", "Sketch"])

    submit = st.form_submit_button("Generate Storyboard")

if submit and story_text:
    st.info("Splitting story into scenes...")
    scenes = split_into_scenes(story_text, num_scenes)

    if not scenes:
        st.error("Failed to split story into scenes. Please check API keys and connectivity.")
    else:
        st.success(f"{len(scenes)} scenes extracted.")
        st.markdown("---")
        st.header("📽️ Generated Storyboard")

        style_map = {
            "Realistic": "",
            "Cartoon": "in cartoon style",
            "Anime": "in anime style",
            "Pixel Art": "in pixel art style",
            "Sketch": "as a pencil sketch"
        }

        for i, scene in enumerate(scenes):
            st.subheader(f"Scene {i+1}")
            st.text(scene)
            with st.spinner("Generating image..."):
                styled_prompt = f"{scene}, {style_map[style]}"
                image = generate_image_from_prompt(styled_prompt)
                if image:
                    st.image(image, caption=scene)
                else:
                    st.warning("⚠️ Failed to generate image for this scene.")
                time.sleep(1)

        st.success("All scenes generated!")
