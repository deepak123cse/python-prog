num = int(input('Enter a Number > 1 : '))
print('')
is_prime=True
num_list= range(2,10);

for x in num_list:
	if (num%x==0 and num>1 and num!=x):
		is_prime=False;
		print(num,'is a not a prime number')
		print(x,'times ',num/x,'is ',num)
		break
else:
	print(num,'is a prime number')
