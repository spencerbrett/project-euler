alpha_score = { 'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,
                'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,
                'u':21,'v':22,'w':23,'x':24,'y':25,'z':26 , '"':0}
def namescore(name):
    name = name.lower()
    letters = list(name)
    score = 0
    for l in letters:
        score += alpha_score[l]
    return score

def getNames(fileName):
    delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
    with open(fileName, 'r') as f:
        names = f.read().split(',')
        names.sort()
        return names

def main():
    names = getNames('names.txt')
    position = 1
    score = 0
    for name in names:
        score += position * namescore(name)
        position += 1
    print score

main()       
