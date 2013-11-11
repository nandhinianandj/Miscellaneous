def isprime(number):
	if number<=1:
		return 0
	check=2
	maxneeded=number
	while check<maxneeded+1:
		maxneeded=number/check
		if number%check==0:
			return 0
		check+=1
	return 1


def main():
    for j in range(5):
        for k in range(10):
            x = (2*j +1)*11001 +110* k;
            if isprime(x):
                print x
if __name__ == '__main__':
    main()
