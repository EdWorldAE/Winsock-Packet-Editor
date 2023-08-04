# Winsock-Packet-Editor
Winsock Packet Editor

Certainly! Here's a detailed README for the Packet Editor application:

---

# Packet Editor GUI

A GUI-based application developed in Python, the Packet Editor allows users to sniff packets from a specific process running on their system, view packet details, and edit these details.

## Features:

1. **Select an Active Network Interface**: The application auto-detects the active network interface but also provides an option for manual selection.
2. **Select a Process**: Users can choose a specific process from a drop-down list to sniff its traffic.
3. **Specify Packet Count**: Determines the number of packets the application will capture before stopping.
4. **View and Edit Packet Details**: Once packets are captured, their details are displayed in a large text field. Users can edit these details directly within the text area.
5. **Send Edited Packets**: After editing, users have the option to send the packets.

## Prerequisites:

- Python
- `tkinter`
- `scapy`
- `psutil`

You can install the required Python libraries using pip:

```bash
pip install scapy psutil
```

## Code Explanation:

1. **Initialization**:
    - Libraries such as `tkinter`, `scapy`, and `psutil` are imported.
    - Functions are defined to get the active network interface and capture and edit packets.
    
2. **Process Selection**:
    - Using `psutil`, all currently running processes on the system are fetched.
    - Process names, along with their PIDs, are displayed in a dropdown (ComboBox) for the user to select from.

3. **Packet Capture and Editing**:
    - The selected process's PID is extracted using a regular expression.
    - The `sniff()` function from `scapy` captures packets from the selected process.
    - Captured packets are displayed in a text field where users can view and edit their details.
    - Note: In this version, while users can edit packet details, these edits are not actually applied to the packets due to the complexity of parsing edited text. The groundwork is laid out for this feature and can be expanded upon.

4. **GUI Components**:
    - **Interface Entry**: For specifying the network interface.
    - **Process ComboBox**: To select a specific process to sniff.
    - **Packet Count Entry**: To specify the number of packets to capture.
    - **Text Field**: A scrollable area to view and edit packet details.
    - **Capture and Edit Button**: Initiates the packet capture and editing process.
    - **Save Edits Button**: Saves any edits made in the text field.

5. **Event Flow**:
    - After specifying the desired settings and process, users can click "Capture and Edit" to start packet capture.
    - Captured packets are displayed in the text field.
    - Users can edit packet details in the text field and then click "Save Edits".
    - Users are prompted with a choice to send the edited packets.

## Running the Application:

1. Ensure you have all the prerequisites installed.
2. Run the Python script.
3. The GUI should appear, allowing you to select the interface, process, and set other parameters.
4. Follow the workflow in the application to capture, edit, and send packets.

---

Remember, the README provides a general overview and explanation of the application. If there's a need for a deeper dive into any part of the code, additional documentation or inline code comments can be helpful.
