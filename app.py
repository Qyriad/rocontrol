#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox, filedialog
import os, sys
import subprocess

fuseeLauncherDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fusee-launcher/") # build path for fusee-launcher dir
fuseeFilePath = os.path.join(fuseeLauncherDir, "fusee-launcher.py") # build path for fusee-launcher file

top = Tk()
top.title("Interface de Fusée")

titleLabel = Label(top, text="Interface de Fusée")

titleLabel.pack()

# fusee error/result code explainer messages
fuseeCodeMessages = ["Done!", "It seems like your Switch isn't plugged in.", "No access to USB. (you should probably re-run the interface script with sudo or Administrator privileges)", "It seems like your Switch isn't on an XHCI backend. Try plugging it in into a USB 3.0 (blue) port.", "Unknown Fusée Gelée error. (try running it on it's own and see what's up)"]

def fusee_exec(payload):
    """
    Executes fusée gelée from a payload file path.

    Arguments:
     * payload - Payload path
    
    Returns: return code
     * 0: A-OK
     * 1: Your Switch isn't plugged in.
     * 2: No access to USB. (re-run w/ sudo, probably)
     * 3: The Switch isn't plugged into an XHCI backend.
     * 4: Unknown Fusée Gelée error.
    """

    result = 0 # default result

    p = subprocess.Popen([sys.executable, fuseeFilePath, payload, '--relocator', os.path.join(fuseeLauncherDir, 'intermezzo.bin')], stdout=subprocess.PIPE, stderr=subprocess.PIPE) # run fusée gelée
    p.wait() # wait for it to close

    output = p.stdout.read().decode("utf-8")
    errout = p.stderr.read().decode("utf-8")
    print(output)
    print(errout)

    if output.lower().startswith("no") and p.returncode == 255: # No TegraRCM device found?
        result = 1
    elif "errno 13" in errout.lower() and p.returncode == 1: # Errno 13: Access Denied (for USB)
        result = 2
    elif "This device needs to be on an XHCI backend." in output and p.returncode == 0:
        result = 3
    elif p.returncode != 0:
        result = 4

    return result

def launch_callback():
    payloadpath = filedialog.askopenfilename(title = "Select payload file", filetypes = [("Payload files", "*.bin")])
    if len(payloadpath) == 0:
        messagebox.showerror("Interface de Fusée", "Please select a file.")
        return
    
    res = fusee_exec(payloadpath)
    if res == 0:
        messagebox.showinfo("Interface de Fusée", fuseeCodeMessages[res])
    else:
        messagebox.showerror("Interface de Fusée", fuseeCodeMessages[res])
        

launchButton = Button(top, text="Launch", command=launch_callback)

launchButton.pack()

if __name__ == "__main__":
    top.mainloop()
