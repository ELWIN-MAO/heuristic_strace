# heuristic_strace
strace with heuristic
forked from https://github.com/strace/strace

# branch information
 master: stable branch, test ok on ubuntu 16.04.
 
 arch: branch test ok on archlinux
 
 vanilla: vanilla strace.

# result data process
 for result data process and process creation graph, process network communication graph, please visit:
 
 https://github.com/ELWIN-MAO/data_process
 
 
# how to use h-strace 
## prepare work:
```
cd ~
git clone https://github.com/ELWIN-MAO/data_process
git clone https://github.com/ELWIN-MAO/heuristic_strace

mkdir -p 

cd heuristic_strace
mkdir -p  ./strace-4.11/build_dir/test_data/

cp ../data_process/*.sh  ./strace-4.11/build_dir/
cp ../data_process/*.py  ./strace-4.11/build_dir/

cp ./h-strace.py ./strace-4.11/build_dir/test_data/

cd ./strace-4.11/build_dir/test_data/
```
## run h-strace:
```
./h-strace.py XWINDOW NULL
./h-strace.py TCP 3389
./h-strace.py UNIX /tmp/.X11-unix/X0
```
 
