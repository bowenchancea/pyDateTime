import datetime
import time

#target = datetime.datetime(2022, 1, 1, 0, 0, 0)
#now = datetime.datetime.now()

#this was used for testing to ensure that I got the correct information
def timeDiff(a, b):
    #calculating timedelta
    remainingTotalTime = (a - b)
    #converting to seconds for conversions
    remainingTotalSeconds = int (remainingTotalTime.total_seconds())
    #calculates days and then remaining seconds after days have been removed
    remD = remainingTotalSeconds // 86400
    remHoursAfterDays = remainingTotalSeconds % 86400
    #calculates hours and then remaining seconds after hours have been removed
    remH = remHoursAfterDays // 3600
    remMinutesAfterHours = remHoursAfterDays % 3600
    #calculates minutes and then remaining seconds after minutes have been removed
    remM = remMinutesAfterHours // 60
    remS = remMinutesAfterHours % 60
    return remD, remH, remM, remS

#returns remaining days
def rD(a, b):
    remainingTotalTime = (a - b)
    remainingTotalSeconds = int (remainingTotalTime.total_seconds())
    remD = remainingTotalSeconds // 86400
    remHoursAfterDays = remainingTotalSeconds % 86400
    remH = remHoursAfterDays // 3600
    remMinutesAfterHours = remHoursAfterDays % 3600
    remM = remMinutesAfterHours // 60
    remS = remMinutesAfterHours % 60
    return remD

#returns remaining hours
def rH(a, b):
    remainingTotalTime = (a - b)
    remainingTotalSeconds = int (remainingTotalTime.total_seconds())
    remD = remainingTotalSeconds // 86400
    remHoursAfterDays = remainingTotalSeconds % 86400
    remH = remHoursAfterDays // 3600
    remMinutesAfterHours = remHoursAfterDays % 3600
    remM = remMinutesAfterHours // 60
    remS = remMinutesAfterHours % 60
    return remH

#returns remaining minutes
def rM(a, b):
    remainingTotalTime = (a - b)
    remainingTotalSeconds = int (remainingTotalTime.total_seconds())
    remD = remainingTotalSeconds // 86400
    remHoursAfterDays = remainingTotalSeconds % 86400
    remH = remHoursAfterDays // 3600
    remMinutesAfterHours = remHoursAfterDays % 3600
    remM = remMinutesAfterHours // 60
    remS = remMinutesAfterHours % 60
    return remM

#returns remaining seconds
def rS(a, b):
    remainingTotalTime = (a - b)
    remainingTotalSeconds = int (remainingTotalTime.total_seconds())
    remD = remainingTotalSeconds // 86400
    remHoursAfterDays = remainingTotalSeconds % 86400
    remH = remHoursAfterDays // 3600
    remMinutesAfterHours = remHoursAfterDays % 3600
    remM = remMinutesAfterHours // 60
    remS = remMinutesAfterHours % 60
    return remS

#creating a now variable so datetime doesn't have to be import in main doc
def now():
    return datetime.datetime.now()

#allowing a date to be specified without importing datetime in main doc
def makeDate(a, b, c, d, e, f):
    return datetime.datetime(a, b, c, d, e, f)

#making a countdown clock function
def countdown(a):
    while 0 == 0: 
        nowCount = now()
        print(rD(a, nowCount), "days,", rH(a, nowCount), "hours,",
        rM(a, nowCount), "minutes, and", rS(a, nowCount), "seconds remaining")
        time.sleep(1)
