from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# 微分する関数のリスト
functions = [
    {"func": "x", "derivative": "1"},
    {"func": "x^2", "derivative": "2x"},
    {"func": "x^3", "derivative": "3x^2"},
    {"func": "2x", "derivative": "2"},
    {"func": "3x^2", "derivative": "6x"},
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_question")
def get_question():
    func = random.choice(functions)
    return jsonify({"question": func["func"], "answer": func["derivative"]})


@app.route("/check_answer", methods=["POST"])
def check_answer():
    data = request.get_json()
    user_answer = data.get("answer", "").strip().lower()
    correct_answer = data.get("correct_answer", "").strip().lower()

    is_correct = user_answer == correct_answer
    message = "正解！" if is_correct else f"不正解です。正解は {correct_answer} です。"
    return jsonify({"correct": is_correct, "message": message})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
