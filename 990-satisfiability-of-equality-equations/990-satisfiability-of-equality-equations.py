class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        def find(x):
            if x not in parent:
                return x
            else:
                return find(parent[x])
        for i in equations:
            if i[1]=="=":
                a = i[0]
                b = i[-1]
                x = find(a)
                y = find(b)
                if x!=y:
                    parent[y] = x
        for i in equations:
            if i[1]=="!" and find(i[0])==find(i[-1]):
                return False
        return True
