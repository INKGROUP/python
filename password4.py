"""
 author:nick
"""





def main():
    f = open('password3.0.txt', 'r')
    # content = f.read()
    # f.close()
    # print(content)

    # line = f.readline()
    # print(line)
    # f.close()

    lines = f.readlines()
    for line in lines:
        print(line)

    f.close()



if __name__ == "__main__":
    main()