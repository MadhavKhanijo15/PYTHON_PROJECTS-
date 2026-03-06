#Who wants to be a millionaire
while True:
    print("Welcome to Who Wants to be a Millionaire ")
    print("If you want to play , enter 'Play' ")
#Intro
    ask1=str(input("Enter - "))
    if ask1=="Play":
        print("Lets Play !! Before we start enter your name")
        name=str(input("Name - "))
        print("Lets play Who wants to be a Millionaire with" , name)
        #Rules
        print("Before I ask you the first question . Let me tell you the rules\nSo rules are as follows - You will be asked three questions , so the question-prize structure is as follows-\nQuestion 1: $5000\nQuestion 2: $50000\nQuestion 3: $5 Million\nIf the answer is right you will get the prize money otherwise you lose. ")
        #Questions
        print("Since now you know the rules\nFirst Question is - Q.1 Whats the capital of India?")
        print("Your options are\nOption A-Lucknow , Option B-Hyderabad , Option C-New Delhi , Option D- Kolkata")
        Answer1=str(input("Answer-"))
        if Answer1=="C" or Answer1=="New Delhi":
            print("Right Anwer!!! You Win $5000")
            print("Second Question is - Q.2 Who amongst the following is the CEO of Microsoft?")
            print("Your options are\nOption A-Sundar Pichai , Option B- Mark Zuckerberg , Option C-Bill Gates , Option D-Satya Nadella")
            Answer2=str(input("Answer - "))
            if Answer2=="D" or Answer2=="Satya Nadella":
                print("Right Answer!!! You win $50000")
                print("Third Question is - Q.3 Which AI Research company owns ChatGPT?")
                print("Your options are\nOption A- OpenAI , Option B- Anthropic , Option C-Google , Option D- Meta")
                Answer3=str(input("Answer - "))
                if Answer3 in ("A","OpenAI"):
                    print("Right Answer!!! You Win $5 Million")
                else:
                    print("Wrong Answer , You win $50000 only.")
            else:
                print("Wrong Answer , You win $5000 only.")
        else:
            print("Wrong Answer , You win $0.")
