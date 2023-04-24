import time, math
from functools import reduce

# При условии a <= b алгоритм Евклида egcd(a,b) возвращает целые числа
# (d, x, y), такие что d = (a,b) и x*a + y*b = d
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    d, y, x = egcd(b % a, a)
    return (d, x - (b // a) * y, y)

# Вернуть b, такое что a*b=1(mod p), при условии, что a и p взаимно простые
def modinv(a, p):
    d, x, y = egcd(a % p, p)
    return x % p
    
class Polynomial:#многочлен
    def __init__(self, array):
        if type(array) == int:
            self.args=[array]
        else:
            self.args = array
        self.degree = len(self.args)-1
        self.type_val = type(self.args[0])
        
    def __str__(self):
        print(self.args)
        string=""
        for i in range (len(self.args)):
            if i==0:
                string+=str(self.args[i])
            elif i==1:
                string+="+"*(self.args[i]>=0)+str(self.args[i])+"x"
            else:
                string+="+"*(self.args[i]>=0)+str(self.args[i])+"x^"+str(i)
        return string

    def __add__(self,other):
        if type(other) == Polynomial:
            result_args_len = max(self.degree,other.degree)+1
            result_args=[self.type_val(0)]*result_args_len
            for i in range (result_args_len):
                if i<self.degree+1:
                    result_args[i]=result_args[i]+self.args[i]
                if i<other.degree+1:
                    result_args[i]=result_args[i]+other.args[i]
            return Polynomial(result_args)
        elif type(other) in [int,ZInt251]:
            result_args=self.args.deepcopy()
            result_args[0]+=other
            return Polynomial(result_args)
        else:
            #print(type(other))
            raise Exception()
        
    def __sub__(self,other):
        if type(other) == Polynomial:
            result_args_len = max(self.degree,other.degree)+1
            result_args=[self.type_val(0)]*result_args_len
            for i in range (result_args_len):
                if i<self.degree+1:
                    result_args[i]=result_args[i]+self.args[i]
                if i<other.degree+1:
                    result_args[i]=result_args[i]-other.args[i]
            return Polynomial(result_args)
        elif type(other) in [int,ZInt251]:
            result_args=self.args.deepcopy()
            result_args[0]-=other
            return Polynomial(result_args)
        else:
            #print(type(other))
            raise Exception()
        
    def __mul__(self,other):
        if type(other) == Polynomial:
            result_args_len = self.degree + other.degree + 1
            result_args = [self.type_val(0)] * result_args_len
            for i in range (result_args_len):
                for j in range (i+1):
                    #print(i,j,result_args)
                    if j < self.degree+1:
                        if i-j < other.degree+1:
                            #print(result_args[i])
                            #print(self.args[j])
                            #print(other.args[i-j])
                            
                            result_args[i] = result_args[i]+self.args[j] * other.args[i-j]
            return Polynomial(result_args)
        elif type(other) in [int,ZInt251] :
            return Polynomial([arg*other for arg in self.args])
        else:
            #print(type(other))
            raise Exception()
        
    def __truediv__(self,other):
        if type(other)==int:
            return Polynomial([arg/other for arg in self.args])
        elif type(other)==ZInt251:
            return Polynomial([arg/other for arg in self.args])
        
    def __call__(self,x):
        return self.compute_value(x)
    def get_degree(self):
        return self.degree
    
    def get_arguments(self):
        return self.args
    
    def derivative(self):
        derivative_args = []
        for i in range (1,len(self.args)):
            derivative_args.append(self.args[i]*i)
        return Polynomial(derivative_args)

    def polynomial_sum(self, other_polynomial):
        result_args=[]
        for i in range (min(len(self.args),len(other_polynomial.args))):
            result_args.append(self.args[i]+other_polynomial.args[i])
        if self.get_degree>other_polynomial.get_degree:
            for i in range (abs(self.get_degree-other_polynomial.get_degree)):
                result_args.append(self.args[i])
        else:
            for i in range (abs(self.get_degree-other_polynomial.get_degree)):
                result_args.append(other_polynomial.args[i])
        return result_args
    
    def compute_value(self, x):
        result=self.type_val(0)
        #print(result)
        for i in range (len(self.args)):
            result=result+self.args[i]*x**i
        #print(result)
        return result
    
    def get_solution_1_degree(self):
        return -self.args[0]/self.args[1]
    
    def solution_between_values(self, left,right):
        while right-left>0.001:
            medium = (right+left)/2
            if self.compute_value(medium)*self.compute_value(right)>0:
                right=medium
            else:
                left=medium
        return medium
    
    def solutions_by_extremums(self,array_extr):
        array_extr.append(-999999)
        array_extr.append(999999)
        array_extr.sort()
        solutions=[]
        for left,right in zip(array_extr[:-1],array_extr[1:]):
            #print(left,right)
            if self.compute_value(left)*self.compute_value(right)<0:
                solutions.append(self.solution_between_values(left,right))
        return solutions

    def all_solutions(self):
        if self.degree==-1:
            return [NaN]
        elif self.degree==0:
            if self.args[0]==0:
                return [NaN]
            else:
                return []
        elif self.degree==1:
            if self.args[1]==0 and -self.args[0]==0:
                return [NaN]
            elif self.args[1]==0 and -self.args[0]!=0:
                return []
            return [-self.args[0]/self.args[1]]
        else:
            solutions_previous = self.derivative().all_solutions()
            return self.solutions_by_extremums(solutions_previous)

    def lagrange_polynomial(xs, ys):
        type_val = type(xs[0])
        #print(type_val)
        x_polynomials = [Polynomial([-x,type_val(1)]) for x in xs]
        result_polynomial = Polynomial([type_val(0)])
        #print(x_polynomials)
        for i in range (len(ys)):
            new_monomial = (reduce(lambda x,y: x.__mul__(y),[x_polynomials[j] for j in range (len(ys)) if j!=i], Polynomial([type_val(1)])))
            #print(new_monomial)
            new_monomial = new_monomial / new_monomial(xs[i])
            #print(new_monomial)
            new_monomial = new_monomial * ys[i]
            #print(new_monomial)
            result_polynomial = result_polynomial + new_monomial
        return result_polynomial

class ZInt251:
    def __init__(self, x):
        if type(x)==int:
            self.x = x % 251
        elif type(x) == list:
            result = len(x)*[0]
            for i in range (len(x)):
                result[i]=ZInt251(x[i])

    #def __call__(other_int):
    #    return ZInt251(other_int)
    
    def __add__(self,other):
        if type(other)==int:
            return ZInt251(self.x+other)
        elif type(other)==ZInt251:
            return ZInt251(self.x+other.x)
        else:
            raise Exception()

    def __sub__(self,other):
        if type(other)==int:
            return ZInt251(self.x-other)
        elif type(other)==ZInt251:
            return ZInt251(self.x-other.x)
        else:
            raise Exception()

    def __mul__(self,other):
        if type(other)==int:
            return ZInt251(self.x*other)
        elif type(other)==ZInt251:
            return ZInt251(self.x*other.x)
        else:
            raise Exception()

    def __truediv__(self, other):
        #print(0)
        #print(self,other)
        for i in range (251):
            if (other*i).x==self.x:
                return ZInt251(i)
        raise Exception()
    
    def __neg__(self):
        return ZInt251((251-self.x)%251)

    def __pow__(self, intpow):
        return ZInt251((self.x**intpow)%251)
    def __str__(self):
        return "ZInt251: "+str(self.x)
    
"""p = Polynomial([1,-1,1])
print(p)
p1=p.derivative()
p1.args
print(p1.get_degree())
current_p=Polynomial([0,-10,0,5,1])
current_p=Polynomial([0,-10,0,5,1,8,9,10,20,89,98,10,20,89,98,10,
                      20,89,98,10,20,89,98,10,20,89,98,10,20,89,98,10,
                      20,89,98,10,20,89,98,10,20,89,98,10,20,89,98,10])
p_massive=[current_p]
while current_p.get_degree()>1:
    current_p=current_p.derivative()
    p_massive.append(current_p)
p_massive=p_massive[::-1]
p_sol1 = p_massive[0].get_solution_1_degree()
p_sol=[p_sol1]
for p in p_massive[1:]:
    p_sol=p.solutions_by_extremums(p_sol)
    #print(p_sol)
print(p_sol)
for ps in p_sol:
    print(p_massive[-1].compute_value(ps))

print(time.process_time())
print(p_massive[-1].all_solutions())"""
#p1=Polynomial([2,6,3])
#p2=Polynomial([0,1])
#p3=Polynomial([0,1])
#print(list(map(ZInt251,[0,1,2])))
#print(reduce(lambda x,y: x.__add__(y),[p1,p2,p3],p1))
#print((p1+p2).args)
#print((p1*p2).args)
#p4=Polynomial.lagrange_polynomial(list(map(ZInt251,[1,2,7])),list(map(ZInt251,[0,1,3])))
#print(p4)
#print(p4(7))
#print(Polynomial([2,6,3]).all_solutions())
#print(time.process_time())
