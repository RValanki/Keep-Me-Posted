# Keep-Me-Posted

# Members
Brenda Dang (33111197)\
Harrison Lane (33110077)\
Bowen Dong (33109834)\
Ayesha Tariq (32497857)\
Ahmed Almasry (31130143)\
Parul Garg (32720254)\
Diya Ramesh (32336012)\
Afia Farzana (32501986)\
Alex Ung (32498853)\
Zihao Wang (32520433)\
Maureen Pham (33117144)\
Rohit Valanki (31451764)\
Marcus Wei (32503881)\
Angelina Leung (33114447)\
Benjamin Cherian (31483534)\
Danny Leung (32478704)

# Installation

To run project locally, run the frontend and backend in 2 seperate terminals. Eg, create one terminal and follow the frontend instructions, then create a different terminal and follow the backend instructions.

# npm install 

If you haven't already install node and npm globally - https://docs.npmjs.com/downloading-and-installing-node-js-and-npm 

# Frontend setup

cd frontend\
npm install\
npm run dev

# backend

if you are using mac use python3 and pip3

Create a virtual environment first time:

cd backend\
python -m venv venv\
source venv/bin/activate\
pip install -r requirements.txt

To start backend:

cd kmp_backend\
python manage.py makemigrations\
python manage.py migrate\
python manage.py runserver