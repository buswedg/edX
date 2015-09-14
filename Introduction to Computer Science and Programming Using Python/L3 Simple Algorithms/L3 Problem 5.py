for count in range(11):
    if count != 0 and count % 2 == 0:
        print count
print "Goodbye!"
# 2, 4, 6, 8, 10, 'Goodbye!'


print "Hello!"
for num in range(0, 10, 2):
    print 10 - num
# 'Hello!', 10, 8, 6, 4, 2


end = 10
total = 0
for next in range(1, end+1):
    total += next
print total
# 55