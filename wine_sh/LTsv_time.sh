#!/bin/sh
script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
cd $script_dir
cd ../LTsv
/mnt/home/Puppy-Linux-571/wine-portable-1.7.18-1-p4/wine-portable "/mnt/home/Puppy-Linux-571/wine-portable-1.7.18-1-p4/wine-data/drive_c/Python34/python.exe LTsv_time.py"
