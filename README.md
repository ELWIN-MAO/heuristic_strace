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


cd heuristic_strace
mkdir -p  ./strace-4.11/build_dir/test_data/

cp ../data_process/*.sh  ./strace-4.11/build_dir/
cp ../data_process/*.py  ./strace-4.11/build_dir/
cp ./socket_to_pid/get_sock_pid2.py ./strace-4.11/build_dir/

#build h-strace
cd ./strace-4.11/build_dir/
sudo apt-get build-dep strace
../configure  --with-libunwind
make -j4

cp ./h-strace.py ./strace-4.11/build_dir/test_data/
```
## run h-strace:
h-strace.py 必须提供两个参数，第1个参数为XWINDOW时表示跟踪某个GUI窗口对应的进程，此时第2个参数要求为NULL。第1个参数为TCP时表示跟踪监听某个TCP端口的进程，地个参数表示监听的端口。 第1个参数为UNIX时，表示监听跟踪监听某个unix domain地址的进程，第2个参数表示unix domain地址。
```
cd ./strace-4.11/build_dir/test_data/
./h-strace.py XWINDOW NULL
./h-strace.py TCP 3389
./h-strace.py UNIX /tmp/.X11-unix/X0
sudo ./gengraph2.sh

#check *.jpg or *.svg for result
```
 
