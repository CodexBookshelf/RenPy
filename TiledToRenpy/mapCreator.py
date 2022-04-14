#CREATED BY CODEXBOOKSHELF
#GITHUB LINK: 

import json

#Para abrir o arquivo climaAgora
def getTiles():
	with open('logicTileset.json') as f:
		data = json.load(f)
	#Lendo o arquivo

	global tilesData
	tilesData = []

	num = 0
	tilesNum = len(data['tiles']) -1
	while num <= tilesNum:
		#print(data['tiles'][num]['id'])
		listaId = [data['tiles'][num]['id']] 
		num2 = 0
		propsNum = len(data['tiles'][num]['properties']) -1
		while num2 <= propsNum:
			listaId.append([data['tiles'][num]['properties'][num2]['name'], data['tiles'][num]['properties'][num2]['value']])
			#print(data['tiles'][num]['properties'][num2]['name'])
			#print(data['tiles'][num]['properties'][num2]['value'])
			num2 += 1
		tilesData.append(listaId)
		num += 1
	print(tilesData[0][0])
	return tilesData

getTiles()

def getMap(): #FUNÇÃO ATUAL PARA CRIAR OS NOMES DOS LABELS
	with open('refugeTown.json') as g:
		data2 = json.load(g)
	tilesList = data2['layers'][0]['data']
	tilesNum2 = len(tilesList)
	tilesH = data2['width']
	tilesV = data2['height']
	num3 = 0

	global listaTiles
	listaTiles = []
	#print("tilesList: "+ str(tilesList))
	#print("tilesNum2: "+ str(tilesNum2))
	#print("tilesH: "+ str(tilesH))
	#print("tilesV: "+ str(tilesV))
	#print("teste1: " + str(tilesList[tilesNum2 - 1]))
	for x in tilesList:
		#if num3 == 0:
		#	listaTeste.append("1_1: " + str(x-1))
		#	num3 += 1	
		#if num3 != 0 and (num3)%tilesH == 0:
		#	listaTeste.append(str(((num3+1)//tilesH)+1) + "_" + str(tilesH) + ": " + str(x))
		#	num3 += 1
		if num3 != 0 and (num3+1)%tilesH==0:
			listaTiles.append([((num3+1)//tilesH), tilesH, (x-1)])
			num3 += 1
		else:
			#listaTeste.append(str(((num3+1)//tilesH)+1) + "_" + str(((num3+1) % tilesH)) + ": " + str(x-1))
			listaTiles.append([(((num3+1)//tilesH)+1), ((num3+1) % tilesH), (x-1)])
			num3 += 1

	#print(listaTiles)
	return listaTiles		

#getMap()

def mountLabels():
	getTiles()
	getMap()
	for y in listaTiles:
		z = 0
		if y[2] == 181: #esta condição elimina todos os tiles vazios de serem escritos no arquivo final
			pass
		else:
			labelName= "label map_"+str(y[0])+"_"+str(y[1])#declaração literal do label
			lName = "map_"+str(y[0])+"_"+str(y[1])#usado para fazer o looping
			labelId = y[2]
			labelInfo = tilesData[labelId]
			with open ('map_vars.rpy', 'a') as i:
				i.write("default {}_discovered = False\n".format(lName))
			with open('maps.rpy', 'a') as h:
				h.write("{}:\n".format(labelName))
			times = [1,2]
			for time in times:
				for w in labelInfo:
					if type(w) != list:
						pass
					else:
						with open('maps.rpy', 'a') as h:
							h.write("    ${} = {}\n".format(w[0], '"'+str(w[1])+'"' if type(w[1])==str else w[1]))
						#o IF/ELSE seguinte garante que as variáveis de navegação sejam postas nos cantos corretos
						if w[0] == "formatoN" and w[1] != " ":
							sul = '    $Sul = "map_{}_{}"\n'.format(str(y[0]+1), str(y[1]))
							with open('maps.rpy', 'a') as h:
								h.write(sul)

						elif w[0] == "formatoL" and w[1] != " ":
							oeste = '    $Oeste = "map_{}_{}"\n'.format(str(y[0]), str(y[1]-1))
							with open('maps.rpy', 'a') as h:
								h.write(oeste)
						elif w[0] == "formatoS" and w[1] != " ":
							norte = '    $Norte = "map_{}_{}"\n'.format(str(y[0]-1), str(y[1]))
							with open('maps.rpy', 'a') as h:
								h.write(norte)
						elif w[0] == "formatoO" and w[1] != " ":
							leste = '    $Leste = "map_{}_{}"\n'.format(str(y[0]), str(y[1]+1))
							with open('maps.rpy', 'a') as h:
								h.write(leste)
						else:
							pass		
				with open('maps.rpy', 'a') as h:
					h.write("    $montaCena()\n    $useKeyItems()\n    $labelAtual = '{}'\n    $store.{}_discovered = True\n".format(lName,lName))
					if time == 1: #cria a fala que torna o label utilizável
						h.write('    notchar " "\n')
			with open('maps.rpy', 'a') as h:
				h.write("    jump {}\n".format(lName)) #cria o looping que torna o label utilizável
				h.write("\n")	

			#print(labelName)
			#print(labelId)
			#print(labelInfo)

	#listaTiles[]	
	#with open('maps.rpy', 'a') as h:
	#	h.write(text)
	#	h.close()

	#aqui preciso escrever os arquivos interagindo entre listaTiles e tilesData

mountLabels()


###################################################################################3
#LIXO:
#def getMap():
#	with open('refugeTown.json') as g:
#		data2 = json.load(g)
#	tilesList = data2['layers'][0]['data']
#	tilesNum2 = len(tilesList)
#	tilesH = data2['width']
#	tilesV = data2['height']
#	num3 = 0
##	print(tilesNum2)
##	print(tilesList)
#	text = " "
#	while num3 <= (tilesNum2 -1):
#		if (num3 +1) // tilesH == 0:
#			labelName = str(((num3 +1) // tilesH) + 1) + "_" + str(num3)
##			text = text + "\n{}, {}".format(labelName, str(tilesList[num3]))
#			text = "\n{}, {}".format(labelName, str(tilesList[num3]))
#			with open('maps.rpy', 'a') as h:
#				h.write(text)
#			print(labelName)
#			print("id: " + str(tilesList[num3]))
#			num3 += 1
#		else:
#			if (num3 +1) % tilesH == 0:
#				labelName = str(((num3 +1) // tilesH) + 1) + "_" + str(tilesH)
##				text = text + "\n{}, {}".format(labelName, str(tilesList[num3]))
#				text = "\n{}, {}".format(labelName, str(tilesList[num3]))
#				with open('maps.rpy', 'a') as h:
#					h.write(text)
#				print(labelName)
#				print("id: " + str(tilesList[num3]))
#				num3 += 1
#			else:
#				labelName = str(((num3 +1) // tilesH) + 1) + "_" + str((num3 +1) % tilesH)
##				text = text + "\n{}, {}".format(labelName, str(tilesList[num3]))
#				text = "\n{}, {}".format(labelName, str(tilesList[num3]))
#				with open('maps.rpy', 'a') as h:
#					h.write(text)
#				print(labelName)
#				print("id: " + str(tilesList[num3]))
#				num3 += 1
#	with open('maps.rpy', 'a') as h:
#		h.close()
#	#Lendo o arquivo e criando uma lista
#
##getTiles()
##getMap()
	#varTeste = ""
	#for x in list(range(1, 201)):
	#	varTeste += str(((x-1)//10)+1) + "_"
	#	if int(x)%10==0 and x >1:
	#		varTeste += "{}...\n".format(x)
	#	else:
	#		varTeste += "{} ".format(x)
	#print(varTeste)
