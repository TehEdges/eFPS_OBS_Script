# OBS SF Streamer Overlay Plugin

A custom OBS plugin (script) that dynamically loads and applies SF streamer overlays from a remote server. Built to simplify integration of live game server data into your OBS scenes.

Created by **SirEdges**.

---

## 🔧 Features

- Connects to a SF API to fetch live SRCDS servers.
- Dynamically updates a selected OBS browser source with the proper overlay URL.
- Optional parameters for centering the overlay and setting a display delay.
- Secure token-based API usage.
- Quick server list refresh directly within OBS UI.

---

## 💻 Requirements

- **OBS Studio for Windows**
- **Python 3.12 for Windows (64-bit)**
    - Must be installed and linked with OBS’s Python scripting environment.
    - https://www.python.org/downloads/release/python-3120/
    - Configured under **Tools -> Scripts**

---

## 🚀 Installation

1. Make sure Python 3.12 (Windows 64-bit) is installed and configured for OBS scripting.
2. Copy the script (`efps_sf_obs_control.py`) into your OBS scripts folder or any other folder:
   - Typically located at:  
     `C:\Program Files\obs-studio\data\obs-plugins\frontend-tools\scripts`
3. In OBS:
   - Go to **Tools > Scripts**
   - Click **+** to add a new script
   - Select the script file
4. Enter your **SF API token** into the provided field.
5. Click **"Load server list"** to fetch available servers.
6. Choose a **browser source** from the list to apply the overlay to.
7. Set **Center** and **Delay** options as needed.

---

## ⚙️ Configuration Options

| Option             | Description |
|--------------------|-------------|
| **SF Token**       | Your API token for accessing the SF Streamer Overlay. |
| **Center Overlay** | Whether to center the overlay in the browser source. |
| **Delay**          | Delay in seconds before displaying events. This should match the SourceTV Delay. |
| **Server List**    | Choose the server whose overlay should be loaded. |
| **Overlay Source** | The OBS browser source to update dynamically. |

---

## 📦 How It Works

1. The script queries the SF API endpoint for online servers.
2. You select the desired server from the dropdown.
3. The script builds a URL and updates the selected browser source in OBS.
4. Any change to the overlay config (server, center, delay) automatically updates the source URL.
