'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

'''
months = "JanFebMarAprMayJunJulAugSepOctNovDec"

while True:
    userinput=int(input("pick a month number 1-12"))
    if userinput<1 or userinput>12:
        break
    end=userinput*3
    start=end-3
    print(months[start:end])
print("goodbye")