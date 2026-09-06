student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#looping through dictionaries
for (key , value) in student_dict.items():
    print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#looping through data frame
for (index, row) in student_data_frame.iterrows():
    print(value)