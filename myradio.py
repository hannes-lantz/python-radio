import vlc
from termcolor import colored

urls = {
    "1": {"name": "P1", "url": "https://http-live.sr.se/p1-mp3-128"},
    "2": {"name": "P2", "url": "https://http-live.sr.se/p2-mp3-128"},
    "3": {"name": "P3", "url": "https://http-live.sr.se/p3-mp3-128"},
    "4": {"name": "P4", "url": "https://http-live.sr.se/p4malmo-mp3-128"},
    "5": {"name": "RIX FM", "url": "https://fm01-ice.stream.khz.se/fm01_mp3"}
}

# Create VLC instance
instance = vlc.Instance()

# Create media player
player = instance.media_player_new()

# Print the menu
def print_menu():
    print(colored('-------------------------------------------------', 'green'))
    print("Select a radio station:")
    for key, value in urls.items():
        print(colored(f"{key}: {value['name']}", 'yellow'))
    print(colored('-------------------------------------------------', 'green'))

# Function to play the selected URL
def play_url(url):
    print(colored('-------------------------------------------------', 'yellow'))
    print(colored("Now playing: " f"{url}", 'green'))
    media = instance.media_new(url)
    player.set_media(media)
    player.play()

# Main program loop
while True:
    print_menu()
    selection = input("Enter the station number (1-4), or 'q' to quit: ")

    if selection == "q":
        break

    if selection in urls:
        selected_url = urls[selection]["url"]
        play_url(selected_url)
        while player.get_state() != vlc.State.Ended:
            selection = input("Enter 'q' to quit: ")
            if selection == "q":
                break
            pass
        player.stop()

# Release the player and instance
player.release()
instance.release()
