student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

with open("nato_phonetic_alphabet.csv") as data:
    nato_data = data.readlines()
    nato_data = {row[0]:row[1].strip() for row in [line.split(",") for line in nato_data]}
    print(nato_data)

import pandas
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data = {row.letter:row.code for (index, row) in nato_data.iterrows()}
print(nato_data)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
nato_list = [nato_data[letter] for letter in user_input]
print(nato_list)
