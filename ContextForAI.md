# Project Context for ECIC Space

## Project Context

The ECIC Space is an initiative driven by AI to bridge the gap between students and educational resources effectively. It comprises multiple sub-projects focusing on different aspects of student interaction and learning enhancement:
- **ECIC Space Main Project** focuses on a dynamic web platform that allows interactions between students and educators, enhanced with AI for grading and feedback.
- **ECIC Wiki** serves as a comprehensive knowledge base about the guildline of the student community.
- **Studybase Tutorial** provides tutorials for how to join ECIC.Space student community.

## Projects Overview

### ECIC.Space
- **Repository Name:** samxiaowastaken/ECIC-Space
- **Description:** Next-Generation Teacher-Student Platform integrating AI for accessibility and efficiency in education.
- **Key Features:**
  - Dashboard Interface
  - Assignment Submission
  - AI-driven Feedback
  - Progress Tracking
- **Technology Stack:**
  - Backend: Python, Flask
  - Frontend: Vue.js, Element Plus
  - Front and back end is half-separated, which means HTML will still use the Flask format, but some front-end animations and requests are taken over by Vue.
- **Project Structure:**
  - `app.py`: Flask application entry point
  - `api/`: API endpoint implementations
  - `static/`: Static files like CSS, JavaScript
  - `templates/`: HTML templates for rendering
  - `README.md`: Project documentation

### ECIC Wiki
- **Repository Name:** samxiaowastaken/ECIC_wiki
- **Structure:**
  - `about.md`: Information about the wiki
  - `home.md`: Homepage content
  - `icon.png`: Wiki icon
  - `基础方针/`: Basic guidelines
  - `用户组/`: User groups

### Studybase Tutorial
- **Repository Name:** samxiaowastaken/StudybaseTutorial
- **Structure:**
  - `bottle.py`: Contains the server-side logic
  - `main.py`: Main Python script
  - `mainpage/`: Main page components
  - `pic/`: Images directory
  - `tutorial/`: Tutorial content files
