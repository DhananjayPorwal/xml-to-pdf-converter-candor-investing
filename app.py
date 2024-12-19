# Importing Libraries
import os
import zipfile
import xml.etree.ElementTree as ET
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from fpdf import FPDF
import streamlit as st
import pandas as pd
import tempfile
import shutil

# Streamlit Configuration
st.set_page_config(page_title="KRA XML CONVERTER", page_icon="logox.png", menu_items={
        'Get Help': 'mailto:dporwal985@gmail.com',
        'Report a bug': "mailto:dporwal985@gmail.com",
        'About': "### Created by [Candor Investing](https://www.candorinvesting.com/)"
    })  # Set wide layout for the page

# Load the custom CSS from an external file
def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Use the function to load the CSS
load_css()

def parse_xml(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        data = {}
        additional_info = []

        for elem in root.iter():
            if elem.tag not in data:
                data[elem.tag] = elem.text.strip() if elem.text else None
            else:
                additional_info.append({elem.tag: elem.text.strip() if elem.text else None})

        return data, additional_info

    except Exception as e:
        return None, f"Error parsing XML: {e}"

def generate_pdf(data, additional_info, output_file, logo_path):
    class PDF(FPDF):
        def footer(self):
            # Set position 1.5 cm from bottom
            self.set_y(-15)
            # Set font for footer
            self.set_font("Arial", size=8)
            # Add the page number
            page_num = self.page_no()
            self.cell(0, 10, f"Page {page_num}", 0, 0, "C")
    
    # Initialize PDF object
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Add header with logo
    if logo_path:
        pdf.image(logo_path, 10, 8, 33)
    pdf.set_font("Arial", size=12)
    pdf.set_xy(50, 10)
    pdf.cell(0, 10, "XML to Readable PDF", ln=True, align="R")
    pdf.ln(10)

    # Add name as heading
    pdf.set_font("Arial", style="B", size=20)
    pdf.set_text_color(0, 102, 204)
    name = data.get("APP_NAME", "Unknown")
    pdf.cell(0, 10, name, ln=True, align="C")
    pdf.ln(10)

    # Add details in key-value pairs without overlapping
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)
    col_width_key = 100  # Width for the key column
    line_height = 8  # Line height for better spacing

    for key, value in data.items():
        if value:
            pdf.set_font("Arial", style="B", size=12)
            pdf.cell(col_width_key, line_height, f"{key}: ", border=0)
            pdf.set_font("Arial", size=12)
            # Wrap long values into multiple lines
            pdf.multi_cell(0, line_height, value)  
            pdf.ln(1)  # Add spacing between lines

    # Add additional info section with wrapping
    if additional_info:
        pdf.ln(5)
        pdf.set_font("Arial", style="B", size=14)
        pdf.cell(0, 10, "Additional Information:", ln=True)
        pdf.set_font("Arial", size=12)
        for info in additional_info:
            for key, value in info.items():
                pdf.cell(col_width_key, line_height, f"{key}: ", border=0)
                pdf.multi_cell(0, line_height, value if value else "Not Provided")  
                pdf.ln(1)

    # Add footer with custom footer method
    pdf.set_y(-30)
    pdf.set_font("Arial", size=8)
    pdf.cell(0, 10, "This tool converts KRA XML files to readable formats. It does not modify any data.", 0, 0, "C")

    # Save the output to the file
    pdf.output(output_file)


