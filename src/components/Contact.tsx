import { MdArrowOutward, MdCopyright } from "react-icons/md";
import "./styles/Contact.css";

const Contact = () => {
  return (
    <div className="contact-section section-container" id="contact">
      <div className="contact-container">
        <h3>Contact</h3>
        <div className="contact-flex">
          <div className="contact-box">
            <h4>Connect</h4>
            <p>
              <a
                href="mailto:reethikakasanagottu@gmail.com"
                data-cursor="disable"
              >
                reethikakasanagottu@gmail.com
              </a>
            </p>
            <p>
              <a
                href="https://www.linkedin.com/in/sree-reethika/"
                target="_blank"
                rel="noreferrer"
                data-cursor="disable"
              >
                LinkedIn — sree-reethika
              </a>
            </p>
            <h4>Education</h4>
            <p>
              M.S. Data Science, Hofstra University, NY — 2024–2025
            </p>
            <p>
              B.Tech Computer Science, Guru Nanak Institutions, Hyderabad —
              2019–2023
            </p>
          </div>
          <div className="contact-box">
            <h4>Social</h4>
            <a
              href="https://github.com/Reethika30"
              target="_blank"
              rel="noreferrer"
              data-cursor="disable"
              className="contact-social"
            >
              GitHub <MdArrowOutward />
            </a>
            <a
              href="https://www.linkedin.com/in/sree-reethika/"
              target="_blank"
              rel="noreferrer"
              data-cursor="disable"
              className="contact-social"
            >
              LinkedIn <MdArrowOutward />
            </a>
            <a
              href="/Sree_Reethika_Kasanagottu_Resume.pdf"
              target="_blank"
              rel="noreferrer"
              data-cursor="disable"
              className="contact-social"
            >
              Resume <MdArrowOutward />
            </a>
            <a
              href="mailto:reethikakasanagottu@gmail.com"
              data-cursor="disable"
              className="contact-social"
            >
              Email <MdArrowOutward />
            </a>
          </div>
          <div className="contact-box">
            <h2>
              Designed and Developed <br /> by <span>Sree Reethika</span>
            </h2>
            <h5>
              <MdCopyright /> 2026
            </h5>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Contact;
