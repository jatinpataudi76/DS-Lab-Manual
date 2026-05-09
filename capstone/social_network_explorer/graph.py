class SocialGraph:
    def __init__(self):
        self.adj = {}  # user_id -> set of friends

    def add_user_node(self, user_id):
        if user_id not in self.adj:
            self.adj[user_id] = set()

    def add_friendship(self, u, v):
        # Undirected (mutual friends)
        self.adj.setdefault(u, set()).add(v)
        self.adj.setdefault(v, set()).add(u)
        print(f"Friendship added: {u} <-> {v}")

    def remove_friendship(self, u, v):
        self.adj.get(u, set()).discard(v)
        self.adj.get(v, set()).discard(u)
        print(f"Friendship removed: {u} <-> {v}")

    def get_friends(self, user_id):
        return list(self.adj.get(user_id, []))