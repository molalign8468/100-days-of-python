import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image) 

data = pandas.read_csv("50_states.csv")
all_states = data["state"].tolist() 


guessed_states = [] 

while len(guessed_states) < 50:
    
    user_answer = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    )

   
    if user_answer is None: 
        break
    user_answer_formatted = user_answer.title()

    if user_answer_formatted == "Exit":
        break

    if user_answer_formatted in all_states:
        if user_answer_formatted not in guessed_states:
            guessed_states.append(user_answer_formatted)

            guessed_state_row = data[data["state"] == user_answer_formatted]

            x_coord = guessed_state_row.x.item()
            y_coord = guessed_state_row.y.item()
            guessed_state_coordinate = (x_coord, y_coord)

            pen = turtle.Turtle()
            pen.speed(0)        
            pen.penup()         
            pen.hideturtle()   
            pen.goto(guessed_state_coordinate)
            pen.write(user_answer_formatted, align="center", font=("Arial", 9, "normal"))
    else:
        print("Incorrect state name, try again!")



missed_states = [state for state in all_states if state not in guessed_states]

if len(guessed_states) == 50:
    print("\nCongratulations! You've guessed all 50 states!")
elif user_answer_formatted == "Exit":
    print("\nGame ended. Here are the states you missed:")
    missed_states_df = pandas.DataFrame(missed_states, columns=["State"])
    missed_states_df.to_csv("states_to_learn.csv", index=False)
    print("Missed states saved to 'states_to_learn.csv'.")
    print(missed_states) 
else:
    print("\nGame over! Here are the states you missed:")
    missed_states_df = pandas.DataFrame(missed_states, columns=["State"])
    missed_states_df.to_csv("states_to_learn.csv", index=False)
    print("Missed states saved to 'states_to_learn.csv'.")
    print(missed_states) 


screen.exitonclick()
