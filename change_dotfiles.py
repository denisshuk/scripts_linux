#!/usr/bin/env python3

import os
import sys

name_of_dotfile = sys.argv[1]

editor = 'nvim'

cmd_backup_file_and_run_editor = f'cp {name_of_dotfile} {name_of_dotfile}.bckp; nvim {name_of_dotfile}'

os.system(cmd_backup_file_and_run_editor)

cmd_source_bashrc = '/home/parallels/myscripts.sl/run_source_bashrc.sh'

os.system(cmd_source_bashrc)

