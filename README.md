# Projeto – Carga e Descarga de um Capacitor

Este projeto demonstra o comportamento de um circuito RC (Resistor–Capacitor) durante os processos de **carga** e **descarga**.

## TinkerCad

A imagem mostra a montagem do circuito incluindo sua operação completa e do **slide switch**.

![Circuito](circuito.png)

O link a seguir mostra o funcionamento do circuito no **Tinkercad**.

🔗 [Veja à simulação no Tinkercad](https://www.tinkercad.com/things/l4P0aHsahoc/editel?returnTo=%2Fdashboard%2Fdesigns%2Fcircuits)



## Gráficos Gerados

A partir dos dados obtidos experimentalmente (`dados_carga.txt`), foram gerados os seguintes gráficos:

1. **Descarga no Resistor**
   ![Descarga no Resistor](descarga_resistor.png)

2. **Carga no Capacitor**
   ![Carga no Capacitor](carga_capacitor.png)

3. **Comparação entre Resistor e Capacitor**
   ![Comparação RC](comparacao_RC.png)


## Código em Python

O processamento dos dados e a geração dos gráficos foram realizados com o script:

📁 [`processar_dados.py`](processar_dados.py)



## Resultados
Os resultados mostram o comportamento esperado do circuito RC:
- A **tensão no capacitor** aumenta exponencialmente durante a carga e decresce durante a descarga;
- A **tensão no resistor** apresenta comportamento inverso, validando o modelo teórico do circuito.