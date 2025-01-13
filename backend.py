from flask import Flask, request, jsonify
from transformers import pipeline
import os
import math

app = Flask(__name__)


TRANSCRIPTS_FOLDER = r"/workspaces/Text-Sentimental-Analysis/transcript"

sentiment_analyzer = pipeline("sentiment-analysis")


def analyze_long_text(text, chunk_size=512):
    
    
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    
    results = []
    for chunk in chunks:
        result = sentiment_analyzer(chunk)
        results.append(result[0])  

    positive_score = sum(res['score'] for res in results if res['label'] == 'POSITIVE')
    negative_score = sum(res['score'] for res in results if res['label'] == 'NEGATIVE')
    total_score = positive_score - negative_score

    if total_score > 0.5:
        overall_sentiment = "Strongly Positive"
    elif total_score > 0:
        overall_sentiment = "Positive"
    elif total_score < -0.5:
        overall_sentiment = "Strongly Negative"
    elif total_score < 0:
        overall_sentiment = "Negative"
    else:
        overall_sentiment = "Neutral"

    return {
        "chunk_results": results,
        "overall_sentiment": overall_sentiment,
        "positive_score": positive_score,
        "negative_score": negative_score,
        "total_score": total_score,
    }


@app.route("/analyze", methods=["POST"])
def analyze():
    """Analyze a single transcript."""
    data = request.json
    if "transcript" not in data:
        return jsonify({"error": "Transcript not provided"}), 400

    transcript = data["transcript"]
    result = analyze_long_text(transcript)

    return jsonify(result)


@app.route("/analyze_all", methods=["GET"])
def analyze_all():
    """Analyze all transcripts in the folder."""
    if not os.path.exists(TRANSCRIPTS_FOLDER):
        return jsonify({"error": f"Folder '{TRANSCRIPTS_FOLDER}' does not exist"}), 400

    all_results = {}
    for file_name in os.listdir(TRANSCRIPTS_FOLDER):
        if file_name.endswith(".txt"):
            file_path = os.path.join(TRANSCRIPTS_FOLDER, file_name)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    transcript = file.read()
                    result = analyze_long_text(transcript)
                    all_results[file_name] = result
            except Exception as e:
                all_results[file_name] = {"error": f"Could not process file: {e}"}

    return jsonify(all_results)


if __name__ == "__main__":
    app.run(debug=True)