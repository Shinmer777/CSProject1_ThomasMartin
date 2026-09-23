customer1 = "nAGI sEISHIRO"
#I wrote the name that way just to prove the functionality of my ".title()"
Soup, Milk, Eggs, Steak, Assorted_Vegetables = 4.99, 7.99, 12.99, 19.99, 16.99
QuanSoup, QuanMilk, QuanEggs, QuanSteak, QuanAV = 3, 2, 2, 1, 4

Total_For_Groceries = (Soup * QuanSoup) + (Milk * QuanMilk) + (Eggs * QuanEggs) + (Steak * QuanSteak) + (Assorted_Vegetables * QuanAV)
Total_Number_of_Groceries = QuanSoup + QuanMilk + QuanEggs + QuanSteak + QuanAV
Average_Cost_Per_Item = Total_For_Groceries/Total_Number_of_Groceries

print(f"{customer1.title()} paid a total of ${Total_For_Groceries:.2f}, with an average of ${Average_Cost_Per_Item:.2f} per item.")
#Evan showed us how to do this format ^




customer2 = "rEO mIKAGE"

Soup, Milk, Eggs, Steak, Assorted_Vegetables = 4.99, 7.99, 12.99, 19.99, 16.99
QuanSoup, QuanMilk, QuanEggs, QuanSteak, QuanAV = 9, 1, 1, 2, 6

Total_For_Groceries = (Soup * QuanSoup) + (Milk * QuanMilk) + (Eggs * QuanEggs) + (Steak * QuanSteak) + (Assorted_Vegetables * QuanAV)
Total_Number_of_Groceries = QuanSoup + QuanMilk + QuanEggs + QuanSteak + QuanAV
Average_Cost_Per_Item = Total_For_Groceries/Total_Number_of_Groceries

print(f"{customer2.title()} paid a total of ${Total_For_Groceries:.2f}, with an average of ${Average_Cost_Per_Item:.2f} per item.")
