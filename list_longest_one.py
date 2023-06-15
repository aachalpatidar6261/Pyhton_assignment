def list_word(my):
    c = 0
    for i in my:
        if len(i)>=c:
            tem = i
            c = len(i)
            
    print("c : ",c,", i:",tem)

a = ["hello","h","llkk","tyuoopkdkdh"]
list_word(a)