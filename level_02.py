import os, shutil

#default path
# path = 'C:/Users/91991/Downloads/'
path = input('Enter path : ')
path = path.replace('\\','/') + '/'

for folder in (os.listdir(path)):
    # print(f"~~~~~~~~~~~~~~~~~~~   {folder}   ~~~~~~~~~~~~~~~~~~~")
    for file in (os.listdir(path + folder)):
        # print(file)
        fName = file[0]

        if os.path.exists(path + folder + '/' + fName.upper()):
            shutil.move(path + folder + '/' + file, path + folder + '/' + fName.upper() + '/' + file)
        else:
            os.makedirs(path + folder + '/' + fName.upper()) 
            shutil.move(path + folder + '/' + file, path + folder + '/' + fName.upper() + '/' + file)

print('Your files are sorted successfully')