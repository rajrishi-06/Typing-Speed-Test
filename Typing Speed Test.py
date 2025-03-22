import tkinter as tk
from tkinter import font, messagebox
from tkinter import colorchooser
import string
import time
import random
from PIL import Image, ImageTk  # For handling images
import pygame  # For playing sounds
import sys, os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

pygame.mixer.init()
error_sound = pygame.mixer.Sound(resource_path("sound-track/error.wav"))

key_sounds = {
    "A": pygame.mixer.Sound(resource_path("sound-track/A.wav")),
    "B": pygame.mixer.Sound(resource_path("sound-track/B.wav")),
    "C": pygame.mixer.Sound(resource_path("sound-track/C.wav")),
    "D": pygame.mixer.Sound(resource_path("sound-track/D.wav")),
    "E": pygame.mixer.Sound(resource_path("sound-track/E.wav")),
    "F": pygame.mixer.Sound(resource_path("sound-track/F.wav")),
    "G": pygame.mixer.Sound(resource_path("sound-track/G.wav")),
    "H": pygame.mixer.Sound(resource_path("sound-track/H.wav")),
    "I": pygame.mixer.Sound(resource_path("sound-track/I.wav")),
    "J": pygame.mixer.Sound(resource_path("sound-track/J.wav")),
    "K": pygame.mixer.Sound(resource_path("sound-track/K.wav")),
    "L": pygame.mixer.Sound(resource_path("sound-track/L.wav")),
    "M": pygame.mixer.Sound(resource_path("sound-track/M.wav")),
    "N": pygame.mixer.Sound(resource_path("sound-track/N.wav")),
    "O": pygame.mixer.Sound(resource_path("sound-track/O.wav")),
    "P": pygame.mixer.Sound(resource_path("sound-track/P.wav")),
    "Q": pygame.mixer.Sound(resource_path("sound-track/Q.wav")),
    "R": pygame.mixer.Sound(resource_path("sound-track/R.wav")),
    "S": pygame.mixer.Sound(resource_path("sound-track/S.wav")),
    "T": pygame.mixer.Sound(resource_path("sound-track/T.wav")),
    "U": pygame.mixer.Sound(resource_path("sound-track/U.wav")),
    "V": pygame.mixer.Sound(resource_path("sound-track/V.wav")),
    "W": pygame.mixer.Sound(resource_path("sound-track/W.wav")),
    "X": pygame.mixer.Sound(resource_path("sound-track/X.wav")),
    "Y": pygame.mixer.Sound(resource_path("sound-track/Y.wav")),
    "Z": pygame.mixer.Sound(resource_path("sound-track/Z.wav")),
}

default_sound = pygame.mixer.Sound(resource_path("sound-track/default.wav"))
def play_key_sound(key):
    sound = key_sounds.get(key.upper(), default_sound)
    sound.play()

# Constants for keyboard drawing
KEY_WIDTH = 50
KEY_HEIGHT = 50
KEY_SPACING_X = 5
KEY_SPACING_Y = 5
START_X = 10
START_Y = 10

