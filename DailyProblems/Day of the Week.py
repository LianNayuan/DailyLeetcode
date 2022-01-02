class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def is_leap(year):
            return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
            
        count = 0

        for i in range(1971,year):
            if is_leap(i):
                count += 366
            else:
                count += 365

        months = [0,31,28,31,30,31,30,31,31,30,31,30,31]    
        for i in range(1,month):
            count += months[i]

        if is_leap(year) and month > 2 :
            count += 1
        
        count += day - 1

        count = count % 7 
        week = ["Friday", "Saturday","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday" ]
        return week[count]
