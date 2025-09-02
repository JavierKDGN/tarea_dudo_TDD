# from src.game.ContadorPintas import ContadorPintas
# from src.game.Dado import Dado

# def test_contar_un_dado():
#     dado = Dado()
#     dado.setValue(3)
#     assert ContadorPintas.contar([dado],3) == 1
# def test_contar_sin_dados():
#     assert ContadorPintas.contar([],1)==0
#     assert ContadorPintas.contar([],2)==0
#     assert ContadorPintas.contar([],3)==0
#     assert ContadorPintas.contar([],4)==0
#     assert ContadorPintas.contar([],5)==0
#     assert ContadorPintas.contar([],6)==0

# def test_contar_sin_ases():
#     dados = []
#     valores = [4,4,2,2,2,5,6]
#     for i in valores:
#         dado = Dado()
#         dado.setValue(i)
#         dados.append(dado)
#     assert ContadorPintas.contar(dados,4) == 2
#     assert ContadorPintas.contar(dados,2) == 3
#     assert ContadorPintas.contar(dados,5) == 1
#     assert ContadorPintas.contar(dados,6) == 1
# def test_contar_con_ases_comodin():
#     dados = []
#     valores = [1,1,1,2,2,2,3,3]
#     for i in valores:
#         dado = Dado()
#         dado.setValue(i)
#         dados.append(dado)

#     assert ContadorPintas.contar(dados,2) == 6
#     assert ContadorPintas.contar(dados,3) == 5
#     assert ContadorPintas.contar(dados,1) == 3
# def test_contar_con_ases_comodin_sin_numero_en_juego():
#     #Los ases solo se asignan a una pinta si esta esta en juego, es decir, si hay al menos una verdadera instancia de esa pinta

#     dados = []
#     valores = [1,1,1,1,2,5,6]
#     for i in valores:
#         dado = Dado()
#         dado.setValue(i)
#         dados.append(dado)
#     assert ContadorPintas.contar(dados,3) == 0
#     assert ContadorPintas.contar(dados,4) == 0
# def test_contar_con_ases_no_comodin():
#     dados = []
#     valores = [1,1,1,2,2,2,3,3]
#     for i in valores:
#         dado = Dado()
#         dado.setValue(i)
#         dados.append(dado)
#     assert ContadorPintas.contar(dados,2,False) == 3
#     assert ContadorPintas.contar(dados,3,False) == 2