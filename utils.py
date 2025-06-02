%%writefile utils.py
from diffusers import StableDiffusionPipeline
import torch

# Load the model once globally
model_id = "stabilityai/stable-diffusion-2"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

#def generate_image_from_prompt(prompt):
#    image = pipe(prompt).images[0]
#    return image
def generate_image_from_prompt(prompt):
    styled_prompt = f"{prompt}, in 2D cartoon style"
    image = pipe(styled_prompt).images[0]
    return image

# Optional: GROQ function (if needed)
import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def split_into_scenes(story_text, num_scenes=5):
    prompt = f"""
Split the following story into {num_scenes} distinct scenes.
For each scene, return the exact sentence(s) from the story that describe the scene,
without changing or renaming anything.
Story:
\"\"\"{story_text}\"\"\"
Respond in a numbered list format.
"""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    json_data = {
        "messages": [
            {"role": "system", "content": "You are a screenplay breakdown assistant."},
            {"role": "user", "content": prompt}
        ],
        "model": "llama3-70b-8192"
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=json_data)

    if response.status_code != 200:
        print(f"Error from GROQ API: {response.status_code}, {response.text}")
        return []

    output = response.json()["choices"][0]["message"]["content"]
    scenes = []
    for line in output.strip().split('\n'):
        line = line.strip()
        if line and (line[0].isdigit() and line[1] in ['.', ')']):
            scene_text = line[line.find('.')+1:].strip()
            scenes.append(scene_text)

    return scenes[:num_scenes]
