from flask import Flask, render_template, request
import random
import inflect
import re

app = Flask(__name__)
p = inflect.engine()


def format_word(words):
    # Replace 'and', ',' and '-'
    replace_dict = {",": "", "-": " "}
    old_word = "and "
    new_word = ""
    pattern = r"\b" + old_word + r"\b"
    formatted_words = "".join(
        [replace_dict.get(c, c) for c in words])
    result_formatted_word = re.sub(
        pattern, new_word, formatted_words).rstrip()
    return result_formatted_word


@app.route('/')
def index():
    number = generate_random_number()
    return render_template('index.html', number=number)


@app.route('/convert', methods=['POST'])
def convert():
    number = int(request.form['number'])
    words = request.form['words']
    correct_words = p.number_to_words(number)

    formatted_words = format_word(words)
    formatted_correct_words = format_word(correct_words)

    if formatted_words.lower() == formatted_correct_words.lower():
        result = "Congratulations! Your answer is correct."
    else:
        result = "Oops! Your answer is incorrect. The correct answer is: " + \
            formatted_correct_words

    print(f'formated words {formatted_words}')
    print(f'formated correct words {formatted_correct_words}')
    return render_template('result.html', number=number, words=words, result=result)


def generate_random_number():
    return random.randint(1000, 500000000)


if __name__ == '__main__':
    app.run(debug=True)
