import streamlit as st

# HTML content for the invoice with embedded JavaScript (jsPDF and DOMPurify)
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
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/dompurify/2.3.7/purify.min.js"></script>
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

<button id="downloadButton" style="padding: 10px; background-color: #4CAF50; color: white; border: none; cursor: pointer;">Download PDF</button>

<script>
    $(document).ready(function() {
        // Make fields editable
        function makeEditable(spanId) {
            $("#" + spanId).on("click", function() {
                const $this = $(this);
                if ($this.find("input").length > 0) return;
                const currentText = $this.text();
                $this.html(`<input type="text" value="${escapeHtml(currentText)}" />`);
                const $input = $this.find("input");
                $input.focus().select();
                $input.on("blur keydown", function(e) {
                    if (e.type === "blur" || (e.type === "keydown" && e.key === "Enter")) {
                        const newText = $input.val().trim() || currentText;
                        $this.text(escapeHtml(newText));
                    }
                });
            });
        }

        function escapeHtml(str) {
            return str.replace(/[&<>"'/]/g, function(match) {
                const escapeMap = {
                    '&': '&amp;',
                    '<': '&lt;',
                    '>': '&gt;',
                    '"': '&quot;',
                    "'": '&#39;',
                    '/': '&#x2F;'
                };
                return escapeMap[match];
            });
        }

        makeEditable("invoice-date");
        makeEditable("invoice-to");
        makeEditable("check-in");
        makeEditable("check-out");
        makeEditable("room_type");
        makeEditable("withac");
        makeEditable("rate");
        makeEditable("fooding");
        makeEditable("duration");
        makeEditable("total");

        // Download PDF using jsPDF
        document.getElementById('downloadButton').onclick = function() {
            const { jsPDF } = window.jspdf;
            const doc = new jsPDF();

            // Capture the content to be converted to PDF
            const invoiceContent = document.querySelector('.container').innerHTML;

            // Sanitize the HTML content using DOMPurify
            const sanitizedContent = DOMPurify.sanitize(invoiceContent);

            // Add the content to PDF
            doc.html(sanitizedContent, {
                callback: function (doc) {
                    doc.save('invoice.pdf');
                },
                margin: [10, 10, 10, 10],
                autoPaging: true
            });
        };
    });
</script>

</body>
</html>
"""

# Title of the app
st.title("Invoice Maker")

# Render HTML content in Streamlit
st.components.v1.html(html_content, height=600, scrolling=True)
