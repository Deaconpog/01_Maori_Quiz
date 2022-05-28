"""" temp_score_board_v1.py
Get score data from user and store it in a list, then
display the highest three entries nicely
Version #1 - Uses a list sorted from highest to lowest displaying highest three
"""

# Set up empty list
scores_of_user = []

# Get 5 items of Data
for item in range(0, 5):
    get_item = input("Enter a score: ")
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
