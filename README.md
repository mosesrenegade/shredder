Shredder

What is with the name? Shredder == Evil bad guy from the Teenage Mutant Ninja Turtles Comic books and TV Shows that I grew up watching.
Shredder wanted to always have Turtle Soup, from collecting many shells.

This application is specifically designed for Web Shells.

---

How to install for Devs.

OSX Users:

$brew install python3
$brew install sqlite3
$pip3 install virtualenv

Clone the Repo:

$git clone https://www.github.com/mosesrenegade/shredder

Use virtualenv:

$cd shredder
$virtualenv venv

Activate VirtualEnv:

$. ./venv/bin/activate

Install dependencies
$pip install -r requirements.txt

The App Listens on port 5000 for development work.

You need a Shell to test with:
$cd shredders/shells
$php -S localhost:8000

This will start a listening server on port 8000. Interact with it by going to the following test url:

http://localhost/php_shell.php?OS

More on this later

TODO for an MVP

Command Channels needs to be obfuscated using Tokenization
Database support for Postgresql
Commands should be sent to Redis for queueing instead of run synchronisly.
 
Authentication support
Migrate command channel to be Jsonified
Automatically import all known information about the attacking host over to database (loot import)
