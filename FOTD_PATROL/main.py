import time
import pyautogui

# Global vars for stats
num_servers = 0
start_time = time.time()


# TODO add region capability
def click_center_of_image(image, CONFIDENCE):
    print(f"Starting search for {image}")
    while True:
        center = pyautogui.locateCenterOnScreen(image, confidence=CONFIDENCE)
        if center is not None:
            print(f"Successfully located {image}, clicking {center}")
            pyautogui.click(center)
            return


def title_screen():
    click_center_of_image("assets/title_screen.png", 0.8)


def adventure():
    click_center_of_image("assets/adventure.png", 0.98)


def sloop():
    click_center_of_image("assets/sloop.png", 0.95)  # 0.98 too big


def closed_crew():
    click_center_of_image("assets/closed_crew.png", 0.98)


def set_sail():
    click_center_of_image("assets/set_sail.png", 0.98)


def join_game():
    title_screen()
    adventure()
    sloop()
    closed_crew()
    set_sail()


def check_notification():
    # TODO finish this scan for FOTD
    pass


def check_server():
    print("Starting search for FOTD")
    in_game = False
    while not in_game:
        check_notification()
        in_game_presence = pyautogui.locateCenterOnScreen("assets/in_game.png", confidence=0.98)
        if in_game_presence is not None:
            print("Recognized to be in game")
            return


def leave_game():
    pyautogui.press("escape")
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.press("enter")
    pyautogui.press("enter")


def hop():
    join_game()
    check_server()
    # delay for stupid join animation
    time.sleep(20)
    leave_game()
    # increment num_servers
    global num_servers
    num_servers += 1

    print_stats()


def print_stats():
    # time stats
    current_time = time.time()
    elapsed_time = current_time - start_time
    elapsed_time = elapsed_time % (24 * 3600)
    hour = elapsed_time // 3600
    elapsed_time %= 3600
    minutes = elapsed_time // 60
    elapsed_time %= 60
    seconds = elapsed_time

    # num servers
    global num_servers
    print()
    print("--------------------------------------------------")
    print(f"Servers checked: {num_servers}")
    print("h:m:s-> %d:%d:%d" % (hour, minutes, seconds))
    print("--------------------------------------------------")
    print()


def hop_bot():
    while True:
        hop()


hop_bot()
