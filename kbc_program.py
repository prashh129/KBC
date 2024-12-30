questions=[
    
  ["What is the capital of Nepal?", "Mount Everest", "KTM Bike Showroom", "Kathmandu", "Facebook Nepal", 3],
  ["What is momo in Nepal?", "National Bird", "Dumpling Dish", "Brand of Motorcycle", "An Expensive Jewelry", 2],
  ["Who is popularly known as 'The Light of Asia'?", "Prithvi Narayan Shah", "Gautam Buddha", "Deepak Bhattarai", "Rajesh Hamal", 2],
  ["What is the primary use of 'Gundruk' in Nepalese households?", "Wallpaper", "Traditional Carpet", "Fermented Vegetable Dish", "Hair Conditioner", 3],
  ["Which festival involves flying kites in Nepal?", "Dashain", "Tihar", "Independence Day", "Budget Announcement Day", 1],
  ["What is the Nepalese currency called?", "Dollar", "Bitcoin", "Rupee", "Dhukuti", 3],
  ["What is a 'Bagh Chal'?", "A Tiger's Movement", "Traditional Board Game", "Local Transportation Service", "A Wrestling Move", 2],
  ["What does the Nepalese flag represent?", "Two Mountains and the Moon", "A Kite Flying Above Everest", "A Pizza Slice and a Triangle Ruler", "The Only Non-Rectangular National Flag", 4],
  ["What is Mount Everest locally called in Nepal?", "Mount Big Boss", "Sagarmatha", "Snowy Peak of Nepal", "Mount Tall Tall", 2],
  ["What is the national animal of Nepal?", "Domestic Cat", "Cow", "Yeti", "Goat Wearing a Tika", 2]


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

