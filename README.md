# Text-Sentimental-Analysis

A simple yet powerful sentiment analysis tool that determines the sentiment of a given text using natural language processing techniques.

## 🚀 Live Demo
Stay tuned! Deployment coming soon.

## 📌 Features
- **Real-time Sentiment Analysis**: Detects positive, negative, and neutral sentiments.
- **User-Friendly Interface**: Built with Streamlit for seamless interaction.
- **Flask API**: Backend API for processing text inputs.
- **Preprocessing with NLTK & TextBlob**: Tokenization, stopword removal, and sentiment scoring.
- **CSV Upload Support**: Analyze sentiment for bulk text data.

## 🛠 Tech Stack
- **Programming Language**: Python
- **Frameworks & Libraries**: Streamlit, Flask, TextBlob, Pandas, NLTK, Requests

## 📂 Project Structure
```
├── transcript/
├── app.py
├── backend.py
├── requirements.txt
├── README.md
```

## 📦 Installation & Setup
### Prerequisites
- Python 3.x installed
- Required dependencies (see `requirements.txt`)

### Steps
1. **Clone the repository**
   ```sh
   git clone https://github.com/dshubh2809/Text-Sentimental-Analysis.git
   cd Text-Sentimental-Analysis
   ```
2. **Create a virtual environment & install dependencies**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. **Run the backend server**
   ```sh
   python backend.py
   ```
4. **Run the Streamlit app**
   ```sh
   streamlit run app.py
   ```
5. Open [http://localhost:8501](http://localhost:8501) to view the app.

## 🎨 UI Preview
![Sentiment Analysis Preview](public/images/preview.png)

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repo and submit pull requests.

