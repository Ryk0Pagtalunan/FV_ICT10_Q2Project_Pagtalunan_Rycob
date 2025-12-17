from pyscript import display, document

def calgwa(e):
    fname_check = document.getElementById("fname").value
    lname_check = document.getElementById("lname").value
    fname = fname_check if fname_check != "" else 0
    lname = lname_check if lname_check != "" else 0

    science = float(document.getElementById("sci").value) if document.getElementById("sci").value != "" else 0
    mathematics = float(document.getElementById("math").value) if document.getElementById("math").value != "" else 0
    english = float(document.getElementById("eng").value) if document.getElementById("eng").value != "" else 0
    filipino = float(document.getElementById("fil").value) if document.getElementById("fil").value != "" else 0
    pe = float(document.getElementById("pe").value) if document.getElementById("pe").value != "" else 0
    ict = float(document.getElementById("ICT").value) if document.getElementById("ICT").value != "" else 0
    grades = (science, mathematics, english, filipino, pe, ict)

    total_weighted = (science * 5 + mathematics * 5 + english * 5 + filipino * 3 + ict * 2 + pe * 1)
    total_units = 5 + 5 + 5 + 3 + 2 + 1
    gwa = total_weighted / total_units

    summary = f"""
    Science: {grades[0]:.0f}
    Mathematics: {grades[1]:.0f}
    English: {grades[2]:.0f}
    Filipino: {grades[3]:.0f}
    PE: {grades[4]:.0f}
    ICT: {grades[5]:.0f}
    """

    if fname == 0 or lname == 0:
        display("N/A?", target="student_info", append=False)
    else:
        display(f'Name: {fname} {lname}', target='student_info', append=False)

    if any(x == 0 for x in [science, mathematics, english, filipino, pe, ict]):
        display("Please input missing score/s, Thank you.", target="summary", append=False)
        display("Not enough info T^T", target="GWAoutput", append=False)
    elif any(x >= 101 for x in [science, mathematics, english, filipino, pe, ict]):
        display("Please input valid score/s, Thank you.", target="summary", append=False)
        display("Make sure they're all valid grades of 1-100 T^T", target="GWAoutput", append=False)
    else:
        display(summary, target='summary', append=False)

        display(f'Your general weighted average is {gwa:.2f}', target='GWAoutput', append=False)



