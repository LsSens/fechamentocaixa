from datetime import date

def calculo():
    diastrabalhados = 0
    data_atual = date.today()
    try:
        with open(f"cfg/config.txt", 'r', encoding='utf-8') as dados:
            texto = dados.readlines()
            diastrampotexto = []
            for m in range(25, 27):
                diastrampotexto.append(texto[0][m])
                diasdetrabalho = int(''.join(list(diastrampotexto)))

        with open(f"cfg/{data_atual.month}-{data_atual.year}.txt", 'r', encoding='utf-8') as dados:
            texto = dados.readlines()
            metatexto = []
            for m in range(16, len(texto[33])-1):
                if texto[33][m] != ',':
                    metatexto.append(texto[33][m])
                    meta = float(''.join(list(metatexto)))

        with open(f"cfg/{data_atual.month}-{data_atual.year}.txt", 'r', encoding='utf-8') as dados:
            texto = dados.readlines()
            metaminimatexto = []
            for m in range(16, len(texto[34])-1):
                if texto[34][m] != ',':
                    metaminimatexto.append(texto[34][m])
                    metaminima = float(''.join(list(metaminimatexto)))

        with open(f"cfg/{data_atual.month}-{data_atual.year}.txt", 'r', encoding='utf-8') as dados:
            texto = dados.readlines()
            valor = []
            valortotal = 0
            for d in range(0, 32):
                for i in range(11,len(texto[d])-1):
                    if texto[d][i] != ',':
                        t = texto[d][i]
                        valor.append(t)
                    if i == len(texto[d])-2:
                        if float(''.join(list(valor))) > 0: # Valor completo, fora da lista
                            diastrabalhados += 1
                        valortotal += float(''.join(list(valor)))
                        valor = []

        texto[32] = ''
        for c in range(35,39):
            texto[c] = ''
        texto.insert(33, f'Total: R$ {valortotal:,.2f}' + '\n')

        if diasdetrabalho-diastrabalhados == 0 and meta-valortotal > 0 :
            texto.insert(37, f'Você não bateu a meta total neste mês' + '\n')
        if (meta-valortotal)/1 <= 0:
            texto.insert(37, f'Você bateu a meta total!' + '\n')
        if diasdetrabalho-diastrabalhados > 0 and (meta-valortotal)/1 > 0:
            texto.insert(37, f'Para bater a meta total, você precisa fazer por dia: R$ {(meta-valortotal)/(diasdetrabalho-diastrabalhados):,.2f}' + '\n')

        if diasdetrabalho-diastrabalhados == 0 and metaminima-valortotal > 0 :
            texto.insert(39, f'Você não bateu a meta minima neste mês')
        if (metaminima-valortotal) <= 0:
            texto.insert(39, f'Você bateu a meta mínima!')
        if diasdetrabalho-diastrabalhados > 0 and metaminima-valortotal > 0:
            texto.insert(39, f'Para bater a meta mínima, você precisa fazer por dia: R$ {(metaminima-valortotal)/(diasdetrabalho-diastrabalhados):,.2f}')

        if meta-valortotal <= 0:
            texto.insert(36, f'Vocês passou a meta total em: R$ {(meta-valortotal)*-1:,.2f}' + '\n')
        else:
            texto.insert(36, f'Faltante para meta total: R$ {meta-valortotal:,.2f}' + '\n')

        if metaminima-valortotal <= 0:
            texto.insert(38, f'Você passou a meta mínima em: R$ {(metaminima-valortotal)*-1:,.2f}'+ '\n')
        else:

            texto.insert(38, f'Faltante para meta mínima: R$ {metaminima-valortotal:,.2f}' + '\n')

        with open(f"cfg/{data_atual.month}-{data_atual.year}.txt", 'w', encoding="utf-8") as escrita:
            escrita.writelines(texto)
    except:
        return