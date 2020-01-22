import sqlparse
import csv
import sys

metaval={}
def condi(order,where,from1,C1):
    #print(order)
    if(C1==[]):
   
        C=[]
        z=""
        D=[]
        attribu=from1[0].split(',')
        #print(len(z))
        if(len(attribu)==1):
            #z=from1[0]
            z=attribu[0]
            z1=z
            file_desc = open (z+".csv" ,'r' )
            cr = csv.reader(file_desc)
            z=metaval[z]
            for i in cr:
                #print(i)
                C.append(i)
            count=0
            for i in range(0,len(z)):
                if(z[i]==where[0]):
                    D.append(count)
                    break;
               
                count=count+1
            D.append(where[1])
            count=0
            flag2=0
            for i in range(0,len(z)):
                if(z[i]==where[2]):
                    D.append(count)
                    flag2=1
                    break
                count=count+1
            if(flag2==0):
                D.append(where[2])
            if(len(where)==7):
                D.append(where[3])
                count=0
                for i in range(0,len(z)):
                    if(z[i]==where[4]):
                        D.append(count)
                        break; 
                    count=count+1
                D.append(where[5])
                count=0
                flag2=0
                for i in range(0,len(z)):
                    if(z[i]==where[6]):
                        D.append(count)
                        flag2=1
                        break
                    count=count+1
                if(flag2==0):
                    D.append(where[6])
                s1=""
                s2=""
                for i in range(0,len(C)):
                    s2=s2+C[i][D[0]]+" "+where[1]+" "+D[2]
                    flg=eval(s2)
                    if(len(where)==7):
                        s1=s1+C[i][D[4]]+" "+D[5]+" "+D[6]
                        #print(s1)
                        flg1=eval(s1)
                        if(where[3]=="and"):
                            if(flg==False or flg1==False):
                                s1=""
                                continue
                        if(where[3]=="or"):
                            if(flg==False and flg1==False):
                                s1=""
                                continue
                    else:
                        if(flg==False):
                            s2=""
                            continue
                    for j in range(0,len(order)):
                        print(C[i][order[j]],"    ",end="\t")
                    print("")
    else:
        D=[]
        count=0
        count1=3
        z=from1[0]
        #print(from1)
        #print(z)
        z=metaval[z]
        z2=from1[1]
        z2=metaval[z2]
        fg=0
        fg1=0
        for i in range(0,len(z)):
            if(z[i]==where[0]):
                fg=1
                D.append(count)
                break;
           
            count=count+1
        count=0
        if(fg==0):
            for i in range(0,len(z2)):
                if(z[i]==where[0]):
                    D.append(count1)
                    break;
            count1=count1+1

        D.append(where[1])
        count=0
        flag2=0
        fg=0
        for i in range(0,len(z)):
            if(z[i]==where[2]):
                D.append(count)
                fg=1
                flag2=1
                break
            count=count+1
        count=0
        if(fg==0):
            count1=3
            for i in range(0,len(z2)):
                if(z2[i]==where[2]):
                    D.append(count1)
                    flag2=1
                count1=count1+1
        if(flag2==0):
            D.append(where[2])
        if(len(where)==7):
            fg=0
            D.append(where[3])
            count=0
            for i in range(0,len(z)):
                if(z[i]==where[4]):
                    fg=1
                    D.append(count)
                    break; 
                count=count+1
            count=0
            if(fg==0):
                count1=3
                for i in range(0,len(z2)):
                    if(z2[i]==where[4]):
                
                        D.append(count1)
                        break;
                count1=count1+1

            D.append(where[5])
            count=0
            flag2=0
            fg=0
            for i in range(0,len(z)):
                if(z[i]==where[6]):
                    D.append(count)
                    fg=1
                    flag2=1
                    break
                count=count+1
           
            if(fg==0):
                count1=3
               # print(z2)
                for i in range(0,len(z2)):
                    if(z2[i]==where[6]):
                        #print("hgjjhg")
                        D.append(count1)
                        flag2=1
                    count1=count1+1
            if(flag2==0):
                D.append(where[6])
        s2=""
        s1="" 
        #print("hello")
        #if(where==[2]!=)
        #print(D)
        for i in range(0,len(C1)):
            s1=""
            s2=""
            #print(where[2])
            #print(D[2])
            if(where[2]==D[2]):
                s2=s2+C1[i][D[0]]+" "+D[1]+" "+str(D[2])
            else:
               # print(s2)
                s2=s2+C1[i][D[0]]+" "+D[1]+" "+C1[i][D[2]]
            flg=eval(s2)
           # print(s2)
            if(len(where)==7):
                if(where[6]==D[6]):
                    s1=s1+C1[i][D[4]]+" "+D[5]+" "+str(D[6])
                else:
                    #print("hello")
                    s1=s1+C1[i][D[4]]+" "+D[5]+" "+C1[i][D[6]]
                #print(s1)
                flg1=eval(s1)
                if(where[3]=="and"):
                    if(flg==False or flg1==False):
                        
                        continue
                if(where[3]=="or"):
                    if(flg==False and flg1==False):
                       
                        continue
            else:
                if(flg==False):
                    
                    continue
            for j in range(0,len(order)):
                print(C1[i][order[j]],"",end="\t")
            print("")


