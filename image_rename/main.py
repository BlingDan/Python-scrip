import os

'''
@:param path_name:   images filefloder
@:param name:       like yourname1.png
@:param start:      a number image_name start like  ***top.png
'''
def rename(path_name, name, start):
    i = start
    for item in os.listdir(path_name):
        os.rename(os.path.join(path_name,item), os.path.join(path_name,(name+str(i)+'.png')))
        i = i + 1

if __name__ == '__main__':
    rename(r'youfile',11)

    # print(os.getcwd())
