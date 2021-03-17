#wor with import so
import os
from datetime import datetime

#print (dir(os))
print(os.getcwd())
print(os.listdir())
os.chdir('..')
print(os.getcwd())

os.mkdir('OS-demo-N')
os.makedirs('OS-demo-1')
print('pasta criadas: ',os.listdir(),'\n')

os.rename('OS-demo-N','OS-demo-2')
print('renomeada a pasta: ',os.listdir(),'\n')

print('info: ',os.stat('OS-demo-2'),'\n')
mod_time = os.stat('OS-demo-2').st_mtime
print('info time: ',datetime.fromtimestamp(mod_time),'\n')

os.rmdir('OS-demo-2')
os.removedirs('OS-demo-1')
print('deletada as pastas: ',os.listdir(),'\n')