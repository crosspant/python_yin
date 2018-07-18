# coding = utf-8

from datetime import datetime
import openpyxl
import re

book = openpyxl.load_workbook('export.xlsx')

active_sheet = book.active
for column in active_sheet.rows:
    kaisiji = column[12].value
    if type(kaisiji) == datetime:
        print(kaisiji.year,end="/")
        print(kaisiji.month,end="/")
        print(kaisiji.day, end="\n")



for column in active_sheet.rows:
    title = column[6].value
    #y = x.value)
    ticket = re.findall("[0-9]{8}-[0-9]{3}-[0-9]{4}", title)
    for tn in ticket:
        print(tn)


for column in active_sheet.rows:
    y = column[18].value
    singokusya = re.findall("[・].+[：||:]", y)
    if singokusya:
        #print(singokusya[1])
        try:
            #catv = re.findall('\w', singokusya[1])
            catv = re.findall('\w', singokusya[1])
            for reg in catv:
                print(reg, end='')
            print()
        except IndexError:
            print()

for column in active_sheet.rows:
    title = column[6].value
    #pattern = re.compile("そ.+]")
    pattern = re.compile("\s\w.+")
    content = pattern.findall(title)
    #contents = re.findall('\w', content)
    #print(content)

    #print(title)
    if title != u"題名":
    #        pass
        for regs in content:
            print(regs, end='')
        #print()
        print()

for column in active_sheet.rows:
    status = column[4].value
    if status != "ステータス":
        print(status)

for column in active_sheet.rows:
    man_hour = column[15].value
    if man_hour != "作業時間の記録":
        print(man_hour)

for column in active_sheet.rows:
    end_date = column[13].value
    if type(end_date) == datetime:
        print(end_date.year,end="/")
        print(end_date.month,end="/")
        print(end_date.day, end="\n")

