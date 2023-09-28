string = "my dad said our mother tongue is malayalam"
y=string.split()
['my' 'dad' 'said' 'our' 'mother' 'tongue' 'is' 'malaylam']
for i in y :
    x=i[-1::]
    if i ==x:
     print( "@" * len(i))
else:
  print(i)

