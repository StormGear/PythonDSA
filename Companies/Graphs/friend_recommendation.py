from collections import defaultdict
# Citadel Question on friend recommendation link: https://www.fastprep.io/problems/citadel-get-recommended-friends
# This question actually appeared in my OA and I was not able to solve it. I am solving it now.
def getRecommendedFriends(n, friendships):
    # Step 1: Build the adjacency list
    friends = defaultdict(set)
    for a, b in friendships:
        friends[a].add(b)
        friends[b].add(a)
    
    recommendations = []
    
    for user in range(n):
        max_common = 0
        best_recommendation = -1
        potential_friends = set()
        
        # Gather potential friends (friends of friends) of the user
        for friend in friends[user]:
            for friend_of_friend in friends[friend]:
                if friend_of_friend != user and friend_of_friend not in friends[user]:
                    potential_friends.add(friend_of_friend)

        print(potential_friends)
        
        # Determine the best recommendation
        for candidate in potential_friends:
            common_friends = len(friends[user] & friends[candidate])
            if common_friends > max_common or (common_friends == max_common and candidate < best_recommendation):
                max_common = common_friends
                best_recommendation = candidate
        
        recommendations.append(best_recommendation)
    
    return recommendations

# Example usage
n = 5
friendships = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
print(getRecommendedFriends(n, friendships))  # Output: [3, 2, 1, 0, 1]
