import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from starting_massage import StartingMassage
from second_level import second_level
import pandas


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My snake game")


    message = StartingMassage()
    screen.tracer(0)

    snake = Snake()
    food = Food()
    boardgame = Scoreboard()

    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)

    speed = 0.1
    can_level_up = True
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(speed)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food.xcor(), food.ycor()) < 16:
            food.refresh()
            snake.grow()
            boardgame.increase_score()
            can_level_up = True

        # Detect collision with wall
        if snake.head.xcor() > 285 or snake.head.xcor() < -285 or\
                snake.head.ycor() > 285 or snake.head.ycor() < -285:
            game_is_on = False

        # Detect collision with tail
        for seg in snake.segments[1:]:
            if snake.head.distance(seg) < 10:
                game_is_on = False

        if boardgame.score % 3 == 0 and boardgame.score != 0 and can_level_up:
            speed = speed - 0.01
            can_level_up = False

        # need to create a second level
        if boardgame.score == 10:
            second_level()

    # highest_score_list_txt = check_highest_score(boardgame)
    changed_index = check_highest_score(boardgame)
    game_over(screen, boardgame, food, changed_index)

    boardgame.clear()
    screen.clear()

    screen.tracer(0)
    screen.listen()
    screen.onkey(key="a", fun=main)
    screen.bgcolor("black")
    screen.update()

    screen.exitonclick()


def game_over(screen, boardgame, food, changed_index):
    boardgame.clear()
    food.hideturtle()
    lose_massage = Turtle()
    lose_massage.penup()
    lose_massage.hideturtle()
    lose_massage.color("white")
    lose_massage.goto(0, 200)
    lose_massage.write(f"The game ended\n your score is: {boardgame.score} ",
                       True, align="center", font=("Ariel", 20, "normal"))

    # update the record's breaker name
    if changed_index >= 0:
        name = screen.textinput(title="New record", prompt="Enter your name")
        data = pandas.read_csv("best_scores.csv")
        data.loc[changed_index, 'name'] = name
        data.to_csv("best_scores.csv", index=False)

    data = pandas.read_csv("best_scores.csv")

    lose_massage.goto(0, -100)
    lose_massage.write(data, True, align="center", font=("Ariel", 20, "normal"))
    screen.update()
    time.sleep(7)
    lose_massage.goto(0, -250)
    lose_massage.write(f" Press 'a' to run again ",
                       True, align="center", font=("Ariel", 24, "normal"))
    screen.update()
    time.sleep(3)

    screen.update()


def check_highest_score(board_game):
    data = pandas.read_csv("best_scores.csv")
    score_list = data["score"].to_list()
    names_list = data["name"].to_list()

    found_changes = False
    change_index = -1
    for num in range(3):
        if found_changes:
            break
        if board_game.score > score_list[0] and num == 0:

            data.loc[0, 'score'] = board_game.score

            data.loc[1, 'score'] = score_list[0]
            data.loc[1, 'name'] = names_list[0]

            data.loc[2, 'score'] = score_list[1]
            data.loc[2, 'name'] = names_list[1]
            change_index = 0
            found_changes = True
        elif board_game.score > score_list[1] and num == 1:

            data.loc[1, 'score'] = board_game.score

            data.loc[2, 'score'] = score_list[1]
            data.loc[2, 'name'] = names_list[1]
            change_index = 1
            found_changes = True
        elif board_game.score > score_list[2] and num == 2:
            data.loc[2, 'score'] = board_game.score
            change_index = 2
            found_changes = True

    data.to_csv("best_scores.csv", index=False)

    return change_index


main()