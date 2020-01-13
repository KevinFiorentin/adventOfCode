grid1 = list()
grid2 = []





def f(grid,flag):
    pos_x = 0
    pos_y = 0
    for wires in grid:
        mov = int(wires[1:])
        if wires[0] == 'R': 
            vec_mov = (1, 0)
        if wires[0] == 'L': 
            vec_mov = (-1, 0)
        if wires[0] == 'U': 
            vec_mov = (0, 1)
        if wires[0] == 'D': 
            vec_mov = (0, -1)


        for _ in range(mov):
            pos_x += vec_mov[0]
            pos_y += vec_mov[1]
    
            if (pos_x, pos_y) not in dic:
                dic[(pos_x, pos_y)] = str(flag)
            elif dic[(pos_x, pos_y)] != str(flag):
                dic[(pos_x,pos_y)] = 'X'

def f2(grid):
    pos_x = 0
    pos_y = 0
    cont = 0
    for wires in grid:
        mov = int(wires[1:])
        if wires[0] == 'R': 
            vec_mov = (1, 0)
        if wires[0] == 'L': 
            vec_mov = (-1, 0)
        if wires[0] == 'U': 
            vec_mov = (0, 1)
        if wires[0] == 'D': 
            vec_mov = (0, -1)
        

        for _ in range(mov):
            pos_x += vec_mov[0]
            pos_y += vec_mov[1]
            cont += 1
            if dic[(pos_x, pos_y)] == 'X':
                dic[(pos_x,pos_y)] = 'X'
                if (pos_x,pos_y) in vec :
                    vec[(pos_x,pos_y)] += cont
                else :
                    vec[(pos_x,pos_y)] = cont


def f3(vec):
    menor = 100000000000000000
    for key, value in vec:
        if vec[(key,value)] < menor:
            menor = vec[(key,value)]
            return vec[(key,value)]


if __name__ == "__main__":
    grid1 = input().split(',')
    grid2 = input().split(',')
    dic = {}
    vec = {}
    f(grid1,0)
    f(grid2,1)

    f2(grid1)
    f2(grid2)

    sla = {k: v for k, v in sorted(vec.items(), key=lambda item: item[1])}
    print(sla)
    
    print(f3(vec))


    #print(value)

    '''
   
    p_x = 0
    p_y = 0
    keys = dic.keys()
    
    for pos in keys:
        if dic[pos] == 'X':
            if  abs(pos[0]) + abs(pos[1]) < menor:
                menor =  abs(pos[0]) + abs(pos[1])
                p_x = pos[0]
                p_y = pos[1]
    
    print(menor)
    '''


     




        