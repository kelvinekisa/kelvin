from collections import Counter
from collections import defaultdict
# 
# import interest as interest

#This file will contain dictionaries manipulation and creation.
CountryHistory ={
    "Kenya": "Nairobi",
    "Independance": 1963,
    "Population": 40000000
}
print(CountryHistory)
users = [
{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }
]
print(users[9])
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}
for i, j in friendship_pairs: # and loop over the friendship pairs to populate it:
    friendships[i].append(j)  # Add j as a friend of user i
    friendships[j].append(i)  # Add i as a friend of user j

# summing up the lenghts of all the friends lists by finding the total number of connections
def number_of_friends(user):
    """"How many does _user_ have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_connections / num_users

print("Total connections are: ", total_connections)
print("Avg connections are: ", avg_connections)

#create a list (user_id, number_of_friends).
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

num_friends_by_id.sort(                                     # sort the list
    key=lambda  id_and_friends: id_and_friends[1],          # by num_friends
    reverse=True)                                            # largest to smallest
# Each pair is (user_id, num_friends):
# [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3),
# (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]

def foaf_ids_bad(user):
    """foaf is a short for "friend of a friend" """
    return [foaf_id
        for friend_id in friendships[user["id"]]
        for foaf_id in friendships[friend_id]
    ]
print(friendships[0])
print(friendships[1])
print(friendships[2])

def friends_of_friends(user, foaf_id=None):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]     # for each of my friends,
        for foaf_id in friendships[friend_id]     # find their friends
        if foaf_id != user_id                     # who aren't me
        and foaf_id not in friendships[user_id]   # and aren't my friends.

    )
print(friends_of_friends(users[3]))

# friends and their interests
interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]
print(interests)

def data_scientists_who_like(target_interests):
    """find the ids of all users who like target interests"""
    return[user_id
           for user_id, user_interest in interests
           if user_interest == target_interests

    ]
# building an index from interests to users:

# keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, interests in interests:
    user_ids_by_interest[interest].append(user_id)

# And another from users to interests
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

#     it’s easy to find who has the most interests in common with a given
# user:
# Iterate over the user’s interests.
# For each interest, iterate over the other users with that interest.
# Keep count of how many times we see each other user

def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )
print(most_common_interests_with(interests))
