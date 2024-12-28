questions=[
    ["Which programming language is used in facebook?","Python","PHP","Javascript","Nepali",2],
    ["Which programming language is used in facebook?","Python","PHP","Javascript","Nepali",2],
    ["Which programming language is used in facebook?","Python","PHP","Javascript","Nepali",2],
    ["Which programming language is used in facebook?","Python","PHP","Javascript","Nepali",2],
    ["Which programming language is used in facebook?","Python","PHP","Javascript","Nepali",2],
    ["Which programming language is used in facebook?","Python","PHP","Javascript","Nepali",2],
    ["Which programming language is used in facebook?","Python","PHP","Javascript","Nepali",2],
    ["Which programming language is used in facebook?","Python","PHP","Javascript","Nepali",2],
    ["Which programming language is used in facebook?","Python","PHP","Javascript","Nepali",2],
    ["Which programming language is used in facebook?","Python","PHP","Javascript","Nepali",2],
    ["Which programming language is used in facebook?","Python","PHP","Javascript","Nepali",2],
]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money=0

for i in range(0,len(questions)):
    question=questions[i]
    print(question[0])
    print(f"a.{question[1]}            b.{question[2]}")
    print(f"b.{question[3]}         d.{question[4]}")
    reply=str(input("Enter your answer(a-d):"))
    if reply=="a":
        reply=1
    elif reply=="b":
        reply=2
    elif reply=="c":
        reply=3
    elif reply=="d":
        reply=4

    if(reply==question[-1]):
        print(f"Correct answer! You have won Rs. {levels[i]}\n\n")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
    else:
        print("Wrong Answer")
        break


print(f"Your takehome money is Rs. {money}")

