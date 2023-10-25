# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
file = pandas.read_csv("nato_phonetic_alphabet.csv")

dic = {row.letter: row.code for (index, row) in file.iterrows()}

#print(dic)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

program_on = True
while program_on:
    user_ask = input("Enter word: ").upper()
    if user_ask == "EXIT PROGRAM":
        program_on = False
    else:
        try:
            list2 = [dic[letter] for letter in user_ask]
            print(list2)
        except KeyError:
            print("Insert only letter please")



