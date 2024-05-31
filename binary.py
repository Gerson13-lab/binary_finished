from flask import Flask, render_template, request

app = Flask(__name__)

# Your original function
def dec_to_binary(num):
    if num < 1:
        return ''
    if num % 2 == 0:
        return '0' + dec_to_binary(num // 2)
    else:
        return '1' + dec_to_binary(num // 2)

# Flask route to handle the form submission
@app.route('/', methods=['GET', 'POST'])
def index():
    binary_result = ""
    user_num = ""
    if request.method == 'POST':
        try:
            user_num = int(request.form['decimal_number'])
            binary_result = dec_to_binary(user_num)[::-1]  # Reverse the string to get the correct binary representation
        except ValueError:
            binary_result = "Please enter a valid integer."
    return render_template('index.html', binary_result=binary_result, user_num=user_num)

if __name__ == '__main__':
    app.run(debug=True)