def distinct1(select,from1):
    temp=select[9]
    #quer=from1[]
    temp5={}
    z=""
    z=from1[0]
    attrib=(metaval[z])
    file_desc = open (z+".csv" ,'r' )
    order=[]
       #cr = csv.reader(file_desc)
    cr=file_desc.readlines()
    #print(cr)
    c=0
    for j in attrib:
        #print(j)
        if(temp==j):
            break;
        c=c+1
    for i in range(0,len(cr)):
        cr[i]=cr[i].rstrip('\n')
        row=cr[i].split(',')
        temp5[row[c]]=0
    print(str(z)+"."+attrib[c])
    for key in temp5:
        print(key)

def aggquery(select,from1):
        #for()
    temp2=select[4:10]
    temp='A'
    if(temp2=="table1" or temp2=="table2"):
        temp=select[11]
    else:
        temp=select[4]

    

    aggq=select[0:3]
   # print(aggq)
    z=""
    z=from1[0]
    #print(metaval[z])
    attrib=(metaval[z])
    file_desc = open (z+".csv" ,'r' )
    order=[]
       #cr = csv.reader(file_desc)
    cr=file_desc.readlines()
    #print(cr)
    c=0
    for j in attrib:
        #print(j)
        if(temp==j):
            break;
        c=c+1
    #INT_MAX=sys.maxsize 
    if(aggq=="max"):
        z1=-sys.maxsize-1 
        z1=int(z1)
        for i in range(0,len(cr)):
            cr[i]=cr[i].rstrip('\n')
            row=cr[i].split(',')
            m=int(row[c])
            if(m>z1):
                z1=m
    if(aggq=="min"):
        z1=100000
        
        for i in range(0,len(cr)):
            cr[i]=cr[i].rstrip('\n')
            row=cr[i].split(',')
            m=int(row[c])
            if(m<z1):
                z1=m

    if(aggq=="sum"):
        z1=0
        for i in range(0,len(cr)):
            cr[i]=cr[i].rstrip('\n')
            row=cr[i].split(',')
            m=int(row[c])
            z1=z1+m
    if(aggq=="avg"):
        z1=0
        for i in range(0,len(cr)):
            cr[i]=cr[i].rstrip('\n')
            row=cr[i].split(',')
            m=int(row[c])
            z1=z1+m
        z1=z1/(len(cr))

           
                #print()
    print(z1," ",end="")

