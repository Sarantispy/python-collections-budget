import matplotlib.pyplot as plt
import collections
import os
from . import Expense


dir_path = os.path.dirname(os.path.realpath(__file__))  # find the .py file current folder
os.chdir(dir_path)                                      # make the folder working directory

expenses = Expense.Expenses()
expenses.read_expenses("C:/GitHub/PluralSight/python-collections-budget/data/spending_data.csv")
spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)
spending_counter = collections.Counter(spending_categories)
top5 = spending_counter.most_common(5)
categories, count = zip(*top5)
fig, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show()
