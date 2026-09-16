# run this in the terminal: 
python app.py

# then a cool webapp with several OK buttons will be loaded


########################## installation #################################

# install whats needed
pip install -r requerements.txt

# if your are using linux:
sudo apt install xclip





##################### what can the OK buttons do ########################

acording to you creativity, here are examples of things the OK button can do: 
 1 copy commands to be pasted in some terminal or script
 2 send commands to execution
 3 send tcl script to execution by vmd, ( but that only works if the vmd has been oppended with a socket)


########### to add a new ok button in the webapp, you do this: ##########

1-create a function on myfuncions.py
2-define the page structure in config.json

in each expandable box, be sure to put in the key inputbox (with some number so that the key is unique) or radiobutton (with a number too) or ok_button
in the "ok_button" key, you should put the function to be called whe the OK button is clicked. 
the arguments will be everithing set in the imput boxes of that section. 
be sure to set the arguments properly in the function definition so to match what will be sent



"inputbox1": "xxx",
"droplist1": ["xxx",
              "xxx",
              "xxx"],
"radiobutton1": "xxx",
"plaintext1": "xxx",



def send_tcl_to_VMD_xxxxxxx():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "xxxxxxx"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'



def call_xxxxx():
    """This function calls a function in cleanpipe directly"""

    import cleanpipe as cl
    
    # call function
    cl.xxxxx()

    return "cl.xxxxx() was called directly"



def clipboard_xxxxxxx():
    """This function sends a text to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"xxxxxxx")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"