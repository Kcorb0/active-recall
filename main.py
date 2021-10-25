import pandas as pd
import random as rd
from start_quiz import start_quiz
from add_question import add_question


def run():

    run = True

    while run:

        print("""
                            
                █████╗  ██████╗████████╗██╗██╗   ██╗███████╗    ██████╗ ███████╗ ██████╗ █████╗ ██╗     ██╗     ███████╗██████╗ 
                ██╔══██╗██╔════╝╚══██╔══╝██║██║   ██║██╔════╝    ██╔══██╗██╔════╝██╔════╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗
                ███████║██║        ██║   ██║██║   ██║█████╗      ██████╔╝█████╗  ██║     ███████║██║     ██║     █████╗  ██████╔╝
                ██╔══██║██║        ██║   ██║╚██╗ ██╔╝██╔══╝      ██╔══██╗██╔══╝  ██║     ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗
                ██║  ██║╚██████╗   ██║   ██║ ╚████╔╝ ███████╗    ██║  ██║███████╗╚██████╗██║  ██║███████╗███████╗███████╗██║  ██║
                ╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝  ╚═══╝  ╚══════╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                                                                                                
            """)
        print("Welcome, enter 'q' at any time to quit")
        start_option = input("Enter 'run' for questions or 'add' to create a new question: ")

        if start_option == "q":
            run = False
        elif start_option == "add":
            add_question()
        elif start_option == "run":
            start_quiz()


if __name__ == "__main__":
    run()