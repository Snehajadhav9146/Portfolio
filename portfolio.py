import streamlit as st
from PIL import Image

# Initialize session state
if 'loggedIn' not in st.session_state:
    st.session_state['loggedIn'] = False

def login():
    st.title('Login')
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == 'Sneha' and password == 'Pratya':
            st.session_state['loggedIn'] = True
        else:
            st.error("Invalid username or password")

# Portfolio Data
portfolio = {
    "name": "Sneha Tukaram Jadhav",
    "about": "Aspiring Data Scientist passionate about leveraging technology to solve real-world problems.",
    "skills": ["Data Science", "Data Analytics", "Python", "Machine Learning", "SQL", "Data Visualization", "Networking", "Tableau"],
    "projects": [
        {
            "title": "IoT-Based Women's Safety System",
            "description": "Developed an IoT system for women's safety with real-time location tracking.",
            "technologies": ["Raspberry Pi", "GPS Module", "Python"],
            "link": "https://github.com/SnehaJadhav1018/iot-safety-system"
        },
        {
            "title": "House Price Prediction",
            "description": "Implemented a machine learning model to predict house prices based on multiple features.",
            "technologies": ["Python", "scikit-learn", "pandas"],
            "link": "https://github.com/SnehaJadhav1018/house-price-prediction"
        },
        {
            "title": "Mall Customer Segmentation",
            "description": "Performed customer segmentation using clustering techniques to analyze spending behavior.",
            "technologies": ["Python", "scikit-learn", "pandas", "Tableau"],
            "link": "https://public.tableau.com/views/MallCustomerSegmentation"
        },
        {
            "title": "Sales Dashboard in Tableau",
            "description": "Designed an interactive Tableau dashboard for sales performance analysis.",
            "technologies": ["Tableau"],
            "link": "https://public.tableau.com/views/SalesDashboard"
        },
        {
            "title": "Employee Data Analysis",
            "description": "Analyzed employee datasets to derive insights on attrition and performance trends.",
            "technologies": ["Python", "pandas", "Tableau"],
            "link": "https://public.tableau.com/views/EmployeeDataAnalysis"
        },
        {
            "title": "Netflix Analysis Dashboard",
            "description": "Developed a Tableau dashboard to analyze Netflix content trends across different genres and regions.",
            "technologies": ["Tableau"],
            "link": "https://public.tableau.com/views/NetflixAnalysisDashboard"
        },
        {
            "title": "IPL Analysis Dashboard",
            "description": "Created an interactive IPL performance dashboard to visualize team and player statistics.",
            "technologies": ["Tableau"],
            "link": "https://public.tableau.com/views/IPLAnalysisDashboard"
        },
        {
            "title": "Customer Churn Prediction",
            "description": "Implemented a machine learning model to predict customer churn based on behavioral data.",
            "technologies": ["Python", "scikit-learn", "pandas", "Tableau"],
            "link": "https://github.com/SnehaJadhav1018/CustomerChurnPrediction"
        },
        {
            "title": "Movie Recommendation System",
            "description": "Built a recommendation system using collaborative filtering to suggest movies based on user preferences.",
            "technologies": ["Python", "scikit-learn", "pandas"],
            "link": "https://github.com/SnehaJadhav1018/MovieRecommendationSystem"
        }
    ],
    "education": "B.E. in Computer Engineering - Ajinkya D.Y. Patil School of Engineering, Lohegaon, Pune (2024)",
    "contact": {
        "Email": "sneha3020jadhav@gmail.com",
        "LinkedIn": "https://www.linkedin.com/in/snehajadhav1018/",
        "GitHub": "https://github.com/Snehajadhav9146",
    },
    "resume": "DS Resume.pdf",  # Updated resume file
}

# Main App
if not st.session_state['loggedIn']:
    login()
else:
    st.set_page_config(page_title=f"{portfolio['name']}'s Portfolio", layout="wide")

    # Sidebar Profile Picture
    uploaded_file = st.sidebar.file_uploader("Upload Profile Picture", type=["jpg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.sidebar.image(image, caption="Uploaded Profile Picture", use_container_width=True)
    else:
        st.sidebar.image("WB img.jpg", caption="Profile Picture", width=150)

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "💡 Skills", "📂 Projects", "🎓 Education & Contact"])

    # Home Tab
    with tab1:
        st.header("Welcome!")
        st.write(portfolio["about"])
        try:
            with open(portfolio["resume"], "rb") as f:
                st.download_button(
                    label="Download Resume",
                    data=f,
                    file_name="Sneha_Jadhav_Resume.pdf",
                    mime="application/pdf",
                )
        except FileNotFoundError:
            st.error("Resume file not found!")

    # Skills Tab
    with tab2:
        st.header("My Skills")
        selected_skill = st.selectbox("Select a skill to learn more:", portfolio["skills"])
        st.write(f"### {selected_skill}")
        st.write(f"I have hands-on experience in {selected_skill}.")

    # Projects Tab
    with tab3:
        st.header("My Projects")
        for project in portfolio["projects"]:
            with st.expander(f"📌 {project['title']}"):
                st.write(project["description"])
                st.write(f"**Technologies Used:** {', '.join(project['technologies'])}")
                st.write(f"[View Project]({project['link']})")

    # Education & Contact Tab
    with tab4:
        st.header("Education")
        st.write(portfolio["education"])
        st.header("Contact")
        st.write(f"- 📧 **Email:** [Send Email](mailto:{portfolio['contact']['Email']})")
        st.write(f"- 🌐 **LinkedIn:** [Visit LinkedIn]({portfolio['contact']['LinkedIn']})")
        st.write(f"- 🐙 **GitHub:** [Visit GitHub]({portfolio['contact']['GitHub']})")

    # Logout Button
    if st.sidebar.button("Logout"):
        st.session_state['loggedIn'] = False
        st.experimental_rerun()
