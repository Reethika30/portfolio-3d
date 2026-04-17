import "./styles/About.css";

const About = () => {
  return (
    <div className="about-section" id="about">
      <div className="about-me">
        <h3 className="title">About Me</h3>
        <p className="para">
          I'm a <b>Full Stack Data Professional</b> with 3+ years of
          experience building scalable ETL/ELT pipelines on Python, SQL,
          Airflow and cloud platforms (Azure, AWS, GCP). I love designing
          analytics-ready data on Snowflake, BigQuery and Redshift —
          partitioning, clustering and tuning queries until they fly. Lately
          I've been shipping LLM-powered data agents and end-to-end AI
          products that take models from notebook to production.
        </p>
      </div>
    </div>
  );
};

export default About;
