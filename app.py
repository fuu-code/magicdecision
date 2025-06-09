from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    with open("answers.txt") as data:
        all_data = [info.strip() for info in data.readlines()]
    answers = all_data

    random_ans = random.choice(answers)

    answer_default = "I'll help you decide"
    question_info = "Ask a question"

    if request.method == "POST":
        question_info = request.form.get("name")
        answer_default = random_ans 
    
    return render_template('index.html', answer=answer_default, question=question_info)


if __name__ == "__main__":
    app.run(debug=False)