def main():

    # Add company logo
    logo_path = "candor_investing_logo.png"  # Ensure this logo file is in the same directory as this script
    st.image(logo_path, width=150)  # You can adjust the width as needed

    st.title("XML to Readable TXT and PDF Converter")
    st.write("Upload XML files to generate readable TXT and PDF files.")

    uploaded_files = st.file_uploader("Upload XML Files", type=["xml"], accept_multiple_files=True)

    if uploaded_files:
        temp_dir = tempfile.mkdtemp()
        txt_files = []
        pdf_files = []

        summary_data = []

        for uploaded_file in uploaded_files:
            file_path = os.path.join(temp_dir, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getvalue())

            data, additional_info = parse_xml(file_path)
            if not data:
                st.error(f"Failed to parse {uploaded_file.name}. Skipping.")
                continue

            # Generate TXT file
            txt_file_name = f"{data.get('APP_PAN_NO', 'Unknown')}_{data.get('APP_NAME', 'Unknown').replace(' ', '_')}.txt"
            txt_file_path = os.path.join(temp_dir, txt_file_name)
            with open(txt_file_path, "w", encoding="utf-8") as txt_file:
                for key, value in data.items():
                    if value:
                        txt_file.write(f"{key}: {value}\n")
                if additional_info:
                    txt_file.write("\nAdditional Information:\n")
                    for info in additional_info:
                        for key, value in info.items():
                            txt_file.write(f"{key}: {value if value else 'Not Provided'}\n")

            txt_files.append(txt_file_path)

            # Generate PDF file
            pdf_file_name = f"{data.get('APP_PAN_NO', 'Unknown')}_{data.get('APP_NAME', 'Unknown').replace(' ', '_')}.pdf"
            pdf_file_path = os.path.join(temp_dir, pdf_file_name)
            generate_pdf(data, additional_info, pdf_file_path, logo_path)
            pdf_files.append(pdf_file_path)

            # Add to summary data
            summary_data.append({
                "Name": data.get("APP_NAME", "Unknown"),
                "Gender": data.get("APP_GEN", "Unknown"),
                "DOB": data.get("APP_DOB_DT", "Unknown"),
                "PAN": data.get("APP_PAN_NO", "Unknown"),
                "Application Date": data.get("APP_DATE", "Unknown"),
                "City": data.get("APP_PER_CITY", "Unknown"),
                "Email": data.get("APP_EMAIL", "Unknown").lower()
            })

        # Display summary table
        st.subheader("Summary")
        df = pd.DataFrame(summary_data)
        st.dataframe(df.style.set_table_attributes('style="margin-left: auto; margin-right: auto;"'), hide_index=True)

        # Provide download options
        if len(uploaded_files) == 1:
            col1, col2 = st.columns(2)
            with col1:
                with open(txt_files[0], "rb") as f:
                    st.download_button("Download TXT File", f, file_name=os.path.basename(txt_files[0]))
            with col2:
                with open(pdf_files[0], "rb") as f:
                    st.download_button("Download PDF File", f, file_name=os.path.basename(pdf_files[0]))
        else:
            now = datetime.now().strftime("%d_%b_%y_%H_%M_%S")

            txt_zip_path = os.path.join(temp_dir, f"Converted_TXT_{now}.zip")
            with zipfile.ZipFile(txt_zip_path, "w") as txt_zip:
                for txt_file in txt_files:
                    txt_zip.write(txt_file, os.path.basename(txt_file))

            pdf_zip_path = os.path.join(temp_dir, f"Converted_PDF_{now}.zip")
            with zipfile.ZipFile(pdf_zip_path, "w") as pdf_zip:
                for pdf_file in pdf_files:
                    pdf_zip.write(pdf_file, os.path.basename(pdf_file))

            col1, col2 = st.columns(2)
            with col1:
                with open(txt_zip_path, "rb") as f:
                    st.download_button("Download All TXT Files as ZIP", f, file_name=os.path.basename(txt_zip_path))
            with col2:
                with open(pdf_zip_path, "rb") as f:
                    st.download_button("Download All PDF Files as ZIP", f, file_name=os.path.basename(pdf_zip_path))

        # Cleanup
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()



# MARK: FOOTER

footer="""<style>
a:link , a:visited{
color: #075e54;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #dcf8c6;
color: #128c7e;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with 💖 by <a href="https://candorinvesting.com/">Candor Investing</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)