# dbFinal2020
Database Take-Home Final Ek-1

./bash.sh               #is used for remove tildas from original data

python dbinit.py        #creates tables.

py -m venv env          #creates virtual environment

 

env\Scripts\activate    #activate virtual environment (I work on windows and there was a security 
                        issue with activate virtual environment then on windows powershell i run this: 
                        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser)

pip install flask       #install flask module (when flask module installed, 
                        #pages works without virtual environment)

python server.py        #starts to work webpages.

