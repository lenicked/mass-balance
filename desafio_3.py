# Balanço de Massa: Extração liquido-liquido

def extracao_liquido_liquido(
    vazao_alimentacao=1000,                # kg/h
    fracao_acido_alimentacao=0.10,         # fração mássica
    vazao_solvente=500,                    # kg/h
    eficiencia_extracao=0.95,              # fração
    fracao_acido_extrato=0.08,             # fração mássica
    fracao_reciclo_raf=0.5                 # fração reciclada do rafinado
):
    # Entrada da alimentação
    acido_in = vazao_alimentacao * fracao_acido_alimentacao
    agua_in = vazao_alimentacao - acido_in

    # Entrada do solvente (éter)
    solvente_in = vazao_solvente

    # Entrada total
    vazao_entrada_total = vazao_alimentacao + solvente_in

    # Ácido extraído (95%)
    acido_extraido = acido_in * eficiencia_extracao

    # Cálculo do extrato (fase rica em éter)
    vazao_extrato = acido_extraido / fracao_acido_extrato
    eter_extrato = vazao_solvente
    agua_extrato = vazao_extrato - acido_extraido - eter_extrato

    # Fase aquosa (raf) contém o restante do ácido e toda a água
    acido_raf = acido_in - acido_extraido
    vazao_raf = acido_raf + (agua_in - agua_extrato)
    agua_raf = agua_in - agua_extrato 

    # Corrente de saída total
    vazao_entrada_total = vazao_extrato + vazao_raf

    # Corrente reciclada
    reciclo = fracao_reciclo_raf * vazao_raf
    nova_alimentacao = vazao_alimentacao + reciclo

    # Resultados
    print("=== RESULTADOS ===")
    print(f"Ácido acético na alimentação: {acido_in:.2f} kg/h")
    print(f"Água na alimentação: {agua_in:.2f} kg/h")
    print(f"Ácido extraído: {acido_extraido:.2f} kg/h")
    print(f"Vazão do extrato: {vazao_extrato:.2f} kg/h")
    print(f"vazão do éter no extrato: {eter_extrato:.2f} kg/h")
    print(f"Vazão do ácido no extrato: {acido_extraido:.2f} kg/h")
    print(f"Vazão de água no extrato: {agua_extrato:.2f} kg/h")
    print(f"Vazão do rafinado: {vazao_raf:.2f} kg/h")
    print(f"Vazão do ácido no rafinado: {acido_raf:.2f} kg/h")
    print(f"vazão de água no rafinado: {agua_raf:.2f} kg/h")
    print(f"Vazão reciclada: {reciclo:.2f} kg/h")
    print(f"Nova alimentação com reciclo: {nova_alimentacao:.2f} kg/h")

    return {
        'extrato': vazao_extrato,
        'raf': vazao_raf,
        'reciclo': reciclo,
        'nova_alimentacao': nova_alimentacao
    }

# Exemplo de uso com os dados do enunciado
extracao_liquido_liquido()
