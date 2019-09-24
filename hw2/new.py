def infixtopostfix(infixexpr):

    st=[]
    outlst=[]
    prec={}
    prec['/']=3
    prec['*']=3
    prec['+']=2
    prec['-']=2
    prec['(']=1
    oplst=['/','*','+','-']

    tokenlst=list(infixexpr)
    for token in tokenlst:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            outlst.append(token)

        elif token == '(':
            st.push(token)

        elif token == ')':
            topToken=st.pop()
            while topToken != '(':
                outlst.append(topToken)
                topToken=st.pop()

        elif token == ' ':
            continue
        else:
            while (st and (prec[st[-1]] >= prec[token])):
                #print token
                outlst.append(st.pop())
                #print outlst

            st.append(token)
            # print (st.peek())

    while st:
        opToken=st.pop()
        outlst.append(opToken)
        #print outlst
    return outlst
    #return " ".join(outlst)

print (infixtopostfix("A * B + C * D"))
