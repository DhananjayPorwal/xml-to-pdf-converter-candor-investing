# XML to Readable TXT Converter

This Streamlit application allows you to:
1. Upload multiple **XML files**.
2. Convert the XML files into formatted **TXT files**.
3. Download all converted TXT files as a single **ZIP file**.
4. View a **summary table** of extracted data.

---

## Setup Instructions

#### Run Locally

1. **Install Python**: Ensure you have Python installed (version 3.8+).
2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
3. **Run the App**:
   ```bash
   streamlit run app.py
   ```
4. Open the app in your browser (default: `http://localhost:8501`).

#### Run on Cloud (Streamlit Sharing)

1. Sign up for **Streamlit Cloud** at: [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Upload your repository (containing `app.py`, `requirements.txt`, etc.) to GitHub.
3. Deploy your app by linking your GitHub repository.

---

### How to Use the App

1. **Upload XML Files**: Drag and drop or select multiple XML files.
2. **Wait for Processing**: Real-time progress will be shown.
3. **Download Results**: Click the "Download All Files as ZIP" button.
4. **View Table**: Check the extracted data in the summary table.

---

## 4. Guide for Non-Technical Users

### Run Locally on Your Computer

1. **Install Python**:
   - Download Python from [python.org](https://www.python.org).
   - Follow installation instructions for your OS (Windows, Mac, or Linux).

2. **Install Streamlit**:
   - Open **Command Prompt** (Windows) or **Terminal** (Mac/Linux).
   - Run:
     ```bash
     pip install streamlit pandas
     ```

3. **Run the Application**:
   - Save the provided code in a file named `app.py`.
   - Open **Command Prompt** or **Terminal** in the folder containing `app.py`.
   - Run:
     ```bash
     streamlit run app.py
     ```
   - The app will open in your browser at `http://localhost:8501`.

4. **Use the App**:
   - Upload XML files.
   - Wait for the files to process.
   - Download the ZIP file and check the summary table.

---

### Run on Cloud (Streamlit Sharing)

1. **Sign Up**:
   - Go to [https://streamlit.io/cloud](https://streamlit.io/cloud) and create an account.

2. **Prepare Code**:
   - Save the code as `app.py`.
   - Create a `requirements.txt` file with the following content:
     ```txt
     streamlit
     pandas
     ```

3. **Upload to GitHub**:
   - Create a GitHub account (if you don’t have one) at [github.com](https://github.com).
   - Create a repository and upload the `app.py` and `requirements.txt` files.

4. **Deploy the App**:
   - On Streamlit Cloud, connect your GitHub repository.
   - Deploy the app and share the generated link.

5. **Use the App**:
   - Visit the app link.
   - Upload XML files, process them, and download the ZIP.

---

Now you have a fully functional Streamlit application with complete instructions for deployment and usage. Let me know if you need further assistance! 🚀