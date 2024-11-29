# Create a list of 10 employee names
employee_list = ["Mwangi Kamau", "Achieng Otieno", "Wanjiku Njoroge", "Mutua Muthoni", "Omondi Okoth","Mumbi Karanja", "Njeri Waithera", "Kiprotich Cheruiyot", "Nyambura Gichuru", "Wafula Simiyu"]

# Split the list into two sub-lists
sub_list1 = employee_list[:5]  # First 5 names
sub_list2 = employee_list[5:]  # Last 5 names

# Add new employee to sub_list2
sub_list2.append("Kriti Brown")

# Remove the second employee from sub_list1
sub_list1.pop(1)

# Merge both sub-lists
merged_list = sub_list1 + sub_list2  

# Salary list and applying a 4% raise
salary_list = [50000, 60000, 55000, 48000, 53000, 52000, 61000, 47000, 51000, 58000] 
salary_list = [salary * 1.04 for salary in salary_list] 

# Sort the salary list and show top 3 salaries
salary_list.sort(reverse=True)  
top_salaries = salary_list[:3]

# Output the results
print("Sub List 1 after removal:", sub_list1)
print("Sub List 2 after adding new employee:", sub_list2)
print("Merged List:", merged_list)
print("Updated Salary List after 4% raise:", salary_list)
print("Top 3 Salaries:", top_salaries)
