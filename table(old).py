#!/usr/bin/python
print 'Content-type: text/html\n'

f = open('statab2008_0301_CrimeRatesByState2004And2005AndByTy_0_Data.csv', 'r')
s = f.readlines()
f.close

i = 0
while i < len(s):
    s[i]=s[i].split(',')
    i+=1

t=[]
t.append(s[40])
t.append(s[11])

html = '<html><head><title>Crime Rates</title></head><body><h2>Jason Lu, Period 10</h2>'
html+= '<center><h1>Crime Rates By State</h1></center>'
html+= '<h1>WHY?</h1> Crime has always been a major problem in the Uniteds States. '
html+= 'There were about 11 million crimes reported in the US in 2005 alone. I will compare the crime rates of New York State and California.<br>'
html+= 'Note: This data shows crime rate, not the number of crimes commited. <hr><h1>The Data</h1>'
###MainTable###
html+= '<table border="3"><tr>'
for x in s[0]:
    html += '<th colspan="11">' + str(x) + '</th>'
html+= '</tr>\n'

for a in s[1:-7]:
    html+= '<tr>'
    for x in a[0:1]+ a[4:9] + a[10:]:
        html+= '<td>' + str(x) + '</td>'
    html+= '</tr>\n'
for a in s[-7:]:
    html+= '<tr>'
    for x in a[0:1]+ a[4:]:
        html+= '<th colspan="11">' + str(x) + '</th>'
    html+= '</tr>\n'
html+= '</table><hr>'
###Analysis Table###
html+= '<h1>Analysis</h1>Looking at the data, we can compare the crime rates of New York to the crime rates of California. <table border="3">'
for x in s[2:4]:
    html+='<tr>'
    for a in x[0:1]+ x[4:9] + x[10:]:
        html+= '<th>' + a + '</th>'
    html+='</tr>'
for b in t:
    html+='<tr>'
    for f in b[0:1]+ b[4:9] + b[10:]:
        html+='<td>' + f + '</td>'
    html+= '</tr>'
html+='</table>'
html+='Based on the table, we can see that in 2005, New York had a lower crime rate than California in all categories except for Violent Robbery.'
###Conclusion###
html+='<hr><h1>The Conclusion</h1>According to the data provided above, New York State was just a little above averge in terms of crime rates across the country. '
html+='When comparing New York and California, the total rate of violent crimes in California was almost 25% greater than that of New York. '
html+='The rate of property crimes in California was more than 50% greater than that of New York.'

html+='<hr><h1>Sources</h1>All data is from:<a href="http://www.infochimps.com/datasets">www.infochimps.com/datasets</a><br>'
html+='Specifically from <a href="http://www.infochimps.com/datasets/crime-rates-by-state-2004-and-2005-and-by-type-2005-cleaned-up-v">www.infochimps.com/datasets/crime-rates</a>'
html+='</body></html>'
print html



