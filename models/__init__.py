import os
import glob

main_path = os.path.dirname(__file__)
paths =  [ os.path.join(main_path , file_name) for file_name in os.listdir(main_path) if not os.path.basename(file_name).startswith('_')]
modules = []
for path in paths:
    modules += [os.path.basename(f)[:-3] for f in glob.glob(path + "/*.py") ]
__all__ = modules

