import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext, ttk
from scapy.all import *
import psutil


def get_active_interface():
    default_route = [r for r in conf.route.routes if r[1] == 0]
    if not default_route:
        return None
    active_interface = default_route[0][3]
    return active_interface


def capture_and_edit(interface, filter_str, count):
    packets = sniff(iface=interface, filter=filter_str, count=count)
    return [edit_packet_gui(packet) for packet in packets]


def edit_packet_gui(packet):
    packet_str = packet.show(dump=True)
    text_field.delete(1.0, tk.END)
    text_field.insert(tk.END, packet_str)
    edit_button.config(state=tk.DISABLED)
    save_button.config(state=tk.NORMAL)
    root.wait_variable(edit_complete)
    edited_packet_str = text_field.get(1.0, tk.END)
    return packet


def start_packet_capture():
    selected_process = process_combobox.get()
    if not selected_process:
        messagebox.showerror("Error", "Please select a process to sniff!")
        return

    interface = interface_var.get()
    filter_str = f'proc {selected_process}'
    count = count_var.get()

    edited_packets = capture_and_edit(interface, filter_str, count)
    send_choice = messagebox.askyesno("Send Packets", "Do you want to send the edited packets?")
    if send_choice:
        for packet in edited_packets:
            sendp(packet, iface=interface)


def save_edits():
    edit_complete.set(1)
    save_button.config(state=tk.DISABLED)
    edit_button.config(state=tk.NORMAL)


root = tk.Tk()
root.title("Packet Editor")

active_interface = get_active_interface() or "eth0"

interface_var = tk.StringVar(root, value=active_interface)
filter_var = tk.StringVar(root)
count_var = tk.IntVar(root, value=1)
edit_complete = tk.IntVar(root, value=0)

tk.Label(root, text="Interface:").grid(row=0, column=0, sticky="e")
tk.Entry(root, textvariable=interface_var).grid(row=0, column=1, padx=5, pady=5)

# List running processes
processes = [(proc.info["pid"], proc.info["name"]) for proc in psutil.process_iter(attrs=["pid", "name"])]

process_names = [f"{proc[1]} (PID: {proc[0]})" for proc in processes]

tk.Label(root, text="Select Process:").grid(row=1, column=0, sticky="e")
process_combobox = ttk.Combobox(root, values=process_names)
process_combobox.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Packet Count:").grid(row=2, column=0, sticky="e")
tk.Entry(root, textvariable=count_var).grid(row=2, column=1, padx=5, pady=5)

text_field = scrolledtext.ScrolledText(root, width=80, height=20)
text_field.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

edit_button = tk.Button(root, text="Capture and Edit", command=start_packet_capture)
edit_button.grid(row=4, column=0, pady=10)

save_button = tk.Button(root, text="Save Edits", state=tk.DISABLED, command=save_edits)
save_button.grid(row=4, column=1, pady=10)

root.mainloop()
