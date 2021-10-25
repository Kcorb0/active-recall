import pandas as pd
import random as rd


def start_quiz():

    state = True
    get_cat = input("What category would you like? ").lower().replace(" ", "_")
    category = pd.read_csv(f'categories/{get_cat}.csv')

    while state:

        q_num = rd.randint(0, len(category.index)-1)
        question = category.iloc[q_num][1]
        answer = category.iloc[q_num][2]
        
        print('\n' + question)

        if ":" in answer:

            ans_list = answer.split(":")
            cnt = 0

            while cnt < len(ans_list):
                user_answer = input(f"\nAnswer ({int(cnt+1)}/{int(len(ans_list))}): ")
                print(" - " + user_answer)
                cnt += 1
            
            print("\nActual Answer: ")
            
            for ans in ans_list:
                print("\n - " + ans)

        else:
            user_answer = input("\nAnswer: ")
            print(f'\nUser answer: {user_answer}')
            print(f'Actual answer: {answer}\n')