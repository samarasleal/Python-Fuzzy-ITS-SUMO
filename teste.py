#!/usr/bin/env python

def geraSinais(NS,SN,OL,LO):
	tempoAmarelo = 3
	UD_G = "GGGGGGrrrrrrrrrrrrrrrrrr" # Cada posicao da variavel e um estado do sinal. Sinais funcionam a partir de estados (esta variavel).
	UD_Y = "yyyyyyrrrrrrrrrrrrrrrrrr"

	DU_G = "rrrrrrGGGGGGrrrrrrrrrrrr"
	DU_Y = "rrrrrryyyyyyrrrrrrrrrrrr"

	RL_G = "rrrrrrrrrrrrGGGGGGrrrrrr"
	RL_Y = "rrrrrrrrrrrryyyyyyrrrrrr"

	LR_G = "rrrrrrrrrrrrrrrrrrGGGGGG"
	LR_Y = "rrrrrrrrrrrrrrrrrryyyyyy"
	
	PROGRAM = []

	for i in range(0,NS):
		PROGRAM.append(UD_G)
	for i in range(0,tempoAmarelo):
			PROGRAM.append(UD_Y) # amarelo

	for i in range(0,SN):
		PROGRAM.append(DU_G)
	for i in range(0,tempoAmarelo):
		PROGRAM.append(DU_Y)

	for i in range(0,OL):
		PROGRAM.append(RL_G)
	for i in range(0,tempoAmarelo):
		PROGRAM.append(RL_Y)

	for i in range(0,LO):
		PROGRAM.append(LR_G)
	for i in range(0,tempoAmarelo):
		PROGRAM.append(LR_Y)

	return PROGRAM

print "Hello World!"
print geraSinais(15,15,15,15)