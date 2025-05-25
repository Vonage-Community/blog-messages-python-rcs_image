# How to Send RCS Image Messages With Python
A python script that allows you to send Rich Communications Services image messages.

> You can find full step-by-step instructions on the [Vonage Developer Blog](#). (Not published yet)



## Prerequisites 
1. [Python 3.6 or higher installed on your machine.](https://www.python.org/downloads/) Python 3.6 or higher is installed on your machine. 
2. [Vonage Developer Account](https://developer.vonage.com/sign-up)
3. A registered RCS Business Messaging (RBM) Agent.
4. A phone with RCS capabilities for testing.



## Instructions
1. Clone this repo
2. Setup a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies:
```
pip install vonage python-dotenv
```
3. Rename the `.env.example` file to `.env`, and add your `VONAGE_APPLICATION_ID` and `RCS_SENDER_ID` values.
4. Add your `private.key` file in the root of the project directory.
5. Run your Python scriopt:
```
python send_rcs_image.py
```

