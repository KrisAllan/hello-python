message = input("Enter a comma separated list of numbers: ")
INPUT = message.split(",")

total = 0.0
for a in range(len(INPUT)):
    SUM = float(INPUT[a])
    total += SUM * SUM

print("Sum of squares: ", total)
 
