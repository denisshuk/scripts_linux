#!/usr/bin/env python3

import os
import sys

name_of_script = sys.argv[1]

cmd_create_file_and_run_editor = f'nvim {name_of_script}.py'

os.system(cmd_create_file_and_run_editor)

cmd_make_scripts_able_run = f'chmod +x {os.getcwd()}/{name_of_script}.py'

os.system(cmd_make_scripts_able_run)

f = open('/home/parallels/.bashrc', 'a')
f.write(f'\nalias {name_of_script}="{name_of_script}.py"')
f.close()

cmd_source_bashrc = '/home/parallels/myscripts.sl/run_source_bashrc.sh'

os.system(cmd_source_bashrc)
print("it's ok")








