import "./styles/Career.css";

const Career = () => {
  return (
    <div className="career-section section-container">
      <div className="career-container">
        <h2>
          My career <span>&</span>
          <br /> experience
        </h2>
        <div className="career-info">
          <div className="career-timeline">
            <div className="career-dot"></div>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>Data Engineer</h4>
                <h5>Hotwire Communications · Fort Lauderdale, FL</h5>
              </div>
              <h3>2025</h3>
            </div>
            <p>
              Designed scalable ETL/ELT pipelines on Python, SQL, Airflow and
              Snowflake, automating ingestion from heterogeneous sources and
              cutting manual reporting by 40%. Built Bronze/Silver/Gold lakehouse
              datasets, Azure Functions ingestion jobs, Node.js data APIs, and
              integrated LLM agents for metadata tagging and natural-language
              querying of warehouse tables.
            </p>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>Data Analyst</h4>
                <h5>BEPEC Solutions Pvt. Ltd · Bangalore, India</h5>
              </div>
              <h3>2021–23</h3>
            </div>
            <p>
              Architected end-to-end cloud pipelines on AWS and GCP processing
              billions of records with SQL, Python and BigQuery. Modeled
              partitioned/clustered warehouse schemas, ran data-quality and
              governance programs, and improved pipeline performance by 25%
              through Airflow parallelization and SQL tuning.
            </p>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>M.S. Data Science</h4>
                <h5>Hofstra University · New York</h5>
              </div>
              <h3>2024–25</h3>
            </div>
            <p>
              GPA 3.8/4.0. Specialised in machine learning, deep learning and
              big-data systems — capstone projects in NLP attention models,
              computer vision and large-scale data engineering on Snowflake.
            </p>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>B.Tech Computer Science</h4>
                <h5>Guru Nanak Institutions · Hyderabad</h5>
              </div>
              <h3>2019–23</h3>
            </div>
            <p>
              GPA 8.9/10. Foundations in algorithms, databases, operating
              systems and distributed computing — with hands-on coursework in
              Python, SQL and cloud computing.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Career;
