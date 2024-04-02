import os, shutil

#set defalut path
# path = "C:/Users/91991/Downloads/"
path = 'F:/download/'
for file in os.listdir(path):
    # for splitting file name and file type
    name, ext = os.path.splitext(file)

    # for storing extention
    extType = ext[1:]

    #ignoring unwanted ext
    if extType == 'ini':
        continue

    #if folder exists then moving file
    if os.path.exists(path + extType):
        shutil.move(path + file, path + extType + '/' + file)

    # now creating folder of extentions that does not exists in that directory
    # and moving file
    else:
        os.makedirs(path + extType)
        shutil.move(path + file, path + extType + '/' + file)
print('Your files are sorted successfully')