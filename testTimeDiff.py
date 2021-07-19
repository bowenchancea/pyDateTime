import timeDiff

#declaring variables for testing
testDate = timeDiff.makeDate(2022, 1, 1, 0, 0, 0)
now = timeDiff.now()

#basic testing
print(timeDiff.rD(testDate, now))
print(timeDiff.rH(testDate, now))
print(timeDiff.rM(testDate, now))
print(timeDiff.rS(testDate, now))

#calling the countdown clock
timeDiff.countdown(testDate)
