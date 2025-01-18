import streamlit as st

# Title of the app
st.title("Invoice Generator")

# Add a note to users about editing
st.markdown(
    """
    ### Instructions:
    - Click on any field in the invoice to edit its value.
    - Once you're done, click the "Download PDF" button to save the invoice as a PDF.
    """
)

# HTML content for the invoice
html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            font-size: 14px;
        }

        .container {
            width: 800px;
            margin: auto;
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

        .invoice-header h1 {
            margin: 0;
            font-size: 32px;
            font-weight: bold;
        }

        .invoice-header h2 {
            font-size: 16px;
            margin-top: 2px;
        }

        .invoice-sub-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        .invoice-details {
            margin-top: 10px;
            margin-bottom: 20px;
        }

        .invoice-details table {
            width: 100%;
            border-collapse: collapse;
        }

        .invoice-details table th,
        .invoice-details table td {
            border: 1px solid #ccc;
            padding: 10px;
            text-align: left;
        }

        .invoice-footer {
            text-align: center;
            font-size: 12px;
            margin-top: 20px;
        }

        .blue-text {
            color: #2b2b95;
        }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
<div class="container">
    <div class="invoice">
        <div class="invoice-header blue-text">
            <h1>INVOICE</h1>
            <h2>NGOVI HOMESTAY</h2>
        </div>

        <div class="invoice-sub-header">
            <div><b>DATE: </b><span id="invoice-date">18 January 2025</span></div>
            <div><b>TO: </b><span id="invoice-to">Ana Awami</span></div>
        </div>

        <div class="invoice-details">
            <table>
                <tr>
                    <th>Check In</th>
                    <td><span id="check-in">14 January 2025</span></td>
                </tr>
                <tr>
                    <th>Check Out</th>
                    <td><span id="check-out">18 January 2025</span></td>
                </tr>
                <tr>
                    <th>Room Cost (2BHK AC Unit)</th>
                    <td>Rs. <span id="rate">3000</span>/day</td>
                </tr>
                <tr>
                    <th>Fooding</th>
                    <td>Rs. <span id="fooding">0</span></td>
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
        </div>

        <div class="invoice-footer">
            <p><b>NGOVI HOMESTAY</b></p>
            <p>5th BYLANE, SHAKUNTALA PATH, DOWNTOWN, 781001, GUWAHATI</p>
            <p>PHONE: +91 9101431108/9366016858</p>
        </div>
    </div>
</div>

<button id="downloadButton" style="margin-top: 20px; padding: 10px; background-color: #4CAF50; color: white; border: none;">Download PDF</button>

<script>
    $(document).ready(function() {
        // Make fields editable
        function makeEditable(spanId) {
            $("#" + spanId).on("click", function() {
                const $this = $(this);
                if ($this.find("input").length > 0) return;
                const currentText = $this.text();
                $this.html(`<input type="text" value="${currentText}" />`);
                const $input = $this.find("input");
                $input.focus().select();
                $input.on("blur keydown", function(e) {
                    if (e.type === "blur" || (e.type === "keydown" && e.key === "Enter")) {
                        const newText = $input.val().trim() || currentText;
                        $this.text(newText);
                    }
                });
            });
        }

        makeEditable("invoice-date");
        makeEditable("invoice-to");
        makeEditable("check-in");
        makeEditable("check-out");
        makeEditable("rate");
        makeEditable("fooding");
        makeEditable("duration");
        makeEditable("total");

        // Download PDF functionality
        $("#downloadButton").on("click", function() {
            const { jsPDF } = window.jspdf;
            const doc = new jsPDF();

            doc.setFontSize(20);
            doc.text("INVOICE", 105, 20, { align: "center" });

            doc.setFontSize(12);
            doc.text("Date: " + $("#invoice-date").text(), 20, 40);
            doc.text("To: " + $("#invoice-to").text(), 20, 50);

            doc.text("Check In: " + $("#check-in").text(), 20, 70);
            doc.text("Check Out: " + $("#check-out").text(), 20, 80);
            doc.text("Room Cost: Rs. " + $("#rate").text() + "/day", 20, 90);
            doc.text("Fooding: Rs. " + $("#fooding").text(), 20, 100);
            doc.text("Duration Of Stay: " + $("#duration").text() + " Days", 20, 110);
            doc.text("Grand Total: Rs. " + $("#total").text(), 20, 120);

            doc.save("invoice.pdf");
        });
    });
</script>
</body>
</html>
"""

# Embed the HTML content in the Streamlit app
st.components.v1.html(html_content, height=800)
