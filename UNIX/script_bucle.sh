root@e660469075e6:~# ls -l
total 4
drwxr-xr-x 2 root root 4096 Sep 17 06:59 Anto
root@e660469075e6:~# touch script_bucle.sh
root@e660469075e6:~# chmod 777 script_bucle.sh
root@e660469075e6:~# nano script_bucle.sh


#!/bin/bash
c=1
while [ true ]
do
echo "Welcome $c times"
( ( c++ ) )
done

root@e660469075e6:~# . script_bucle.sh
Welcome 1 times
bash: c++: command not found
Welcome 1 times
bash: c++: command not found
Welcome 1 times
bash: c++: command not found
Welcome 1 times
bash: c++: command not found
Welcome 1 times
bash: c++: command not found
Welcome 1 times
bash: c++: command not found
Welcome 1 times
bash: c++: command not found
Welcome 1 times
bash: c++: command not found
Welcome 1 times
bash: c++: command not found
Welcome 1 times
bash: c++: command not found
Welcome 1 times
bash: c++: command not found
Welcome 1 times
bash: c++: command not found
Welcome 1 times
bash: c++: command not found
Welcome 1 times
bash: c++: command not found
Welcome 1 times
bash: c++: command not found
Welcome 1 times
bash: c++: command not found
Welcome 1 times