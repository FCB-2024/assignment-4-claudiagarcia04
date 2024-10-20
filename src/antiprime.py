import sys

# Funció per comptar el nombre de divisors d'un nombre
def comptar_divisors(n):
	comptador = 0
	divisor = 1
	while divisor <= n:
		if n % divisor == 0:
			comptador += 1
		divisor += 1
	return comptador

## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main():
	# Agafem el valor de la línia de comandes
	n = int(sys.argv[1])
    
    # Comptem els divisors de n
	divisors_n = comptar_divisors(n)
    
    # Comparar amb tots els nombres menors que n
	es_antiprime = True  # Suposem que n és antiprime
	i = 1
	while i < n:
		if comptar_divisors(i) >= divisors_n:
			es_antiprime = False  # Si algun nombre més petit té tants o més divisors, no és antiprime
			break  # Ja podem parar la cerca
		i += 1
    
    # Retornem el resultat segons si és antiprime o no
	if es_antiprime:
		return "anti-prime"
	else:
		return "not anti-prime"

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main())