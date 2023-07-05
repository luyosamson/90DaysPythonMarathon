years=(2007,2006,2005,2013,2020,2030)
for i in years:
    print(i)

years=[2001,2002,2003,2004,2005,2007]

for i in range(len(years)):
   print(years[i])

for i in range(2,12):
    print(i)

lang=["Python","PHP","Java","Js","Ruby"]
for i,languages in enumerate(lang,start=1):
    print(f'{i}:{languages}')
