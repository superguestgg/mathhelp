import time
class Polynomial:#многочлен
    def __init__(self, array):
        self.args=array
        
    def get_derivative(self):
        derivative_args = []
        for i in range (1,len(self.args)):
            derivative_args.append(self.args[i]*i)
        return Polynomial(derivative_args)

    def get_sum(self, other_polynomial):
        result_args=[]
        for i in range (max(len(self.args),len(other_polynomial.args))):
            result_args.append(self.args[i]+other_polynomial.args[i])

    
    def get_str(self):
        string=""
        for i in range (len(self.args)):
            string+="+"+str(self.args[i])+"x^"+str(i)
        return string
    
    def get_value(self, x):
        result=0
        for i in range (len(self.args)):
            result+=self.args[i]*x**i
        return result
    
    def get_degree(self):
        return(len(self.args)-1)
    
    def get_solution_1_degree(self):
        return -self.args[0]/self.args[1]
    
    def get_solution_between_values(self, left,right):
        while right-left>0.001:
            medium = (right+left)/2
            if self.get_value(medium)*self.get_value(right)>0:
                right=medium
            else:
                left=medium
        return medium
    
    def get_solution_by_extremums(self,array_extr):
        array_extr.append(-999999)
        array_extr.append(999999)
        array_extr.sort()
        solutions=[]
        for left,right in zip(array_extr[:-1],array_extr[1:]):
            #print(left,right)
            if self.get_value(left)*self.get_value(right)<0:
                solutions.append(self.get_solution_between_values(left,right))
        
        return solutions


p = Polynomial([1,1,1])
p1=p.get_derivative()
p1.args
print(p1.get_degree())
current_p=Polynomial([0,-10,0,5,1])
current_p=Polynomial([0,-10,0,5,1,8,9,10,20,89,98,10,20,89,98,10,
                      20,89,98,10,20,89,98,10,20,89,98,10,20,89,98,10,
                      20,89,98,10,20,89,98,10,20,89,98,10,20,89,98,10])
p_massive=[current_p]
while current_p.get_degree()>1:
    current_p=current_p.get_derivative()
    p_massive.append(current_p)
p_massive=p_massive[::-1]
p_sol1 = p_massive[0].get_solution_1_degree()
p_sol=[p_sol1]
for p in p_massive[1:]:
    p_sol=p.get_solution_by_extremums(p_sol)
    #print(p_sol)
print(p_sol)
for ps in p_sol:
    print(p_massive[-1].get_value(ps))

print(time.process_time())
