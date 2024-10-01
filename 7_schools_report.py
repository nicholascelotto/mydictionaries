"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $60,000

- Have to be part of conference

- 2 separate for loops
---- 1 for grad rate
---- 1 for total price

"""


import json

infile = open('school_data.json', 'r')

schools = json.load(infile)

conference_schools = [372,108,107,130]

num1 = 0
num2 = 0

for s in schools:
    if type(schools[num1]["Graduation rate  women (DRVGR2020)"]) == int:
        if schools[num1]["Graduation rate  women (DRVGR2020)"] > 75:
            print(f"University: {schools[num1]["instnm"]}")
            print(f"Graduation Rate for Women: {schools[num1]["Graduation rate  women (DRVGR2020)"]}%")
            print('\n')
    num1 += 1



for s in schools:
    if schools[num2]["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] > 60000:
        print(f"University: {schools[num2]["instnm"]}")
        print(f"Total price for in-state students living off campus: ${schools[num2]["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]:,.2f}")
        print('\n')
    num2 += 1


infile.close()
