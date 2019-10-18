#apt-get update
# apt-get install -y  python3.6 \
#                     python3-venv \
#                     python3-dev \
#                     python3-setuptools \
#                     libpq-dev \
#                     build-essential \
#                     binutils \
#                     g++

rm -rf $HOME/.pyzz
mkdir $HOME/.pyzz
python3 -m venv $HOME/.pyzz/
$HOME/.pyzz/bin/pip install --upgrade pip
$HOME/.pyzz/bin/pip install .

#ZSHELL
if [ -z "$(grep '$HOME/.pyzz/bin' $HOME/.localrc)" ]; then
   echo 'export PATH=$HOME/.pyzz/bin/:$PATH' >> $HOME/.localrc
fi

#BASH
if [ -z "$(grep '$HOME/.pyzz/bin' $HOME/.bashrc)" ]; then
   echo 'export PATH=$HOME/.pyzz/bin/:$PATH' >> $HOME/.bashrc
fi
