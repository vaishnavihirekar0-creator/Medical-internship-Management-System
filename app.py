import streamlit as st

st.set_page_config(
    page_title="Medical Internship Management System",
    layout="wide"
)

# ---------- LOGIN ----------
if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:

    st.title("Medical Internship Management System")
    st.caption("Internship Management Portal")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.session_state.login = True
            st.rerun()
        else:
            st.error("Invalid username or password")

    st.stop()


# ---------- SIDEBAR ----------
st.sidebar.title("Medical Internship System")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Student Records",
        "Internship Records",
        "Notifications",
        "Certificates",
        "Documents",
        "Reports"
    ]
)

if st.sidebar.button("Logout"):
    st.session_state.login = False
    st.rerun()


# ---------- DASHBOARD ----------
if page == "Dashboard":

    st.title("Dashboard")
    st.write("Overview of medical internship activities.")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Students", "25")
    c2.metric("Active Internships", "12")
    c3.metric("Completed", "9")
    c4.metric("Pending Certificates", "4")

    st.divider()

    st.subheader("Recent Student Records")

    st.dataframe(
        [
            ["INT001", "Rahul Patil", "Cardiology", "Active"],
            ["INT002", "Priya Sharma", "Medicine", "Completed"],
            ["INT003", "Amit Joshi", "Surgery", "Active"],
        ],
        column_config={
            0: "Intern ID",
            1: "Student Name",
            2: "Department",
            3: "Status"
        },
        hide_index=True,
        use_container_width=True
    )

    st.subheader("Upcoming / Pending")

    st.info("Rahul Patil — Internship ends on 15 October.")
    st.warning("Priya Sharma — Completion certificate pending.")
    st.warning("Amit Joshi — Joining document pending.")


# ---------- STUDENT RECORDS ----------
elif page == "Student Records":

    st.title("Student Records")

    search = st.text_input("Search student")

    st.subheader("Add Student")

    name = st.text_input("Student Name")
    roll_no = st.text_input("Roll Number")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    college = st.text_input("College")

    if st.button("Add Student"):
        if name and roll_no:
            st.success("Student added successfully.")
        else:
            st.error("Enter student name and roll number.")

    st.divider()

    st.subheader("Student List")

    st.dataframe(
        [
            ["INT001", "Rahul Patil", "123", "Cardiology"],
            ["INT002", "Priya Sharma", "124", "Medicine"],
            ["INT003", "Amit Joshi", "125", "Surgery"]
        ],
        column_config={
            0: "Intern ID",
            1: "Name",
            2: "Roll Number",
            3: "Department"
        },
        hide_index=True,
        use_container_width=True
    )


# ---------- INTERNSHIP RECORDS ----------
elif page == "Internship Records":

    st.title("Internship Records")

    student = st.selectbox(
        "Select Student",
        ["Rahul Patil", "Priya Sharma", "Amit Joshi"]
    )

    hospital = st.text_input("Hospital")
    department = st.selectbox(
        "Department",
        ["Medicine", "Surgery", "Cardiology", "Pediatrics"]
    )
    supervisor = st.text_input("Supervisor")

    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input("Start Date")

    with col2:
        end_date = st.date_input("End Date")

    status = st.selectbox(
        "Status",
        ["Upcoming", "Active", "Completed"]
    )

    if st.button("Save Internship"):
        st.success("Internship record saved successfully.")


# ---------- NOTIFICATIONS ----------
elif page == "Notifications":

    st.title("Notifications")

    st.warning("Internship ending soon: Rahul Patil — 15 October")
    st.warning("Certificate pending: Priya Sharma")
    st.info("Internship starting soon: Amit Joshi")
    st.info("Joining document pending: Amit Joshi")


# ---------- CERTIFICATES ----------
elif page == "Certificates":

    st.title("Certificates")

    student = st.selectbox(
        "Student",
        ["Rahul Patil", "Priya Sharma", "Amit Joshi"]
    )

    certificate_type = st.selectbox(
        "Certificate Type",
        ["Internship Certificate", "Completion Certificate"]
    )

    certificate = st.file_uploader(
        "Upload Certificate",
        type=["pdf", "jpg", "png"]
    )

    if st.button("Save Certificate"):
        if certificate:
            st.success("Certificate uploaded successfully.")
        else:
            st.warning("Please select a certificate.")

    st.divider()

    st.subheader("Certificate Status")

    st.dataframe(
        [
            ["Rahul Patil", "Internship Certificate", "Issued"],
            ["Priya Sharma", "Completion Certificate", "Pending"],
            ["Amit Joshi", "Internship Certificate", "Not Uploaded"]
        ],
        column_config={
            0: "Student",
            1: "Certificate",
            2: "Status"
        },
        hide_index=True,
        use_container_width=True
    )


# ---------- DOCUMENTS ----------
elif page == "Documents":

    st.title("Documents")

    student = st.selectbox(
        "Select Student",
        ["Rahul Patil", "Priya Sharma", "Amit Joshi"]
    )

    document_type = st.selectbox(
        "Document Type",
        ["ID Proof", "Joining Letter", "Completion Certificate"]
    )

    document = st.file_uploader(
        "Upload Document",
        type=["pdf", "jpg", "png"]
    )

    if st.button("Upload Document"):
        if document:
            st.success("Document uploaded successfully.")
        else:
            st.warning("Please select a document.")

    st.divider()

    st.subheader("Document Status")

    st.write("ID Proof — Available")
    st.write("Joining Letter — Available")
    st.write("Completion Certificate — Pending")


# ---------- REPORTS ----------
elif page == "Reports":

    st.title("Reports")

    st.subheader("Internship Summary")

    st.dataframe(
        [
            ["Medicine", 8, 5, 2, 1],
            ["Surgery", 6, 3, 2, 1],
            ["Cardiology", 5, 2, 2, 1],
            ["Pediatrics", 6, 2, 3, 1]
        ],
        column_config={
            0: "Department",
            1: "Total",
            2: "Active",
            3: "Completed",
            4: "Upcoming"
        },
        hide_index=True,
        use_container_width=True
    )

    st.button("Download Report")