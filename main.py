def satisfativel(F):
    simbolos = set(abs(literal) for clausula in F for literal in clausula)
    valoracao = {}
    satisfativel, valoração_satisfativel = dpll(F, valoracao)
    if satisfativel:
        return "Satisfatível", valoração_satisfativel
    else:
        return "Insatisfatível", None

def dpll(clausulas, valoracao):
    if all(len(c) == 0 for c in clausulas):
        return True, valoracao.copy()
    if any(len(c) == 0 for c in clausulas):
        return False, {}
    
    for clausula in clausulas:
        for literal in clausula:
            if -literal not in valoracao and literal not in valoracao:
                break
        else:
            continue
        break
    else:
        literal = None

    if literal is not None:
        valoracao[literal] = True
        clausulas = [c for c in clausulas if literal not in c]
        return dpll(clausulas, valoracao)

    for clausula in clausulas:
        for literal in clausula:
            if literal not in valoracao:
                valoracao[literal] = True
                clausulas = [c for c in clausulas if -literal not in c]
                resultado, valoração_satisfativel = dpll(clausulas, valoracao)
                if resultado:
                    return True, valoração_satisfativel
                del valoracao[literal]
                break

    for clausula in clausulas:
        for literal in clausula:
            if -literal not in valoracao:
                valoracao[-literal] = False
                clausulas = [c for c in clausulas if literal not in c]
                resultado, valoração_satisfativel = dpll(clausulas, valoracao)
                if resultado:
                    return True, valoração_satisfativel
                del valoracao[-literal]
                break

    return False, {}

def ler(nome_arquivo):
    clausulas = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            if linha.startswith('c'):
                continue  
            elif linha.startswith('p'):
                continue  
            else:
                clausula = [int(x) for x in linha.split() if x != '0' and x != ''] 
                if clausula:
                    clausulas.append(clausula)
    return clausulas


nome_arquivo = "arquivo.cnf"


clausulas_cnf = ler(nome_arquivo)


resultado, valoração_satisfativel = satisfativel(clausulas_cnf)
if resultado:
    print("Satisfatível")
    print("Valoração que satisfaz a fórmula CNF:", valoração_satisfativel)
else:
    print("Insatisfatível") 
