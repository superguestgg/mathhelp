import time

class Polynomial:#многочлен
    def __init__(self, array):
        self.args=array
        self.degree = len(self.args)-1
        
    def __str__(self):
        string=""
        for i in range (len(self.args)):
            if i==0:
                string+=str(self.args[i])
            elif i==1:
                string+="+"*(self.args[i]>=0)+str(self.args[i])+"x"
            else:
                string+="+"*(self.args[i]>=0)+str(self.args[i])+"x^"+str(i)
        return string
    
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
    
    def compute_value(self, x):
        result=0
        for i in range (len(self.args)):
            result+=self.args[i]*x**i
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


p = Polynomial([1,-1,1])
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
print(p_massive[-1].all_solutions())
print(Polynomial([0]).all_solutions())
print(time.process_time())
