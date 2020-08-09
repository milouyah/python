import glob
import os

print('test')

def get_file_list():
    file_list = glob.glob('./[0-9].*')
    print(file_list)
    
    file_list = glob.glob('./*.md')
    print(file_list)


    file_list = glob.glob('??????.md')
    print(file_list)

    os.chdir('../')
    file_list = glob.glob('**/*.md', recursive=True)
    print(file_list)

    file_list=glob.glob('./**/', recursive=True)
    print(file_list)

if __name__ == '__main__':
    get_file_list()

