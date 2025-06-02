# 🎬 Script2Scene - AI Storyboard Generator

**Script2Scene** is an AI-powered web app that takes a short story or script and automatically:
- Splits it into meaningful visual scenes (using Groq's LLaMA3),
- Generates an image for each scene (using HuggingFace Diffusers & Stable Diffusion),
- Displays a complete storyboard — in the style you choose!


## 🚀 Features

- ✂️ **Automatic Scene Splitting** using LLaMA 3 via Groq API
- 🎨 **AI Image Generation** via Stable Diffusion (`diffusers`)
- 🎭 **Selectable Styles**: Realistic, Cartoon, Anime, Pixel Art, Sketch
- 🖼️ **Storyboard View**: See your entire story illustrated, scene by scene
- 🌐 **Deployable from Colab with a public link using LocalTunnel**


## 🔧 Requirements

Dependencies are listed in `requirements.txt`

Install them with:

```bash
pip install -r requirements.txt
```


## 🔑 API Keys Required

### To acquire API key:
* Go to groq.com > Developers > Free API Key or Go to https://console.groq.com/keys
* Login with account
* Select Create API KEY > Enter display name for API key (any) > Submit > copy the API Key > Paste it where it says "your_groq_api_key_here"

Now, make sure to set the following as environment variable (you can use `.env` file or manually set them):

```env
GROQ_API_KEY=your_groq_api_key
```


## 💻 How to Run in Google Colab

1. Upload `app.py`, `utils.py`, and `requirements.txt` to Colab.
2. Install dependencies:

```python
!pip install -r requirements.txt
```

3. Set your API key in the notebook:

```python
import os
os.environ['GROQ_API_KEY'] = "your_groq_api_key"
```

4. Launch Streamlit with public access:

```python
!wget -q -O - ipv4.icanhazip.com  # Show Colab IP (optional)
!streamlit run app.py & npx localtunnel --port 8501  # Get public URL
```

5. Visit the generated URL to use your app! 🎉


## 📁 Project Structure

```
script2scene/
│
├── app.py               # Streamlit UI
├── utils.py             # Scene splitting + image generation
├── requirements.txt     # Dependencies
└── README.md            # You're here!
```


## 🤖 Models Used

* **LLaMA3-70B** from Groq (for breaking story into scenes)
* **Stable Diffusion 2 / OpenJourney** via HuggingFace (for scene image generation)


## ✨ Future Ideas

* Add character and location tracking
* Add audio narration
* Download full storyboard as PDF or ZIP


## 🧑‍💻 Author

* Zahra Batool :D

