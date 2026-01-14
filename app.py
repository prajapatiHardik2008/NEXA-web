from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os
import apikeys

app = Flask(__name__)
api_open = apikeys.openai
# OpenAI Client (SECURE)
client = OpenAI(api_key=api_open)
@app.route('/')
def home():
    return render_template('index.html')


def nexa_ai(command):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are Nexa, a smart female AI assistant. "
                    "Made by Hardik on 24 January 2025. "
                    "Give short, clear answers."
                )
            },
            {"role": "user", "content": command}
        ]
    )
    return response.choices[0].message.content


@app.route('/run', methods=['POST'])
def run_api():
    data = request.get_json()
    question = data.get('question')

    if not question:
        return jsonify({"ans": "No question received."})

    answer = nexa_ai(question)
    return jsonify({"ans": answer})


if __name__ == '__main__':
    app.run(debug=True)
