

class Matrix2d:
    def __init__(self, array):
        self.args = array
        self.shape = (len(array),len(array[0]))

        
    def calc_determine4(self):
        c=type(self.args[0][0])(0)
        ar = self.args
        for i in range (self.shape[1]):
            jj=0
            for j in range (self.shape[1]):
                if j==i:
                    continue
                aa=[0,1,2,3]
                aa.pop(aa.index(i))
                aa.pop(aa.index(j))
                #print(i,j,aa)
                k1, k2 = aa
                if ((i+jj)%2==0):
                    #print("+")
                    c += ar[0][i]*ar[1][j]*(ar[2][k1]*ar[3][k2]-ar[2][k2]*ar[3][k1])
                else:
                    c -= ar[0][i]*ar[1][j]*(ar[2][k1]*ar[3][k2]-ar[2][k2]*ar[3][k1])
                jj+=1
        return c
    
    def calc_determine5(self):
        c=type(self.args[0][0])(0)
        ar = self.args
        for i in range (self.shape[1]):
            zz=0
            for z in range (self.shape[1]):
                if z==i:
                    continue
                jj=0
                for j in range (self.shape[1]):
                    if j==i or j==z:
                        continue
                    aa=[0,1,2,3,4]
                    aa.pop(aa.index(i))
                    aa.pop(aa.index(z))
                    aa.pop(aa.index(j))
                    #print(i,j,aa)
                    k1, k2 = aa
                    if ((i+jj+zz)%2==0):
                        #print("+")
                        c += ar[0][i]*ar[1][z]*ar[2][j]*(ar[3][k1]*ar[4][k2]-ar[3][k2]*ar[4][k1])
                    else:
                        c -= ar[0][i]*ar[1][z]*ar[2][j]*(ar[3][k1]*ar[4][k2]-ar[3][k2]*ar[4][k1])
                    jj+=1
                zz+=1
        return c
    
    def calc_determine(self):
        c = type(self.args[0][0])(0)
        ar = self.args
        if self.shape[0]==2 and self.shape[1]==2:
            return ar[0][0]*ar[1][1] - ar[0][1]*ar[1][0]
        for i in range (self.shape[1]):
            new_matrix = []
            for y in range (1, self.shape[0]):
                new_matrix.append([])
                for x in range (self.shape[1]):
                    if x==i:
                        continue
                    new_matrix[y-1].append(ar[y][x])
            if i%2==0:
                c += Matrix2d(new_matrix).calc_determine() * ar[0][i]
            else:
                c -= Matrix2d(new_matrix).calc_determine() * ar[0][i]
        return c

class ComplexInt:
    def __init__(self, x, y=0):
        self.x=x
        self.y=y
        
    def __add__(self,other):
        return ComplexInt(self.x+other.x ,self.y+other.y)

    def __sub__(self,other):
        return ComplexInt(self.x-other.x, self.y-other.y)

    def __mul__(self,other):
        return ComplexInt(self.x*other.x-self.y*other.y, self.x*other.y+self.y*other.x)

    def __str__(self):
        return str(self.x)+"+i*"+str(self.y)


#tests
m=Matrix2d([[0,1,2,3],[1,0,1,2],[2,1,0,1],[3,2,1,0]])
m5=Matrix2d([[0,1,1,1,1],[1,0,1,1,1],[1,1,0,1,1],[1,1,1,0,1],[1,1,1,1,0]])

print(m.calc_determine())
print(m.calc_determine4())
print(m5.calc_determine5())
print(m5.calc_determine())

mm=5*[0]
for i in range (5):
    mm[i]=[]
    for j in range (5):
        mm[i].append(ComplexInt(m5.args[i][j],0))
print(mm)
print(Matrix2d(mm).calc_determine5())
print(Matrix2d(mm).calc_determine())
#print(m.shape)
m2=Matrix2d([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
print(m2.calc_determine4())
print(m2.calc_determine())

ulearn_matrix=[
    [(1,0),(-1,0),(0,1),(0,-1),(1,0)],
    [(0,1),(0,-1),(1,0),(-1,0),(1,0)],
    [(0,1),(0,1),(0,-1),(-1,0),(1,0)],
    [(-1,0),(0,1),(0,-1),(1,0),(1,0)],
    [(1,0),(0,1),(0,-1),(1,0),(1,0)]]
um=5*[0]
for i in range (5):
    um[i]=[]
    for j in range (5):
        um[i].append(ComplexInt(ulearn_matrix[i][j][0],ulearn_matrix[i][j][1]))
print(Matrix2d(um).calc_determine5())
print(Matrix2d(um).calc_determine())
