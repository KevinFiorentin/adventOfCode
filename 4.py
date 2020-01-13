m = 272091
M = 815432

def f():
    
    count = 0
    for i in range(m,M+1):
        aux = str(i)
        flag1 = True
    
        vec = [0,0,0,0,0,0,0,0,0,0]
        for pos in range(0,5):
            
            vec[int(aux[pos]) ] += 1
            
            if int(aux[pos]) > int(aux[pos+1]):
                flag1 = False
                break 
         
        
        vec[ int(aux[5]) ] += 1
        
        if flag1  :
            
            print(vec)
            if 2 in vec:
                count += 1

    return count
         
if __name__ == "__main__":
    print(f())