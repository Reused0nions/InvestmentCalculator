print("Please input all answers in numbers with a max digit count of 16 and \ndo not input any letters any symbols.")
print("Calculations will differ from actual end product. Compound is yearly\nand monthly additions are added at the end of each month")
BaseMoney = input("How much money is deposited at the start? ")
MonthlyAddition = input("How much money is added monthly? ")
ReturnRate = input("How high is the return rate? Answer in whole numbers \n (e.g. 6% = 6, 10% = 10.) ")
Years = input("How far in years do you want to calculate? ")
Year = 0
print("=====================================")
for x in range(int(Years)):
    Year = Year + 1
    NumberIncrease = int(ReturnRate) + 100
    AdditionPerYear = round(float(BaseMoney), 2) + int(MonthlyAddition) * 12
    YearEndAmount = AdditionPerYear / 100 * NumberIncrease
    YearEndAmountRounded = round(YearEndAmount, 2)
    Interest = round(YearEndAmountRounded - round(AdditionPerYear, 2), 2)
    print("$" + str(YearEndAmountRounded) + " Year:" + str(Year) + ", " + str(Interest) + " = interest |")
    print("=====================================")
    BaseMoney = YearEndAmountRounded
input("Press any key to finish! ")