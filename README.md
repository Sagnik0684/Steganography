**.gitignore**
```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]

# Virtual environment
venv/
.env

# Streamlit cache
.streamlit/

# Output files
output_images/
*.png
*.jpg
*.jpeg

# OS-specific files
.DS_Store
Thumbs.db
```  

**README.md**
```
# Steganography App

This is a simple **Steganography App** built with Python and Streamlit that allows users to hide and reveal messages inside images.

## Features
- Upload an image via **drag & drop**
- Choose to **hide or reveal** a message
- Enter a custom filename for output
- Download the processed image

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/steganography-app.git
   cd steganography-app
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate  # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the Streamlit app:
```bash
streamlit run steganography_app.py
```
Then open the displayed **localhost URL** in your browser.

## Hosting for Others on Local Network
Find your local IP:
```bash
ipconfig getifaddr en0  # For Mac (WiFi)
```
Run Streamlit with:
```bash
streamlit run steganography_app.py --server.address 0.0.0.0 --server.port 8501
```
Share **http://YOUR_LOCAL_IP:8501** with others on the same network.

## Contributing
Feel free to fork this repo and submit pull requests!
t