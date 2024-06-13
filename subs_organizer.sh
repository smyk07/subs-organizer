#!/bin/bash

echo "Downloading script.py..."

curl -o script.py https://raw.githubusercontent.com/smyk07/subs-organizer/master/script.py

echo --------------------

python3 ./script.py

echo --------------------

read -p "Do you want to delete the script.py file? (y/n) " yn

case $yn in
y) rm ./script.py ;;
n) exit ;;
*)
	echo invalid response...
	exit 1
	;;
esac
