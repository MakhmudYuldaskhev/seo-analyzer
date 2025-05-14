import tkinter as tk
import threading
import time
import pyautogui

def gradual_typing(text, total_lines=1000):
    steps = [text[:i + 1] for i in range(len(text))]  # ['m', 'm+', 'm+z', 'm+z=', 'm+z=S']
    repeat_per_step = total_lines // len(steps)
    count = 0
    for step in steps:
        for _ in range(repeat_per_step):
            pyautogui.write(step)
            pyautogui.press('enter')
            count += 1
            time.sleep(0.05)
            if count >= total_lines:
                return


# def start_typing():
#     user_text = entry.get()
#     if user_text.strip():
#         threading.Thread(target=gradual_typing, args=(user_text,)).start()

def start_typing():
    user_text = entry.get()
    if user_text.strip():
        def delayed_typing():
            time.sleep(5)  # foydalanuvchiga Telegram oynasini bosishga vaqt beriladi
            gradual_typing(user_text)

        threading.Thread(target=delayed_typing).start()


# GUI oynasi
root = tk.Tk()
root.title("Bosqichma-bosqich Yozuvchi")
root.geometry("380x200")

label = tk.Label(root, text="Matn kiriting (masalan: m+z=S):", font=("Arial", 11))
label.pack(pady=10)

entry = tk.Entry(root, width=35, font=("Arial", 12))
entry.pack()

start_button = tk.Button(root, text="Boshlash", font=("Arial", 12), command=start_typing)
start_button.pack(pady=15)

info_label = tk.Label(root, text="Telegramdagi yozuv maydonini sichqoncha bilan bosing!", fg="red", wraplength=340)
info_label.pack()

root.mainloop()
