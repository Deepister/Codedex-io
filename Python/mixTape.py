playlist = [
  'Porches - rangerover',
  'Mount Eerie - You Swan, Go On',
  'Carolyn Polachek - Look at Me Now',
  'Pinegrove - Darkness',
  'LVP UP - Spirit Was',
  'Mitski - First Love / Late Spring'
]

# print normally) 
print(playlist)
#filler line 
print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

#print using  a for-in loop 
for i in playlist:
    print(i)
 #filler line 
print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')   

 #print using for-in with range() and len() functions 
for i in range(len(playlist)):
        print(playlist[i])