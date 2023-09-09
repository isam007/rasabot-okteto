1. Create a SmartBot Folder (this will be our root directory) and open it in VS Code
2. Make sure you have Python 3.10 installed: python --version. Higher versions are not compatible with Rasa yet.
3. If you have Python 3.10, then move on, otherwise install it from https://www.python.org/downloads/release/python-3100/ 
-- Make sure to select "Add Path" during installation.
4. Open New terminal in VS Code
5. Navigate to SmartBot Folder and create a virtual environment in Python: 
python -m venv ./rasa
-- You should see rasa folder created in our root directory.
6. There is a Scripts subfolder that we will use to activate this ./rasa virtual enviroment (VE) every time we need to re-enter.
7. Activate your VE:    .\rasa\Scripts\activate   
-- You should now see (rasa) in front of your command line
8. Now we need to install Rasa in this virtual environment: pip install rasa
-- It will take some time
9. Now lets initialise rasa: rasa init
-- When prompted type a directory name for your new project, yes to create it and train the basic model
10. Now lets initialise rasa: rasa init
-- When prompted type a directory name for your new project, yes to create it and train and test the basic model
-- Ctrl + C if you need to exit back to the command line
11. Now that we have a backend we can add the front end.
12. Just download this Chatbot-Widget into your OmdenaBot project folder and run index.html https://github.com/isam007/Chatbot-Widget
13. To run the backend server use: rasa run --enable-api --cors "*" 
-- Note! If you also use actions and modified actions.py file, you should then first run actions from a new terminal in the VS Code: rasa run actions  and then rasa run --enable-api --cors "*" in another terminal. Both servers should be running at the same time if you use actions.
14. Now just go to your browser where index.html file opened and test a chatbot.
15. Now you are ready to train your model. Note, every time you add new questions and responses to yml files in your data folder, you should run rasa train to train new model. And you should see new model appear in the models folder.
