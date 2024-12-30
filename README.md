# Large Text Model & Large Image Model using Gemini

# visit Link - https://textmode.streamlit.app/
---
# visit Link - https://large-image-model.streamlit.app/

## Overview
This repository showcases two powerful AI models built using Google's **Gemini API**:
1. **Large Text Model** - A model designed for processing and generating human-like text.
2. **Large Image Model** - A model for image understanding and generation.

The project demonstrates the integration of **Google's Generative AI** capabilities to handle text and image inputs with advanced processing features.

---

## Features
- **Text Model**: 
  - Processes and generates meaningful, coherent text.
  - Flexible input for various applications like summaries, translations, or creative writing.
- **Image Model**:
  - Analyzes and describes uploaded images.
  - Supports applications like image tagging, object detection, and more.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/chandankrsah09/Large-image-model.git
cd Large-image-model
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory with the following content:
```plaintext
GOOGLE_API_KEY=your-google-api-key
```

Replace `your-google-api-key` with your actual API key for the Gemini service.

### 5. Run the Application
Run the application using:
```bash
python app.py
```

---

## Usage
1. **Text Input**:
   - Enter a prompt in the input box to generate or process text using the **Large Text Model**.

2. **Image Input**:
   - Upload an image file (`.jpg`, `.jpeg`, `.png`) to analyze and generate insights using the **Large Image Model**.

3. The app displays the model's response for both text and image inputs.

---

## Project Structure
```
.
├── app.py                 # Main application file
├── vision.py              # Code for image model
├── requirements.txt       # Python dependencies
├── .env.example           # Example for environment variables
├── README.md              # Project documentation
└── venv/                  # Virtual environment (not included in repo)
```

---

## Future Enhancements
- Support for multimodal inputs (text + image).
- Enhanced model fine-tuning for domain-specific use cases.
- Integration with additional APIs for richer features.

---

## Contribution
Contributions are welcome! Feel free to open issues or submit pull requests to improve this repository.

---

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

---
