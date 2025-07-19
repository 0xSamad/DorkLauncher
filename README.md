# Google DorkLauncher for Bug Bounty Recon

A professional GUI-based tool for automating Google dork queries during bug bounty reconnaissance. Designed with a clean Tkinter interface, this tool helps security researchers and bug bounty hunters perform passive enumeration efficiently, using custom dork lists in a structured batch-based approach.

## 🧰 Features

- **Domain-Specific Dorking** – Easily target any domain or subdomain scope
- **Load Custom Dork Lists** – Use or modify the included `dorks.txt` (XSS, admin panels, sensitive files, etc.)
- **Batch-Based Execution** – Open search results in manageable groups to reduce rate limits and noise
- **Jump to Specific Batch** – Resume where you left off after reboot or session pause
- **Threaded Execution** – Keeps the GUI responsive while tabs are being opened
- **Clean & Lightweight UI** – Simple interface with no browser automation or dependencies

## 📂 Included

- `dork_launcher.py` – The main application script
- `dorks.txt` – A sample list of Google dorks useful for recon (can be customized or extended)

## 🚀 Getting Started

1. **Install Python 3**
2. **Clone the repo or download the script**
3. Run the launcher:
   ```bash
   python3 dork_launcher.py
   ```
4. From the GUI:
   - Load your `dorks.txt` file
   - Enter a target domain (e.g., `example.com`)
   - Click **"Start Dorking"** to open the first batch
   - Use **"Next Batch"** or **"Jump to Batch"** as needed

## ✅ Use Cases

- Passive reconnaissance for bug bounty programs (HackerOne, Bugcrowd, Synack, etc.)
- Identifying exposed files, misconfigurations, and sensitive endpoints
- Manual OSINT targeting wildcard or large-scope programs

## ⚠️ Disclaimer

This tool uses `webbrowser.open_new_tab()` to open search queries in your default browser. Opening too many tabs too quickly may trigger CAPTCHAs or rate-limiting by Google. Use responsibly.

## 📖 License

This project is provided for educational and research purposes only.
