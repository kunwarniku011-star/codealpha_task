print("=======================")
print("WELCOME TO BASIC CHATBOT" )
print("=======================")
print("hello! i am your chatbot")
print("type 'bye' to exit")
while True:
    user_input=input("\nyou:").lower()
    if user_input =="hello":
        print("chatbot: hi there!")
    elif user_input =="how are you?":
        print("chatbot: i am good, thank you!")
    elif user_input =="what is your name?":
        print("chatboot:goodbye!")
        break
    else:
        print("chatbot: i am sorry, i don't understand that.")


