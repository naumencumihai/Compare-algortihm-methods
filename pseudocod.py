
quicksort (vector[], inceput, sfarsit)
	if (inceput < sfarsit)
		# ip - index de partitie
		ip = partition (vector, inceput, sfarsit)

		quicksort (vector, inceput, ip - 1) # inainte de ip
		quicksort (vector, ip + 1, sfarsit) # dupa ip


# Functie de partitie
partition (vector, inceput, sfarsit)
	# pivot - element in jurul caruia se face partitia
	pivot = vector[sfarsit]

	i = (inceput - 1)

	for (j = inceput ... sfarsit - 1)
		if (vector[j] < pivot)
			i++
			swap (vector[i], vector[j])

	swap (vector[i + 1], vector[sfarsit])
	return (i + 1)





quicksort (vector = {1, 8, 3, 9, 4, 5, 7})
	partitie ({1, 8, 3, 9, 4, 5, 7} | pivot = 7)
		i = -1; j = 0
			i++
		...
		i = 0; j = 2
			i++
			vector[1] <-> vector[2] | 8 <-> 3
		...
		i = 1; j = 4
			i++
			vector[2] <-> vector[4] | 8 <-> 4
		i = 2; j = 5
			i++
			vector[3] <-> vector[5] | 9 <-> 5
		vector[4] <-> vector[6] | 8 <-> 7
	=> vector = {1, 3, 4, 5, 7, 9, 8}

	quicksort (stanga)
		partitie({1, 3, 4, 5} | pivot = 5)
			...
				partitie({1} | pivot = 1)
		=> vector stanga sortat

	quicksort (dreapta)
		partitie ({9, 8} | pivot = 8)
			...
			vector[0] <-> vector[1] | 9 <-> 8
		=> vector dreapta sortat
=> vector sortat



RezolvareSudoku (tabla[N][N]) # N = 9

	# Verifica daca mai exista locuri goale
	if (!GasesteLocGol (tabla, rand, coloana))
		return true # Succes

	for (n = 1 ... 9)
		if (SeRespectaConditiile (tabla, rand, coloana, n))

			tabla[rand][coloana] = n;

			# Verificare recursiva
			if (RezolvareSudoku(tabla))
				return true # Succes

			# Nu duce la solutie, se incearca urmatorul numar
			tabla[rand][coloana] = 0

	return false # Esec (nicio solutie posibila)




PrindeHotii (vector[N], k)
	# Se tin minte pozitiile
	for i = 0 ... N
		if vector[i] == 'P'
			AdaugaPozitiePolitist
		else if vector[i] == 'H'
			AdaugaPozitieHot

	rezultat = 0
	h = 0
	p = 0

	while h < NumarHoti si p < NumarPolitisti
		# hoti, pol - vectori cu pozitiile
		if |hoti[h] - pol[p]| <= k
			rezultat++
			h++
			p++
		else if hoti[h] < pol[p]
			h++
		else
			p++


           0   1   2   3   4   5
vector = {'H' 'H' 'P' 'P' 'H' 'P'}
k = 2

se vor crea 2 vectori cu pozitiile
aferente politistilor si hotilor:

hoti[] = {0, 1, 4}
pol[] = {2, 3, 5}

rezultat = 0
h = 0
p = 0

|hoti[0] - pol[0]| = 2 (<= k)
	rezultat = 1
	h = 1
	p = 1

|hoti[1] - pol[1]| = 2 (<= k)
	rezultat = 2
	h = 2
	p = 2

|hoti[2] - pol[2]| = 1 (<= k)
	rezultat = 3
	h = 3
	p = 3

> Final
> rezultat = 3 # toti cei 3 hoti sunt prinsi



MineazaAur(Mina[m][n], m, n)
	D[m][n] # Matricea rezultatelor

	for coloana = n - 1 ... 0
		for linie = 0 ... m - 1
			if coloana == n - 1
				dreapta = 0
			else
				dreapta = D[linie][coloana + 1]

			if linie == 0 sau coloana == n - 1
				dreapta-sus = 0
			else
				dreapta-sus = D[linie - 1][coloana + 1]

			if linie == m - 1 sau coloana == n - 1
				dreapta-jos = 0
			else
				dreapta-jos = D[linie + 1][coloana + 1]

			D[linie][coloana] = Mina[linie][coloana] +
								+ maxim(dreapta, dreapta-sus, dreapta-jos)

	# Valoarea maxima se va regasi pe prima coloana
	rezultat = maxim(D[i][0], unde i = 0 .. n - 1)


Mina:

-------------
0	3	5	0

3	1	0	4

1	5	0	1

2	2	5	1
-------------

Coloana 3:

-------------
0	0	0	0

0	0	0	4

0	0	0	1

0	0	0	1
-------------

Coloana 2:

-------------
0	0	9	0

0	0	4	4

0	0	1	1

0	0	6	1
-------------

Coloana 1:

-------------
0	12	9	0

0	10	4	4

0	11	1	1

0	8	6	1
-------------

Coloana 0:

-------------
12	12	9	0

15	10	4	4

12	11	1	1

13	8	6	1
-------------

Rezultatul va fi maximul de pe
prima coloana.

Rezultat = 15