# Sample keyboard layouts (Mac and Windows)
mac_layout = [
    ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', ('BachSpace', 2)],
    [('Tab', 2), 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
    [('CapsLock', 2), 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'", ('Enter', 2)],
    [('Shift', 2), 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', ('Shift_R', 2), '🔼'],
    ['Fn', 'Control', 'Option', ('⌘', 1), ('Space', 6), ('⌘-', 1), 'Option_R', '⬅️', '⬇️', '➡️'],
]

windows_layout = [
    ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', ('BackSpace', 2)],
    [('Tab', 2), 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
    [('CapsLock', 2), 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'", ('Enter', 2)],
    [('Shift', 2), 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', ('Shift_R', 2), '🔼'],
    [('Ctrl', 1), ('Win', 1), ('Alt', 1), ('Space', 6), ('AltGr', 1), ('Menu', 1), ('Ctrl', 1), '⬅️', '⬇️', '➡️'],
]


class TypingTestApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing 🚄 Test")
        self.master.geometry("900x700")

        # Containers for different screens
        self.splash_frame = tk.Frame(master)
        self.config_frame = tk.Frame(master)
        self.test_frame = tk.Frame(master)

        # Configuration variables
        self.user_mode = tk.StringVar(value="easy")
        self.time_option = tk.StringVar(value="5")
        self.custom_time = tk.StringVar()
        self.keyboard_type = tk.StringVar(value="mac")
        self.time_limit = 5  # default in minutes
        self.hit_color = tk.StringVar(value="#4C585B")
        self.hit_color.trace_add("write", self.update_hit_color_display)

        # For the test screen
        self.text = ""
        self.current_index = 0
        self.timer_started = False
        self.start_time = None
        self.timer_id = None

        # New variables for tracking progress
        self.no_of_wrongs = 0  # counts the number of wrong key presses

        # Create the three screens
        self.create_splash_screen()
        self.create_config_screen()
        self.create_test_screen()  # Setup will be done in setup_test_screen()


        # Start with splash screen, then move to config screen after 2 seconds
        self.show_frame(self.splash_frame)
        self.master.after(5000, lambda: self.show_frame(self.config_frame))

    def show_frame(self, frame):
        for f in (self.splash_frame, self.config_frame, self.test_frame):
            f.pack_forget()
        frame.pack(fill="both", expand=True)

    def create_splash_screen(self):
        self.splash_frame.configure(bg="white")
        try:
            image = Image.open(resource_path("typewriter.webp"))
            self.typewriter_img = ImageTk.PhotoImage(image)
            img_label = tk.Label(self.splash_frame, image=self.typewriter_img, bg="white")
            img_label.pack(pady=20)
        except Exception as e:
            img_label = tk.Label(self.splash_frame, text="Typewriter Image", font=("Helvetica", 20), bg="white")
            img_label.pack(pady=20)
        loading_label = tk.Label(self.splash_frame, text="Loading...", font=("Helvetica", 16), bg="white")
        loading_label.pack(pady=10)

    def create_config_screen(self):
        frame = self.config_frame
        # Create a container frame with two columns:
        container = tk.Frame(frame)
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # Left side: Image (left half of the original typewriter.png)
        left_frame = tk.Frame(container)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=10)
        try:
            full_image = Image.open(resource_path("typewriter.webp"))
            width, height = full_image.size
            # Crop the left half of the image
            left_half = full_image.crop((0, 0, width // 2, height))
            self.typewriter_half = ImageTk.PhotoImage(left_half)
            img_label = tk.Label(left_frame, image=self.typewriter_half)
            img_label.pack(pady=10)
        except Exception as e:
            img_label = tk.Label(left_frame, text="Typewriter Image", font=("Helvetica", 20))
            img_label.pack(pady=10)

        # Right side: Options
        right_frame = tk.Frame(container)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=10)

        # Title
        title = tk.Label(right_frame, text="Configure Your Typing Test", font=("Helvetica", 20))
        title.pack(pady=10)

        # Keyboard type selection
        kb_frame = tk.LabelFrame(right_frame, text="Keyboard Type", padx=10, pady=10)
        kb_frame.pack(pady=10, fill="x")
        for kb in ["mac", "windows"]:
            rb = tk.Radiobutton(kb_frame, text=kb.capitalize(), variable=self.keyboard_type, value=kb)
            rb.pack(side="left", padx=10)
        # Keyboard Hit Effect Color selection using a color picker
        hit_color_frame = tk.LabelFrame(right_frame, text="Keyboard Hit Color", padx=10, pady=10)
        hit_color_frame.pack(pady=10, fill="x")
        choose_button = tk.Button(hit_color_frame, text="Select Color", command=self.choose_hit_color)
        choose_button.pack(side="left", padx=5)
        # Display the currently chosen color
        self.hit_color_display = tk.Label(hit_color_frame, textvariable=self.hit_color, bg=self.hit_color.get(),
                                          width=10)
        self.hit_color_display.pack(side="left", padx=5)

        # Skill level selection
        level_frame = tk.LabelFrame(right_frame, text="Skill Level", padx=10, pady=10)
        level_frame.pack(pady=10, fill="x")
        for level in ["easy", "medium", "hard"]:
            rb = tk.Radiobutton(level_frame, text=level.capitalize(), variable=self.user_mode, value=level)
            rb.pack(side="left", padx=10)

        # Time limit selection
        time_frame = tk.LabelFrame(right_frame, text="Time Limit (minutes)", padx=10, pady=10)
        time_frame.pack(pady=10, fill="x")
        for t in [1, 3, 5]:
            rb = tk.Radiobutton(time_frame, text=str(t), variable=self.time_option, value=str(t),
                                command=self.disable_custom)
            rb.pack(side="left", padx=10)
        rb_custom = tk.Radiobutton(time_frame, text="Custom", variable=self.time_option, value="custom",
                                   command=self.enable_custom)
        rb_custom.pack(side="left", padx=10)
        self.custom_time_entry = tk.Entry(time_frame, textvariable=self.custom_time, state="disabled", width=5)
        self.custom_time_entry.pack(side="left", padx=10)
        # Label "mins" beside the custom timer chooser
        custom_label = tk.Label(time_frame, text="mins")
        custom_label.pack(side="left", padx=5)

        # Start button
        start_button = tk.Button(right_frame, text="Start Test", font=("Helvetica", 16), command=self.start_test)
        start_button.pack(pady=20)

        # Ensure both columns expand equally
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)

    def disable_custom(self):
        self.custom_time_entry.config(state="disabled")

    def enable_custom(self):
        self.custom_time_entry.config(state="normal")

    def start_test(self):
        # Determine the time limit
        if self.time_option.get() == "custom":
            try:
                self.time_limit = int(self.custom_time.get())
                if self.time_limit <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid positive integer for custom time.")
                return
        else:
            self.time_limit = int(self.time_option.get())

        # Load text from file based on user mode
        try:
            with open(f"data/{self.user_mode.get()}.txt", "r", encoding="utf-8") as file:
                lines = file.read().splitlines()
        except Exception as e:
            messagebox.showerror("File Error", f"Could not load text file for mode {self.user_mode.get()}.")
            return

        # Assume paragraphs are on rows 1, 3, 5, etc.
        paragraph_candidates = [line for idx, line in enumerate(lines) if idx % 2 == 0 and line.strip() != ""]
        if not paragraph_candidates:
            messagebox.showerror("Data Error", "No paragraphs found in the data file.")
            return

        # Choose a random paragraph
        self.text = random.choice(paragraph_candidates)

        # Reset index, timer, and wrong key counter
        self.current_index = 0
        self.timer_started = False
        self.start_time = None
        self.no_of_wrongs = 0

        self.setup_test_screen()
        self.show_frame(self.test_frame)

    def create_test_screen(self):
        """Placeholder; setup_test_screen() will configure the test screen."""
        pass

    def setup_test_screen(self):
        # Clear the test_frame
        for widget in self.test_frame.winfo_children():
            widget.destroy()

        # Create a plain frame (with a darker background) for the text widget and timer
        top_frame = tk.Frame(self.test_frame, bg="#D3D3D3", padx=20, pady=20)
        top_frame.pack(pady=20)

        # Custom font for the typing window
        custom_font = font.Font(family="Helvetica", size=24)
        # Create the Text widget using the original text
        text_widget = tk.Text(top_frame, state="normal", width=100, height=8, font=custom_font)
        text_widget.pack(ipadx=10, ipady=10)  # Added internal padding
        text_widget.insert("1.0", self.text)
        text_widget.config(state="disabled")
        # Configure tag for highlighting the current character
        text_widget.tag_configure("current", background="yellow")
        self.text_widget = text_widget

        # Timer placed below the text widget
        self.timer_label = tk.Label(top_frame, text=f"Time: {self.time_limit:02d}:00", font=("Helvetica", 16),
                                    bg="#D3D3D3")
        self.timer_label.pack(pady=(10, 0))

        # Create the keyboard canvas below the top frame
        self.canvas = tk.Canvas(self.test_frame, bg="white", width=837, height=280)
        self.canvas.pack(pady=20)
        layout = mac_layout if self.keyboard_type.get() == "mac" else windows_layout
        self.key_items = self.draw_keyboard(self.canvas, layout)

        # Bind key events for typing simulation and key highlighting
        self.master.bind("<Key>", self.simulate_typing)
        self.master.bind_all("<KeyPress>", self.on_key_press)
        self.master.focus_force()

        # Highlight the first character and ensure it's visible
        self.update_cursor()

    def update_hit_color_display(self, *args):
        self.hit_color_display.config(bg=self.hit_color.get())
    def choose_hit_color(self):
        # Open a color chooser dialog with the current hit color as the initial value.
        color = colorchooser.askcolor(title="Choose Hit Effect Color", initialcolor=self.hit_color.get())
        if color[1] is not None:
            self.hit_color.set(color[1])

    def draw_keyboard(self, canvas, layout):
        key_items = {}
        y = START_Y
        for row in layout:
            x = START_X
            for key_item in row:
                if isinstance(key_item, tuple):
                    key, span = key_item
                else:
                    key = key_item
                    span = 1
                width = KEY_WIDTH * span + KEY_SPACING_X * (span - 1)
                rect = canvas.create_rectangle(
                    x, y, x + width, y + KEY_HEIGHT,
                    fill="lightgray", outline="black"
                )
                canvas.create_text(
                    x + width / 2,
                    y + KEY_HEIGHT / 2,
                    text=key,
                    font=("Helvetica", 14)
                )
                key_items[key] = rect
                x += width + KEY_SPACING_X
            y += KEY_HEIGHT + KEY_SPACING_Y
        return key_items

    def highlight_key(self, canvas, key_items, key_label):
        if key_label in key_items:
            rect_id = key_items[key_label]
            # Use the user-defined hit color
            hit_color = self.hit_color.get()
            canvas.itemconfig(rect_id, fill=hit_color)
            canvas.after(100, lambda: canvas.itemconfig(rect_id, fill="lightgray"))
        else:
            print(f"No key found for: {key_label}")

    def on_key_press(self, event):
        key_map = {
            "space": "Space",
            "Return": "Enter",
            "BackSpace": "BackSpace",
            "Shift_L": "Shift",
            "Shift_R": "Shift_R",
            "Control_L": "Control",
            "Control_R": "Control",
            "Alt_L": "Option",  # For mac, left Alt as Option
            "Alt_R": "Option_R",  # For mac, right Alt as Option_R
            "Alt": "Option",
            "AltGr": "Option_R",
            "grave": "`",
            "minus": "-",
            "equal": "=",
            "bracketleft": "[",
            "bracketright": "]",
            "backslash": "\\",
            "Caps_Lock": "CapsLock",
            "semicolon": ";",
            "apostrophe": "'",
            "comma": ",",
            "period": ".",
            "slash": "/",
            "Super_L": "⌘",  # Map Super_L to Command (⌘)
            "Up": "🔼",
            "Down": "⬇️",
            "Left": "⬅️",
            "Right": "➡️",
            "Meta_R": "⌘-",
            "Meta_L": "⌘",
        }

        if event.keysym in string.ascii_lowercase:
            display_key = event.keysym.upper()
        else:
            display_key = key_map.get(event.keysym, event.keysym)
        self.highlight_key(self.canvas, self.key_items, display_key)

    def update_cursor(self):
        self.text_widget.tag_remove("current", "1.0", tk.END)
        if self.current_index < len(self.text):
            pos = f"1.{self.current_index}"
            self.text_widget.tag_add("current", pos, f"1.{self.current_index + 1}")
            self.text_widget.see(pos)  # Auto-scroll to show current character
        else:
            self.text_widget.tag_remove("current", "1.0", tk.END)

    def filterKey(self, key):
        allowed_chars = string.ascii_letters + string.digits + string.punctuation + " "
        if key and key in allowed_chars:
            return key
        else:
            return None

    def change_to_red_cursor(self):
        self.text_widget.tag_config("current", background="red")

    def change_to_yellow_cursor(self):
        self.text_widget.tag_config("current", background="yellow")

    def simulate_typing(self, event):
        ch = self.filterKey(event.char)
        if ch is None:
            return
        if not self.timer_started:
            self.timer_started = True
            self.start_time = time.time()
            self.update_timer()
        # If correct key pressed, update progress; otherwise, record wrong key.
        if self.current_index < len(self.text) and ch == self.text[self.current_index]:
            self.current_index += 1
            self.change_to_yellow_cursor()
            self.update_cursor()
            play_key_sound(ch)
            # End test if entire paragraph is completed
            if self.current_index >= len(self.text):
                self.end_test()
        else:
            self.no_of_wrongs += 1
            self.change_to_red_cursor()
            if error_sound:
                error_sound.play()

    def update_timer(self):
        elapsed = int(time.time() - self.start_time)
        remaining = self.time_limit * 60 - elapsed
        if remaining <= 0:
            self.timer_label.config(text="Time: 00:00")
            self.end_test()
        else:
            mins, secs = divmod(remaining, 60)
            self.timer_label.config(text=f"Time: {mins:02d}:{secs:02d}")
            self.timer_id = self.master.after(1000, self.update_timer)

    def end_test(self):
        # Unbind key events so no further input is processed
        self.master.unbind("<Key>")
        self.master.unbind_all("<KeyPress>")
        # Calculate and display the results (simulate sending data to an API)
        self.show_results()

    def show_results(self):
        # Calculate elapsed time in seconds (if timer started)
        elapsed = time.time() - self.start_time if self.start_time else 0
        correct_chars = self.current_index
        wrong_keys = self.no_of_wrongs
        # Standard calculation: one word is considered as 5 characters.
        wpm = (correct_chars / 5) / (elapsed / 60) if elapsed > 0 else 0
        accuracy = (correct_chars / (correct_chars + wrong_keys) * 100) if (correct_chars + wrong_keys) > 0 else 0
        result_str = (
            f"Results:\n"
            f"WPM: {wpm:.2f}\n"
            f"Accuracy: {accuracy:.2f}%\n"
            f"Correct Characters: {correct_chars}\n"
            f"Wrong Keys: {wrong_keys}"
        )
        # Simulate sending data to an external API by printing/logging the payload.
        messagebox.showinfo("Test Results", result_str)


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()
