def help(st):
    l=len(st)
    aa=100*[0]
    now="plus"
    xmax=0
    now2=0
    now3=0
    sign="+"
    for i in range (l):
        if st[i]=="+":
            xmax=max(xmax,now3)
            aa[now3]=aa[now3]+now2
            if sign=="-":
               aa[now3]=aa[now3]-2*now2

            now="beforex"
            sign="+"
            now2=0
            now3=0
        elif st[i]=="-":
            aa[now3]=aa[now3]+now2
            xmax=max(xmax,now3)
            if sign=="-":
               aa[now3]=aa[now3]-2*now2
            now="beforex"
            sign="-"
            now2=0
            now3=0
        elif (st[i]).isdigit()==True:
            if now!="afterx":
                now2=now2*10+int(st[i])
            else :
                now3=now3*10+int(st[i])
        elif st[i]=="x" or st[i]=="*" or st[i]=="^":
            now="afterx"
            if now2==0:
                now2=1
        else:
            print("error0")
    aa[now3]=aa[now3]+now2
    if sign=="-":
        aa[now3]=aa[now3]-2*now2
    aax=[0]*(xmax+1)
    for i in range (xmax+1):
        aax[i]=aa[i]
    return(aax)
#00000000000000000000000end
#11111111111111111111111start

def reducemonomials(st):
    print("waiting...1...")
    l=len(st)
    aa=100*[0]
    now="plus"
    now2=0
    now3=0
    sign="+"
    for i in range (l):
        if st[i]=="+":
            aa[now3]=aa[now3]+now2
            if sign=="-":
               aa[now3]=aa[now3]-2*now2

            now="beforex"
            sign="+"
            now2=0
            now3=0
        elif st[i]=="-":
            aa[now3]=aa[now3]+now2
            if sign=="-":
               aa[now3]=aa[now3]-2*now2
            now="beforex"
            sign="-"
            now2=0
            now3=0
        elif (st[i]).isdigit()==True:
            if now!="afterx":
                now2=now2*10+int(st[i])
            else :
                now3=now3*10+int(st[i])
        elif st[i]=="x" or st[i]=="*" or st[i]=="^":
            now="afterx"
            if now2==0:
                now2=1
        else:
            print("error1")
    aa[now3]=aa[now3]+now2
    if sign=="-":
        aa[now3]=aa[now3]-2*now2
    stend=""
    for i in range (l):
        stendi=""
        if aa[i]!=0:
            stendi=str(aa[i])
            if i==1:
                stendi+="x^1"
            elif i!=0:
                stendi+="x^"+str(i)
            stendi+="+"
        stend=stendi+stend
    return stend
#1111111111111111111111111111111111111111end
#3333333333333333333333333333333333333333start
def multiplypolynomials(aaaa):
    #aaa=aaa.replace("(","")
    #aaa=aaa.replace(")","")
    aaaa=aaaa.split("*")
    for i in range (len(aaaa)):
        aaaa[i]=reducemonomials(aaaa[i])
    l=len(aaaa)
    print(l)
    aa=aaaa[0]
    for i in range (1,l):
        print("!")
        workwiththis=aa+"*"+aaaa[i]
        aa=multiply2polynomials(workwiththis)
        
    print(aa)
    stend=""
    for i in range (l):
        stendi=""
        if aa[i]!=0:
            stendi=str(aa[i])
            if i==1:
                stendi+="x^1"
            elif i!=0:
                stendi+="x^"+str(i)
            stendi+="+"
        stend=stendi+stend
    return aa
#333333333333333333333333333333end
#222222222222222222222222222222start

