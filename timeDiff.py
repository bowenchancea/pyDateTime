import datetime

#target = datetime.datetime(2022, 1, 1, 0, 0, 0)
#now = datetime.datetime.now()

#this was used for testing to ensure that I got the correct information
def timeDiff(a,b,c,d,e,f):
    target = datetime.datetime(a, b, c, d, e, f)
    now = datetime.datetime.now()
    remainingTotalTime = (target - now)
    remainingTotalSeconds = int (remainingTotalTime.total_seconds())
    remD = remainingTotalSeconds // 86400
    remHoursAfterDays = remainingTotalSeconds % 86400
    remH = remHoursAfterDays // 3600
    remMinutesAfterHours = remHoursAfterDays % 3600
    remM = remMinutesAfterHours // 60
    remS = remMinutesAfterHours % 60
    return(remD, remH, remM, remS)

#returns remaining days
def rD(a, b, c, d, e, f):
    target = datetime.datetime(a, b, c, d, e, f)
    now = datetime.datetime.now()
    remainingTotalTime = (target - now)
    remainingTotalSeconds = int (remainingTotalTime.total_seconds())
    remD = remainingTotalSeconds // 86400
    remHoursAfterDays = remainingTotalSeconds % 86400
    remH = remHoursAfterDays // 3600
    remMinutesAfterHours = remHoursAfterDays % 3600
    remM = remMinutesAfterHours // 60
    remS = remMinutesAfterHours % 60
    return(remD)

#returns remaining hours
def rH(a, b, c, d, e, f):
    target = datetime.datetime(a, b, c, d, e, f)
    now = datetime.datetime.now()
    remainingTotalTime = (target - now)
    remainingTotalSeconds = int (remainingTotalTime.total_seconds())
    remD = remainingTotalSeconds // 86400
    remHoursAfterDays = remainingTotalSeconds % 86400
    remH = remHoursAfterDays // 3600
    remMinutesAfterHours = remHoursAfterDays % 3600
    remM = remMinutesAfterHours // 60
    remS = remMinutesAfterHours % 60
    return(remH)

#returns remaining minutes
def rM(a, b, c, d, e, f):
    target = datetime.datetime(a, b, c, d, e, f)
    now = datetime.datetime.now()
    remainingTotalTime = (target - now)
    remainingTotalSeconds = int (remainingTotalTime.total_seconds())
    remD = remainingTotalSeconds // 86400
    remHoursAfterDays = remainingTotalSeconds % 86400
    remH = remHoursAfterDays // 3600
    remMinutesAfterHours = remHoursAfterDays % 3600
    remM = remMinutesAfterHours // 60
    remS = remMinutesAfterHours % 60
    return(remM)

#returns remaining seconds
def rS(a, b, c, d, e, f):
    target = datetime.datetime(a, b, c, d, e, f)
    now = datetime.datetime.now()
    remainingTotalTime = (target - now)
    remainingTotalSeconds = int (remainingTotalTime.total_seconds())
    remD = remainingTotalSeconds // 86400
    remHoursAfterDays = remainingTotalSeconds % 86400
    remH = remHoursAfterDays // 3600
    remMinutesAfterHours = remHoursAfterDays % 3600
    remM = remMinutesAfterHours // 60
    remS = remMinutesAfterHours % 60
    return(remS)

#testing:

#print("Days Remaining:   ", rD(2022,1,1,0,0,0))
#print("Hours Remaining:  ", rH(2022, 1, 1, 0, 0, 0))
#print("Minutes Remaining:", rM(2022, 1, 1, 0, 0, 0))
#print("Seconds Remaining:", rS(2022, 1, 1, 0, 0, 0))

