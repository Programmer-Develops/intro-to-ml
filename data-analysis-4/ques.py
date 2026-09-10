from qa import Quest

questions = [
    "National bird of India\n(a)Peacock\n(b)Hen\n(c)Crow\n(d)Pigeon",
    "Largest Continent\n(a)Australia\n(b)North America\n(c)China\n(d)Middle East",
    "Capital of France\n(a)London\n(b)Berlin\n(c)Paris\n(d)Madrid",
    "Largest Ocean\n(a)Atlantic\n(b)Indian\n(c)Arctic\n(d)Pacific",
    "Highest Mountain\n(a)K2\n(b)Kangchenjunga\n(c)Mount Everest\n(d)Lhotse"
]

# for i in questions:
#     print(i)

allques = [Quest(questions[0], "a"), Quest(questions[1], "c"), Quest(questions[2], "c"), Quest(questions[3], "d"), Quest(questions[4], "c")]

score = 0

for i in allques:
    answer = input(i.q)
    if answer == i.a:
        score += 1
        print("Correct Answer")
    else:
        print("Incorrect Answer")

print("Your score is: ", score)