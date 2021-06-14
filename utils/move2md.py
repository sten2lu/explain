import os 
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('--path', '-p', type=str)

if __name__ == '__main__':
    args = parser.parse_args()
    path = args.path


    for f in os.listdir(path):
        f_path = os.path.join(path, f)

        if os.path.isfile(f_path):
            print("Upgrading: {}".format(f))
            with open(f_path, 'r') as file:
                text = file.readlines()
            
            os.remove(f_path)
            os.mkdir(f_path)

            with open(os.path.join(f_path, f'{f}.md'), 'w') as file:
                file.writelines(text)

