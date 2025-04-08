from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # ⬅ Loads .env into environment variables

api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
client = OpenAI(api_key=api_key)

# Fact-checking prompt
FACT_PROMPT = (
    "You are analyzing a short passage of text. Even if the text is incomplete or cut off, "
    "your job is to:\n"
    "1. Infer the most likely full factual claims based on what's visible.\n"
    "2. Evaluate the truth of each inferred claim using public knowledge.\n"
    "3. Output a list of claims, each marked as True, False, or Uncertain, followed by a short explanation.\n"
    "4. Use your judgment and critical thinking to discern truth from satire or parody, and identify if the text is being satirical and/or ironic.\n"
    "Be thorough and confident. Do not skip partial statements—analyze what can be reasonably inferred."
)

@app.route("/fact-check", methods=["POST"])
def fact_check():
    data = request.get_json()
    text = data.get("text", "")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a fact-checking assistant."},
            {"role": "user", "content": f"{FACT_PROMPT}\n\nText: {text}"}
        ],
        max_tokens=500
    )

    reply = response.choices[0].message.content.strip()
    return jsonify({"verdict": reply})

if __name__ == "__main__":
    app.run(port=5005)
