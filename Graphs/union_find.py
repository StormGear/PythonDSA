class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.size = [0] * n # size/number of nodes in a set with root i
        self.rank = [1] * n # height of a set with root i

    def find(self, x): # Find the root/representative of a node within a set
        res = x

        if res != self.par[res]:
            self.par[res] = self.find(self.par[res]) # path compression
        return res

    def union(self, x,y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y: # they belong to the same set, no union possible
            return False
        
        # merging with size
        if self.size[root_x] > self.size[root_y]:
            self.par[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.par[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        # merging with rank
        if self.rank[root_x] > self.rank[root_y]:
            self.rank[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.rank[root_x] = root_y
        else:
            self.rank[root_y] = root_x
            self.rank[root_x] += 1

        return True # union has been made