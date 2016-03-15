#!/bin/sh
script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
cd $script_dir
/mnt/home/Puppy-Linux-571/wine-portable-1.7.18-1-p4/wine-portable msiexec /i "/mnt/home/Puppy-Linux-571/wine-portable-1.7.18-1-p4/wine-data/drive_c/ooblog/install/python-3.4.3.msi"
