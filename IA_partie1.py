"""Nom: Kola --- Prénom: Valentin --- Matricule: 000482170"""

#fonction qui définira Move
def helpi(M):
    from random import randint
    total_p=[]
    for a in range(0,len(M)):
        total_p.append(M[a][1])
    for i in range(0,len(total_p)):
        if total_p[i]==max(total_p):
            if len(total_p)==4 and total_p[0]==total_p[1]==total_p[2]==total_p[3] :
                a=randint(0,3)
                move=M[a][0]
            elif total_p[i]==total_p[0]:
                a=randint(1,2)
                if a==1:
                    move=M[i][0]
                if a==2:
                    move=M[0][0]
            elif total_p[i]==total_p[1]:
                a=randint(1,2)
                if a==1:
                    move=M[i][0]
                if a==2:
                    move=M[1][0]
            elif total_p[i]==total_p[2]:
                a=randint(1,2)
                if a==1:
                    move=M[i][0]
                if a==2:
                    move=M[2][0]
            elif total_p[i]==total_p[3]:
                a=randint(1,2)
                if a==1:
                    move=M[i][0]
                if a==2:
                    move=M[3][0]
            else:
                move=M[i][0]
    return move
#fonction qui définira Ps
def proba(M):
    from random import randint
    total_p = []
    for a in range(0, len(M)):
        total_p.append(M[a][1])
    for i in range(0, len(total_p)):
        if total_p[i] == max(total_p):
            if total_p[i] == total_p[0]:
                a = randint(1, 2)
                if a == 1:
                    ps = M[i][1]
                if a == 2:
                    ps = M[0][1]
            elif total_p[i] == total_p[1]:
                a = randint(1, 2)
                if a == 1:
                    ps = M[i][1]
                if a == 2:
                    ps = M[1][1]
            elif total_p[i] == total_p[2]:
                a = randint(1, 2)
                if a == 1:
                    ps = M[i][1]
                if a == 2:
                    ps = M[2][1]
            elif total_p[i] == total_p[3]:
                a = randint(1, 2)
                if a == 1:
                    ps = M[i][1]
                if a == 2:
                    ps = M[3][1]
            else:
                ps = M[i][1]
    return ps
def makeMove(M,last,strategy,eps,alpha):
    from random import randint
    #M
    r=randint(0,100)/100
    if r>=eps:
# """on suit la strategy greedy"""
        move=helpi(M)
        ps=proba(M)

    elif r<eps:
        #"""Hasard"""
        a=randint(0,len(M)-1)
        move=M[a][0]
        ps = M[a][1]
    #strategy
    if strategy=='TD(0)':
        if last==None:
            None
        else:
            last[1]=(1-alpha)*last[1]+alpha*ps
    elif strategy=='Q-learning':
        if last==None:
            None
        else:
            ps1=max(M)
            last[1]=(1-alpha)*last[1]+alpha*ps1[1]
    return move
def endGame(won,history,stragery,alpha):
    if bool(won)==True:
        if stragery=='TD(0)' or stragery=='Q-learning':
            history[len(history)-1][1] = (1 - alpha) * history[len(history)-1][1] + alpha * 1
        elif stragery=='Monte Carlo':
            for i in range(0,len(history)):
                history[i-1][1]=((1-alpha**(i-1))*history[i-1][1])+((alpha**(i-1))*1)
    else:
        if stragery=='TD(0)' or stragery=='Q-learning':
            history[len(history)-1][1] = (1 - alpha) * history[len(history)-1][1] + alpha * 0
        elif stragery=='Monte Carlo':
            for j in range(0,len(history)):
                history[j-1][1]=((1-alpha**(j-1))*history[j-1][1])+((alpha**(j-1))*0)
    return None