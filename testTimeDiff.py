import timeDiff
import time

#declaring variables for testing
testDate = timeDiff.makeDate(2022, 1, 1, 0, 0, 0)
now = timeDiff.now()

#basic testing
print(timeDiff.rD(testDate, now))
print(timeDiff.rH(testDate, now))
print(timeDiff.rM(testDate, now))
print(timeDiff.rS(testDate, now))

#making a countdown clock
while 0 == 0: 
    now = timeDiff.now()
    print(timeDiff.rD(testDate, now), "days,", timeDiff.rH(testDate, now), "hours,",
    timeDiff.rM(testDate, now), "minutes, and", timeDiff.rS(testDate, now), "seconds remaining")
    time.sleep(1)
