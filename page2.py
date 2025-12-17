from pyscript import display, document

def calgwa(e):
    fname = document.getElementById("fname").value if document.getElementById("fname").checked else 0
    lname = document.getElementById("lname").value if document.getElementById("lname").checked else 0

    science = float(document.getElementById("sci").value) if document.getElementById("sci").checked else 0
    mathematics = float(document.getElementById("math").value) if document.getElementById("math").checked else 0
    english = float(document.getElementById("eng").value) if document.getElementById("eng").checked else 0
    filipino = float(document.getElementById("fil").value) if document.getElementById("fil").checked else 0
    pe = float(document.getElementById("pe").value) if document.getElementById("pe").checked else 0
    ict = float(document.getElementById("ICT").value) if document.getElementById("ICT").checked else 0
    List = (science, mathematics, english, filipino, pe, ict)

    sum = (science * 5 + mathematics * 5 + english * 5 + filipino * 3 + ict * 2 + pe * 1)
    totalunits = ((5*3) + 3 + 2 + 1)
    gwa = sum / totalunits

    summary = f"""
    Science: {List[0]:.0f}
    Mathematics: {List[1]:.0f}
    English: {List[2]:.0f}
    Filipino: {List[3]:.0f}
    PE: {List[4]:.0f}
    ICT: {List[5]:.0f}
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

