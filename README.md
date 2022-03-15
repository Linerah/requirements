# Gym Schedule App - Team 5

An app that will let users book a gym slot and let the administration of the gym set limits on the amount of people that can go to the facilities at a given time.

## Virtual Environment

Setting up a virtual ennvirment, makes it easier to collaborate by having all the packages installed in the project itself.

### 1. Istalling virtual environment: 
``` 
pip3 install virtualenv
```
### 2. Create a virtual environment: 
The command bellow created the VE in the env file. (Do not run this) 
``` 
python -m virtualenv env
``` 

### 3. Activate the virtual environment: 
Run the commands below in the **backend folder**.
	
You can activate the python environment by running the following command:

- Mac OS / Linux
``` 
source mypython/bin/activate
``` 
- Windows:

```	
ve\Scripts\activate
```
If it doesnt let you activate it, run this command first: 
```
 Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
``` 
You should see the name of your virtual environment in brackets on your terminal line e.g. (mypython).

Any python commands you use will now work with your virtual environment

## 4. Deactivate the virtual environment: (run in the backend folder)

To decativate the virtual environment and use your original Python environment, simply type ‘deactivate’.

```
deactivate
```


## 5. Installing packages in the virtual environment: (do not run this)

Installing Flask:
```	
pip3 install flask flask-sqlalchemy 
```	


## Running App

After activating the virtual environment, run the following in the backend folder:
```	
python app.py
```	

