# ============================================================
# TÍTULO: DAS RAMIFICAÇÕES À ÁLGEBRA: MODELAR SEQUÊNCIAS
# AUTORA: Celeste Silva
# DATA: Abril de 2026
# DESCRIÇÃO: Simulador pedagógico baseado na Árvore de Munari
# LICENÇA: MIT License — uso, cópia e modificação permitidos
#          com atribuição à autora (ver ficheiro LICENSE).
# DIREITOS: © 2026 Celeste Silva. 
# ============================================================

import turtle
import time
import math

# --- CONFIGURAÇÃO DO ECRÃ ---
ecra = turtle.Screen()
ecra.setup(width=1100, height=750) 
ecra.bgcolor("#FDFCF8") 
ecra.title("DAS RAMIFICAÇÕES À ÁLGEBRA: MODELAR SEQUÊNCIAS")

# Tartaruga dedicada para os cálculos manuais e termo geral
escritor_geral = turtle.Turtle()
escritor_geral.hideturtle()
escritor_geral.penup()

def limpar_area_calculos():
    """Limpa apenas a área do termo geral e cálculos manuais"""
    escritor_geral.clear()

def escrever_matematica_geral(x_base, y, base, exp, res, cor="#3E2723", tamanho=12, n_ordem=None):
    """Escreve o termo calculado manualmente com ajuste dinâmico para a esquerda"""
    res_f = f"{res:,}".replace(",", ".")
    
    # AJUSTE DINÂMICO: Quanto maior o número, mais ele recua para a esquerda
    # para garantir que o final do número se mantenha alinhado à margem
    largura_estimada = len(res_f) * 9 
    if len(res_f) > 10:
        x = x_base - (largura_estimada - 80)
    else:
        x = x_base

    escritor_geral.penup()
    escritor_geral.color(cor)
    
    if n_ordem is not None:
        escritor_geral.goto(x, y)
        escritor_geral.write("u", font=("Georgia", tamanho, "italic"))
        escritor_geral.goto(x + 15, y - 7)
        escritor_geral.write(str(n_ordem), font=("Georgia", int(tamanho*0.8), "italic"))
        escritor_geral.goto(x + 40, y)
        escritor_geral.write("=", font=("Georgia", tamanho, "bold"))
        x_calc = x + 65
    else:
        x_calc = x

    escritor_geral.goto(x_calc, y)
    escritor_geral.write(str(base), font=("Georgia", tamanho, "bold"))
    n_pixels = 18 if int(base) < 10 else 28
    escritor_geral.goto(x_calc + n_pixels, y + 10)
    escritor_geral.write(str(exp), font=("Georgia", int(tamanho*0.8), "bold"))
    escritor_geral.goto(x_calc + n_pixels + 35, y)
    escritor_geral.write(f"= {res_f}", font=("Georgia", tamanho, "bold"))

def escrever_matematica_arvore(x, y, base, exp, res, cor="#3E2723", tamanho=12, n_ordem=None):
    """Termos automáticos da árvore: Alinhamento fixo em x=360"""
    turtle.penup()
    turtle.color(cor)
    res_f = f"{res:,}".replace(",", ".")
    if n_ordem is not None:
        turtle.goto(x, y)
        turtle.write("u", font=("Georgia", tamanho, "italic"))
        turtle.goto(x + 15, y - 7)
        turtle.write(str(n_ordem), font=("Georgia", int(tamanho*0.8), "italic"))
        turtle.goto(x + 40, y)
        turtle.write("=", font=("Georgia", tamanho, "bold"))
        x_calc = x + 65
    else:
        x_calc = x
    turtle.goto(x_calc, y)
    turtle.write(str(base), font=("Georgia", tamanho, "bold"))
    n_pixels = 18 if int(base) < 10 else 28
    turtle.goto(x_calc + n_pixels, y + 10)
    turtle.write(str(exp), font=("Georgia", int(tamanho*0.8), "bold"))
    turtle.goto(x_calc + n_pixels + 35, y)
    turtle.write(f"= {res_f}", font=("Georgia", tamanho, "bold"))

def escrever_termo_geral_final(base):
    """Escreve o Termo Geral alinhado fixamente à coluna da árvore (x=360)"""
    x_f = 360 
    y_f = 320 
    escritor_geral.penup()
    escritor_geral.color("#558B2F") 
    escritor_geral.goto(x_f, y_f)
    escritor_geral.write("u", font=("Georgia", 18, "italic"))
    escritor_geral.goto(x_f + 18, y_f - 8)
    escritor_geral.write("n", font=("Georgia", 12, "italic"))
    escritor_geral.goto(x_f + 45, y_f)
    escritor_geral.write("=", font=("Georgia", 18, "bold"))
    escritor_geral.goto(x_f + 75, y_f)
    escritor_geral.write(str(base), font=("Georgia", 18, "bold"))
    rec_exp = 25 if int(base) < 10 else 35
    escritor_geral.goto(x_f + 75 + rec_exp, y_f + 15)
    escritor_geral.write("n-1", font=("Georgia", 12, "bold"))

