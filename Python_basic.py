
hippos = 0
answer = 'y'
while answer == 'y':
	hippos += 1
	print(str(hippos) + ' balancing hippos!')
	answer = input('Add another hippo? (y/n)')

	
  '''
1 balancing hippos!
Add another hippo? (y/n)y
2 balancing hippos!
Add another hippo? (y/n)y
3 balancing hippos!
Add another hippo? (y/n)y
4 balancing hippos!
Add another hippo? (y/n)n
'''


##################################################

for counter in range(1, 11):
    print('Emma\'s Room - Keep out!!!')

    
'''    
Emma's Room - Keep out!!!
Emma's Room - Keep out!!!
Emma's Room - Keep out!!!
Emma's Room - Keep out!!!
Emma's Room - Keep out!!!
Emma's Room - Keep out!!!
Emma's Room - Keep out!!!
Emma's Room - Keep out!!!
Emma's Room - Keep out!!!
Emma's Room - Keep out!!!
'''


##################################################

while True:
	print('This is an infinite loop!')


#Ctrl-C to escape infinite loop


##################################################

while True:
	answer = input('Are you bored yet? (y/n) ')
	if answer == 'y':
		print('How rude!')
		break


'''
Are you bored yet? (y/n) n
Are you bored yet? (y/n) n
Are you bored yet? (y/n) n
Are you bored yet? (y/n) n
Are you bored yet? (y/n) y
How rude!
'''





