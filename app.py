from flask import Flask, render_template, request

app = Flask(__name__)

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        if not char.isalpha():
            final_message += char
        else:        
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        custom_key = request.form['key']
        direction = request.form['direction']

        if direction == 'encrypt':
            result = encrypt(text, custom_key)
        else:
            result = decrypt(text, custom_key)

        return render_template('index.html', result=result, text=text, custom_key=custom_key, direction=direction)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
