
year = int(input("enter a year :"))
x = int(year)
if x >=1582:
 if x%4:
     print("common year")
 elif x%100:
     print("Leap year")
 elif x%400:
     print("Leap year")
 else:
     print("Leap year")
     
