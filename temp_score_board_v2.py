"""" temp_score_board_v2.py
Get score data from user and store it in a list, then
display the highest three entries nicely
Version #2 - uses a list with reverse ordering, this makes the code organize
from highest to lowest, and I have implemented an int input rather than just
a string input this allows for numbers such as 10 to be sorted in a similar
manner.
"""

# Set up empty list
scores_of_user = []

# Get 5 items of Data
for item in range(0, 5):
    get_item = int(input("Enter a score: "))
    scores_of_user.append(get_item)

scores_of_user.sort(reverse=True)

# Show that everything made it to the list...
print()
print("*** The Full List of Scores ***")
print(scores_of_user)

print()

print("*** Highest Three Scores ***")
for item in range(0, 3):
    print(scores_of_user[item])

