## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main() :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
	import sys

	n = int(sys.argv[1])

	def comptar_divisors(n):
		comptador = 0
		divisor = 1
		while n >= divisor:
			if n % divisor == 0:
					comptador +=1
			divisor +=1
		return comptador

	def main():
		n = int(sys.argv[1])

		divisors_n = comptar_divisors(n)

		es_anitprime = True
		i = 1
		while i < n:
			if comptar_divisors(i) >= divisors_n:
				es_anitprime = False
				break
			i += 1
		if es_anitprime:
			print("antiprime")
		else:
			print("not anti-prime")



	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"
	return("anti-prime")

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main())
