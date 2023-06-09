import curses
import vlc

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

logo_1 = r"""
               _ _       
              | (_)      
 _ __ __ _  __| |_  ___  
| '__/ _` |/ _` | |/ _ \ 
| | | (_| | (_| | | (_) |
|_|  \__,_|\__,_|_|\___/ 
"""


# Create VLC instance
instance = vlc.Instance()
instance.log_unset()

# Create media player
player = instance.media_player_new()

def print_menu(stdscr):
    stdscr.clear()
    stdscr.attron(curses.color_pair(2))
    stdscr.border()
    stdscr.addstr(0, 2, "Select a radio station:", curses.A_BOLD)

    row = 1
    for key, value in urls.items():
        stdscr.addstr(row, 4, f"{key}: {value['name']}")
        row += 1

    stdscr.refresh()

def play_url(url):
    media = instance.media_new(url)
    player.set_media(media)
    player.play()

def main(stdscr):
    # Initialize curses
    stdscr = curses.initscr()
    curses.start_color()
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    current_row = 1  # Track the current selected row

    while True:
        print_menu(stdscr)

        # Highlight the current selected row
        stdscr.chgat(current_row, 1, -1, curses.A_REVERSE)
        stdscr.refresh()

        selection = stdscr.getch()

        if selection == ord('q'):
            break

        if selection == curses.KEY_RESIZE:
            continue

        if selection == curses.KEY_UP and current_row > 1:
            current_row -= 1
        elif selection == curses.KEY_DOWN and current_row < len(urls):
            current_row += 1
        elif selection == ord('\n'):
            selected_key = str(current_row)
            if selected_key in urls:
                stdscr.clear()
                stdscr.border()
                stdscr.addstr(0, 2, f"Now playing: {urls[selected_key]['name']}", curses.A_BOLD)
                stdscr.refresh()

                # Play the selected URL
                url = urls[selected_key]['url']
                play_url(url)

                stdscr.addstr(2, 2, f"URL: {url}")
                logo_rows = logo_1.split('\n')
                logo_start_row = (curses.LINES - len(logo_rows)) // 12
                logo_start_col = (curses.COLS - len(logo_rows[0])) // 22
                for i, row in enumerate(logo_rows):
                    stdscr.addstr(logo_start_row + i, logo_start_col, row)
                stdscr.refresh()

                while True:
                    selection = stdscr.getch()

                    if selection == ord('q'):
                        break

                    if selection == curses.KEY_RESIZE:
                        continue

                    if selection == ord('\n'):
                        break

    # End curses
    curses.endwin()


# Run the main function
if __name__ == "__main__":
    curses.wrapper(main)
