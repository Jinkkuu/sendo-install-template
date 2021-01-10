import os
print('DO NOT USE THIS FOR VIDEO TRANSFERS OR PHOTO TRANSFERS, IT WILL CORRUPT IT!\n\nDo you want to install it?')
q1=input('[y/n]:')
if q1 == 'y':
  os.system('unzip package.lvd')
  os.system('rm package.lvd')
  os.system('cat files/package/* >program.py')
  os.system('rm files/package/ -r')
  print('Finished!')
else:
  print('Goodbye!')
