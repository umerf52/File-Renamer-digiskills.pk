import os
from os import listdir
from os.path import isfile, join

def rename_func(cwd):
        target_file_names = set()
        EXT = '.mkv'
        DESCRIPTION = '.description'

        onlyfiles = [f for f in os.listdir(cwd) if isfile(join(cwd, f))]
        for f in onlyfiles:
                file_name_wo_ext = f.split('.')[0]
                if (file_name_wo_ext in target_file_names):
                        continue
                elif (((file_name_wo_ext + EXT) in onlyfiles) and ((file_name_wo_ext + DESCRIPTION) in onlyfiles)):
                        target_file_names.add(file_name_wo_ext)

                for f in target_file_names:
                        new_file_name = ''
                        with open(join(cwd, f+DESCRIPTION), 'r') as input_file:
                                new_file_name = input_file.readline()

                        topic_start = f.find('Topic') + 5
                        slice_obj = slice(topic_start, topic_start+3, 1)
                        topic_string = 'Topic ' + f[slice_obj] + ' - '

                        os.rename(join(cwd, f+EXT), join(cwd, topic_string+new_file_name+EXT))
                        os.remove(join(cwd, f+DESCRIPTION))

def main():
        start_dir = os.getcwd()
        for root, subdirs, files in os.walk(start_dir):
                if not subdirs:
                        rename_func(root)

if __name__=='__main__':
        main()