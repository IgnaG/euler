def solve():
    numbers = xrange(1,1000001)
    max_number = -1
    max_chain = -1
    for number in numbers:
    	chain = do_chain(number)
    	if chain > max_chain: max_number = number
    	max_chain = max(max_chain, chain)
    return max_number

def do_chain(n):
	number = n
	chain = 1
	while(number != 1):
		if number % 2 == 0:
			number = number/2
		else:
			number = 3*number+1
		chain+=1
	return chain
            
def main():
    print solve()

if __name__ == '__main__':
    main()