def escrever_assinatura():
    turtle.penup()
    turtle.color("#9E9E9E") 
    y_rodape = -330
    x_ref = -520
    turtle.goto(x_ref, y_rodape)
    # Alteração: Aplicado "bold italic" para dar relevo ao livro e autor
    turtle.write("Inspirado em 'Drawing a Tree' de Bruno Munari", font=("Georgia", 9, "bold italic"))
    x_autoria = 220 
    turtle.goto(x_autoria, y_rodape)
    # Alteração: Mantido "bold" para dar relevo ao nome da autora Celeste Silva
    turtle.write("© 2026 Celeste Silva | Todos os direitos reservados", font=("Georgia", 9, "bold"))

def aguardar_clique():
    clicou = [False]
    def detetar_clique(x, y): clicou[0] = True
    ecra.onclick(detetar_clique)
    try:
        while not clicou[0]:
            ecra.update()
            time.sleep(0.1)
    except:
        pass
    ecra.onclick(None)

def executar_simulador():
    base_atual = 2
    arvore_desenhada = False
    correndo = True 
    
    while correndo:
        try:
            if arvore_desenhada:
                escolha = ecra.textinput("Menu", "'A' - Nova Árvore | 'T' - Calcular Termo (un) | 'S' - Sair")
                if not escolha or escolha.lower() == 's': 
                    correndo = False
                    continue
                if escolha.lower() == 't':
                    n_al = ecra.numinput("Cálculo do Termo Geral", 
                                       "Qual é a ordem (n) do termo que desejas calcular?", 
                                       default=10, minval=1)
                    if n_al:
                        limpar_area_calculos() 
                        escrever_termo_geral_final(base_atual) 
                        
                        n_al = int(n_al)
                        escrever_matematica_geral(360, 280, base_atual, n_al-1, base_atual**(n_al-1), n_ordem=n_al)
                        ecra.update()
                    continue
                else:
                    turtle.clearscreen()
                    escritor_geral.clear() 
                    ecra.bgcolor("#FDFCF8")
                    turtle.hideturtle()
                    turtle.tracer(0, 0)
                    arvore_desenhada = False

            escrever_assinatura()
            
            # Base máxima limitada a 4
            res_b = ecra.numinput("Parâmetros", "Base (2 a 4):", default=2, minval=2, maxval=4)
            if res_b is None: break
            
            base_atual = int(res_b)
            
            # Limites dinâmicos para n de acordo com a base
            max_n = 8 if base_atual == 2 else 5
            res_n = ecra.numinput("Parâmetros", f"Níveis (máx {max_n} para base {base_atual}):", 
                                 default=5, minval=1, maxval=max_n)
            if res_n is None: break
            
            num_niveis = int(res_n)
            fator_g = 1 / math.sqrt(base_atual)
            g_ini = 2.5 / (fator_g ** (num_niveis - 1))
            niveis = [[((0, -280), 90, 115, g_ini)]]
            
            for n in range(num_niveis):
                escrever_matematica_arvore(360, -250 + (n * 60), base_atual, n, base_atual**n, n_ordem=n+1)
                proximos = []
                angulo_total = 100 * (0.8 ** n) 
                for pos, ang, tam, gross in niveis[n]:
                    turtle.penup(); turtle.goto(pos); turtle.setheading(ang); turtle.pendown()
                    turtle.pensize(max(1, gross)); turtle.color("#3E2723"); turtle.forward(tam)
                    if n < num_niveis - 1:
                        esp = angulo_total / (base_atual - 1)
                        for i in range(base_atual):
                            novo_ang = (ang + angulo_total/2) - (i * esp)
                            proximos.append((turtle.position(), novo_ang, tam * 0.72, gross * fator_g))
                    else:
                        turtle.penup(); turtle.color("#558B2F"); turtle.dot(gross * 2 + 6)
                niveis.append(proximos)
                ecra.update()
                
                if n < num_niveis - 1:
                    turtle.penup(); turtle.goto(-150, -330); turtle.color("#3E2723")
                    turtle.write(f"CLICA PARA O NÍVEL {n+2}", font=("Georgia", 10, "bold"))
                    aguardar_clique()
                    turtle.undo()

            arvore_desenhada = True
            turtle.penup(); turtle.goto(-150, -330); turtle.color("#558B2F")
            turtle.write("CLICA PARA O MENU", font=("Georgia", 11, "bold"))
            aguardar_clique()
            turtle.undo()
            
        except:
            correndo = False

    try:
        turtle.bye()
    except:
        pass

if __name__ == "__main__":
    try:
        turtle.hideturtle(); turtle.speed(0); turtle.tracer(0, 0)
        executar_simulador()
    except:
        pass
