
# AutoType

AutoType is a simple text expander for Linux. It is sort of like Autokey, except it works off of text files that you put in your `~/AutoType` directory. AutoType is a 
python3 script that uses pyautogui to let you type an abbreviation for something and it expands to whatever you have in the matching text file.

## Installation

1. Put `AutoType.py` somewhere on your system, perhaps your `~/bin` directory.
2. Create a keyboard shortcut that calls `~/bin/AutoType.py`
```
For example for Gnome you can :
go to "Setting > Keyboard-Shortcuts"  and create a keyboard shortcut like this:

name: AutoType
command: /usr/bin/python3 /home/yourName/bin/AutoType.py
shortcut: Ctrl+Shift+Q
```
3. Create a `~/AutoTypeFiles` directory where you store text files for expanding abbreviations




If those aren't already installed on your system you can install them from pip package manager without any trouble. 


```
pip install PyQt5 
sudo apt install pyautogui 
```

## Usage

The text expansion files reside in your `~/AutoTypeFiles` directory and can be organized in subdirectories. 
Name the files in the format of `abbreviation` where the filename is the thing you want to type and the content of the file is what
you want to have pasted into your document.

I have `Ctrl+Shift+Q` assigned to run `~/bin/AutoType.py`. 
So, if I'm typing an email, it doesn't matter if I'm in gmail (using Firefox, Chrome, Opera, or Vivaldi),
Thunderbird, Vim, or Nylas, the workflow is the same. 
I have a couple different email signatures that I use. 
For example, if want to use my email signature, 
I'll create a file `~/AutoType/sign.txt` that has all of my contact information.


### How To Use AutoType

After setting up the keyboard shortcut to launch AutoType, to use AutoType:

- Put your cursor where you want your text to be typed
- Type `Ctrl+Shift+Q` (or whatever keyboard shortcut you set up)
- A window will appear asking for your text file
- Select one of your file and hit Enter (or click "Start Typing")
- The contents of `~/AutoType/yourFile.txt` is typed into your document


## Contributing

1. Fork AutoType
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D



## Credits

Written by Ali Sharifi Neyestani

## License

MIT License 
