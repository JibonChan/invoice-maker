import streamlit as st
import weasyprint
from io import BytesIO

# HTML content of the invoice (same as earlier)
html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            font-size: 14px;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 800px;
            margin: 0 auto;
            background-color: #F0F0F0;
            padding: 20px;
            overflow-x: auto;
        }

        .invoice {
            border: 1px solid #ccc;
            padding: 20px;
            background-color: white;
        }

        .invoice-header {
            text-align: center;
            margin-bottom: 20px;
        }
        .invoice-sub-header {
            width: 96%;
            margin: auto 2%;
            color: #2b2b32;
            display: flex;
            justify-content: space-between;
        }

        .invoice-header h1 {
            margin: 0;
            font-size: 40px;
            font-weight: bold;
        }

        .invoice-header h2 {
            font-size: 16px;
            margin-top: 2px;
        }

        .invoice-details {
            margin-top: 10px;
            margin-bottom: 20px;
            color: #2b2b32;
        }

        .invoice-details table {
            width: 96%;
            border-collapse: collapse;
        }

        .invoice-details table th,
        .invoice-details table td {
            border: 1px solid #ccc;
            padding: 10px;
            text-align: left;
        }

        .invoice-details table th {
            font-weight: normal;
            background-color: #f2f2f2;
        }

        .invoice-footer {
            text-align: center;
            font-size: 12px;
            margin-top: 20px;
        }

        .invoice-footer p {
            font-weight: bold;
            margin: 0;
            padding: 0;
        }

        .invoice-date,
        .invoice-to {
            margin-bottom: 0px;
        }

        .blue-text {
            color: #5e5b95;
        }

    </style>
</head>
<body>

<div class="container" id="invoice-container">
    <div class="invoice">
        <div class="invoice-header blue-text">
            <h1>INVOICE</h1>
            <h2>NGOVI HOMESTAY</h2>
        </div>

        <div class="invoice-sub-header">
            <div class="invoice-date">
                <b class="blue-text">DATE :</b> <span id="invoice-date">18 January 2025</span>
            </div>
            <div class="invoice-to">
                <b class="blue-text">TO :</b> <span id="invoice-to">Ana Awami</span>
            </div>
        </div>

        <hr>

        <div class="invoice-details">
            <center>
                <table>
                    <tr>
                        <th>Check In</th>
                        <td><span id="check-in">14th January 2025</span></td>
                    </tr>
                    <tr>
                        <th>Check Out</th>
                        <td><span id="check-out">18th January 2025</span></td>
                    </tr>
                    <tr>
                        <th>Room Cost (<span id="room_type">2</span>BHK <span id="withac">AC</span> Unit)</th>
                        <td>Rs. <span id="rate">3000</span>/day</td>
                    </tr>
                    <tr>
                        <th>Fooding</th>
                        <td>Rs. <span id="fooding">0</span> (Lunch and Dinner)</td>
                    </tr>
                    <tr>
                        <th>Duration Of Stay</th>
                        <td><span id="duration">4</span> Days</td>
                    </tr>
                    <tr>
                        <th>Grand Total</th>
                        <td>Rs. <span id="total">12000</span></td>
                    </tr>
                </table>
            </center>
        </div>

        <div class="invoice-footer blue-text">
            <p>NGOVI HOMESTAY | 5th BYLANE, SHAKUNTALA PATH, DOWNTOWN, 781001, GUWAHATI</p>
            <p>PHONE: +91 9101431108/9366016858</p>
        </div>
    </div>
</div>

</body>
</html>
"""

# Function to convert HTML to PDF
def html_to_pdf(html):
    # Convert HTML to PDF using weasyprint
    pdf = weasyprint.HTML(string=html).write_pdf()
    return pdf

# Title of the app
st.title("Invoice Maker")

# Render HTML content in Streamlit
st.components.v1.html(html_content, height=600, scrolling=True)

# Button to generate PDF
if st.button('Download Invoice as PDF'):
    # Convert HTML content to PDF
    pdf = html_to_pdf(html_content)
    
    # Display download link
    st.download_button(
        label="Download PDF",
        data=pdf,
        file_name="invoice.pdf",
        mime="application/pdf"
    )
