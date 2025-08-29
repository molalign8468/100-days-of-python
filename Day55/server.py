from flask import Flask
import random

app = Flask(__name__)


rand_num = random.randint(0,9)

print(rand_num)
@app.route("/")
def Home():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        "<img align='middle' width='352' "
        "src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGEzbHZuOW9xdmI4N2hjMXFzNmtoNHJnb3d6eXcyNnNhYXZlbmhycSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUn3CftPBajoflzROU/giphy.gif' "
        "height='324'>"
    )

@app.route("/<int:num>")
def gusse(num):
    if num ==rand_num:
        return ( "<h1 style='color:green'>You found me!</h1>"
        "<img align='middle' width='352' "
        "src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' "
        "height='324'>")
    elif num > rand_num:
        return ( "<h1 style='color:purple'>Too high,try again!</h1>"
        "<img align='middle' width='352' "
        "src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' "
        "height='324'>")
    else:
        return ( "<h1 style='color:red'>Too low,try again!</h1>"
        "<img align='middle' width='352' "
        "src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' "
        "height='324'>")

        

if __name__ == "__main__":
    app.run(debug=True)
