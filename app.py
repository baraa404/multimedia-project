import tkinter as tk # للواجهة الرسومية
from tkinter import messagebox # للرسائل التحذيرية
from gtts import gTTS # لتحويل النص إلى كلام

#################### براء مبروك عبد النبي عبد الروؤف ####################
# تحويل النص إلى كلام بالبايثون

def play_text():
    # خد النص اللي دخلناه في خانة الإدخال دي
    text = text_entry.get()
    if text.strip():  # يعني لو النص مش فاضي
        # حول النص ده لملف MP3
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
    else:
        # لو النص فاضي، أظهر رسالة تحذيرية دي
        messagebox.showwarning("خطأ", "Please enter some text to play")

def reset_text():
    # مسح النص في خانة الإدخال 
    text_entry.delete(0, tk.END)

def exit_program():
    # غلق البرنامج 
    root.destroy()

# إنشاء نافذة الجرافيك دي
root = tk.Tk()
root.title("Text to Speech")
root.geometry("400x300")
root.configure(bg="light blue")  # لون خلفية خفيف أزرق دي

# العنوان الرئيسي 
header = tk.Label(root, text="Text to Speech", font=("Arial", 20, "bold"), bg="light blue", fg="black")
header.pack(pady=10)

# عنوان فرعي 
sub = tk.Label(root, text="Enter your text:", font=("Arial", 12), bg="light blue", fg="black")
sub.pack()

# خانة إدخال النص 
text_entry = tk.Entry(root, width=40, font=("Arial", 14), justify="center", bd=2, relief="solid")
text_entry.pack(pady=10)

# إطار لأزرار التحكم 
button = tk.Frame(root, bg="#add8e6")
button.pack(pady=20)

# زر التشغيل 
play = tk.Button(button, text="Play", font=("Arial", 12, "bold"), bg="green", fg="white", width=10, command=play_text)
play.grid(row=0, column=0, padx=10)

# زر المسح 
set_b = tk.Button(button, text="Set", font=("Arial", 12, "bold"), bg="blue", fg="white", width=10, command=reset_text)
set_b.grid(row=0, column=1, padx=10)

# زر الخروج 
exit_button = tk.Button(button, text="Exit", font=("Arial", 12, "bold"), bg="Red", fg="white", width=10, command=exit_program)
exit_button.grid(row=0, column=2, padx=10)

# الفوتر الي تحت 
footer = tk.Label(root, text="Developed by : baraa mabrok ", font=("Arial", 10), bg="light blue", fg="black")
footer.pack(side="bottom", pady=10)

# بدء تشغيل البرنامج
root.mainloop()
