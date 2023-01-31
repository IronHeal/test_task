from article2title import *

def main(): # pragma: no cover
    print("1 3 5 7 9 1 3 5 7 9 1 3 5")
    print(article2title("test 1 2 3"))
    print(article2title("test  one two tree 4 five six seven"))
    print(article2title("Volvo released a new car with the following spec: V6 236HP. It will cost $22647 and going to be sold in New York only"))

if __name__ == "__main__": # pragma: no cover
    main()
