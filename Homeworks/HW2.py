

people_cv={1:{"Name":"Lea","Surname":"Williams","Education":"MIT","GPA":"3.50"},
2:{"Name":"Lisa","Surname":"Earnhart","Education":"Harvard University","GPA":"3.63"},
3:{"Name":"Claire","Surname":"Badeaux","Education":"University Of Paris","GPA":"3.80"},
4:{"Name":"Harper","Surname":"Eaton","Education":"NYU","GPA":"3.44"},
5:{"Name":"Ella","Surname":"Cai","Education":"UCLA","GPA":"3.65"}}
for a_id, a_info in people_cv.items():
    print("\nApplicant ID:", a_id)

    for key in a_info:
        print(key + ':', a_info[key])