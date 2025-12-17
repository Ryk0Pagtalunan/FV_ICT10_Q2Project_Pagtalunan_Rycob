from pyscript import display, document

def club_info_show(e):
    club_selected = int(document.getElementById("clubselect").value)
    Clubs_Advisors = {"Marching Band Club": "Mr. Emilio Alumno", 
                      "Glee Club": "Mr. Denver Martin", 
                      "Dance Club": "Mr. Alfred Cases", 
                      "Math Club": "Mr. Nicole Gabuya", 
                      "Science Club": "Ms. Jameelyn Maramag", 
                      "Social Science Club": "Mr. Roberto Lim"}
    
    Clubs_Meeting_Time = {"Marching Band Club": "Tuesday and Wednesday 03:00-4:30 PM", 
                          "Glee Club": "Monday 03:00- 05:00 PM", 
                          "Dance Club": "Tuesday 03:00 - 05:00 PM", 
                          "Math Club": "Monday 02:30- 03:00 PM", 
                          "Science Club": "Tuesday  03:00 - 04:00 PM", 
                          "Social Science Club": "Tuesday 03:00 - 4:00 PM"}
    
    Clubs_Location = {"Marching Band Club": "Band Room", 
                      "Glee Club": "High School Music Room", 
                      "Dance Club": "Teatro Preciosa", 
                      "Math Club": "Room 404", 
                      "Science Club": "Room 404", 
                      "Social Science Club": "Room 409"}
    
    Clubs_Description = {"Marching Band Club": "A club for people with interests in music and performances.", 
                         "Glee Club": "A club for people with singing hobbies and school preformances.", 
                         "Dance Club": "A club for people with dance hobbies and school preformances.", 
                         "Math Club": "A club for people who loves math and want to challenge their knowledge.", 
                         "Science Club": "A club for people who love science.", 
                         "Social Science Club": "A club for people who loves discussing philosophy."}
    
    Clubs_Member_Count = {"Marching Band Club": "25", 
                         "Glee Club": "20", 
                         "Dance Club": "34", 
                         "Math Club": "12", 
                         "Science Club": "16", 
                         "Social Science Club": "8"}
    
    if club_selected == 1:
        display(f"""Marching Band Club\n
Advisor: {Clubs_Advisors["Marching Band Club"]}\n
Meeting Time: {Clubs_Meeting_Time["Marching Band Club"]}\n
Location: {Clubs_Location["Marching Band Club"]}\n
Number of Members: {Clubs_Member_Count['Marching Band Club']}\n
Category: Non-Academic\n
Description: {Clubs_Description['Marching Band Club']}""", target="info_output", append=False)

    elif club_selected == 2:
        display(f"""Glee Club\n
Advisor: {Clubs_Advisors["Glee Club"]}\n
Meeting Time: {Clubs_Meeting_Time["Glee Club"]}\n
Location: {Clubs_Location["Glee Club"]}\n
Number of Members: {Clubs_Member_Count['Glee Club']}\n
Category: Non-Academic\n
Description: {Clubs_Description['Glee Club']}""", target="info_output", append=False)
    
    elif club_selected == 3:
        display(f"""Dance Club\n
Advisor: {Clubs_Advisors["Dance Club"]}\n
Meeting Time: {Clubs_Meeting_Time["Dance Club"]}\n
Location: {Clubs_Location["Dance Club"]}\n
Number of Members: {Clubs_Member_Count['Dance Club']}\n
Category: Non-Academic\n
Description: {Clubs_Description['Dance Club']}""", target="info_output", append=False)

    elif club_selected == 4:
        display(f"""Math Club\n
Advisor: {Clubs_Advisors["Math Club"]}\n
Meeting Time: {Clubs_Meeting_Time["Math Club"]}\n
Location: {Clubs_Location["Math Club"]}\n
Number of Members: {Clubs_Member_Count['Math Club']}\n
Category: Academic\n
Description: {Clubs_Description['Math Club']}""", target="info_output", append=False)

    elif club_selected == 5:
        display(f"""Science Club\n
Advisor: {Clubs_Advisors["Science Club"]}\n
Meeting Time: {Clubs_Meeting_Time["Science Club"]}\n
Location: {Clubs_Location["Science Club"]}\n
Number of Members: {Clubs_Member_Count['Science Club']}\n
Category: Academic\n
Description: {Clubs_Description['Science Club']}""", target="info_output", append=False)

    elif club_selected == 6:
        display(f"""Social Science Club\n
Advisor: {Clubs_Advisors["Social Science Club"]}\n
Meeting Time: {Clubs_Meeting_Time["Social Science Club"]}\n
Location: {Clubs_Location["Social Science Club"]}\n
Number of Members: {Clubs_Member_Count['Social Science Club']}\n
Category: Academic\n
Description: {Clubs_Description['Social Science Club']}""", target="info_output", append=False)

    elif club_selected == 0:
        display(f"""Error, Please select a valid club.""", target="info_output", append=False)