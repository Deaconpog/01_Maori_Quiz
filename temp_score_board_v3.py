"""" temp_score_board_v3.py
Get score data from user and store it in a list, then
display the highest three entries nicely
Version #3 - Code carries out previously however now also asks users for their
name alongside the score, and prints off both, essentially showing the user
with the highest score
"""

# Set up empty list
scores_name_of_user = {}

# Get 5 items of Data
for item in range(0, 2):
    get_item = int(input("Enter a score: "))
    get_score = input("Enter name: ")
    scores_name_of_user[get_score] = get_item
    print()

print(scores_name_of_user)
sort_list = sorted(scores_name_of_user.items(), key=lambda x:x[1], reverse=True)
print(sort_list)

#Show that everything made it to the list...
print()
print("*** The Full List of Scores ***")
print(sort_list)

print()

print("*** Highest Three Scores ***")
for item in range(0, 3):
    print(sort_list[item])
