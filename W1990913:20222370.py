# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: W1990913/20222370
# Date: 20.04.2023


marks = [0, 20, 40, 60, 80, 100, 120]
progress = 0
trailer = 0
retriever = 0
excluded = 0

data_list = []
id_list = []

all_data = {}


def credit_score(message):
    while True:
        try:
            input_mark = int(input(message))
            if input_mark not in marks:
                print("Out of range.")
                continue
            else:
                return input_mark

        except ValueError:
            print("Integer required.")
            continue


while True:
    while True:
        student_id = input("Enter UOW number: ").lower()
        if len(student_id) != 8 or student_id[0] != "w" :
            print("Invalid ID")
            continue
        elif student_id in id_list:
            print("You have entered the same ID before")    
            continue
        else:
            break
        
    id_list.append(student_id)
    
    while True:
        pass_mark = credit_score("Please enter your credits at pass: ")
        defer_mark = credit_score("Please enter your credit at defer: ")
        fail_mark = credit_score("Please enter your credit at fail: ")

        total = pass_mark + defer_mark + fail_mark

        if total != 120:
            print("Total incorrect.")
            continue

        elif pass_mark == 120:
            progress += 1
            outcome = "Progress"

        elif pass_mark == 100:
            trailer += 1
            outcome = "Progress (module trailer)"

        elif fail_mark >= 80:
            excluded += 1
            outcome = "Exclude"

        else:
            retriever += 1
            outcome = "Do not progress - module retriever"
            
        print(outcome)

        data_list.append([outcome, "-", pass_mark, defer_mark, fail_mark])
        break

  
    all_data[student_id] = {
        "outcome": outcome,
        "pass": pass_mark,
        "defer": defer_mark,
        "fail": fail_mark
    }

    print()

    while True:
        print("Would you like to enter another set of data?")
        continue_quit = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
        print()
        if continue_quit == "y":
            break
        elif continue_quit == "q":
            break
        else:
            print("Invalid input")
            continue
    if continue_quit == "y":
        continue
    elif continue_quit == "q":
        break


print("-" * 65)
print("Histogram\n")
print("Progress", progress, ": ", progress * "*")
print("Trailer", trailer, ": ", trailer * "*")
print("Retriever", retriever, ": ", retriever * "*")
print("Excluded", excluded, ": ", excluded * "*")
print()
total_o = progress + trailer + retriever + excluded
print(total_o, "outcomes in total")
print("-" * 65)

print()

for results in data_list:
    print(results[0], results[1], results[2], ",", results[3], ",", results[4]) 

file = open("part3_textfile.txt", "w")
file.write("Part 3:\n")
for i in data_list:
    file.write(i[0] + i[1] + str(i[2]) + "," + str(i[3])+ "," + str(i[4]) +"\n")
file.close()


print()

for student_id, value in all_data.items():
    outcome = value["outcome"] 
    pass_mark = value["pass"]
    defer_mark = value["defer"]
    fail_mark = value["fail"]
    print(student_id, ":", outcome, "-", pass_mark, ",", defer_mark, ",", fail_mark)
    

#Reference list
#https://www.w3schools.com/python/gloss_python_loop_dictionary_items.asp
#https://tutorial.eyehunts.com/python/nested-dictionary-python-user-input-example-code/

