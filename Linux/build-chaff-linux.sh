# Stop on errors
set -e

# Create project directory
mkdir Chaff-Linux-Project
cd Chaff-Linux-Project

# Convert Chaff PyPi package to binary (https://stackoverflow.com/questions/39913847/is-there-a-way-to-compile-a-python-application-into-static-binary)
wget https://raw.githubusercontent.com/Invizabel/Chaff/refs/heads/main/Python/src/Chaff.py
python3 -m venv env
source env/bin/activate
pip install cython
cython Chaff.py --embed
gcc -Os $(python3-config --includes) Chaff.c -o Chaff $(python3-config --ldflags --embed)
