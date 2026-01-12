import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- THEME COLORS ----------------
BG = "#1e1e2e"
PANEL = "#2a2a3d"
BTN = "#4f9cff"
TEXT = "#ffffff"
SUCCESS = "#4CAF50"
ERROR = "#FF5252"

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Deadlock & Banker's Algorithm")
root.geometry("900x650")
root.configure(bg=BG)

style = ttk.Style()
style.theme_use("clam")

style.configure("TNotebook", background=BG, borderwidth=0)
style.configure("TNotebook.Tab", background=PANEL, foreground=TEXT, padding=10)
style.map("TNotebook.Tab", background=[("selected", BTN)])

# ---------------- TITLE ----------------
tk.Label(
    root,
    text="Operating Systems Lab Project",
    font=("Arial", 20, "bold"),
    bg=BG,
    fg=TEXT
).pack(pady=15)

# ---------------- NOTEBOOK ----------------
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=15, pady=15)

# ---------------- BANKER TAB ----------------
banker_tab = tk.Frame(notebook, bg=PANEL)
notebook.add(banker_tab, text="Banker's Algorithm")

# Inputs
tk.Label(banker_tab, text="Processes:", bg=PANEL, fg=TEXT).grid(row=0, column=0, padx=10, pady=10)
p_entry = tk.Entry(banker_tab)
p_entry.grid(row=0, column=1)

tk.Label(banker_tab, text="Resources:", bg=PANEL, fg=TEXT).grid(row=0, column=2, padx=10)
r_entry = tk.Entry(banker_tab)
r_entry.grid(row=0, column=3)

alloc_entries = []
max_entries = []

def create_banker_inputs():
    for w in banker_tab.grid_slaves():
        if int(w.grid_info()["row"]) > 1:
            w.destroy()

    alloc_entries.clear()
    max_entries.clear()

    p = int(p_entry.get())

    tk.Label(banker_tab, text="Allocation Matrix", bg=PANEL, fg=TEXT).grid(row=1, column=0, columnspan=2)
    tk.Label(banker_tab, text="Max Matrix", bg=PANEL, fg=TEXT).grid(row=1, column=2, columnspan=2)

    for i in range(p):
        a = tk.Entry(banker_tab, width=20)
        a.grid(row=i+2, column=0, columnspan=2, pady=4)
        alloc_entries.append(a)

        m = tk.Entry(banker_tab, width=20)
        m.grid(row=i+2, column=2, columnspan=2, pady=4)
        max_entries.append(m)

    tk.Label(banker_tab, text="Available Resources", bg=PANEL, fg=TEXT).grid(row=p+2, column=0)
    global avail_entry
    avail_entry = tk.Entry(banker_tab, width=20)
    avail_entry.grid(row=p+2, column=1, columnspan=3)

    tk.Button(
        banker_tab,
        text="Run Banker's Algorithm",
        bg=BTN,
        fg="white",
        font=("Arial", 11, "bold"),
        command=run_banker
    ).grid(row=p+3, column=1, pady=15)

    global banker_result
    banker_result = tk.Label(banker_tab, bg=PANEL, fg=TEXT, font=("Arial", 12))
    banker_result.grid(row=p+4, column=0, columnspan=4)

def run_banker():
    try:
        p = int(p_entry.get())
        r = int(r_entry.get())

        allocation = [list(map(int, e.get().split())) for e in alloc_entries]
        maxm = [list(map(int, e.get().split())) for e in max_entries]
        available = list(map(int, avail_entry.get().split()))

        need = [[maxm[i][j] - allocation[i][j] for j in range(r)] for i in range(p)]
        work = available[:]
        finish = [False] * p
        seq = []

        while len(seq) < p:
            found = False
            for i in range(p):
                if not finish[i] and all(need[i][j] <= work[j] for j in range(r)):
                    work = [work[j] + allocation[i][j] for j in range(r)]
                    finish[i] = True
                    seq.append(f"P{i}")
                    found = True
            if not found:
                break

        if len(seq) == p:
            banker_result.config(
                text="SAFE STATE\nSafe Sequence: " + " → ".join(seq),
                fg=SUCCESS
            )
        else:
            banker_result.config(
                text="UNSAFE STATE (Deadlock Possible)",
                fg=ERROR
            )
    except:
        messagebox.showerror("Input Error", "Please check all inputs")

tk.Button(
    banker_tab,
    text="Create Input Fields",
    bg=BTN,
    fg="white",
    command=create_banker_inputs
).grid(row=0, column=4, padx=10)

# ---------------- DEADLOCK TAB ----------------
deadlock_tab = tk.Frame(notebook, bg=PANEL)
notebook.add(deadlock_tab, text="Deadlock Detection")

tk.Label(deadlock_tab, text="Processes:", bg=PANEL, fg=TEXT).grid(row=0, column=0, padx=10, pady=10)
p2_entry = tk.Entry(deadlock_tab)
p2_entry.grid(row=0, column=1)

tk.Label(deadlock_tab, text="Resources:", bg=PANEL, fg=TEXT).grid(row=0, column=2)
r2_entry = tk.Entry(deadlock_tab)
r2_entry.grid(row=0, column=3)

alloc2 = []
req2 = []

def create_deadlock_inputs():
    for w in deadlock_tab.grid_slaves():
        if int(w.grid_info()["row"]) > 1:
            w.destroy()

    alloc2.clear()
    req2.clear()

    p = int(p2_entry.get())

    for i in range(p):
        a = tk.Entry(deadlock_tab, width=20)
        a.grid(row=i+2, column=0, columnspan=2, pady=4)
        alloc2.append(a)

        r = tk.Entry(deadlock_tab, width=20)
        r.grid(row=i+2, column=2, columnspan=2, pady=4)
        req2.append(r)

    tk.Label(deadlock_tab, text="Available Resources", bg=PANEL, fg=TEXT).grid(row=p+2, column=0)
    global avail2
    avail2 = tk.Entry(deadlock_tab, width=20)
    avail2.grid(row=p+2, column=1, columnspan=3)

    tk.Button(
        deadlock_tab,
        text="Detect Deadlock",
        bg=BTN,
        fg="white",
        font=("Arial", 11, "bold"),
        command=run_deadlock
    ).grid(row=p+3, column=1, pady=15)

    global deadlock_result
    deadlock_result = tk.Label(deadlock_tab, bg=PANEL, fg=TEXT, font=("Arial", 12))
    deadlock_result.grid(row=p+4, column=0, columnspan=4)

def run_deadlock():
    try:
        p = int(p2_entry.get())
        r = int(r2_entry.get())

        allocation = [list(map(int, e.get().split())) for e in alloc2]
        request = [list(map(int, e.get().split())) for e in req2]
        available = list(map(int, avail2.get().split()))

        work = available[:]
        finish = [False] * p

        while True:
            found = False
            for i in range(p):
                if not finish[i] and all(request[i][j] <= work[j] for j in range(r)):
                    work = [work[j] + allocation[i][j] for j in range(r)]
                    finish[i] = True
                    found = True
            if not found:
                break

        dead = [f"P{i}" for i in range(p) if not finish[i]]

        if dead:
            deadlock_result.config(
                text="Deadlocked Processes: " + ", ".join(dead),
                fg=ERROR
            )
        else:
            deadlock_result.config(
                text="No Deadlock Detected",
                fg=SUCCESS
            )
    except:
        messagebox.showerror("Input Error", "Please check all inputs")

tk.Button(
    deadlock_tab,
    text="Create Input Fields",
    bg=BTN,
    fg="white",
    command=create_deadlock_inputs
).grid(row=0, column=4, padx=10)

root.mainloop()
