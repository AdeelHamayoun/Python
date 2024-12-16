inputlist = list()
questionslist = list()

inputlist = input("Please enter list of strings: ")

for question in inputlist:
    print(question)
    if question != '"' | question != ' ':
        questionslist.append(question)
    questionslist.find(",")

print(questionslist)




"32 + 698", "3801 - 2", "45 + 43", "123 + 49"





# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]):
