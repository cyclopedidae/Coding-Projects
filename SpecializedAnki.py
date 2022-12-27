import random

answer = None
rand = None

words = [       "x-ia",
                "x-in",
                "x-ogenesis",
                "x-ostenosis",
                "x-optosis",
                "x-ostomy",
                "x-opexy [diagnostic]",
                "x-opexy [therapeutic]",
                "x-olysis [diagnostic]",
                "x-olysis [therapeutic]",
                "x-oclast", 
                "x-ostat",
                "x-ogen",
                "x-ogenic",
                "x-ogenous"]

definitions = [ "an abnormal condition involving x",
                "a substance of x", 
                "the production of x",
                "the narrowing of x",
                "the downward displacement of x",
                "the making of an opening in x",
                "the adhesion of x"
                "the fixation of x"
                "the disintegration of x"
                "the separation of the adhesions of x"
                "something which breaks x"
                "something which stops x"
                "a substance which produces x"
                "producing x"
                "produced by x"]

def question():
    global answer
    global rand

    rand = random.randint(0,14)

    print("What is the definition of " + words[rand] + "?")
    answer = input()

    check_answer()

def check_answer():
    global answer
    global rand

    correct = False

    while(not correct):
        if(answer == definitions[rand]):
            print("Correct!")
            correct = True

            question()

        else:
            print("Try again.")
            answer = input()

question()