class huffman(object):
    def __init__(self, left= None, right = None):
        self.left = left
        self.right = right
    
    def nodes(self):
        return (self.left, self.right)
    
    def children(self):
        return (self.left, self.right)
        
    def __str__(self):
        return f"{self.left}_{self.right}"

def tree(node, left = True, binary=""):
    if type(node) is str: return {node: binary}
    (l,r) = node.children()
    d = {}
    d.update(tree(l, True, binary + "0"))
    d.update(tree(r, False, binary + "1"))
    return d

message = "geekforgeeks".lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
total = {i:0 for i in alphabet}
new = {}

for i in message:
    total[i] +=1

for i in total:
    if total[i] == 0: pass
    elif total[i] in new:
        new[total[i]] = new[total[i]] + i
    else:
        new[total[i]] = i

highestKeys = sorted(new, reverse=True)
final = []
for x in highestKeys:
    for y in new[x]:
        final.append((y,x))

nodes = final

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = huffman(key1, key2)
    nodes.append((node, c1+c2))
    nodes = sorted(nodes, key = lambda x:x[1], reverse=True)

huffCode = tree(nodes[0][0])

for (char, frequency) in final:
    print(char, huffCode[char])
print("DONT FORGET to communicate tree along with encoding with above")
#I'd like to thank programiz.com for helping with this, geeksforgeeks has a more optimal version however.
