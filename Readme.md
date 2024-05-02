# Cyber Security Basis
Sample code to ilustrate sombe cyber security basis

Features:
- Password strength
- Web site protocol
- Hash function
- Security headers
- Caesar cipher
- XOR Algorithm


## Run ML model
```
python CheckPwd.py
python CheckWebsiteProtocol.py
python SimpleHashFunction.py
python GetSecurityHeaders.py
python XORAlgorithm.py
```

## Installing using GitHub
- Fork the project into your GitHub
- Clone it into your dektop
```
git clone https://github.com/jacesca/CiberSecurityBasis.git
```
- Setup environment (it requires python3)
```
python -m venv venv
source venv/bin/activate  # for Unix-based system
venv\Scripts\activate  # for Windows
```
- Install requirements
```
pip install -r requirements.txt
```

## Others
- Proyect in GitHub: https://github.com/jacesca/CiberSecurityBasis
- Commands to save the environment requirements:
```
conda list -e > requirements.txt
# or
pip freeze > requirements.txt

conda env export > env.yml
```
- For coding style
```
black model.py
flake8 model.py
```

## Extra documentation
- [format built-in function](https://docs.python.org/3/library/functions.html#format)
- [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#formatspec)
- [int buit-in function](https://docs.python.org/3/library/functions.html#int)
