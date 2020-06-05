""""
    author:yintengfei
"""
import turtle
def painter(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count = count + 1

def main():
    size = 50
    while size <= 300:
        turtle.pencolor('blue')
        painter(size)
        size += 30
        turtle.right(60)


    turtle.exitonclick()
if __name__ == "__main__":
    main()