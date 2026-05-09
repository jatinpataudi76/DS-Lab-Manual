def recommend_friends(user_id, profiles, graph):
    """Rank non-friends by common interests"""
    my_interests = set(profiles.users[user_id]["interests"])
    my_friends = set(graph.get_friends(user_id))
    my_friends.add(user_id)

    scores = []
    for other_id, data in profiles.users.items():
        if other_id in my_friends:
            continue
        common = len(my_interests & set(data["interests"]))
        if common > 0:
            scores.append((other_id, data["name"], common))

    # Sort by common interests (descending)
    scores.sort(key=lambda x: x[2], reverse=True)
    return scores