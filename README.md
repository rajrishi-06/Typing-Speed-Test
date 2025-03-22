```markdown
# Typing Speed Test

A simple, interactive, and customizable typing speed test that helps improve your typing skills with dynamic feedback, unique typewriter key sounds, and detailed performance metrics.

---

## Overview

The Typing Speed Test application is built using Python's Tkinter for the user interface, Pillow for image handling, and Pygame for sound effects. The app displays a splash screen, lets you configure options (keyboard type, skill level, time limit, hit effect color), and then starts a typing test on a randomly chosen paragraph. As you type, the app plays unique typewriter sounds for each correct key and an error sound for any incorrect key. When the test is finished (either by completing the text or when time runs out), it calculates and displays your Words Per Minute (WPM), accuracy, and other statistics.

---

## Features

- **Splash Screen:** Displays a typewriter image and a loading message.
- **Configuration Options:** Choose keyboard layout (Mac/Windows), skill level (easy, medium, hard), time limit (predefined or custom), and key hit effect color.
- **Typing Test:** The app presents a random paragraph to type.
- **Dynamic Feedback:** Plays unique typewriter sounds for correct key presses and an error sound for incorrect entries.
- **Automatic Scrolling:** Keeps the current character visible as you type.
- **Performance Metrics:** Calculates WPM, accuracy, total correct characters, and wrong keys.

---

## Requirements

To run the project locally, you will need:

- **Python 3.x:** It is recommended to use an official CPython distribution (download from [python.org](https://www.python.org/downloads/)).
- **Tkinter:** Usually comes pre-installed with Python.
- **Pillow:** For handling images.
- **Pygame:** For playing sounds.
- **FFmpeg (Optional):** If you plan to work with audio conversions or use additional audio formats, install FFmpeg.

### Installing Dependencies

Open your terminal (or command prompt) and run:

```bash
pip install pillow pygame
```

> **Note:** Tkinter is typically included with Python installations on Windows and macOS. If not, refer to your operating system’s package manager or documentation.

---

## Running the Application Locally

1. **Clone or Download the Repository:**
   - **Clone:**  
     ```bash
     git clone https://github.com/yourusername/typing-speed-test.git
     cd typing-speed-test
     ```
   - **Download:**  
     Download the ZIP file from the repository’s GitHub page and extract it.

2. **Organize Resources:**
   - Ensure you have the following directories in the project root:
     - `data/` — Contains text files (e.g., `easy.txt`, `medium.txt`, `hard.txt`) used for the typing tests.
     - `sound-track/` — Contains sound files:
       - Individual typewriter key sounds (`A.wav`, `B.wav`, …, `Z.wav`)
       - `default.wav` for any undefined key.
       - `error.wav` for wrong key presses.
     - Images such as `typewriter.webp` should be in the same directory or an accessible folder (the `resource_path` function will handle this when packaged).

3. **Run the Application:**

   In your terminal, run:

   ```bash
   python your_script_name.py
   ```

   Replace `your_script_name.py` with the name of the main Python file (for example, `typing_test_app.py`).

4. **Using the Application:**

   - **Splash Screen:**  
     When the app launches, a splash screen appears with a typewriter image and a “Loading...” message.
   
   - **Configuration Screen:**  
     After a few seconds, the configuration screen lets you:
     - Choose the **Keyboard Type** (Mac or Windows).
     - Select **Skill Level** (easy, medium, hard).
     - Set the **Time Limit** (choose from 1, 3, 5 minutes or a custom value).
     - Pick a **Keyboard Hit Color** using the color chooser.
     - Click **Start Test** to begin.
   
   - **Typing Test Screen:**  
     The test screen displays a randomly chosen paragraph. As you type:
     - Correct key presses play unique typewriter sounds.
     - Incorrect key presses trigger an error sound.
     - The current character is highlighted and auto-scrolled into view.
     - A timer counts down based on your selected time limit.
   
   - **Results:**  
     Once you finish the text or time runs out, the app calculates your WPM, accuracy, and displays your results.

---

## Downloadable Releases

If you prefer not to run the application from source, downloadable executables are available:

- **Windows (.exe inside ZIP)** → [Typing_Speed_Test_Windows_v1.0.zip](https://github.com/rajrishi-06/Typing-Speed-Test/releases/download/v1.0.0/Typing_Speed_Test_Windows_v1.0.zip)
- **macOS (.app inside ZIP)** → [Typing_Speed_Test_MacOSx_v1.0.zip](https://github.com/rajrishi-06/Typing-Speed-Test/releases/download/v1.0.0/Typing_Speed_Test_MacOSx_v1.0.zip)

After downloading:


- **On Windows:** Run the executable or extract and run the ZIP file.
- **On macOS:** Open the `.app` file. If macOS security settings prevent launching the app, right-click on it and select **Open**.

---

## Packaging with PyInstaller

If you wish to create your own executable, you can use [PyInstaller](https://www.pyinstaller.org/):

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Create an executable:
   ```bash
   pyinstaller --onefile --windowed your_script_name.py
   ```

   This command creates a single-file executable in the `dist` folder. The `resource_path` function in the code ensures that resources are properly located in the packaged app.

---

## Contributing

Contributions are welcome! If you have suggestions or bug fixes, please fork the repository and create a pull request. For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is open-source.

---

Enjoy the Typing Speed Test and happy typing!
