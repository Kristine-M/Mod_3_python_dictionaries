# You have a dictionary representing weekly sales data for a store. 
# Your task is to create a deep copy of this data and update the sales
# figures for a specific week.

# Given Sales Data:

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}
# Create a deep copy of weekly_sales.
import copy

copied_data = copy.deepcopy(weekly_sales)

# Update the sales figure for "Electronics" in "Week 2" to 18000 in the copied data.
copied_data["Week 2"]["Electronics"] = 18000

print("Original ", weekly_sales["Week 2"]["Electronics"])
print("Deep Copy ", copied_data["Week 2"]["Electronics"])