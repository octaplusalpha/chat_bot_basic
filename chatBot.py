import datetime
from difflib import get_close_matches
from datetime import datetime


def tell_time():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H:%M")
    if formatted_time < '12':
        return f'{formatted_time}AM'
    else:
        return f'{formatted_time}PM'

def tell_day():
    current_day = datetime.now()
    day = current_day.strftime("%A")
    return day

def get_best_match(user_question: str, questions: dict) -> str|None:
    questions: list[str] = [q for q in questions]
    matches: list[str] = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    if matches:
        return matches[0]

def chat_bot(knowledge: dict):
    conversation = True
    while conversation:
        user_input: str = input('You: ').lower()

        best_match: str|None = get_best_match(user_input, knowledge)
        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:

            if 'bye' in user_input.lower():
                print('Bot: Bye, Have a nice day!')
                conversation = False
            else:
                print('Bot: Please refer to other sources, my knowledge is limited for now.')




if __name__ == '__main__':
    brain: dict = {'hello': 'hi, im Bobbot',
                   'hi': 'Hello I am Bobbot, what can i do for you today?',
                   'what time is it': f'The time is {tell_time()}.',
                   'thank you': 'You are welcome.',
                   'what day is it': f'Today is {tell_day()}'}

    chat_bot(brain)


