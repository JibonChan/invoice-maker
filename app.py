import streamlit as st

# Hardcode credentials
SECRET_USERNAME = "ano"
SECRET_PASSWORD = "anoAwomi@123#"

# Function to check credentials
def check_credentials(username, password):
    return username == SECRET_USERNAME and password == SECRET_PASSWORD

# Title of the app
st.title("Invoice Generator")

# Session state to track login status
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Function to show login form
def show_login_form():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Verify login
    if st.button("Login"):
        if check_credentials(username, password):
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.experimental_rerun()  # Force the app to rerun and show invoice content
        else:
            st.error("Invalid username or password. Please try again.")

# Function to show invoice content after login
def show_invoice():
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
                margin: 0;
                padding: 0;
            }

            .scrollable-container {
                max-height: 600px; /* Set a max height for the scrollable container */
                overflow-y: auto;
                padding: 10px;
                border: 1px solid #ccc;
                background-color: #f9f9f9;
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
        <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    </head>
    <body>
    <div class="scrollable-container">
        <div class="container">
            <div id="invoice-content" class="invoice">
                <div class="invoice-header blue-text">
                <h1>INVOICE</h1>
                <h2>NGOVI HOMESTAY</h2>
                </div>

                <div class="invoice-sub-header">
                    <div class="invoice-date">
                        <b class="blue-text">DATE :</b> <span id="invoice-date">18 January 2025</span>
                    </div>
                    <div class="invoice-to">
                        <b class="blue-text">TO :</b> <span id="invoice-to">Customer name</span> <span><br> +91 <span id="phone_no">8888888888</span></span>
                    </div>
                </div>

                <hr></hr>

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
                    <p>PHONE: +91 9101431108  |  9366016858</p>
                </div>
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
            makeEditable("phone_no");

            // Download PDF functionality
            $("#downloadButton").on("click", function() {
                const invoiceElement = document.getElementById("invoice-content"); 
                html2canvas(invoiceElement, { scale: 3 }).then(function(canvas) { // Increased scale for better quality
                    const imgData = canvas.toDataURL("image/png");
                    const { jsPDF } = window.jspdf;
                    const doc = new jsPDF("p", "mm", "a4");

                    const pdfWidth = doc.internal.pageSize.getWidth();
                    const pdfHeight = (canvas.height * pdfWidth) / canvas.width;

                    doc.addImage(imgData, "PNG", 0, 0, pdfWidth, pdfHeight);
                    doc.save("invoice.pdf");
                });
            });
        });
    </script>
    </body>
    </html>
    """

    # Embed the HTML content in the Streamlit app
    st.components.v1.html(html_content, height=800, scrolling=True)

# Main app flow
if not st.session_state.logged_in:
    show_login_form()
else:
    show_invoice()
