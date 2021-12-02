from flask import Flask  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!: under construction go to "/dojo"'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    return ('Hi ' + str(name) + "!")

@app.route('/repeat/<num>/<word>')
def repeat(num,word):
    return (str(word) * int(num))

@app.route('/<yea>')
def route(yea):
    if yea != 'say' or yea != 'repeat':
        return 'Sorry! No response. Try again.'
if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
