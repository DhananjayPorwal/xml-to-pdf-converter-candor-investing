# XML to Readable TXT and PDF Converter

This web app converts KRA (KYC Registration Agency) downloaded XML files into a readable format, including both TXT and PDF versions. It allows users to easily view and download the extracted data from the XML files.

---

This Streamlit application allows you to:
1. Upload multiple **XML files**.
2. Convert the XML files into formatted **TXT** and **PDF** files.
3. Download individual files or **download all converted files as ZIP archives**.
4. View a **summary table** of extracted data, such as Name, Gender, PAN, DOB, Email, etc.

---

## Setup Instructions

### Run Locally

1. **Install Python**: Ensure you have Python installed (version 3.8+).

2. **Install Dependencies**:
   You can use the `requirements.txt` file to install all necessary dependencies. Make sure you have the following content in your `requirements.txt`:
   ```txt
   streamlit == 1.41.1
   pandas == 2.2.3
   fpdf == 1.7.2
   ```

   Then, install the dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**:
   ```bash
   streamlit run app.py
   ```
4. Open the app in your browser (default: `http://localhost:8501`).

---

### Run on Cloud (Streamlit Sharing)

1. Sign up for **Streamlit Cloud** at: [https://streamlit.io/cloud](https://www.streamlit.io/cloud).
2. Upload your repository (containing `app.py`, `requirements.txt`, etc.) to **GitHub**.
3. Deploy your app by linking your GitHub repository.

---

### How to Use the App

1. **Upload XML Files**: Drag and drop or select multiple XML files.
2. **Wait for Processing**: The app will parse and convert the files to **TXT** and **PDF** formats.
3. **Download Results**: 
   - If only one file is uploaded, you can download the **TXT** and **PDF** files individually.
   - If multiple files are uploaded, you can download all converted files as **ZIP archives**.
4. **View Table**: Check the extracted data from the XML files in the summary table.

---

## Guide for Non-Technical Users

### Run Locally on Your Computer

1. **Install Python**:
   - Download Python from [python.org](https://www.python.org).
   - Follow installation instructions for your OS (Windows, Mac, or Linux).

2. **Install Streamlit**:
   - Open **Command Prompt** (Windows) or **Terminal** (Mac/Linux).
   - Run:
     ```bash
     pip install streamlit pandas fpdf
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
   - Download the ZIP file containing all converted TXT and PDF files, or download them individually.
   - View the summary table of extracted data.

---

### Run on Cloud (Streamlit Sharing)

1. **Sign Up**:
   - Go to [https://streamlit.io/cloud](https://www.streamlit.io/cloud) and create an account.

2. **Prepare Code**:
   - Save the code as `app.py`.
   - Create a `requirements.txt` file with the following content:
     ```txt
     streamlit == 1.41.1
     pandas == 2.2.3
     fpdf == 1.7.2
     ```

3. **Upload to GitHub**:
   - Create a GitHub account (if you don’t have one) at [github.com](https://github.com).
   - Create a repository and upload the `app.py` and `requirements.txt` files.

4. **Deploy the App**:
   - On Streamlit Cloud, connect your GitHub repository.
   - Deploy the app and share the generated link.

5. **Use the App**:
   - Visit the app link.
   - Upload XML files, process them, and download the ZIP containing all converted TXT and PDF files.

---

### Features and Functionality:

- **Upload Multiple XML Files**: Supports batch processing, allowing you to upload and process multiple XML files at once.

- **Conversion to TXT & PDF**: Each uploaded XML file will be converted to both a **TXT** file and a **PDF** file. The PDF is styled with headers, footers, and data in a readable format.

- **Summary Table**: A summary table is generated showing important extracted information from the XML files, such as:
  - Name
  - Gender
  - Date of Birth
  - PAN Number
  - Application Date
  - Email Address
  - City

- **Download Options**:
  - **Single File**: If only one XML file is uploaded, you can download the converted TXT and PDF files individually.
  - **Multiple Files**: If multiple XML files are uploaded, all converted TXT and PDF files can be downloaded as **ZIP archives**.

- **Clean Design**: The app has a simple and easy-to-navigate UI, with a professional look and feel, including a company logo and a fixed footer with a link to **Candor Investing**.

---

### Notes:

- **Temporary Files**: The app uses temporary directories to store uploaded files and processed results. All files are automatically cleaned up after processing is complete.
- **Logo**: Make sure to place a `candor_investing_logo.png` file in the same directory as `app.py` for the logo to be displayed correctly in the PDF header.
