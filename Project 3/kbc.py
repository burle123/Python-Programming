questions = [
  [
    "Which company developed the Windows OS?", "Apple", "Microsoft", "Google",
    "IBM", "None", 2
  ],
  [
    "What does CPU stand for?", "Central Processing Unit", "Central Power Unit", "Computer Processing Utility",
    "Control Program Unit", "None", 1
  ],
  [
    "Which is the smallest unit of data in a computer?", "Bit", "Byte", "Nibble",
    "Word", "None", 1
  ],
  [
    "Which programming language is known as the mother of all languages?", "Assembly", "C", "Java",
    "Python", "None", 2
  ],
  [
    "HTML is used for?", "Styling", "Scripting", "Structuring Web Pages",
    "Database", "None", 3
  ],
  [
    "Which one is a frontend framework?", "React", "Django", "Laravel",
    "Spring", "None", 1
  ],
  [
    "In Python, which keyword is used to define a function?", "func", "function", "def",
    "define", "None", 3
  ],
  [
    "Who is known as the father of computers?", "Charles Babbage", "Alan Turing", "Bill Gates",
    "Steve Jobs", "None", 1
  ],
  [
    "Which is the default port of HTTP?", "21", "25", "80",
    "443", "None", 3
  ],
  [
    "Which device is used to connect multiple networks?", "Router", "Switch", "Hub",
    "Bridge", "None", 1
  ],
  [
    "Which company created the Java programming language?", "Google", "Microsoft", "Sun Microsystems",
    "IBM", "None", 3
  ],
  [
    "Which protocol is used to send emails?", "HTTP", "SMTP", "FTP",
    "IMAP", "None", 2
  ],
  [
    "What does AI stand for?", "Automated Input", "Artificial Intelligence", "Applied Interface",
    "Advanced Internet", "None", 2
  ],
  [
    "Which symbol is used to comment a single line in Python?", "#", "//", "/* */",
    "<!-- -->", "None", 1
  ],
  [
    "Which data structure works on FIFO principle?", "Stack", "Queue", "Tree",
    "Graph", "None", 2
  ],
  [
    "Which gas do plants release during photosynthesis?", "Oxygen", "Carbon Dioxide", "Nitrogen",
    "Hydrogen", "None", 1
  ],
  [
    "Which planet is known as the Red Planet?", "Earth", "Venus", "Mars",
    "Jupiter", "None", 3
  ],
  [
    "Who invented the light bulb?", "Nikola Tesla", "Thomas Edison", "Alexander Graham Bell",
    "Isaac Newton", "None", 2
  ],
  [
    "Which currency is used in Japan?", "Yuan", "Dollar", "Yen",
    "Won", "None", 3
  ],
  [
    "Which is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Pacific Ocean",
    "Arctic Ocean", "None", 3
  ],
  [
    "Which element has the chemical symbol 'Au'?", "Silver", "Gold", "Copper",
    "Aluminium", "None", 2
  ],
  [
    "Who was the first person to travel in space?", "Neil Armstrong", "Yuri Gagarin", "Buzz Aldrin",
    "Valentina Tereshkova", "None", 2
  ],
  [
    "Which Indian mathematician invented the concept of zero?", "Aryabhata", "Brahmagupta", "Bhaskara",
    "Ramanujan", "None", 2
  ],
  [
    "Which planet has the fastest rotation in the Solar System?", "Mars", "Jupiter", "Saturn",
    "Neptune", "None", 2
  ],
  [
    "Which Mughal emperor built the Taj Mahal?", "Akbar", "Jahangir", "Shah Jahan",
    "Aurangzeb", "None", 3
  ]
]


levels=[1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 20000000, 40000000, 80000000, 160000000, 320000000, 640000000, 1250000000, 2500000000, 5000000000, 10000000000]

money = 0

for i in range(0,len(questions)):
    question=questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(question[0])
    print(f"a. {question[1]}                   b.{question[2]}")
    print(f"c. {question[3]}                   d.{question[4]}")
    answer = int (input("Enter you answer (1-4) or 0 to Quit : "))
    if answer == 0:
        print(f"You have won Rs. {money}")
        break
    elif answer == question[-1]:
        print(f"Correct answer! You have won Rs. {levels[i]}")
        if i in [4,9,14,19]:
            money = levels[i]
            print(f"Congratulations! You have reached a safe level and will leave with Rs. {money}")
    else:
        print(f"Wrong answer! The correct answer is option {question[-1]}")
        print(f"You have won Rs. {money}")
        break
    print("\n")        
