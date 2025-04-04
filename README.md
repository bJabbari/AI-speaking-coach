# AI Speaking Coach (FastAPI Demo)

This is a simple model deployment demo using FastAPI. It demonstrates how to:

- Load a local image captioning model (BLIP-1)
- Use a remote LLM API (Together.AI) for text generation
- Chain their outputs to create a natural language response from an image

The main goal is to showcase the flexibility of using FastAPI for serving local models and integrating external APIs. This approach can be adapted for building scalable multimodal applications.

## How it works

1. A user uploads an image.
2. The app uses the [BLIP-1 image captioning model](https://huggingface.co/Salesforce/blip-image-captioning-base) to generate a visual description.
3. This caption is passed to a language model (via Together.AI API) to produce a speaking-style response (e.g., for CELPIP/PTE test prep).

This is a simplified setup for demonstration purposes. In real-world use cases, modern multimodal models (e.g. BLIP-2, Gemini 1.5 Pro) can directly process both text and images for much richer outputs.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/speaking-coach-demo.git
cd speaking-coach-demo
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your environment

Create a `.env` file and add your API keys:

```env
HF_API_TOKEN=your_huggingface_token
TOGETHER_API_KEY=your_together_api_key
```

### 5. Run the app

```bash
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000` in your browser.

## Deploying on GitHub & Render

### Upload to GitHub

1. Initialize a local Git repo:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/your-username/speaking-coach-demo.git
git push -u origin main
```

### Deploy on Render

1. Go to [render.com](https://render.com)
2. Click "New Web Service"
3. Connect your GitHub repository
4. Choose:
   - Runtime: Python 3
   - Start command: `uvicorn main:app --host=0.0.0.0 --port=10000`
5. Add your environment variables (`.env`) in Render's dashboard
6. Click "Deploy"

## Reference

- [BLIP-1: Salesforce/blip-image-captioning-base on Hugging Face](https://huggingface.co/Salesforce/blip-image-captioning-base)

---

Built for demonstration and educational purposes.
