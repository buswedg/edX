num = 10
for num in range(5):
    print num
print num
# 0, 1, 2, 3, 4, 4


divisor = 2
for num in range(0, 10, 2):
    print num/divisor
# 0, 1, 2, 3, 4


for variable in range(20):
    if variable % 4 == 0:
        print variable
    if variable % 16 == 0:
        print 'Foo!'
# 0, 'Foo!', 4, 8, 12, 16, 'Foo!'


for letter in 'hola':
    print letter
# 'h', 'o', 'l', 'a'


count = 0
for letter in 'Snow!':
    print 'Letter # ' + str(count) + ' is ' + str(letter)
    count += 1
    break
print count
# 'Letter # 0 is S', 1