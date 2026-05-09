from profiles import ProfileManager
from graph import SocialGraph
from bfs_dfs import bfs_shortest_path, dfs_explore
from sorting import recommend_friends

pm = ProfileManager()
sg = SocialGraph()

def demo():
    # ── Add 6-8 users ──
    users = [
        ("u1", "Alice",   20, ["music", "travel", "coding"]),
        ("u2", "Bob",     22, ["gaming", "music", "sports"]),
        ("u3", "Charlie", 21, ["coding", "travel", "books"]),
        ("u4", "Diana",   23, ["music", "books", "art"]),
        ("u5", "Eve",     20, ["sports", "gaming", "travel"]),
        ("u6", "Frank",   24, ["coding", "music", "gaming"]),
        ("u7", "Grace",   22, ["art", "travel", "books"]),
        ("u8", "Hank",    21, ["sports", "coding", "music"]),
    ]
    print("\n===== ADDING USERS =====")
    for uid, name, age, interests in users:
        pm.add_user(uid, name, age, interests)
        sg.add_user_node(uid)

    # ── Update 2 profiles ──
    print("\n===== UPDATING PROFILES =====")
    pm.update_profile("u1", age=21, interests=["music", "travel", "coding", "art"])
    pm.update_profile("u3", name="Charles")

    # ── Show 3 profiles ──
    print("\n===== SHOWING PROFILES =====")
    for uid in ["u1", "u2", "u3"]:
        pm.show_profile(uid)

    # ── Add 10 friendships ──
    print("\n===== ADDING FRIENDSHIPS =====")
    connections = [
        ("u1","u2"), ("u1","u3"), ("u2","u4"),
        ("u3","u5"), ("u4","u6"), ("u5","u6"),
        ("u6","u7"), ("u7","u8"), ("u2","u8"),
        ("u3","u4"), ("u1","u5"),
    ]
    for a, b in connections:
        sg.add_friendship(a, b)

    # ── Remove 1 friendship ──
    print("\n===== REMOVING FRIENDSHIP =====")
    sg.remove_friendship("u1", "u5")

    # ── BFS: 2 shortest path queries ──
    print("\n===== BFS SHORTEST PATH =====")
    for start, end in [("u1","u6"), ("u2","u7")]:
        path = bfs_shortest_path(sg, start, end)
        if path:
            names = [pm.users[x]["name"] for x in path]
            print(f"Path {start}→{end}: {' -> '.join(names)} (Degrees: {len(path)-1})")
        else:
            print(f"No path between {start} and {end}")

    # ── DFS: depth=2 and depth=3 ──
    print("\n===== DFS EXPLORATION =====")
    for depth in [2, 3]:
        discovered = dfs_explore(sg, "u1", depth)
        discovered.discard("u1")
        names = [pm.users[x]["name"] for x in discovered]
        print(f"DFS from Alice (depth={depth}): {names}")

    # ── Recommendations ──
    print("\n===== FRIEND RECOMMENDATIONS for Alice =====")
    recs = recommend_friends("u1", pm, sg)
    for uid, name, common in recs:
        print(f"  {name}: {common} common interest(s)")

if __name__ == "__main__":
    demo()