#def check
def cart_prod(selec,attribu,where):
    rows, cols = (1000, 1000) 
    arr = [[0]*cols]*rows 
    print(arr[0][0])
   
    if(selec[0]=='*'):
        z=""
        z=attribu[0]
        z1=""
        z1=attribu[1]
        file_desc = open (z+".csv" ,'r' )
            #file_desc1 = open (z1+".csv" ,'r' )
            #order=[]
               #cr = csv.reader(file_desc)
        temp=selec[0].split(',')
        cr = csv.reader(file_desc)
        #cr = csv.reader(file_desc)

        file_desc1 = open (z1+".csv" ,'r' )
        cr1 = csv.reader(file_desc1)
        A=[]
        B=[]
        for row1 in cr:
            A.append(row1)
        for row2 in cr1:
            B.append(row2)
        C=[]
        order=[]
        for i in range(len(A)):
            for j in range(len(B)):
                X=[]
                X.extend(A[i])
                X.extend(B[j])
                C.append(X)
        AB1=metaval[z]
        AB2=metaval[z1]

        for i in range(0,len(AB1)):
            print(z+"."+AB1[i],end="\t")
        for i in range(0,len(AB2)):
            print(z1+"."+AB2[i],end="\t")
        print("")
        if(where==[]):
            for i in range(0,len(C)):
                for j in range(0,len(C[0])):
                    print(C[i][j],"      ",end="\t")
                print("")
        else:
            
            D=[]
            count=0
            count1=3
            z=attribu[0]
            z=metaval[z]
            z2=attribu[1]
            z2=metaval[z2]
            fg=0
            fg1=0
            for i in range(0,len(z)):
                if(z[i]==where[0]):
                    fg=1
                    D.append(count)
                    break;
               
                count=count+1
            count=0
            if(fg==0):
                for i in range(0,len(z2)):
                    if(z[i]==where[0]):
                        D.append(count1)
                        break;
                count1=count1+1

            D.append(where[1])
            count=0
            flag2=0
            fg=0
            for i in range(0,len(z)):
                if(z[i]==where[2]):
                    D.append(count)
                    fg=1
                    flag2=1
                    break
                count=count+1
            count=0
            if(fg==0):
                count1=0
                for i in range(0,len(z2)):
                    if(z2[i]==where[2]):
                        D.append(count)
                        flag2=1
                    count1=count1+1
            if(flag2==0):
                D.append(where[2])
            if(len(where)==7):
                fg=0
                D.append(where[3])
                count=0
                for i in range(0,len(z)):
                    if(z[i]==where[4]):
                        fg=1
                        D.append(count)
                        break; 
                    count=count+1
                count=0
                if(fg==0):
                    count1=3
                    for i in range(0,len(z2)):
                        if(z2[i]==where[4]):
                    
                            D.append(count1)
                            break;
                    count1=count1+1

                D.append(where[5])
                count=0
                flag2=0
                fg=0
                for i in range(0,len(z)):
                    if(z[i]==where[6]):
                        D.append(count)
                        fg=1
                        flag2=1
                        break
                    count=count+1
               
                if(fg==0):
                    count1=3
                    print(z2)
                    for i in range(0,len(z2)):
                        if(z2[i]==where[6]):
                            #print("hgjjhg")
                            D.append(count1)
                            flag2=1
                        count1=count1+1
                if(flag2==0):
                    D.append(where[6])
            s2=""
            s1="" 
            #print("hello")
            #if(where==[2]!=)
            
            for i in range(0,len(C)):
                s1=""
                s2=""
               # print("hello")
                if(where[2]==D[2]):
                    s2=s2+C[i][D[0]]+" "+D[1]+" "+str(D[2])
                else:
                    s2=s2+C[i][D[0]]+" "+D[1]+" "+C[i][D[2]]
                flg=eval(s2)
                #print(s2)
                if(len(where)==7):
                    if(where[6]==D[6]):
                        s1=s1+C[i][D[4]]+" "+D[5]+" "+str(D[6])
                    else:
                        #print("hello")
                        s1=s1+C[i][D[4]]+" "+D[5]+" "+C[i][D[6]]
                    #print(s1)
                    flg1=eval(s1)
                    if(where[3]=="and"):
                        if(flg==False or flg1==False):
                            
                            continue
                    if(where[3]=="or"):
                        if(flg==False and flg1==False):
                           
                            continue
                else:
                    if(flg==False):
                        
                        continue
                for j in range(0,len(C[0])):
                    print(C[i][j],"     ",end="\t")
                print("")
                
            #condi2()
        return
        z=""
        z=attribu[0]
        z1=""
        z1=attribu[1]
        #print(metaval[z])
        attrib=(metaval[z])
        attrib1=(metaval[z1])
        file_desc = open (z1+".csv" ,'r' )
        #file_desc1 = open (z1+".csv" ,'r' )
        #order=[]
           #cr = csv.reader(file_desc)
        cr = csv.reader(file_desc)
        #cr1 = csv.reader(file_desc1)
        print(cr)
        stra=""
       
        for row2 in cr:
            stra=""
            for i in row2:
                stra+=str(i)+"\t"
            #print(stra)
               # temp1=str(i)
               # print("HELLO")
            col1=str(i)
            col2=""
            if(where==[]):

               # for i1 in range(0,len(col1)):
                    #if()
                file_desc1 = open (z+".csv" ,'r' )
                cr1 = csv.reader(file_desc1)
                for row in cr1:
                    print(stra,end="")
                    for j in range(0,len(row)):
                        print(row[j],end="\t")
                    print()


            #cr1=0  
    else:
        z=""
        z=attribu[0]
        z1=""
        z1=attribu[1]
        #print(metaval[z])
        attrib=(metaval[z])
        attrib1=(metaval[z1])
        file_desc = open (z+".csv" ,'r' )
        #file_desc1 = open (z1+".csv" ,'r' )
        #order=[]
           #cr = csv.reader(file_desc)
        temp=selec[0].split(',')
        cr = csv.reader(file_desc)

        file_desc1 = open (z1+".csv" ,'r' )
        cr1 = csv.reader(file_desc1)
        A=[]
        B=[]
        for row1 in cr:
            A.append(row1)
        for row2 in cr1:
            B.append(row2)
        C=[]
        order=[]
        for i in range(len(A)):
            for j in range(len(B)):
                X=[]
                X.extend(A[i])
                X.extend(B[j])
                C.append(X)
        flag=-1
        #print(temp)
        for i in temp:
            #print(i)
            c=-1
            for j in attrib:
                tem=i.split('.')
                #print(tem)
                if(tem[0]==z):
                   # print("amrit")
                    i=tem[1]
                if(tem[0]==z1):
                    continue
                c=c+1
                #print(j)
                if(i==j):
                    flag=0
                    print("HELLOMATCH")
                    break;
                #c=c+1
            if(flag==-1):
                c=-1
            if(c!=-1): 
                flag=-1   
                order.append(c)
        flag=-1
        #print(attrib1)
       # print(temp)
        for i in temp:
            c=2
            for j in attrib1:
                tem=i.split('.')
                if(tem[0]==z1):
                    i=tem[1]
                if(tem[0]==z):
                    continue
                c=c+1
                if(i==j):
                    flag=0
                    print("HELLO")
                    break;
            if(flag==-1):
                c=2
            if(c!=2):
                flag=-1
                print("asd")
                order.append(c)
        print(order)
        #print
        # for i in range(0,len(C)):
        #     for j in range(0,len(C[0])):
        #         print(C[i][j],end=" ")
        #     print("")
        for i in range(0,len(temp)):
            print(temp[i]," ",end="\t")
        print("")
        if(where==[]):
            for i in range(0,len(C)):
                for j in range(0,len(order)):
                    #print(i," ",order[j])
                    print(C[i][order[j]]," ",end="\t")
                print("")  
        else:
            #return
            condi(order,where,attribu,C)  


        #print(C[0][3])
       # for i in range(0,100):
            #for j in range(0,5):
                #print(arr[i][j],"\t",end="")
           # print()
                    #print(row[j],end="\t")
                #print()








        
