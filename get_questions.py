import pandas as pd
import random as rd


def get_questions(category, length="max"):

    cat = category.lower().replace(" ", "_")

    try:
        questions = pd.read_csv(f'categories/{cat}.csv')
    except FileNotFoundError:
        print(f"Could not find '{category}' check search and try again.")

    max_num = len(questions.index)
    question = []

    for i in range(max_num):
        question.append([i, questions.iloc[i][1], questions.iloc[i][2]])

    return question


if __name__ == "__main__":
    print(get_questions("Machine Learning"))