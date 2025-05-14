import tkinter as tk
import threading
import time
import pyautogui


# Matnni bosqichma-bosqich yuborish funksiyasi
def gradual_typing(text, total_lines=1000, zigzag=False, connected=False):
    steps = [text[:i + 1] for i in range(len(text))]  # ['m', 'm+', 'm+z', 'm+z=', 'm+z=S']
    repeat_per_step = total_lines // len(steps)
    count = 0

    if connected:  # Ulanadigan so‘zlar bilan yuborish
        connected_steps = text.split()  # Har bir so‘zni alohida yuborish
        for word in connected_steps:
            pyautogui.write(word)
            pyautogui.press('enter')
            time.sleep(0.05)
            count += 1
            if count >= total_lines:
                return
    elif zigzag:  # Zigzag tarzida yuborish uchun
        for i in range(total_lines):
            current_text = text[:i % len(text) + 1]  # Harflar bilan zigzag qilish
            pyautogui.write(current_text)
            pyautogui.press('enter')
            time.sleep(0.05)
            count += 1
            if count >= total_lines:
                return
    else:  # Oddiy tarzda yuborish
        for step in steps:
            for _ in range(repeat_per_step):
                pyautogui.write(step)
                pyautogui.press('enter')
                count += 1
                time.sleep(0.05)
                if count >= total_lines:
                    return


# Foydalanuvchi boshlash uchun funksiya
def start_typing():
    user_text = entry.get()
    try:
        repeat_count = int(repeat_entry.get())  # Nechta marta yuborilishini olish
    except ValueError:
        repeat_count = 1000  # Agar foydalanuvchi raqam bermasa, 1000 qilib olish

    zigzag_mode = zigzag_var.get()  # Zigzag bo‘lsinmi?
    connected_mode = connected_var.get()  # Ulanadigan so‘zlar bo‘lsinmi?

    if user_text.strip():
        def delayed_typing():
            time.sleep(5)  # Foydalanuvchiga Telegram oynasini bosishga vaqt beriladi
            gradual_typing(user_text, total_lines=repeat_count, zigzag=zigzag_mode, connected=connected_mode)

        threading.Thread(target=delayed_typing).start()


# GUI oynasi
root = tk.Tk()
root.title("Bosqichma-bosqich Yozuvchi")
root.geometry("380x320")

label = tk.Label(root, text="Matn kiriting (masalan: m+z=S):", font=("Arial", 11))
label.pack(pady=10)

entry = tk.Entry(root, width=35, font=("Arial", 12))
entry.pack()

repeat_label = tk.Label(root, text="Nechta marta yuborilsin?", font=("Arial", 11))
repeat_label.pack(pady=5)

repeat_entry = tk.Entry(root, width=10, font=("Arial", 12))
repeat_entry.pack()

# Zigzag va ulanadigan so‘zlar uchun checkboxlar
zigzag_var = tk.BooleanVar()
zigzag_check = tk.Checkbutton(root, text="Zigzag tarzida yuborish", variable=zigzag_var, font=("Arial", 10))
zigzag_check.pack(pady=5)

connected_var = tk.BooleanVar()
connected_check = tk.Checkbutton(root, text="Ulanadigan so‘zlarni yuborish", variable=connected_var, font=("Arial", 10))
connected_check.pack(pady=5)

# Butun so‘z va harflab yuborish uchun tugmalar
start_button = tk.Button(root, text="Harf yuborish", font=("Arial", 12), command=start_typing)
start_button.pack(pady=10)

start_button_zigzag = tk.Button(root, text="Butun yuborish", font=("Arial", 12), command=start_typing)
start_button_zigzag.pack(pady=10)

info_label = tk.Label(root, text="Telegramdagi yozuv maydonini sichqoncha bilan bosing!", fg="red", wraplength=340)
info_label.pack()

root.mainloop()

