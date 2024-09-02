from flask import Flask, render_template, request, session, flash
import secrets

app = Flask(__name__)
app.secret_key = '33e39e0900b163192212aeec94c05b04' 

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        total_questions = 2  
        answers = {f'question{i}': request.form.get(f'question{i}') for i in range(1, total_questions + 1)}

        if any(answer is None for answer in answers.values()):
            flash('Eksik sorular var, lütfen tüm soruları cevaplayın.')
            return render_template('nlp-quiz.html')

        score = calculate_score(answers)
        session['best_score'] = max(score, session.get('best_score', 0))
        return render_template('result.html', score=score)

    return render_template('nlp-quiz.html')

def calculate_score(answers):
    score = 0
    if answers.get('question1') == 'Doğal Dil İşleme':
        score += 1
    if answers.get('question2') == 'NLTK':
        score += 1
    return score * 50

if __name__ == '__main__':
    app.run(debug=True)
