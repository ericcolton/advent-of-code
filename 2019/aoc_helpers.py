import sys
import os

def get_input_filepath(filepath):
    if len(sys.argv) > 1:
        return sys.argv[1]
    dirname = os.path.dirname(filepath)
    basename = os.path.basename(filepath)

    input_basename = basename.rstrip('.py') + '_input.txt'
    return os.path.join(dirname, 'input_files', input_basename)
