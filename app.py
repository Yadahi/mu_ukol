from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

'''jednoducha funkcia, ktorá zmení čísla na textovú reprezentáciu'''
def alphabet_position(text, number):
    dictt = {'0': 'nula', '1': 'jeden', '2': 'dva', '3': 'tri', '4': 'štyri', '5': 'päť', '6': 'šest', '7': 'sedem',
             '8': 'osem', '9': 'deväť'
             }
    x = 0
    new_string = ''
    for letter in text:
        if letter in dictt and (x < int(number)):
            x += 1
            new_string += dictt[letter]
        else:
            new_string += letter
    return new_string

@app.route('/')
def show_home():
    return render_template('form.html', result='unknown yet')

@app.route('/calculate_result')
def calculate_result():
    a = str(request.args.get('val1'))
    b = int(request.args.get('val2'))

    string = alphabet_position(a, b)
    return jsonify({'result':string})

if __name__ == '__main__':
    app.run(debug=True)