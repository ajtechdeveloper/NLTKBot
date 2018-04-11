from __future__ import print_function
from nltk.chat.util import Chat, reflections

pairs = (
    (r'quit',
     ( "Thank you. It was good talking to you.",
       "Good-bye.")),

    (r'Who are you(.*)',
     ( "My name is Alpha.",
       "I'm Alpha.")),

    (r'What is your name(.*)',
     ( "My name is Alpha.",
       "I'm Alpha.")),

    (r'What do you do(.*)',
     ( "I speak my mind out.",
       "I chat.",
       "I like making friends.")),

    (r'Then(.*)',
     ( "Nothing special. You tell me.",
       "What else?",
       "Nothing from me. What about you?")),

    (r'How are you(.*)',
     ( "I am fine. Thank You. How are you?",
       "I am fine. How about you?",
       "Fine. Thank You. How about you?")),

    (r'Hi(.*)',
     ( "Hi!!! What is your name?",
       "Hello.",
       "Hi. Great to meet you.")),

    (r'My name is (.*)',
     ( "Hi %1!!!",
       "Hello %1.",
       "Hi %1. Great to meet you.")),

    (r'You tell me(.*)',
     ( "What?",
       "Tell me about yourself.",
       "WHat do you do?")),

    (r'What else(.*)',
     ( "Nothing special. You tell me.",
       "Nothing from me. What about you?")),

    (r'I need (.*)',
     ( "Why do you need %1?",
       "Why?",
       "Are you sure?")),

    (r'How (.*)',
     ( "I am not aure.",
       "I'm not sure. What do you think?",
       "Sorry, I don't know.")),

    (r'Hello(.*)',
     ( "Hi... How are you today?",
       "Hello, How are you?")),

    (r'Yes',
     ( "You seem certain.",
       "Alright")),

    (r'My (.*)',
     ( "I see, your %1.",
       "Oh ok.")),

    (r'(.*)\?',
     ( "Why do you ask that?",
       "I am not sure.",
       "I do not know the answer to your question")),

    (r'(.*)',
     ( "Alright.",
       "I see.",
       "Very interesting."))
)

friend_chatbot = Chat(pairs, reflections)

def friend_chat():
    print("Friend\n---------")
    print("You can talk to me by typing in English.")
    print('Enter "quit" to Quit.')
    print('='*72)
    print("Hello. My name is Alpha. Tell me something about yourself..")

    friend_chatbot.converse()

def demo():
    friend_chat()

if __name__ == "__main__":
    demo()