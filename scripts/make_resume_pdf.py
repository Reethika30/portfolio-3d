"""Generate Sree Reethika's resume PDF for the portfolio public/ folder."""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, HRFlowable
)

OUT = "public/Sree_Reethika_Kasanagottu_Resume.pdf"

styles = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=styles["Heading1"], alignment=TA_CENTER,
                    fontSize=18, spaceAfter=4, textColor=HexColor("#111111"))
SUB = ParagraphStyle("Sub", parent=styles["Normal"], alignment=TA_CENTER,
                     fontSize=9.5, spaceAfter=10, textColor=HexColor("#444444"))
H2 = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=12,
                    spaceBefore=10, spaceAfter=4, textColor=HexColor("#1a1a1a"))
H3 = ParagraphStyle("H3", parent=styles["Heading3"], fontSize=10.5,
                    spaceBefore=6, spaceAfter=1, textColor=HexColor("#222222"))
META = ParagraphStyle("META", parent=styles["Italic"], fontSize=9,
                      textColor=HexColor("#666666"), spaceAfter=3)
P = ParagraphStyle("P", parent=styles["Normal"], fontSize=9.5, leading=12.5,
                   spaceAfter=2)
B = ParagraphStyle("B", parent=P, leftIndent=10, bulletIndent=0)


def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(t, B), leftIndent=12, bulletColor=HexColor("#444"))
         for t in items],
        bulletType="bullet", bulletFontSize=7, leftIndent=12)


def hr():
    return HRFlowable(width="100%", thickness=0.6,
                      color=HexColor("#999999"), spaceBefore=2, spaceAfter=4)


story = []
story.append(Paragraph("SREE REETHIKA KASANAGOTTU", H1))
story.append(Paragraph(
    "+1 (571) 523-6224 &nbsp;|&nbsp; "
    "<a href='mailto:reethikakasanagottu@gmail.com'>reethikakasanagottu@gmail.com</a> &nbsp;|&nbsp; "
    "<a href='https://www.linkedin.com/in/sree-reethika/'>linkedin.com/in/sree-reethika</a> &nbsp;|&nbsp; "
    "<a href='https://github.com/Reethika30'>github.com/Reethika30</a>", SUB))

story.append(Paragraph("PROFESSIONAL SUMMARY", H2)); story.append(hr())
story.append(Paragraph(
    "Detail-oriented and organized Data Engineer with 3+ years of experience building "
    "scalable ETL/ELT pipelines using Python, SQL, and cloud platforms (Azure, AWS, GCP). "
    "Proficient in data warehousing and data design in BigQuery, Snowflake, and Redshift, "
    "with expertise in performance optimization, partitioning, and clustering. Self-motivated "
    "team player with strong communication skills and a commitment to delivering results in "
    "Agile environments.", P))

story.append(Paragraph("CORE SKILLS", H2)); story.append(hr())
story.append(bullets([
    "<b>Data Engineering:</b> ETL/ELT Pipelines, Data Ingestion, Data Modeling, Performance Optimization, Partitioning &amp; Clustering",
    "<b>Languages &amp; Tools:</b> Python, SQL, Apache Airflow, DBT, Node.JS, PySpark",
    "<b>Cloud &amp; Data:</b> AWS, Azure, GCP, BigQuery, Snowflake, Redshift, Databricks",
    "<b>Data Quality:</b> Data Validation, Data Quality Management, Data Governance, Metadata Management",
    "<b>Collaboration:</b> Stakeholder Communication, Technical Documentation, Agile / Scrum, Cross-Functional Teamwork",
]))

story.append(Paragraph("TECHNICAL SKILLS", H2)); story.append(hr())
story.append(bullets([
    "<b>Programming &amp; Scripting:</b> Python (Pandas, NumPy, PySpark), R, SQL, Node.JS",
    "<b>Databases &amp; Data Warehousing:</b> BigQuery (Data Design &amp; Modeling), Snowflake, Amazon Redshift, PostgreSQL, Oracle SQL Developer, RDBMS Design",
    "<b>Data Engineering &amp; Pipelines:</b> ETL/ELT Pipeline Design, Apache Airflow, DBT, Data Ingestion Automation, Data Quality Management, Data Governance, Performance Tuning, Partitioning, Clustering",
    "<b>Cloud Platforms &amp; Tools:</b> Microsoft Azure (Functions, Data Factory), AWS (S3, Lambda, Glue), GCP (BigQuery, Dataflow), Databricks",
    "<b>AI/ML &amp; LLMs:</b> LLM Integration, AI Agents, Generative AI (OCI Certified)",
    "<b>Collaboration &amp; Delivery:</b> Stakeholder Requirements Gathering, Cross-Functional Collaboration, Technical Documentation, API Integration, Agile / Scrum",
]))

story.append(Paragraph("PROFESSIONAL EXPERIENCE", H2)); story.append(hr())
story.append(Paragraph("<b>Data Engineer | Hotwire Communications</b>", H3))
story.append(Paragraph("Fort Lauderdale, Florida &nbsp;|&nbsp; February 2025 &ndash; December 2025", META))
story.append(bullets([
    "Designed and developed scalable ETL/ELT data pipelines using Python, SQL, Airflow, and Snowflake, automating data ingestion and transformation from multiple heterogeneous data sources and reducing manual reporting workload by 40%.",
    "Built analytics-ready datasets using Bronze/Silver/Gold architecture, enabling industrialized data collection, storage, modeling, and analysis of massive operational datasets across multiple systems.",
    "Automated hourly and daily data ingestion workflows using Azure Functions, converting compressed files to structured CSVs and ensuring data compatibility and consistency across systems.",
    "Developed simple to moderately complex SQL queries for data extraction, transformation, and validation, ensuring data accuracy, completeness, and consistency across all dashboards and reports prior to stakeholder release.",
    "Built data service endpoints using Node.JS to support API-driven data ingestion, working with Staff Data Engineers to design and develop data infrastructure enabling connectivity between internal tools and cloud-based pipeline systems.",
    "Implemented performance optimization best practices including partitioning, clustering, and SQL query tuning to optimize data queries and reduce costs across cloud environments.",
    "Integrated LLM-based solutions and AI agents to automate data cataloging, metadata tagging, and natural language querying of datasets, improving data discoverability for non-technical stakeholders.",
    "Collaborated with data scientists, analysts, and product owners to design data solutions, exercising good judgment and active listening to translate business requirements, define KPIs, and deliver actionable dashboards.",
    "Created comprehensive documentation for data pipelines, workflows, and configurations, contributing to knowledge sharing and onboarding across the analytics team.",
]))

