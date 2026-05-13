def transform(num):
    air_level = {'优': (0,50),'良': (51,100),'轻度污染':(101,150),
                 '中度污染':(151,200),'重度污染':(201,300),'严重污染':(301,500)}
    for k in air_level:
        if num>=air_level[k][0]  and (num<=air_level[k][1]):
            return k

records={'2023-06-01':[49,21],
         '2023-06-02':[140,32],
         '2023-06-03':[81,28],
         '2023-06-04':[67,19],
         '2023-06-05':[47,27],
         '2023-06-06':[65,29]}
good=0
print('日期\t\tAQI\tPM2.5\t空气质量')
for date in records:
    AQI=records[date][0]
    records[date].append(transform(int(AQI)))
    if records[date][2] == '优': 
        good=good+1
    print('{}\t{}\t{}\t{}'.format(date,records[date][0],records[date][1],records[date][2]))
print('空气质量为优的天数有{}天'.format(good))
