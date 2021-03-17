#work with try except
try:
    f = open('curruptfile.txt')
except IOError as e:
    print(e)
except Exception as e:
    print('Error')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")