story.append(Paragraph("<b>Data Analyst | BEPEC Solutions PVT. LTD</b>", H3))
story.append(Paragraph("Bangalore, India &nbsp;|&nbsp; May 2021 &ndash; December 2023", META))
story.append(bullets([
    "Architected and implemented end-to-end cloud data pipelines (AWS, GCP) supporting analytics and machine learning initiatives, processing billions of records using SQL, Python, and cloud-native tools.",
    "Designed and maintained data models and schemas in BigQuery, supporting analytical and financial workloads with optimized table structures, partitioning, and clustering strategies.",
    "Built efficient and scalable data pipelines integrating data from heterogeneous channels, working with APIs, connectors, and cloud services to ensure seamless data flow and compatibility.",
    "Conducted data quality checks and validation processes using SQL and Python, developing simple to complex queries to ensure data accuracy, completeness, and consistency across all data products.",
    "Optimized data processing performance by 25% through Airflow task parallelization and SQL query tuning in BigQuery, reducing pipeline latency and compute costs.",
    "Contributed to data governance initiatives, establishing best practices for data quality, access controls, and metadata management in cloud environments.",
    "Actively participated in Agile team ceremonies including sprint planning, standups, and retrospectives, managing priorities in a fast-paced environment.",
    "Compiled comprehensive documentation of data engineering processes and systems, contributing to team knowledge sharing and collaborative projects.",
]))

story.append(Paragraph("EDUCATION", H2)); story.append(hr())
story.append(Paragraph("<b>Master of Science in Data Science</b> &mdash; Hofstra University, Hempstead, New York", P))
story.append(Paragraph("January 2024 &ndash; December 2025 &nbsp;|&nbsp; GPA: 3.8/4.0", META))
story.append(Paragraph("<b>Bachelor of Technology in Computer Science</b> &mdash; Guru Nanak Institutions, Hyderabad, India", P))
story.append(Paragraph("August 2019 &ndash; July 2023 &nbsp;|&nbsp; GPA: 8.9/10.0", META))

story.append(Paragraph("PROJECTS", H2)); story.append(hr())
story.append(Paragraph("<b>Retail Data Warehouse &mdash; Star-Schema Analytics on Snowflake</b>", H3))
story.append(Paragraph("Python, SQL, Snowflake, dbt, Airflow", META))
story.append(bullets([
    "Built a star-schema retail data warehouse with fact/dimension tables, ELT pipelines, and BI-ready aggregates.",
    "Implemented partitioning, clustering, and incremental dbt models for cost-efficient analytics.",
]))
story.append(Paragraph("<b>Seq2Seq with Bahdanau Attention &mdash; Neural Documentation Generator</b>", H3))
story.append(Paragraph("Python, PyTorch, Gradio, Hugging Face Spaces", META))
story.append(bullets([
    "Trained an encoder-decoder LSTM with Bahdanau attention to generate natural-language documentation from code tokens.",
    "Deployed an interactive Gradio demo on Hugging Face Spaces with model weights published as a GitHub Release.",
]))
story.append(Paragraph("<b>YOLOv8 + ByteTrack &mdash; Real-Time Detection &amp; Multi-Object Tracking</b>", H3))
story.append(Paragraph("Python, Ultralytics YOLOv8, ByteTrack, Streamlit, Docker, Hugging Face", META))
story.append(bullets([
    "Built a Streamlit app for image/video object detection and persistent ID tracking using YOLOv8 + ByteTrack.",
    "Containerized with Docker and deployed to Hugging Face Spaces (Docker SDK).",
]))
story.append(Paragraph("<b>Multi-Lingual Sentiment &amp; Emotion Dashboard</b>", H3))
story.append(Paragraph("Python, XLM-RoBERTa, DistilRoBERTa, Streamlit, Plotly, Docker", META))
story.append(bullets([
    "Built a real-time NLP dashboard combining XLM-RoBERTa sentiment with DistilRoBERTa fine-grained emotion classification across multiple languages.",
    "Interactive Plotly visualisations and CSV batch scoring; deployed to Hugging Face Spaces.",
]))

story.append(Paragraph("CERTIFICATIONS", H2)); story.append(hr())
story.append(bullets([
    "Oracle Cloud Infrastructure 2025 Certified Data Science Professional",
    "Oracle Cloud Infrastructure 2025 Certified Generative AI Professional",
    "SnowPro Advanced: Data Engineer Certification",
    "Microsoft Certified: Power BI Data Analyst Associate",
]))

doc = SimpleDocTemplate(OUT, pagesize=LETTER,
                        leftMargin=0.7*inch, rightMargin=0.7*inch,
                        topMargin=0.55*inch, bottomMargin=0.55*inch,
                        title="Sree Reethika Kasanagottu - Resume",
                        author="Sree Reethika Kasanagottu")
doc.build(story)
print("Wrote", OUT)
