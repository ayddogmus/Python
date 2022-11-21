from cgi import print_form


website = "https://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karekter dizisinde kaç karakter bulunmaktadır ?

result = len(course)
lenght = len(website)
print(result)

# 2- 'website' içinde www karakterlerini alın.

result = website[8:11]
print(result)

# 3- 'website' içinde com karakterlerini alın.

result = website[23:27]
lenght = website[lenght-3:lenght]
print(result)
print(lenght)


# 4- 'coruse' içnden ilk 15 karakterlerini alın.

result = course[0:15]
result = course[-15:-1]
print(result)
print(result)
# 5- 'course' ifadesindeki karakterleri tersten yazdırın.

result = course[::-1]
print(result)



name, surname, age, job = 'Bora', 'Yılmaz', 32, 'Mühendis'

# 6- Yukarıda verişen değişkenler ile ekrana aşağıdaki ifadeyi  yazdırın.
#    'Benim adım Bora Yılmaz, yaşım 32 ve mesleğim Mühendis'

result = "Benim adım "+ name+ " " +surname+ ",Yaşım "+ str(age)+ " ve mesleğim "+ job
result = "Benim adım {} {}, Yaşım {} ve mesleğim {}.".format(name,surname,age,job)
result = f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}"
print(result)
print(result)
print(result)

# 7- 'Hello world' ifadedesinki w harfini 'W' ile değiştirin.

s = 'Hello world'
s = s[0:6] + 'W'+ s[7:11]
print(s)

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

x = 'abc' *3
print(x)