300# -*- coding: utf-8 -*-

error = 1
while error:
    print('\nEnter values in form \'2400\' to represent 24:00')
    time1 = int(input('Please input the first Military Time: '))
    time2 = int(input('Please input the second Military Time: '))

    if(not(time1 > 2400 or time1 < 0 or time2 > 2400 or time2 < 0)):
        error = 0
        if time1 // 1200 == 0:
            M1 = 'AM'
            hour1 = (time1 % 1200) // 100
            minute1 = (time1 % 1200) % 100
        elif time1 // 1200 == 1:
            M1 = 'PM'
            hour1 = ((time1 - 1200) % 1200) // 100
            minute1 = ((time1 - 1200) % 1200) % 100
        if time2 // 1200 == 0:
            M2 = 'AM'
            hour2 = (time2 % 1200) // 100
            minute2 = (time2 % 1200) % 100
        elif time2 // 1200 == 1:
            M2 = 'PM'
            hour2 = ((time2 - 1200) % 1200) // 100
            minute2 = ((time2 - 1200) % 1200) % 100
        
        time3 = abs(time1 - time2)
        hour3 = (time3 % 1200) // 100
        if time3 % 100 >= 60:
            hour3+=1
            minute3 = ((time3 % 1200) % 100) - 60
        else:
            minute3 = (time3 % 1200) % 100
        
        print('Time 1: ',hour1,':',minute1,M1)
        print('Time 2: ',hour2,':',minute2,M2)
        print('Time Elapsed: ',hour3,'hour(s) and',minute3,'minute(s)')
    else:
        print('\n!!PLEASE INPUT A VALID TIME!!')

