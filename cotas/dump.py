for a in chunks:
    index = chunks.index(a)
    obj = Cotas()
    obj.credito =  int(re.sub('\D','',a[0][0]))/100
    obj.entrada =   (int(re.sub('\D','',a[1][0]))/100) + (obj.credito * 0.07)
    obj.carta =  a[3][0]
    obj.vencimento =  int(a[4][0][0:2])
    # PASSAR ISSO AQUI PRA INT!!!
    parcelas_str =  a[2][0]
    parcelas_list = parcelas_str.rsplit(" ")
    new_list = []
    for b in parcelas_list:
        c = re.sub('\D','',b)
        if c != "":
            new_list.append(int(c))

    for d in new_list:
        i = new_list.index(d)

        if i % 2 != 0:
            new_list[i] = d / 100

        parcelas = [new_list[x:x+2] for x in range(0, len(new_list), 2)]
        parcelaobj = Parcelas()
        for x in parcelas:
            parcelaobj.qt_parcelas = x[0]
            parcelaobj.valor_parcelas = x[1]
            print(parcelaobj)
        print("-"*30)
    print("="*40)

        


"""    for j in obj_list:
        print("-------------------")
        print("Administradora: ", j.carta)
        print("Crédito: ",j.credito)
        print("Entrada: ",j.entrada)
        print("Parcelas: ")
        for b in j.parcelas:
            print(b)
        print("Segmento:", j.segmento)
        print("Vencimento: ",j.vencimento)
        print("Código: ", j.codigo)"""