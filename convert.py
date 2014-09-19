f = open('Data.csv', 'r')
s = f.readlines()
f.close

i = 0
html=''
while i < len(s):
    s[i]=s[i].split(',')
    i+=1
for x in s[0]:
    html += str(x) + ','
html += '\n'

for a in s[1:-7]:
    for x in a[0:1]+ a[4:9] + a[10:]:
        html+= str(x)+','
    html+= '\n'
for a in s[-7:]:
    for x in a[0:1]+ a[4:]:
        html+= str(x)+','
    html+= '\n'
f = open('Data.txt', 'w')
f.write(html)
f.close()
