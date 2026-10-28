"""
Career Role Definitions for Career Recommendation Engine
Defines 12 standard engineering career paths with domain classification,
important technical topics, preferred aptitude competencies, key skills, and descriptions.
"""

CAREER_ROLES = [
    {
        "role": "Software Developer",
        "domain": "IT",
        "important_topics": [
            "Programming",
            "Data Structures & Algorithms",
            "OOP",
            "Operating Systems"
        ],
        "preferred_aptitude": [
            "Logical Reasoning",
            "Quantitative Aptitude"
        ],
        "technical_weight": 0.50,
        "aptitude_weight": 0.25,
        "placement_weight": 0.25,
        "skills": [
            "Python/Java/C++",
            "Data Structures & Algorithms",
            "Git & Version Control",
            "System Design Basics",
            "Clean Code Practices"
        ],
        "description": "Designs, writes, tests, and maintains robust software applications across platforms and services."
    },
    {
        "role": "Frontend Developer",
        "domain": "IT",
        "important_topics": [
            "Programming",
            "OOP",
            "Computer Networks"
        ],
        "preferred_aptitude": [
            "Logical Reasoning",
            "Verbal Ability"
        ],
        "technical_weight": 0.50,
        "aptitude_weight": 0.25,
        "placement_weight": 0.25,
        "skills": [
            "JavaScript/TypeScript",
            "HTML5 & CSS3",
            "React/Vue/Angular",
            "Responsive Web Design",
            "REST API Integration"
        ],
        "description": "Constructs interactive, user-facing web interfaces, ensuring high usability, responsiveness, and performance."
    },
    {
        "role": "Backend Developer",
        "domain": "IT",
        "important_topics": [
            "Programming",
            "OOP",
            "DBMS",
            "SQL"
        ],
        "preferred_aptitude": [
            "Logical Reasoning",
            "Quantitative Aptitude"
        ],
        "technical_weight": 0.50,
        "aptitude_weight": 0.25,
        "placement_weight": 0.25,
        "skills": [
            "Java/Python/Go",
            "SQL & Relational Databases",
            "REST & GraphQL APIs",
            "Microservices Architecture",
            "Authentication & Security"
        ],
        "description": "Builds server-side logic, database schemas, and microservice APIs that power modern web and mobile applications."
    },
    {
        "role": "Full Stack Developer",
        "domain": "IT",
        "important_topics": [
            "Programming",
            "OOP",
            "DBMS",
            "SQL",
            "Computer Networks"
        ],
        "preferred_aptitude": [
            "Logical Reasoning",
            "Quantitative Aptitude"
        ],
        "technical_weight": 0.50,
        "aptitude_weight": 0.25,
        "placement_weight": 0.25,
        "skills": [
            "Frontend (React/TypeScript)",
            "Backend (Node/Python/Java)",
            "SQL & NoSQL Databases",
            "REST APIs",
            "DevOps Basics & Docker"
        ],
        "description": "Develops complete end-to-end applications spanning user interfaces, backend services, and database layers."
    },
    {
        "role": "Data Analyst",
        "domain": "IT",
        "important_topics": [
            "SQL",
            "DBMS",
            "Programming"
        ],
        "preferred_aptitude": [
            "Data Interpretation",
            "Quantitative Aptitude"
        ],
        "technical_weight": 0.50,
        "aptitude_weight": 0.25,
        "placement_weight": 0.25,
        "skills": [
            "Advanced SQL",
            "Python (Pandas, NumPy)",
            "Tableau/Power BI",
            "Statistical Analysis",
            "Excel & Dashboarding"
        ],
        "description": "Extracts, transforms, and visualizes structured business data to uncover actionable operational insights."
    },
    {
        "role": "Data Scientist",
        "domain": "IT",
        "important_topics": [
            "Programming",
            "Data Structures & Algorithms",
            "SQL",
            "DBMS"
        ],
        "preferred_aptitude": [
            "Quantitative Aptitude",
            "Data Interpretation",
            "Logical Reasoning"
        ],
        "technical_weight": 0.50,
        "aptitude_weight": 0.25,
        "placement_weight": 0.25,
        "skills": [
            "Python/R",
            "Machine Learning (Scikit-learn)",
            "Statistical Modeling",
            "Data Preprocessing & EDA",
            "SQL & Data Pipelines"
        ],
        "description": "Applies statistical modeling, predictive algorithms, and experimental analysis to solve complex analytical problems."
    },
    {
        "role": "ML Engineer",
        "domain": "IT",
        "important_topics": [
            "Programming",
            "Data Structures & Algorithms",
            "OOP",
            "DBMS"
        ],
        "preferred_aptitude": [
            "Quantitative Aptitude",
            "Logical Reasoning"
        ],
        "technical_weight": 0.50,
        "aptitude_weight": 0.25,
        "placement_weight": 0.25,
        "skills": [
            "Python & C++",
            "Deep Learning (PyTorch/TensorFlow)",
            "MLOps & Model Deployment",
            "Docker & Kubernetes",
            "Data Engineering Basics"
        ],
        "description": "Productionizes machine learning models into high-throughput scalable software systems and inference pipelines."
    },
    {
        "role": "DevOps Engineer",
        "domain": "IT",
        "important_topics": [
            "Operating Systems",
            "Computer Networks",
            "Programming"
        ],
        "preferred_aptitude": [
            "Logical Reasoning",
            "Quantitative Aptitude"
        ],
        "technical_weight": 0.50,
        "aptitude_weight": 0.25,
        "placement_weight": 0.25,
        "skills": [
            "Linux & Shell Scripting",
            "CI/CD (Jenkins, GitHub Actions)",
            "Docker & Kubernetes",
            "Terraform & Infrastructure as Code",
            "Cloud Platforms (AWS/GCP/Azure)"
        ],
        "description": "Automates continuous integration, continuous deployment, and resilient infrastructure scaling for software products."
    },
    {
        "role": "QA Engineer",
        "domain": "IT",
        "important_topics": [
            "Programming",
            "OOP",
            "SQL",
            "Operating Systems"
        ],
        "preferred_aptitude": [
            "Logical Reasoning",
            "Verbal Ability"
        ],
        "technical_weight": 0.50,
        "aptitude_weight": 0.25,
        "placement_weight": 0.25,
        "skills": [
            "Automated Testing (Selenium/Playwright)",
            "Test Case Design & Bug Reporting",
            "API Testing (Postman/RestAssured)",
            "Python/Java Scripting",
            "CI/CD Integration"
        ],
        "description": "Ensures software quality, reliability, and security through systematic automated testing, manual testing, and regression analysis."
    },
    {
        "role": "Cloud Engineer",
        "domain": "IT",
        "important_topics": [
            "Computer Networks",
            "Operating Systems",
            "DBMS",
            "SQL"
        ],
        "preferred_aptitude": [
            "Logical Reasoning",
            "Quantitative Aptitude"
        ],
        "technical_weight": 0.50,
        "aptitude_weight": 0.25,
        "placement_weight": 0.25,
        "skills": [
            "AWS/Azure/GCP Services",
            "Networking (VPC, DNS, Subnets)",
            "Linux Administration",
            "Cloud Security & IAM",
            "Serverless & Microservices"
        ],
        "description": "Architects, provisions, and maintains highly available cloud computing infrastructure and distributed services."
    },
    {
        "role": "Cybersecurity Analyst",
        "domain": "IT",
        "important_topics": [
            "Computer Networks",
            "Operating Systems",
            "Programming"
        ],
        "preferred_aptitude": [
            "Logical Reasoning",
            "Verbal Ability"
        ],
        "technical_weight": 0.50,
        "aptitude_weight": 0.25,
        "placement_weight": 0.25,
        "skills": [
            "Network Security & Firewalls",
            "Vulnerability Assessment & Penetration Testing",
            "Cryptography Basics",
            "Incident Response & SIEM",
            "Linux & Scripting"
        ],
        "description": "Monitors systems for security threats, mitigates network vulnerabilities, and enforces cybersecurity safeguards."
    },
    {
        "role": "Embedded Engineer",
        "domain": "Core",
        "important_topics": [
            "Embedded Systems",
            "Microcontrollers",
            "Digital Electronics",
            "Microprocessors",
            "Electronic Devices"
        ],
        "preferred_aptitude": [
            "Logical Reasoning",
            "Quantitative Aptitude"
        ],
        "technical_weight": 0.50,
        "aptitude_weight": 0.25,
        "placement_weight": 0.25,
        "skills": [
            "Embedded C & C++",
            "ARM Cortex & Microcontroller Interfacing",
            "RTOS (FreeRTOS)",
            "Communication Protocols (SPI, I2C, UART, CAN)",
            "Circuit Debugging & Oscilloscopes"
        ],
        "description": "Develops firmware and hardware interfaces for microcontroller-based embedded devices, IoT hardware, and real-time systems."
    }
]
