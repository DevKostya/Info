import fun

a=input("a=") # задаем коэффициент а
b=input("b=") # задаем коэффициент b
# создаем алфавит
Dictionary = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
try:
    a=int(a)
    b=int(b)
except ValueError:
    print("a and b are not int")
else:
    if (a>0): # проверяем на корректность вводимых значений, а именно чтобы а было больше 0
        if ((fun.NOD(a,len(Dictionary))==1 and b < (len(Dictionary))) or a==1): #  проверяем на корректность вводимых значений,
            fun.rewrite("input", "inputClear")  # убираем из текста все знаки припинания и записываем в inputClear.txt
            fun.encryption("inputClear", "encryption", a, b, Dictionary)  # шифруем
            fun.decryption("encryption", "decryption", a, b, Dictionary)  # дешифруем
            Dict=fun.Dict("Дюймовочка") #составляем словарь из файла Дюймовочка
            fun.Break("encryption","breakdecryprion",Dict,Dictionary) #пытаемся взломать методом перебора
            print("Done")
        else:
            print("Нужно указывать коэффициент а таким, чтобы НОД размера алфавита и коэффициентом был равен 1, так же числа a и b не должны превышать размер алфавита")
    else:
        print("Коэффициент а не может быть равен нулю или меньше, так как не будет обратного числа по модулю m")
end=input()

