import os
os.system('clear')
v1='cat files/package/* >'
v1+=open('filename.lvd','r').read()
print('Sendo Package Manager 1.1\n\nDo you want to install it?')
q1=input('[y/n]:')
if q1 == 'y':
  os.system('unzip package.lvd')
  os.system('rm package.lvd')
  os.system(v1)
  os.system('rm files/package/ -r')
  print('Finished!')
else:
  print('Goodbye!')