def multiply2polynomials(aaa):
    print("waiting...2...")
    aaa=aaa.replace("(","")
    aaa=aaa.replace(")","")
    aaa=aaa.split("*")
    st1=reducemonomials(aaa[0])
    st2=reducemonomials(aaa[1])
    st=st1
    l=len(st)
    aa=100*[0]
    now="plus"
    now2=0
    now3=0
    sign="+"
    for i in range (l):
        if st[i]=="+":
            aa[now3]=aa[now3]+now2
            if sign=="-":
               aa[now3]=aa[now3]-2*now2

            now="beforex"
            sign="+"
            now2=0
            now3=0
        elif st[i]=="-":
            aa[now3]=aa[now3]+now2
            if sign=="-":
               aa[now3]=aa[now3]-2*now2
            now="beforex"
            sign="-"
            now2=0
            now3=0
        elif (st[i]).isdigit()==True:
            if now!="afterx":
                now2=now2*10+int(st[i])
            else :
                now3=now3*10+int(st[i])
        elif st[i]=="x" or st[i]=="*" or st[i]=="^":
            now="afterx"
        else:
            print("error")
    aa[now3]=aa[now3]+now2
    if sign=="-":
        aa[now3]=aa[now3]-2*now2

    l1=l
    aa1=aa
    #print(aa1)
    #1234567890qwertyuiop
    st=st2
    l=len(st)
    aa=100*[0]
    now="plus"
    now2=0
    now3=0
    sign="+"
    for i in range (l):
        if st[i]=="+":
            aa[now3]=aa[now3]+now2
            if sign=="-":
               aa[now3]=aa[now3]-2*now2

            now="beforex"
            sign="+"
            now2=0
            now3=0
        elif st[i]=="-":
            aa[now3]=aa[now3]+now2
            if sign=="-":
               aa[now3]=aa[now3]-2*now2
            now="beforex"
            sign="-"
            now2=0
            now3=0
        elif (st[i]).isdigit()==True:
            if now!="afterx":
                now2=now2*10+int(st[i])
            else :
                now3=now3*10+int(st[i])
        elif st[i]=="x" or st[i]=="*" or st[i]=="^":
            now="afterx"
        else:
            print("error")
    aa[now3]=aa[now3]+now2
    if sign=="-":
        aa[now3]=aa[now3]-2*now2
    l2=l
    aa2=aa
    #print(aa2)
    l=(l1+l2)
    aa=[0]*(l1+l2)
    for i in range (l1):
        for j in range (l2):
            aa[i+j]+=aa1[i]*aa2[j]
        stend=""
    #print(aa)
    
    for i in range (l):
        stendi=""
        if aa[i]!=0:
            stendi=str(aa[i])
            if i==1:
                stendi+="x^1"
            elif i!=0:
                stendi+="x^"+str(i)
            stendi+="+"
        stend=stendi+stend
    return stend

#222222222222222222222222222222end

#444444444444444444444444444444start
def solveequation(aaaaa):
    print("waiting...4...")
    aaaaa=aaaaa.replace("==", "=")
    aaaaa=aaaaa.split("=")
    if len(aaaaa)!=2 :
        return "error"
    else:
        if aaaaa[0]=="" or aaaaa[1]=="":
            return "error"
        else:
            aaaa=multiplypolynomials(aaaaa[0])
            print("binpoisk")
            aa=help(aaaa)
            notmatter=0
            for i in range (len(aa)):
                if aa[i]!=0:
                    notmatter=aa[i]
            if notmatter<0:
                for i in range (len(aa)):
                    if aa[i]!=0:
                        aa[i]=-aa[i]                
            result=int(aaaaa[1])
            print(result)
            r=1000
            l=-1000
            m=9
            while r-l>=0.000000000001:
                
                m=(r+l)/2
                resultm=0
                for i in range (len(aa)):
                    resultm+=(aa[i])*(m**i)
                if abs(resultm-result)<=0.000000000001:
                    print("lox")
                    r=m
                    l=m
                elif resultm>result:
                    r=m
                else :
                    l=m
            return m




#444444444444444444444444444444end
#555555555555555555555555555555start
def calculatethevalue(aaaa):
    print("waiting...5...")
    aaaa=aaaa.replace("_", " x=")
    aaaa=aaaa.split(" x=")
    if len(aaaa)!=2:
        return "error5"
    else:
        m=int(aaaa[1])
        result=0
        aaaa[0]=multiplypolynomials(aaaa[0])
        aa=help(aaaa[0])
        for i in range (len(aa)):
            result+=(aa[i])*m**i
        return result

#555555555555555555555555555555end
#mixmixmixmix start
def mix(equation):
    if equation.count("_")!=0 or equation.count(" x=")!=0:
        return calculatethevalue(equation)
    elif equation.count("=")>0:
        return solveequation(equation)
    elif equation.count("*")>1:
        return multiplypolynomials(equation)
    elif equation.count("*")==1:
        return multiply2polynomials(equation)
    else:
        return reducemonomials(equation)
    
#mixmixmixmix end
typ, equation=map(str, input().split( ))
if typ=="1" or typ=="reducemonomials":
    print(reducemonomials(equation))
elif typ=="2" or typ=="multiply2polynomials":
    print(multiply2polynomials(equation))
elif typ=="3" or typ=="multiplypolynomials":
    print(multiplypolynomials(equation))
elif typ=="4" or typ=="solveequation":
    print(solveequation(equation))
elif typ=="5" or typ=="calculatethevalue":
    print(calculatethevalue(equation))
elif typ=="mix":
    print(mix(equation))



    
