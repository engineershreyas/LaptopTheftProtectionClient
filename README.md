Laptop Theft Security Client
============================

### What is it?
Have you ever been working on your laptop at somewhere and wanted to leave the place you were sitting for a bit? Perhaps you want to go to the bathroom, or order a new cup of coffee, or just go for a walk. Your two usual options are:

* Ask someone to watch your stuff for you, which is unnecessary interaction that can be bothersome to either you or the person you are asking
     
* Hide your stuff, which is a lot of work, especially when you take into account hiding it and unhiding it
     
Laptop Theft Protection Client, or LTPC, is an alternative, technological solution to this problem.

When you need to leave your laptop, all you need to do is start the client, register, login, and LTPC will continuously ping a server, that expects a ping in a certain interval. If there is no ping in that interval, the server will text your phone, letting you know that your laptop has stopped broadcasting so that you can check on your laptop immediately.

### What are the technological details?
Laptop Theft Protection has two parts:

1. The Client

2. [The Server](https://github.com/engineershreyas/LaptopTheftProtectionServer)

The client is a simple Python 2 commad-line program that allows you to register, or if you're already registered, login, and begin the pinging. The server is a Node.js application that resides on Heroku (or any cloud/localhost of your choice) that keeps a table of "Users", identified only by their phone numbers and a password, as well as a table of "Numbers", which are unique rows that are identified by phone numbers and keep track of how many times a number has been pinged. When a User logs in, an interval function is created on the server that periodically checks the last time a Number has been pinged against the current time. If the difference is greater than a max interval, the server uses the Twilio API to send a SMS to the User's phone number, letting them know to check on their laptop. Once the User comes back, they can manually end the pinging, which will clear the interval and reset the number of pings for that Number to 0.

### How can I use this?
Currently, this project exists as an open source project, with the code for both the server and the client available. If you would like, you can DIY with the following steps (using Heroku):

1. Create a Twilio account
2. Create a Heroku app for the server and add mLab MongoDB as an add-on
3. In the server repo, add a file called `config.js` that looks like this
    ```
    module.exports = {
        'secret' : '<some secret password for JWT>',
        'localDatabase' : 'mongodb://localhost/<some name for your local database>',
        'remoteDatabase' : 'mongodb://<your remote mongo db url>',
        'liveAccountSid' : '<your sid for your live Twilio account>',
        'liveAuthToken' : '<your auth token for your live Twilio account>',
        'testAccountSid' : '<your sid for your test Twilio account>',
        'testAuthToken' : '<your auth token for your test Twilio account>
    };
    ```
4. Push your server code to Heroku
5. In your client repo, add a file called `config.py` that looks like this
    ```
    REMOTE_BASE = "https://<your_heroku_app>.herokuapp.com"
    ```
6. Run the client with `python ltpc.py` and enjoy!

### FAQ

1. ###### What if I don't want to set up my own Twilio and Heroku account?
   That's fine! I'm working on a way to set up a payment method so that you can simply install the client and donate a small    amount the keep the server and Twilio account running
2. ###### How can I contribute?
    Make an issue highlighting a feature you are trying to add or bug you want to fix. Then, fork the repository and make your changes, and make a pull request!
    
### Contact
Email: shreyashirday@gmail.com
