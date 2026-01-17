import tkinter as tk
from tkinter import ttk, messagebox

BG = "#F4F1EE"
PANEL = "#3B0A14"
BTN = "#7A0019"
TEXT = "#FFFFFF"
ACCENT = "#C9A227"
SUCCESS = "#2E7D32"
ERROR = "#C62828"

root = tk.Tk()
root.title("DHA Suffa University | OS Lab Project")
root.geometry("900x650")
root.configure(bg=BG)

style = ttk.Style()
style.theme_use("clam")

style.configure("TNotebook", background=BG, borderwidth=0)
style.configure(
    "TNotebook.Tab",
    background=PANEL,
    foreground=TEXT,
    padding=12,
    font=("Arial", 11, "bold")
)
style.map(
    "TNotebook.Tab",
    background=[("selected", BTN)],
    foreground=[("selected", TEXT)]
)

tk.Label(
    root,
    text="DHA Suffa University\nOperating Systems Laboratory",
    font=("Arial", 22, "bold"),
    bg=BG,
    fg=BTN
).pack(pady=20)

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=15, pady=15)

banker_tab = tk.Frame(notebook, bg=PANEL)
notebook.add(banker_tab, text="Banker’s Algorithm")

tk.Label(banker_tab, text="Number of Processes", bg=PANEL, fg=TEXT).grid(row=0, column=0, padx=10, pady=10)
p_entry = tk.Entry(banker_tab)
p_entry.grid(row=0, column=1)

tk.Label(banker_tab, text="Number of Resources", bg=PANEL, fg=TEXT).grid(row=0, column=2, padx=10)
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

    tk.Label(banker_tab, text="Allocation Matrix", bg=PANEL, fg=ACCENT).grid(row=1, column=0, columnspan=2)
    tk.Label(banker_tab, text="Maximum Matrix", bg=PANEL, fg=ACCENT).grid(row=1, column=2, columnspan=2)

    for i in range(p):
        a = tk.Entry(banker_tab, width=22)
        a.grid(row=i + 2, column=0, columnspan=2, pady=4)
        alloc_entries.append(a)

        m = tk.Entry(banker_tab, width=22)
        m.grid(row=i + 2, column=2, columnspan=2, pady=4)
        max_entries.append(m)

    tk.Label(banker_tab, text="Available Resources", bg=PANEL, fg=ACCENT).grid(row=p + 2, column=0)
    global avail_entry
    avail_entry = tk.Entry(banker_tab, width=22)
    avail_entry.grid(row=p + 2, column=1, columnspan=3)

    tk.Button(
        banker_tab,
        text="Check System Safety",
        bg=BTN,
        fg=TEXT,
        font=("Arial", 11, "bold"),
        command=run_banker
    ).grid(row=p + 3, column=1, pady=15)

    global banker_result
    banker_result = tk.Label(banker_tab, bg=PANEL, fg=TEXT, font=("Arial", 12))
    banker_result.grid(row=p + 4, column=0, columnspan=4)

def run_banker():
    try:
        p = int(p_entry.get())
        r = int(r_entry.get())

        allocation = [list(map(int, e.get().split())) for e in alloc_entries]
        maximum = [list(map(int, e.get().split())) for e in max_entries]
        available = list(map(int, avail_entry.get().split()))

        need = [[maximum[i][j] - allocation[i][j] for j in range(r)] for i in range(p)]
        work = available[:]
        finish = [False] * p
        sequence = []

        while len(sequence) < p:
            progress = False
            for i in range(p):
                if not finish[i] and all(need[i][j] <= work[j] for j in range(r)):
                    work = [work[j] + allocation[i][j] for j in range(r)]
                    finish[i] = True
                    sequence.append(f"P{i}")
                    progress = True
            if not progress:
                break

        if len(sequence) == p:
            banker_result.config(
                text="System is in a SAFE state\nSafe Sequence: " + " → ".join(sequence),
                fg=SUCCESS
            )
        else:
            banker_result.config(
                text="System is in an UNSAFE state\nDeadlock may occur",
                fg=ERROR
            )
    except:
        messagebox.showerror("Invalid Input", "Please enter correct values for all fields")

tk.Button(
    banker_tab,
    text="Generate Input Fields",
    bg=BTN,
    fg=TEXT,
    command=create_banker_inputs
).grid(row=0, column=4, padx=10)

deadlock_tab = tk.Frame(notebook, bg=PANEL)
notebook.add(deadlock_tab, text="Deadlock Detection")

tk.Label(deadlock_tab, text="Number of Processes", bg=PANEL, fg=TEXT).grid(row=0, column=0, padx=10, pady=10)
p2_entry = tk.Entry(deadlock_tab)
p2_entry.grid(row=0, column=1)

tk.Label(deadlock_tab, text="Number of Resources", bg=PANEL, fg=TEXT).grid(row=0, column=2)
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
        a = tk.Entry(deadlock_tab, width=22)
        a.grid(row=i + 2, column=0, columnspan=2, pady=4)
        alloc2.append(a)

        r = tk.Entry(deadlock_tab, width=22)
        r.grid(row=i + 2, column=2, columnspan=2, pady=4)
        req2.append(r)

    tk.Label(deadlock_tab, text="Available Resources", bg=PANEL, fg=ACCENT).grid(row=p + 2, column=0)
    global avail2
    avail2 = tk.Entry(deadlock_tab, width=22)
    avail2.grid(row=p + 2, column=1, columnspan=3)

    tk.Button(
        deadlock_tab,
        text="Analyze Deadlock",
        bg=BTN,
        fg=TEXT,
        font=("Arial", 11, "bold"),
        command=run_deadlock
    ).grid(row=p + 3, column=1, pady=15)

    global deadlock_result
    deadlock_result = tk.Label(deadlock_tab, bg=PANEL, fg=TEXT, font=("Arial", 12))
    deadlock_result.grid(row=p + 4, column=0, columnspan=4)

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
            progress = False
            for i in range(p):
                if not finish[i] and all(request[i][j] <= work[j] for j in range(r)):
                    work = [work[j] + allocation[i][j] for j in range(r)]
                    finish[i] = True
                    progress = True
            if not progress:
                break

        deadlocked = [f"P{i}" for i in range(p) if not finish[i]]

        if deadlocked:
            deadlock_result.config(
                text="Deadlock detected in processes: " + ", ".join(deadlocked),
                fg=ERROR
            )
        else:
            deadlock_result.config(
                text="No deadlock detected. System is stable.",
                fg=SUCCESS
            )
    except:
        messagebox.showerror("Invalid Input", "Please enter correct values for all fields")

tk.Button(
    deadlock_tab,
    text="Generate Input Fields",
    bg=BTN,
    fg=TEXT,
    command=create_deadlock_inputs
).grid(row=0, column=4, padx=10)

root.mainloop()
