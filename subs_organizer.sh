#!/bin/bash

echo "Downloading script.py..."

curl -o script.py https://raw.githubusercontent.com/smyk07/subs-organizer/master/script.py

echo --------------------

python3 ./script.py

echo --------------------

echo "Deleting the script.py file..."

rm ./script.py

echo "Thanks for using smyk07/subs-organizer"
