### Desenvolvido por:
Henrique de Lima Barroso
</br>


<strong>Agradecimento:</strong></br>
<i>Alessandro Vivas - por incentivar estes estudos.</i>

<i>UNIVERSIDADE FEDERAL DOS VALES DO JEQUITINHONHA E MUCURI (UFVJM) - CAMPUS JK.
</br>2022</i>


### Configurações

A primeira coisa a ser feita é a criação do ambiente virtual para este projeto. Instale os pacotes caso ainda não tenha e depois crie o ambiente virtual:
```shell
# Install these packages, case you don't already have it.
sudo apt-get install python3-pip
sudo pip3 install virtualenv 

# Create the Virtual Environment
virtualenv env
```
Ative o ambiente virtual:
```shell
source env/bin/activate
```

Instale os requisitos do sistema:
```shell
pip install -r requirements.txt
```
Instale o MongoDB Server no seu sistema operacional:
```shell
sudo apt install -y mongodb
```
Confira a instalação:
```shell
sudo systemctl status mongodb
```


### Rodando o projeto
Inicie o servidor:
```shell
python run.py
```
</br>

