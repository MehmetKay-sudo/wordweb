import tkinter as tk
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize

def analyze_text():
    text = text_entry.get("1.0", "end-1c")  # Get the text from the input field
    tokens = word_tokenize(text)  # Tokenize the text using NLTK
    words = [word.lower() for word in tokens]  # Convert words to lowercase
    word_counts = Counter(words)
    frequencies = "\n".join([f"{word}: {count}" for word, count in word_counts.items()])
    results_text.delete("1.0", tk.END)  # Clear previous results
    results_text.insert(tk.END, frequencies)  # Display the frequencies

# Create the main window
window = tk.Tk()
window.title("Word Frequency Analyzer")

# Create the input field for text
text_entry = tk.Text(window, height=10, width=40)
text_entry.pack()

# Create the "Analyze" button
analyze_button = tk.Button(window, text="Analyze", command=analyze_text)
analyze_button.pack()

# Create the text area for displaying the frequencies
results_text = tk.Text(window, height=10, width=40)
results_text.pack()

# Download necessary NLTK data (only required once)
nltk.download("punkt")

# Start the GUI main loop
window.mainloop()
