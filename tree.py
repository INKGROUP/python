"""
 author:nick
"""
import turtle

def draw_branch(branch_length):
    if branch_length > 5:
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length - 15)

        turtle.left(40)
        draw_branch(branch_length - 15)

        turtle.right(20)
        turtle.backward(branch_length)

def main():
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    draw_branch(100)
    turtle.exitonclick()
if __name__ == "__main__" :
    main()