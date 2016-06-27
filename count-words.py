from sys import argv
from PTree import *

print(argv)
targets = argv[1].split(':')
code_slot = int(argv[2]) - 1

trees = ParseFiles(argv[2:])

def updateCoding(tree,target,slot):
    def countwords(tree,target,target_found):
        count = 0
        if target_found == 1:
            if tree.height > 0:
                for x in tree.content:
                    count += countwords(x,target,1)
            else:
                return 1
        else:
            if tree.height > 0:
                for x in tree.content:
                    if x.name in target:
                        count += countwords(x,target,1)
        return count

    if tree.height > 0:
        coding = 0
        for c in tree.content:
            if 'CODING' in c.name:
                coding = 1
            else:
                c = updateCoding(c,target,slot)
        if coding == 1:
            count = 0
            for c in tree.content:
                if 'CODING' not in c.name:
                    count += countwords(c, target, 0)
            for c in tree.content:
                if 'CODING' in c.name:
                    s = c.content.split(':')
                    s[slot] = str(count)
                    c.content = ':'.join(s)
    return tree



for key in trees:
    newtrees = []
    for tree in trees[key]:
        ntree = updateCoding(tree,targets,code_slot)
        newtrees.append(ntree)
    outfile = open(key+'_'+'_'.join(targets)+'.cod','w')
    for tree in newtrees:
        outfile.write(str(tree)+'\n')
    outfile.close()
