import threading
import tkinter as tk
from tkinter import ttk, messagebox
from google import genai
from google.genai.errors import ClientError

API_KEY = "YOUR_API_KEY"

try:
    client = genai.Client(api_key=API_KEY)
    chat = client.chats.create(model="gemini-2.0-flash")
except Exception as e:
    client = None
    chat = None

def append_message(sender, message, tag):
    chat_display.config(state="normal")
    chat_display.insert(tk.END, f"{sender}: ", f"{tag}_header")
    chat_display.insert(tk.END, f"{message}\n\n", tag)
    chat_display.config(state="disabled")
    chat_display.see(tk.END)

def call_gemini(user_text):
    global chat
    try:
        if not chat:
            raise RuntimeError("Chat session is not initialized. Please verify your API key.")
        
        response = chat.send_message(user_text)
        r.after(0, lambda: append_message("Agent", response.text.strip(), "agent"))
    except ClientError as e:
        err_msg = f"[API Error {e.code}]: {e.message}"
        r.after(0, lambda: append_message("System", err_msg, "error"))
    except Exception as e:
        r.after(0, lambda: append_message("System", f"Error: {e}", "error"))
    finally:
        r.after(0, enable_inputs)

def send_message(event=None):
    user_text = input_entry.get().strip()
    if not user_text:
        return

    if user_text.lower() == "exit":
        r.destroy()
        return

    input_entry.delete(0, tk.END)
    append_message("User", user_text, "user")

    send_btn.config(state="disabled")
    input_entry.config(state="disabled")
    status_label.config(text="Agent is thinking...", fg="#38bdf8")

    threading.Thread(target=call_gemini, args=(user_text,), daemon=True).start()

def enable_inputs():
    send_btn.config(state="normal")
    input_entry.config(state="normal")
    input_entry.focus()
    status_label.config(text="Ready. Type 'exit' or close window to leave.", fg="#94a3b8")

r = tk.Tk()
r.title("Gemini Chat Studio")
r.geometry("780x600")
r.minsize(600, 450)
r.configure(bg="#0f172a")

header_frame = tk.Frame(r, bg="#0f172a", pady=10)
header_frame.pack(fill=tk.X)

tk.Label(header_frame, text="Gemini AI Chat", font=("Segoe UI", 16, "bold"), fg="#f8fafc", bg="#0f172a").pack()

chat_card = tk.Frame(r, bg="#1e293b", highlightbackground="#334155", highlightthickness=1)
chat_card.pack(fill=tk.BOTH, expand=True, padx=16, pady=(0, 10))

chat_display = tk.Text(chat_card, wrap=tk.WORD, font=("Segoe UI", 10), bg="#0b0f19", fg="#f8fafc", insertbackground="#38bdf8", relief="flat", padx=14, pady=12, state="disabled")
chat_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

chat_display.tag_config("user_header", foreground="#38bdf8", font=("Segoe UI", 10, "bold"))
chat_display.tag_config("user", foreground="#e2e8f0")
chat_display.tag_config("agent_header", foreground="#4ade80", font=("Segoe UI", 10, "bold"))
chat_display.tag_config("agent", foreground="#f8fafc")
chat_display.tag_config("error", foreground="#f43f5e", font=("Segoe UI", 9, "italic"))

scroll_y = ttk.Scrollbar(chat_card, orient=tk.VERTICAL, command=chat_display.yview)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
chat_display.config(yscrollcommand=scroll_y.set)

input_card = tk.Frame(r, bg="#1e293b", padx=10, pady=8, highlightbackground="#334155", highlightthickness=1)
input_card.pack(fill=tk.X, padx=16, pady=(0, 6))

input_entry = tk.Entry(input_card, font=("Segoe UI", 11), bg="#0f172a", fg="#f8fafc", insertbackground="#38bdf8", relief="flat", highlightbackground="#475569", highlightthickness=1)
input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(4, 8), ipady=5)
input_entry.bind("<Return>", send_message)

send_btn = tk.Button(input_card, text="Send", command=send_message, font=("Segoe UI", 10, "bold"), bg="#0284c7", fg="#ffffff", activebackground="#0369a1", activeforeground="#ffffff", relief="flat", padx=16, pady=4, cursor="hand2")
send_btn.pack(side=tk.RIGHT)

status_bar = tk.Frame(r, bg="#0f172a", padx=16, pady=4)
status_bar.pack(fill=tk.X)

status_label = tk.Label(status_bar, text="Ready. Type 'exit' or close window to leave.", font=("Segoe UI", 9), fg="#94a3b8", bg="#0f172a")
status_label.pack(side=tk.LEFT)

input_entry.focus()

r.mainloop()