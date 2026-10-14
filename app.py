import streamlit as st

st.set_page_config(page_title="NEET Important Chapters", page_icon="🩺", layout="centered")

DATA = {
    "Biology": {
        "Human Physiology (combined)": 12.0,
        "Ecology & Environment": 7.5,
        "Molecular Basis of Inheritance": 6.5,
        "Cell: The Unit of Life + Cell Cycle": 6.0,
        "Biotechnology (Principles + Applications)": 6.0,
        "Principles of Inheritance & Variation": 5.5,
        "Human Reproduction + Reproductive Health": 5.0,
        "Plant Physiology": 5.0,
        "Animal Kingdom + Biological Classification": 5.0,
        "Sexual Reproduction in Flowering Plants": 4.5,
        "Biomolecules": 3.0,
    },
    "Physics": {
        "Mechanics (Laws of Motion, Rotational Motion, Gravitation)": 7.0,
        "Modern Physics + Semiconductors + Atoms & Nuclei": 5.5,
        "Current Electricity": 4.0,
        "Electrostatics + Capacitance": 4.0,
        "Moving Charges & Magnetism + EMI + AC": 4.0,
        "Ray Optics + Wave Optics": 3.5,
        "Thermodynamics + KTG": 3.5,
        "Units, Measurements & Errors": 2.0,
    },
    "Chemistry": {
        "Organic Chemistry (GOC, Hydrocarbons, Carbonyls, Amines)": 10.0,
        "Chemical Bonding & Molecular Structure": 4.0,
        "Electrochemistry + Chemical Kinetics": 4.0,
        "Coordination Compounds": 3.5,
        "p-Block Elements": 3.5,
        "Equilibrium (Chemical + Ionic)": 3.0,
        "d- & f-Block + Solutions": 3.0,
        "Thermodynamics": 2.5,
    },
}

def priority(weight):
    if weight >= 6:
        return "🔥 Critical"
    if weight >= 4:
        return "⭐ High Priority"
    return "📌 Medium Priority"

st.title("🩺 NEET Important Chapters")
st.caption("A focused chapter checklist for your NEET preparation")
st.warning("Question-weightage figures are rough estimates, not predictions or guarantees. Check the current official NEET syllabus.")

subject = st.selectbox("Choose subject", ["All Subjects", *DATA.keys()])
search = st.text_input("🔎 Search chapters", placeholder="e.g. Genetics, Optics, Bonding").strip().lower()

subjects = DATA if subject == "All Subjects" else {subject: DATA[subject]}
chapters = [(sub, chapter, weight) for sub, items in subjects.items() for chapter, weight in items.items() if search in chapter.lower()]
chapters.sort(key=lambda item: item[2], reverse=True)

critical = sum(1 for _, _, weight in chapters if weight >= 6)
high = sum(1 for _, _, weight in chapters if 4 <= weight < 6)
col1, col2, col3 = st.columns(3)
col1.metric("Chapters shown", len(chapters))
col2.metric("Critical", critical)
col3.metric("High priority", high)

st.subheader("Your chapter list")
if not chapters:
    st.info("No matching chapters. Try another search.")
else:
    for sub, chapter, weight in chapters:
        with st.container(border=True):
            st.markdown(f"**{chapter}**")
            st.caption(sub)
            col1, col2 = st.columns(2)
            col1.write(priority(weight))
            col2.write(f"Estimated weight: {weight:g} questions/year")
            st.checkbox("Mark as revised", key=f"revised_{sub}_{chapter}")

st.divider()
st.caption("Use this list for prioritisation, not as a substitute for the full syllabus, NCERT, and question practice.")
