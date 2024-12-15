import pyautogui
import random
import time
import subprocess

# List of common words to create meaningful search queries
words = [
    "python", "automation", "tutorial", "programming", "code", 
    "development", "machine", "learning", "data", "science", 
    "artificial", "intelligence", "web", "design", "software", 
    "engineering", "algorithm", "database", "network", "security"
]

def generate_random_query():
    # Generate a random query using a combination of words
    return ' '.join(random.choices(words, k=random.randint(1, 3)))  # Randomly choose 1 to 3 words

def open_bing_and_search(query):
    # Open Microsoft Edge and go to Bing
    subprocess.Popen(['start', 'msedge', 'https://www.bing.com/?form=ML2PCO'], shell=True)
    time.sleep(5)  # Wait for the browser to open and load the page

    # Type the search query into the Bing search box
    pyautogui.write(query, interval=0.1)  # Type the query with a slight delay between each character
    pyautogui.press('enter')  # Press Enter to perform the search

    time.sleep(5)  # Wait for the search results to load

    # Close the browser tab
    pyautogui.hotkey('ctrl', 'w')  # This closes the current tab

def main():
    while True:  # Non-stoppable loop
        random_query = generate_random_query()
        print(f"Searching for: {random_query}")
        open_bing_and_search(random_query)
        time.sleep(1)  # Wait for 1 second before the next search

if __name__ == "__main__":
    main()