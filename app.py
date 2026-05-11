"""
Web Portfolio Streamlit
Profile: Freelance Academic Researcher & Data Specialist

Run the application with:
    streamlit run app.py
"""

from __future__ import annotations

from io import StringIO
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st


# ---------------------------------------------------------------------------
# Base Streamlit page configuration
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Professional Portfolio | Danu Yuliannesta",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------------------------
# Project constants and asset locations
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
PORTFOLIO_DIR = BASE_DIR / "assets" / "portfolio"

PROFILE = {
    "name": "Danu Yuliannesta",
    "age": "24",
    "education": "Bachelor of Information Systems, Dian Nuswantoro University",
    "role": "Freelance Academic Researcher & Data Specialist",
    "summary": (
        "I help students, researchers, and professionals turn research ideas "
        "into structured academic writing, analysis-ready data, "
        "and defensible insights."
    ),
}


SERVICES = [
    {
        "title": "Academic Research",
        "icon": "[Research]",
        "description": (
            "Support for thesis writing, journal articles, literature reviews, "
            "theoretical frameworks, research methodology, and results interpretation."
        ),
    },
    {
        "title": "Statistical Analysis",
        "icon": "[Data]",
        "description": (
            "Quantitative data processing using SPSS, SmartPLS, Excel, and Python. "
            "Includes validity testing, reliability testing, regression, SEM-PLS, and data visualization."
        ),
    },
    {
        "title": "Python Automation",
        "icon": "[Python]",
        "description": (
            "Automated workflows for data cleaning, dataset analysis, "
            "simple search engine development, controlled scraping, and Pandas-based reporting."
        ),
    },
]


RESEARCH_PROJECTS = [
    {
        "name": "SEM-PLS Analysis for Consumer Behavior Research",
        "type": "Quantitative Research",
        "summary": (
            "Analyzed relationships between latent variables using SmartPLS "
            "and prepared academic interpretations ready to be included in research reports."
        ),
        "tools": "SmartPLS, SPSS, Academic Writing",
        "image": "research_sem_pls.png",
    },
    {
        "name": "Journal Article Assistance",
        "type": "Academic Writing",
        "summary": (
            "Developed article structure, strengthened theoretical arguments, refined methodology, "
            "and aligned the manuscript with the target journal format."
        ),
        "tools": "Reference Review, Editing, Journal Formatting",
        "image": "research_journal_article.png",
    },
    {
        "name": "Descriptive Statistics Dashboard for Research",
        "type": "Data Analysis",
        "summary": (
            "Built statistical summaries, variable distribution views, and visualizations "
            "to support research result interpretation."
        ),
        "tools": "SPSS, Excel, Data Visualization",
        "image": "research_dashboard.png",
    },
]


PROGRAMMING_PROJECTS = [
    {
        "name": "CSV Analyzer with Pandas",
        "type": "Python App",
        "summary": (
            "An application for reading CSV files, displaying descriptive statistics, "
            "missing values, and interactive data previews."
        ),
        "tools": "Python, Pandas, Streamlit",
        "image": "programming_csv_analyzer.png",
    },
    {
        "name": "Simple Document Search Engine",
        "type": "Information Retrieval",
        "summary": (
            "A keyword-scoring search prototype designed to support "
            "document exploration and research reference discovery."
        ),
        "tools": "Python, NumPy, Search Logic",
        "image": "programming_search_engine.png",
    },
    {
        "name": "Dataset Cleaning Automation",
        "type": "Data Pipeline",
        "summary": (
            "A Python script for cleaning columns, handling missing values, "
            "and exporting analysis-ready data."
        ),
        "tools": "Python, Pandas, Automation",
        "image": "programming_data_cleaning.png",
    },
]


