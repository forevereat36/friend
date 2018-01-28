
# -*- coding: utf-8 -*-

from collections import Counter


def CalcProbability(array, result):
    resultkey = list(result.keys())[0]
    resultcount = Counter(result[resultkey])

    dict = {}
    count = Counter(array)
    for item in count:
        if item == "yes":
            dict[item] = count[item] / resultcount["yes"]
        elif item == "no":
            dict[item] = count[item] / resultcount["no"]
    return dict

def Statistics(friend, result):
    frienddict = {}
    resultkey = list(result.keys())[0]

    for item in friend:
        for i in range(0, len(friend[item])):
            friendelement = friend[item][i]
            resultelement = result[resultkey][i]
            if friendelement in frienddict:
                frienddict[friendelement].append(resultelement)
            else:
                temparr = []
                temparr.append(resultelement)
                frienddict[friendelement] = temparr

    newfriend = {}
    for key in frienddict:
        newfriend[key] = CalcProbability(frienddict[key], result)

    newresult = {}
    resultkey = list(result.keys())[0]
    for item in result[resultkey]:
        if item in newresult:
            newresult[item] += 1
        else:
            newresult[item] = 1
    newresult["yes"] = newresult["yes"] / len(result[resultkey])
    newresult["no"] = newresult["no"] / len(result[resultkey])
    return newfriend, newresult

def judgeresult(newfriend, newresult, judge):
    yesresult = 1
    noresult = 1
    for item in judge:
        yesresult = yesresult * newfriend[item]["yes"]
        noresult = noresult * newfriend[item]["no"]

    yesresult = yesresult * newresult["yes"]
    noresult = noresult * newresult["no"]

    if yesresult >= noresult:
        print("友達確率：" + str(yesresult) + "，不友達確率：" + str(noresult) + "，友達になる！")
    else:
        print("友達確率：" + str(yesresult) + "，不友達確率：" + str(noresult) + "，友達にならない！")


if __name__ == '__main__':
    friend = {'职业': ['上班', '上班', '学生', '学生', '学生', '上班', '上班', '学生', '学生', '学生', '上班', '上班', '学生', '上班'],
                 '长相': ['正常', '正常', '正常', '正常', '高', '高', '高', '正常', '高', '高', '高', '正常', '高', '正常'],
                 '年龄': ['大', '大', '合适', '小', '小', '小', '合适', '大', '大', '小', '大', '合适', '合适', '小'],
                 '性格': ['热情', '热情', '热情', '善良', '高冷', '高冷', '高冷', '善良', '高冷', '善良', '善良', '善良', '热情', '善良']}
    result = {'女友': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']}
    newfriend, newresult = Statistics(friend, result)
    evidence=[]
    e1=""
    e2=""
    e3=""
    e4=""
    e1=input("请输入年龄条件（大，合适，小）：")
    while e1 not in ["大","合适","小"]:
            e1=input("请输入正确的年龄条件（大，合适，小）：")
    e2=input("请输入性格条件（热情，善良，高冷）：")    
    while e2 not in ["热情","善良","高冷"]:
            e2=input("请输入正确的性格条件（热情，善良，高冷）：")
    e3=input("请输入长相条件（正常，高）：")        
    while e3 not in ["正常","高"]:
            e3=input("请输入正确的长相条件（正常，高）：")
    e4=input("请输入职业条件（学生，上班）：")
    while e4 not in ["学生","上班"]:
            e4=input("请输入正确的职业条件（学生，上班）：")

    evidence.append(e1)
    evidence.append(e2)
    evidence.append(e3)
    evidence.append(e4)
    
    judgeresult(newfriend, newresult, evidence)
    
