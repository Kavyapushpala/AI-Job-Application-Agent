import re

# ----------------------------------------
# Skills Database
# ----------------------------------------

SKILLS_DATABASE = [
    "Python", "Java", "C", "C++", "JavaScript", "TypeScript",
    "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch",
    "Scikit-learn", "OpenCV", "NLP", "Computer Vision",
    "LLM", "LangChain", "LangGraph",
    "React", "Next.js", "FastAPI", "Flask",
    "HTML", "CSS", "Bootstrap", "Tailwind CSS",
    "SQL", "MySQL", "PostgreSQL", "MongoDB",
    "Supabase", "SQLite",
    "Git", "GitHub", "Docker", "Linux",
    "AWS", "Azure", "Google Cloud",
    "REST API", "Pandas", "NumPy", "Power BI"
]

# ----------------------------------------
# Education Keywords
# ----------------------------------------

EDUCATION_KEYWORDS = [
    "Bachelor",
    "B.Tech",
    "B.E",
    "BSc",
    "M.Tech",
    "M.E",
    "MSc",
    "MBA",
    "Intermediate",
    "SSC",
    "High School"
]


# ----------------------------------------
# Generic Section Extractor
# ----------------------------------------

def extract_section(text, section_names):

    lines = text.split("\n")

    section = []

    capture = False

    for line in lines:

        cleaned = line.strip()

        if not cleaned:
            continue

        lower = cleaned.lower()

        # Start section
        if any(name in lower for name in section_names):
            capture = True
            continue

        # Stop section
        if capture:

            if (
                "education" in lower or
                "skills" in lower or
                "projects" in lower or
                "experience" in lower or
                "certification" in lower or
                "achievement" in lower or
                "languages" in lower or
                "interests" in lower
            ):
                break

            section.append(cleaned)

    return section


# ----------------------------------------
# Email
# ----------------------------------------

def extract_email(text):

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    match = re.search(pattern, text)

    return match.group() if match else None


# ----------------------------------------
# Phone
# ----------------------------------------

def extract_phone(text):

    pattern = r"(?:\+91[-\s]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    return match.group() if match else None


# ----------------------------------------
# Name
# ----------------------------------------

def extract_name(text):

    for line in text.split("\n"):

        line = line.strip()

        if line:
            return line

    return "Unknown"


# ----------------------------------------
# Skills
# ----------------------------------------

def extract_skills(text):

    found = []

    text_lower = text.lower()

    for skill in SKILLS_DATABASE:

        if skill.lower() in text_lower:

            found.append(skill)

    return sorted(list(set(found)))


# ----------------------------------------
# Education
# ----------------------------------------

def extract_education(text):

    education = []

    for line in text.split("\n"):

        for keyword in EDUCATION_KEYWORDS:

            if keyword.lower() in line.lower():

                education.append(line.strip())

    return list(set(education))


# ----------------------------------------
# Projects
# ----------------------------------------

def extract_projects(text):

    return extract_section(
        text,
        ["projects", "project"]
    )


# ----------------------------------------
# Experience
# ----------------------------------------

def extract_experience(text):

    return extract_section(
        text,
        [
            "experience",
            "work experience",
            "professional experience",
            "internship",
            "internships"
        ]
    )


# ----------------------------------------
# Certifications
# ----------------------------------------

def extract_certifications(text):

    return extract_section(
        text,
        [
            "certifications",
            "certification",
            "licenses"
        ]
    )


# ----------------------------------------
# Main Parser
# ----------------------------------------

def parse_resume(text):

    return {

        "name": extract_name(text),

        "email": extract_email(text),

        "phone": extract_phone(text),

        "skills": extract_skills(text),

        "education": extract_education(text),

        "projects": extract_projects(text),

        "experience": extract_experience(text),

        "certifications": extract_certifications(text)

    }