def runquery(arg):
    temp5=[]
    select=[]
    from1=[]
    where=[]
    arg = sqlparse.split(str(arg))
    for i in arg:
        q_break = sqlparse.parse(i)
        q_tokens = q_break[0].tokens
        l = sqlparse.sql.IdentifierList(q_tokens).get_identifiers()
        #print(l)
        #temp=q_tokens.split()
        f=1
        f1=1
        f2=1
        for i in l:
            t13=str(i).split(" ")
            #print(t13)
            if(t13[0]=="where"):
                for j in range(1,len(t13)):
                    where.append(t13[j])
            if(str(i)==' '):
              continue;
            if(str(i)=="select"):
                #print("kwer")
                f=0
                continue;
            if(str(i)=="from"):
                f=1
                f1=0
                continue;
            if(f==0):
                select.append(str(i))
           
          
           
            if(f1==0):
                from1.append(str(i))

   # print(select[1])
   
    if(where==[]):

        if(select[0]=='*'):
            z=""
            attribu=from1[0].split(',')
            #print(len(z))
            if(len(attribu)==1):
                z=from1[0]
                file_desc = open (z+".csv" ,'r' )
                cr = csv.reader(file_desc)

                for i in cr:
                    print(i)
            else:
                cart_prod(select[0],attribu,where)
                return

        else:
            flag1=0
            temp=select[0].split(',')
            temp9=from1[0].split(',')
            if(len(temp9)>1):
                C=[]
                cart_prod(select,temp9,C)
            else:

                print("BYEE")
                #print(temp[0][0:3])
                k=len(temp)
                #print(k)
                c9=0
                while(k):
                    if(temp[0][0:3]=="max" or temp[0][0:3]=="min" or temp[0][0:3]=="sum" or temp[0][0:3]=="avg"):
                        aggquery(temp[c9],from1)
                        c9=c9+1
                        flag1=1
                           # return
                    else:
                        break

                    k=k-1
                if(temp[0][0:8]=="distinct"):
                    distinct1(temp[0],from1)
                    return
                if(flag1==1):
                    return    
                #print(temp[0])
                #for()
                z=""
                z=from1[0]
                #print(metaval[z])
                attrib=(metaval[z])
                file_desc = open (z+".csv" ,'r' )
                order=[]
               #cr = csv.reader(file_desc)
                cr=file_desc.readlines()
                #print(cr)
                #for i in range(0,len(cr)):
        		 # cr[i]=cr[i].rstrip('\n')
        		  #row=cr[i].split(',')
        		  #print(row[0])
                for i in temp:
                    #print(i)
                    c=0
                    for j in attrib:
                        #tem=i.split('.')

                        #print(j)
                        if(i==j):
                            break;
                        c=c+1
                    order.append(c)
                for i in  range(0,len(order)):
                    print(z+"."+attrib[i]," ",end="\t")
                print("")
                for i in range(0,len(cr)):
                    cr[i]=cr[i].rstrip('\n')
                    row=cr[i].split(',')
                    for j in range(0,len(order)):
                        print(row[order[j]],"     ",end="\t")
                        #print()
                    print("")

    else:
       
        if(select[0]=='*'):
            C=[]
            z=""
            D=[]
            attribu=from1[0].split(',')
            #print(len(z))
            if(len(attribu)==1):
                #z=from1[0]
                z=attribu[0]
                z1=z
                file_desc = open (z+".csv" ,'r' )
                cr = csv.reader(file_desc)
                z=metaval[z]
                for i in cr:
                    print(i)
                    C.append(i)
                count=0
                for i in range(0,len(z)):
                    if(z[i]==where[0]):
                        D.append(count)
                        break;
                   
                    count=count+1
                D.append(where[1])
                count=0
                flag2=0
                for i in range(0,len(z)):
                    if(z[i]==where[2]):
                        D.append(count)
                        flag2=1
                        break
                    count=count+1
                if(flag2==0):
                    D.append(where[2])
                if(len(where)==7):
                    D.append(where[3])
                    count=0
                    for i in range(0,len(z)):
                        if(z[i]==where[4]):
                            D.append(count)
                            break; 
                        count=count+1
                    D.append(where[5])
                    count=0
                    flag2=0
                    for i in range(0,len(z)):
                        if(z[i]==where[6]):
                            D.append(count)
                            flag2=1
                            break
                        count=count+1
                    if(flag2==0):
                        D.append(where[6])
               
                s2=""
                s1="" 
                #print("hello")
                #print(D)
                for j in range(0,len(z)):
                    print(z1+"."+z[j],"",end="\t")
                print("")
                for i in range(0,len(C)):
                   

                    s2=s2+C[i][D[0]]+" "+where[1]+" "+D[2]
                    flg=eval(s2)
                    if(len(where)==7):
                        s1=s1+C[i][D[4]]+" "+D[5]+" "+D[6]
                        #print(s1)
                        flg1=eval(s1)
                        if(where[3]=="and"):
                            if(flg==False or flg1==False):
                                s1=""
                                continue
                        if(where[3]=="or"):
                            if(flg==False and flg1==False):
                                s1=""
                                continue
                    else:
                        if(flg==False):
                            s2=""
                            continue
                    for j in range(0,len(C[0])):
                        print(C[i][j],"    ",end="\t")
                    print("")
                    s1=""
                    s2=""



                #print(C[0][0])

            else:
                cart_prod(select[0],attribu,where)
                return

           # print(i)
        else:
            flag1=0
            temp=select[0].split(',')
            temp9=from1[0].split(',')
            if(len(temp9)>1):
                cart_prod(select,temp9,where)
            else:

                print("BYEE")
                print(temp[0][0:3])
                k=len(temp)
                #print(k)
                c9=0
                while(k):
                    if(temp[0][0:3]=="max" or temp[0][0:3]=="min" or temp[0][0:3]=="sum" or temp[0][0:3]=="avg"):
                        aggquery(temp[c9],from1)
                        c9=c9+1
                        flag1=1
                           # return
                    else:
                        break

                    k=k-1
                if(temp[0][0:8]=="distinct"):
                    distinct1(temp[0],from1)
                    return
                if(flag1==1):
                    return    
                #print(temp[0])
                #for()
                z=""
                z=from1[0]
                #print(metaval[z])
                attrib=(metaval[z])
                file_desc = open (z+".csv" ,'r' )
                order=[]
               #cr = csv.reader(file_desc)
                cr=file_desc.readlines()
                #print(cr)
                #for i in range(0,len(cr)):
                 # cr[i]=cr[i].rstrip('\n')
                  #row=cr[i].split(',')
                  #print(row[0])
                for i in temp:
                    #print(i)
                    c=0
                    for j in attrib:
                        #tem=i.split('.')

                        print(j)
                        if(i==j):
                            break;
                        c=c+1
                    order.append(c)
                #condi(order,where,from1)
                for i in  range(0,len(order)):
                    print(z+"."+attrib[i]," ",end="\t")
                print("")
                condi(order,where,from1)
               

fd = open ('metadata.txt','r')

name="" 
name5=""      
flag5 = False 

for row in fd:

    row = row.strip()

            
    if(flag5 == True):
        name = str(row)
        metaval[name]=[]
        flag5 = False

            
    if(str(row) == '<begin_table>'):
        flag5 = True

            
    if(str(row) != '<begin_table>' and str(row) != '<end_table>' and str(row) != name):
        metaval[name].append(str(row))
#print(metaval["table1"])
runquery(sys.argv[1])
