## **Let's learn Python together with my naive method & make useful utility application from the scratch**
... and you don't need any prior knowledge about programing :) just open mind.

How to approach learning as activity?

That is very often dilemma for the educators in any field of human knowledge. Experts who are well educated and skilled in some topic are not always great motivators for the beginners who are just making their first bite in the new knowledge fruit.
Same thing goes with learning new language. You can start with grammar and slowly build words repository, or you can go with “naive” approach and just start speaking. Native speaking girlfriend or boyfriend can accelerate learning of new language faster than any teacher 😊. The key concept is to learn most common phrases and complete sentences, and with time master the whole language. It is in nutshell a same learning experience and method that we all had when we learn to use language in the first years of our life. Rules for spelling and grammar will follow in the future one day.
So, we want to learn new programing language and you want to see some tangible results for your effort. A new application made by you will be a great motivator for further learning.
Problem with traditional approach, and something what educators often fail to understand, is that motivation level will drop down with time invested. Starting with language syntax and core concepts of programing language will prolong time to build something useful. “Hello World” kind of app will just not be good enough to boost motivation for beginner in any programming language.
Anyhow all above mentioned is my personal experience and now I will not elaborate it anymore. It is much better to start coding something useful in the “naïve” way.

Let’s start!

My assumption is that you are total beginner in Python and that you are using Microsoft Windows environment. Just to mention that switch to Linux is very easy since Python is almost fully multiplatform language.

**Step 1: Set your Python development environment**
a) Install Python on your windows machine.
- go to the https://www.python.org/downloads/windows/ to get Latest Python 3 Release and download the windows installer (e.g. Windows x86-64 executable installer)
- run it the installer.
- check the option "Add Python 3.x to PATH" on the first screen and click Next
- on next screen choose "Customize installation" and check all options ("Documentation", "pip", "tcl/tk and IDLE", "Python test suite", "py launcher", "for all users..." and click Next
- on the next screen just Customize install location (e.g. C:\Python38)

b) add Python to Path - in order for Python commands to available at the windows command prompt we have to do the following
- search for "environment variables" term in windows search
- choose option "Edit the system environment variables" and select "Environment Variables"
- under the "System variables" double click at "Path" item
- in the dialog select option "New" and each time add following entries:
            C:\Python38\
            C:\Python38\Scripts\
            C:\Python38\Lib\site-packages\PyInstaller\
- click OK to close dialogs


c) install version control - this is optional (GIT is my choice)
- go to https://git-scm.com/download/win
- download GIT version control installer and run it with all default settings

d) install additional python tools and libraries - this will be used to enable copying of images from clipboard to our app
- search for "cmd" term in windows search and select "Command Prompt"
python -m pip install --upgrade pip
pip install pyinstaller
pip install pillow

e) install tool (IDE) for your programing needs (PyCharm is my choice)
- go to https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC
- download and run installer with all default settings


**Step 2: let's start project**
- Start PyCharm and select "Create new project"
    -> at Location text box enter following path:"C:\Users\<*put your user name here*>\Desktop\MyPython\PyNotePlus" and this will create project location on your desktop.
    -> expand section "Project Interpreter: New Virtualenv environment" and select "Existing interpreter" and click button with "...". The new dialog will open and you select "System Interpreter" (e.g. C:\Python38\python.exe) and click OK.
- Now you will see your development environment :) and I hope this is a love at first sight.
    -> on the left side (tree view) right click at "PyNotePlus" under "Project" and select New -> Python File and provide Name "PyNotePlus". Here is where the whole program code will be placed.
    -> get the code from link below (or from provided PyNotePlus.py file) and copy it.
    -> pass the code the right side of the editor window in PyCharm.
- Review the code!
    -> every line of the code is well documented and you will have basic idea how all works.
- Run the App for the first time from PyCharm
    -> right click at the "PyNotePlus.py" file and choose "Run'PyNotePlus'"
    -> Python interpreter will do its magic and code will be interpreted in beautiful desktop application that will pop up in front of all windows. Ok, it is not most beautiful app but it is defenetly useful. It is great utility tool which can be used as adttionla clipborad for text and for image pasting. It is useful when you have to compare or copy data between applications. It will stay always on top.

(optional) you can also add your project to your GIT version control: VCS -> Import into Version Control -> Create Git Repository... and click OK

**Step 3: final touch, package everything in the portable python desktop application**
As you maybe noticed above, we installed "pyinstaller" tool.
- search for "cmd" term in windows search and select "Command Prompt". Console window will appear.
- position yourself to location of your project by writing the following command in console window:
    cd C:\Users\<*put your user name here*>\Desktop\MyPython\PyNotePlus
- build executable by writing the following command in console window:
    pyinstaller --noconsole --onefile PyNotePlus.py
- open File Explorer App on your windows and go to: "C:\Users\<*put your user name here*>\Desktop\MyPython\PyNotePlus\dist"
- here you will find your application "PyNotePlus.exe" ready for usage and sharing with your friends.