# ---------------------------------------------------------------------------
# Custom styling
# ---------------------------------------------------------------------------
def inject_custom_css() -> None:
    """Inject lightweight CSS for a polished professional layout."""

    st.markdown(
        """
        <style>
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1180px;
        }

        .hero {
            padding: 2.5rem;
            border-radius: 16px;
            background:
                radial-gradient(circle at 88% 18%, rgba(255, 255, 255, 0.16), transparent 0 18%),
                radial-gradient(circle at 100% 100%, rgba(77, 124, 171, 0.18), transparent 0 28%),
                linear-gradient(135deg, #102840 0%, #173b5f 58%, #224c75 100%);
            color: #ffffff;
            margin-bottom: 1.75rem;
            overflow: hidden;
        }

        .hero h1 {
            font-size: 2.7rem;
            line-height: 1.08;
            margin-bottom: 0.6rem;
        }

        .hero p {
            max-width: 700px;
            font-size: 1.05rem;
            line-height: 1.75;
            color: #edf4ff;
        }

        .metric-strip {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.85rem;
            margin: 1.25rem 0 0;
        }

        .metric-item {
            padding: 0.95rem 1rem;
            border: 1px solid #d9e2ef;
            border-radius: 10px;
            background: #ffffff;
            color: #172033;
        }

        .metric-item strong {
            display: block;
            font-size: 1rem;
            color: #0f2742;
        }

        .section-title {
            margin-top: 0.75rem;
            margin-bottom: 0.25rem;
            color: #0f2742;
        }

        .soft-card {
            height: 100%;
            padding: 1.1rem;
            border: 1px solid #d9e2ef;
            border-radius: 10px;
            background: #ffffff;
            box-shadow: 0 1px 4px rgba(15, 39, 66, 0.05);
        }

        .soft-card h3 {
            margin-top: 0;
            color: #0f2742;
            font-size: 1.12rem;
        }

        .bio-card {
            padding: 1.15rem;
            border: 1px solid #d9e2ef;
            border-radius: 12px;
            background: #ffffff;
            box-shadow: 0 1px 4px rgba(15, 39, 66, 0.05);
        }

        .bio-card h3 {
            margin: 0 0 0.9rem 0;
            color: #0f2742;
        }

        .bio-row {
            padding: 0.65rem 0;
            border-bottom: 1px solid #e8eef6;
        }

        .bio-row:last-child {
            border-bottom: none;
        }

        .bio-label {
            display: block;
            font-size: 0.82rem;
            font-weight: 600;
            color: #506176;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }

        .bio-value {
            display: block;
            margin-top: 0.18rem;
            color: #172033;
            font-size: 1rem;
        }

        .tag {
            display: inline-block;
            margin-bottom: 0.6rem;
            padding: 0.18rem 0.55rem;
            border-radius: 999px;
            background: #e8eef6;
            color: #1f3f63;
            font-size: 0.78rem;
            font-weight: 600;
        }

        .note-box {
            padding: 1rem;
            border-left: 4px solid #1f77b4;
            border-radius: 8px;
            background: #f4f8fc;
            color: #172033;
        }

        .project-image-frame {
            border: 1px solid #d9e2ef;
            border-radius: 12px;
            overflow: hidden;
            background: #f7f9fc;
            margin-bottom: 0.9rem;
        }

        .project-empty {
            padding: 1rem;
            border: 1px dashed #b5c3d4;
            border-radius: 12px;
            background: #f7f9fc;
            color: #506176;
            margin-bottom: 0.9rem;
        }

        @media (max-width: 800px) {
            .hero {
                background: #102840;
                padding: 1.5rem;
            }

            .hero h1 {
                font-size: 2rem;
            }

            .metric-strip {
                grid-template-columns: 1fr;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Reusable view components
# ---------------------------------------------------------------------------
def render_sidebar() -> str:
    """Render the sidebar navigation and return the selected page."""

    with st.sidebar:
        st.title("Portfolio")
        st.caption(PROFILE["role"])

        page = st.radio(
            "Navigation",
            ["Home", "Portfolio", "Services", "Tool Demo"],
            label_visibility="collapsed",
        )

        st.divider()
        st.subheader("Quick Profile")
        st.write(f"Name: {PROFILE['name']}")
        st.write(f"Age: {PROFILE['age']}")
        st.write("Education:")
        st.caption(PROFILE["education"])

        st.divider()
        st.subheader("Core Skills")
        st.write("- Academic Writing")
        st.write("- SPSS & SmartPLS")
        st.write("- Python, Pandas, NumPy")
        st.write("- Search Engine Prototype")

    return page


def render_card(title: str, tag: str, description: str, icon: str | None = None) -> None:
    """Render a compact card for a service or project."""

    icon_markup = f"{icon} " if icon else ""
    st.markdown(
        f"""
        <div class="soft-card">
            <span class="tag">{tag}</span>
            <h3>{icon_markup}{title}</h3>
            <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_biodata() -> None:
    """Render the portfolio owner's professional biodata."""

    st.markdown(
        f"""
        <div class="bio-card">
            <h3>Professional Biodata</h3>
            <div class="bio-row">
                <span class="bio-label">Name</span>
                <span class="bio-value">{PROFILE["name"]}</span>
            </div>
            <div class="bio-row">
                <span class="bio-label">Age</span>
                <span class="bio-value">{PROFILE["age"]}</span>
            </div>
            <div class="bio-row">
                <span class="bio-label">Educational Background</span>
                <span class="bio-value">{PROFILE["education"]}</span>
            </div>
            <div class="bio-row">
                <span class="bio-label">Specialization</span>
                <span class="bio-value">Academic research, statistical analysis, and Python automation</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def get_project_image_path(filename: str) -> Path:
    """Return the absolute path for a portfolio image."""

    return PORTFOLIO_DIR / filename


def render_project(project: dict[str, str]) -> None:
    """Render a full project block with an image when available."""

    image_path = get_project_image_path(project["image"])

    if image_path.exists():
        st.image(str(image_path), use_container_width=True)
    else:
        st.markdown(
            f"""
            <div class="project-empty">
                Project image is not available yet.<br>
                Save the project screenshot as <strong>{project["image"]}</strong>
                inside the <strong>assets/portfolio</strong> folder.
            </div>
            """,
            unsafe_allow_html=True,
        )

    render_card(
        title=project["name"],
        tag=project["type"],
        description=f'{project["summary"]}<br><br><strong>Tools:</strong> {project["tools"]}',
    )


# ---------------------------------------------------------------------------
# Home page
# ---------------------------------------------------------------------------
def show_home() -> None:
    """Render the opening page with the hero section and profile summary."""

    st.markdown(
        f"""
        <div class="hero">
            <h1>{PROFILE["name"]}</h1>
            <p>
                {PROFILE["role"]}. {PROFILE["summary"]}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="metric-strip">
            <div class="metric-item">
                <strong>Academic Research</strong>
                Thesis support, journals, methodology, interpretation
            </div>
            <div class="metric-item">
                <strong>Data Specialist</strong>
                SPSS, SmartPLS, Pandas, NumPy
            </div>
            <div class="metric-item">
                <strong>Python Automation</strong>
                Data cleaning, reporting, and search tools
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    left_col, right_col = st.columns([1.15, 0.85], gap="large")

    with left_col:
        st.markdown('<h2 class="section-title">Profile Overview</h2>', unsafe_allow_html=True)
        st.write(
            """
            I focus on work that combines academic rigor, data analysis capability,
            and technical automation. My main areas include academic writing,
            research data processing, statistical interpretation, and practical Python tools
            that help accelerate analytical workflows.
            """
        )
        st.markdown(
            """
            <div class="note-box">
                I deliver structured analysis, clear documentation,
                and outputs that are ready to support both academic and professional needs.
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right_col:
        render_biodata()


# ---------------------------------------------------------------------------
# Services page
# ---------------------------------------------------------------------------
def show_services() -> None:
    """Render the three main service categories."""

    st.markdown('<h1 class="section-title">Services</h1>', unsafe_allow_html=True)
    st.write("These services are designed to support research work from concept development to final reporting.")

    columns = st.columns(3, gap="medium")
    for column, service in zip(columns, SERVICES):
        with column:
            render_card(
                title=service["title"],
                tag="Service",
                description=service["description"],
                icon=service["icon"],
            )

    st.write("")
    st.info(
        "Each service can be tailored to the project scope, data type, institutional or journal format, and timeline."
    )


# ---------------------------------------------------------------------------
# Portfolio page
# ---------------------------------------------------------------------------
def show_portfolio() -> None:
    """Render research and programming projects in a two-column layout."""

    st.markdown('<h1 class="section-title">Portfolio</h1>', unsafe_allow_html=True)
    st.write(
        "The following are some examples of projects that I have completed. "
    )

    research_col, programming_col = st.columns(2, gap="large")

    with research_col:
        st.subheader("Research Projects")
        for project in RESEARCH_PROJECTS:
            render_project(project)
            st.write("")

    with programming_col:
        st.subheader("Programming Projects")
        for project in PROGRAMMING_PROJECTS:
            render_project(project)
            st.write("")

    st.caption(
        "Those are some of the results of my project "
    )


# ---------------------------------------------------------------------------
# Tool Demo helpers
# ---------------------------------------------------------------------------
def load_csv(uploaded_file) -> pd.DataFrame | None:
    """Read an uploaded CSV file and return a DataFrame."""

    if uploaded_file is None:
        return None

    try:
        bytes_data = uploaded_file.getvalue()
        text_data = bytes_data.decode("utf-8")
        return pd.read_csv(StringIO(text_data))
    except UnicodeDecodeError:
        st.error("The file could not be read as UTF-8. Please save the CSV again using UTF-8 encoding.")
    except pd.errors.ParserError:
        st.error("The CSV format is invalid. Please check the delimiter, header, or inconsistent rows.")
    except Exception as exc:
        st.error(f"An error occurred while reading the file: {exc}")

    return None


def show_dataframe_summary(df: pd.DataFrame) -> None:
    """Display a preview, descriptive statistics, and missing-value information."""

    st.subheader("Preview Data")
    st.dataframe(df.head(20), use_container_width=True)

    numeric_df = df.select_dtypes(include=[np.number])

    overview_col, missing_col = st.columns(2, gap="large")
    with overview_col:
        st.metric("Rows", f"{df.shape[0]:,}")
        st.metric("Columns", f"{df.shape[1]:,}")

    with missing_col:
        total_missing = int(df.isna().sum().sum())
        st.metric("Total Missing Values", f"{total_missing:,}")
        st.metric("Numeric Columns", f"{numeric_df.shape[1]:,}")

    if numeric_df.empty:
        st.warning("This dataset does not contain numeric columns, so numeric descriptive statistics are unavailable.")
        return

    st.subheader("Descriptive Statistics")
    st.dataframe(numeric_df.describe().T, use_container_width=True)

    st.subheader("Missing Values by Column")
    missing_values = df.isna().sum().sort_values(ascending=False)
    st.dataframe(
        missing_values.rename("missing_values").to_frame(),
        use_container_width=True,
    )


def show_manual_number_demo() -> None:
    """Alternative demo for visitors who want to test manual numeric input."""

    st.subheader("Manual Number Input")
    raw_numbers = st.text_area(
        "Enter numbers separated by commas",
        value="78, 82, 90, 75, 88, 91, 69",
        help="Example: 10, 15, 20, 25",
    )

    try:
        numbers = [float(item.strip()) for item in raw_numbers.split(",") if item.strip()]
    except ValueError:
        st.error("Please make sure every input is numeric and separated by commas.")
        return

    if not numbers:
        st.warning("Please enter at least one number for analysis.")
        return

    series = pd.Series(numbers, name="value")
    summary = pd.DataFrame(
        {
            "Statistic": ["Count", "Mean", "Median", "Minimum", "Maximum", "Std Dev"],
            "Value": [
                series.count(),
                series.mean(),
                series.median(),
                series.min(),
                series.max(),
                series.std(ddof=1) if len(series) > 1 else 0,
            ],
        }
    )

    st.dataframe(summary, use_container_width=True, hide_index=True)
    st.line_chart(series)


# ---------------------------------------------------------------------------
# Tool Demo page
# ---------------------------------------------------------------------------
def show_tool_demo() -> None:
    """Render an interactive demo that showcases Pandas-based data analysis."""

    st.markdown('<h1 class="section-title">Tool Demo</h1>', unsafe_allow_html=True)
    st.write(
        "Upload a CSV file to preview the data, inspect descriptive statistics, and review missing values."
    )

    demo_mode = st.radio(
        "Choose Demo Mode",
        ["Upload CSV", "Number Input"],
        index=0,
        horizontal=True,
    )

    if demo_mode == "Upload CSV":
        uploaded_file = st.file_uploader(
            "Upload file CSV",
            type=["csv"],
            help="Use a CSV file with column headers in the first row.",
        )

        df = load_csv(uploaded_file)
        if df is not None:
            show_dataframe_summary(df)
        else:
            st.markdown(
                """
                <div class="note-box">
                    This demo uses Pandas to read datasets, select numeric columns,
                    calculate descriptive statistics, and inspect missing values.
                </div>
                """,
                unsafe_allow_html=True,
            )

    else:
        show_manual_number_demo()


# ---------------------------------------------------------------------------
# Application entry point
# ---------------------------------------------------------------------------
def main() -> None:
    """Control the main application flow based on the sidebar selection."""

    inject_custom_css()
    selected_page = render_sidebar()

    if selected_page == "Home":
        show_home()
    elif selected_page == "Portfolio":
        show_portfolio()
    elif selected_page == "Services":
        show_services()
    elif selected_page == "Tool Demo":
        show_tool_demo()


if __name__ == "__main__":
    main()
