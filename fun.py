# -*- coding: utf-8 -*-
import re

# функция возвращающая наибольший общий делитель
def NOD(a,b):
    while (a != 0 and b != 0):
        if (a > b):
            a = a % b
        else:
            b = b % a
    return a+b

# функция, которая из файла filePath убирает все знаки припинания и приводит все буквы в нижний регистр, записывает в файл filePath1
def rewrite(filePath,filePath1):
    arrayLine = []
    with open(filePath, "r") as file_handler:
        for line in file_handler:
            line = line.lower()
            line = re.sub(r'[,.!?:;–«»—]', '', line)
            arrayLine.append(line)
    with open(filePath1, "w") as file_handler:
        for line in arrayLine:
            file_handler.write(line)

#шифруем все буквы из файла filePath и записываем в filePath1
def encryption(filePath,filePath1,a,b,Dictionary):
    arrayLine = []
    with open(filePath, "r") as file_handler:
        for line in file_handler:
            finishLine=""
            for char in line:
                try:
                    Dictionary.index(char)
                except ValueError:
                    finishLine = finishLine + char
                else:
                    x=Dictionary.index(char)
                    axb=x*a+b
                    length=len(Dictionary)
                    finishLine=finishLine+Dictionary[axb%length]

            arrayLine.append(finishLine)
    with open(filePath1, "w") as file_handler:
        for line in arrayLine:
            file_handler.write(line)

#дешифруем все буквы из файла filePath и записываем в filePath1
def decryption(filePath,filePath1,a,b,Dictionary):
    arrayLine = []
    aReverse=1
    #высчитываем обратный коэффициент
    while ((a*aReverse)%len(Dictionary)!=1):
        aReverse=aReverse+1
    with open(filePath, "r") as file_handler:
        for line in file_handler:
            finishLine=""
            for char in line:
                try:
                    Dictionary.index(char)
                except ValueError:
                    finishLine = finishLine + char
                else:
                    x=Dictionary.index(char)
                    axb=aReverse*(x-b)
                    length=len(Dictionary)
                    finishLine=finishLine+Dictionary[axb%length]
            arrayLine.append(finishLine)
    with open(filePath1, "w") as file_handler:
        for line in arrayLine:
            file_handler.write(line)

#составляем словарь Dict слов из файла filePath
def Dict(filePath):
    Dict=[]
    with open(filePath, "r") as file_handler:
        for line in file_handler:
            matchWords = re.findall(r"\w+",line.lower())
            for word in matchWords:
                try:
                    Dict.index(word)
                except ValueError:
                    Dict.append(word)
    Dict.sort()
    return Dict

#пытаемся взломать файл filePath и, если получается, то записываем в filePath1
def Break(filePath,filePath1,Dict,Dictionary):
    for a in range(1,33):
        for b in range(0,33):
            arrayLine = []
            flag=0
            with open(filePath, "r") as file_handler:
                for line in file_handler:
                    if (flag==1):
                        break
                    finishLine=""
                    for char in line:
                        try:
                            Dictionary.index(char)
                        except ValueError:
                            finishLine = finishLine + char
                        else:
                            x=Dictionary.index(char)
                            axb=a*(x-b)
                            length=len(Dictionary)
                            finishLine=finishLine+Dictionary[axb%length]
                    matchWords = re.findall(r"\w+", finishLine)
                    for word in matchWords:
                        try:
                            Dict.index(word)
                        except ValueError:
                            flag=1
                            break
                    arrayLine.append(finishLine)
            if (flag==0):
                with open(filePath1, "w") as file_handler:
                    for line in arrayLine:
                        file_handler.write(line)