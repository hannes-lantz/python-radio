import vlc
from termcolor import colored

urls = {
    "1": {"name": "P1", "url": "https://http-live.sr.se/p1-mp3-128"},
    "2": {"name": "P2", "url": "https://http-live.sr.se/p2-mp3-128"},
    "3": {"name": "P3", "url": "https://http-live.sr.se/p3-mp3-128"},
    "4": {"name": "P4", "url": "https://http-live.sr.se/p4malmo-mp3-128"},
    "5": {"name": "RIX FM", "url": "https://fm01-ice.stream.khz.se/fm01_mp3"},
    "6": {"name": "Bandit Rock", "url": "https://fm02-ice.stream.khz.se/fm02_mp3"},
    "7": {"name": "P3 Din Gata", "url": "https://live-cdn.sr.se/pool3/dingata/dingata.isml/dingata-audio=192000.m3u8"},
    "8": {"name": "Mix Megapol", "url": "http://tx-bauerse.sharp-stream.com/http_live.php?i=mixmegapol_instream_se_mp3"},
    "9": {"name": "NRJ", "url": "http://tx-bauerse.sharp-stream.com/http_live.php?i=nrj_instreamtest_se_mp3"}
}

# Create VLC instance
instance = vlc.Instance()
instance.log_unset()

# Create media player
player = instance.media_player_new()

# Print the menu
def print_menu():
    print(colored('╔═════════════════════════════════════════════╗', 'green'))
    print(colored('║            Select a radio station:          ║', 'green'))
    print(colored('║                                             ║', 'green'))
    for key, value in urls.items():
        print(colored('║', 'green') + colored(f"  {key}: {value['name']: <40}", 'magenta') + colored('║', 'green'))
    print(colored('║                                             ║', 'green'))
    print(colored('╚═════════════════════════════════════════════╝', 'green'))

# Function to play the selected URL
def play_url(url):
    media = instance.media_new(url)
    player.set_media(media)
    player.play()

# Main program loop
while True:
    print_menu()
    selection = input("Enter the station number (1-9), or 'q' to quit: ")

    if selection == "q":
        break

    if selection in urls:
        print(colored('=================================================', 'green'))
        print(colored("Now playing: " + urls[selection]["name"], 'magenta'))

        selected_url = urls[selection]["url"]
        play_url(selected_url)
        while player.get_state() != vlc.State.Ended:
            selection = input("Enter 'q' to go back: ")
            if selection == "q":
                break
            pass
        player.stop()

# Release the player and instance
player.release()
instance.release()
