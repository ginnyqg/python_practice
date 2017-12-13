
##################################################
# for loop
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
# while loop
##################################################

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
# infinite loop & stop infinte loop
##################################################

while True:
	print('This is an infinite loop!')


#Ctrl-C to escape infinite loop


##################################################
# Escape infinite loop
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


##################################################
# Nested loop
##################################################

for hooray_counter in range(1, 4):
	for hip_counter in range(1, 3):
		print('Hip')
	print('Hooray!')

	
'''	
Hip
Hip
Hooray!
Hip
Hip
Hooray!
Hip
Hip
Hooray!
'''




