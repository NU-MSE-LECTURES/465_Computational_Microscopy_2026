---
layout: default
title: Home
hero:
  title: "Advanced Computational Methods for Electron Microscopy"
  description: "Master the intersection of electron microscopy, data science, and machine learning. Learn to analyze 4D-STEM data, implement computational simulations, and apply AI techniques to materials characterization."
  buttons:
    - text: "View Schedule"
      url: "/schedule"
      class: "btn-primary"
    - text: "Assignments"
      url: "/assignments"
      class: "btn-secondary"
    - text: "GitHub Repository"
      url: "https://github.com/NU-MSE-LECTURES/465_Computational_Microscopy_2026"
      class: "btn-outline"
---

## Course Overview

This advanced graduate course integrates rigorous theoretical foundations in electron microscopy with cutting-edge computational methods and machine learning techniques. Students will develop both analytical thinking through deep understanding of imaging theory, dynamical diffraction, and electron crystallography, and innovative computational approaches through algorithm implementation and automated analysis pipeline development.

<div class="course-highlights">
  <div class="highlight-box">
    <h3>🔬 Advanced EM Analysis</h3>
    <p>Master 4D-STEM, phase STEM, and advanced imaging techniques using modern Python libraries</p>
  </div>
  
  <div class="highlight-box">
    <h3>🤖 Machine Learning Integration</h3>
    <p>Implement deep learning for automated image segmentation, pattern recognition, and defect detection</p>
  </div>
  
  <div class="highlight-box">
    <h3>⚡ Computational Simulations</h3>
    <p>Perform multislice calculations, Bloch wave theory, and focal series reconstruction</p>
  </div>
  
  <div class="highlight-box">
    <h3>📊 Reproducible Workflows</h3>
    <p>Develop version-controlled, documented analysis pipelines for materials characterization</p>
  </div>
</div>

## Quick Start

Get started with the course materials:

1. **Environment Setup**: Follow the [Week 1 instructions](week_01_foundations/) to set up your Python environment
2. **GitHub Repository**: Access all course materials at [GitHub]({{ site.repository }})
3. **First Assignment**: Complete the [environment setup assignment](assignments/assignment_01/)

## Course Information

<div class="course-info">
  <div class="info-section">
    <h3>Instructor</h3>
    <p><strong>{{ site.course.instructor }}</strong><br>
    Office: {{ site.course.office }}<br>
    Email: <a href="mailto:{{ site.course.email }}">{{ site.course.email }}</a></p>
  </div>
  
  <div class="info-section">
    <h3>Meeting Times</h3>
    <p><strong>Lectures:</strong> Tuesday & Thursday, 2:00-3:30 PM<br>
    <strong>Office Hours:</strong> {{ site.course.office_hours }}</p>
  </div>
  
  <div class="info-section">
    <h3>Prerequisites</h3>
    <p>Graduate standing in Materials Science, Physics, Chemistry, or related field; Python programming experience; undergraduate EM coursework</p>
  </div>
</div>

## Learning Objectives

By the end of this course, students will be able to:

- Master advanced EM data analysis techniques for S/TEM, phase STEM, and 4D STEM datasets
- Implement machine learning algorithms for automated electron microscopy analysis
- Perform computational simulations using multislice and Bloch wave methods
- Develop reproducible research workflows with version control and best practices
- Critically evaluate current literature and emerging AI/ML methods in electron microscopy
- Design and execute independent computational projects addressing real materials challenges

## Assessment

- **Weekly Programming Assignments (35%)**: 8 hands-on assignments building practical skills
- **Major Computational Project (40%)**: Independent research project with GitHub repository
- **Project Presentation (15%)**: Conference-style presentation of results
- **Participation and Peer Review (10%)**: Active engagement and collaboration

## Important Dates

- **January 5**: First day of classes
- **January 19**: No classes (Martin Luther King Jr. Day)
- **February 13**: Last day to drop a class
- **March 21**: End of Winter Classes, Final projects due

---

<div class="call-to-action">
  <h3>Ready to Get Started?</h3>
  <p>Begin with <a href="week_01_foundations/" class="btn btn-primary">Week 1: Foundations & Environment Setup</a></p>
</div>

<style>
.hero-section {
  text-align: center;
  padding: 2rem 0;
  background: linear-gradient(135deg, #4e2a84, #6c42a5);
  color: white;
  margin: -2rem -2rem 2rem -2rem;
  border-radius: 0 0 10px 10px;
}

.hero-section h1 {
  color: white;
  margin-bottom: 0.5rem;
}

.lead {
  font-size: 1.2em;
  margin-bottom: 0.5rem;
}

.subtitle {
  font-size: 1em;
  opacity: 0.9;
}

.course-highlights {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.highlight-box {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  border-left: 4px solid #4e2a84;
}

.highlight-box h3 {
  margin-top: 0;
  color: #4e2a84;
}

.course-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin: 2rem 0;
}

.info-section {
  background: #ffffff;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.info-section h3 {
  margin-top: 0;
  color: #4e2a84;
  border-bottom: 2px solid #f0f0f0;
  padding-bottom: 0.5rem;
}

.call-to-action {
  text-align: center;
  background: #f8f9fa;
  padding: 2rem;
  border-radius: 8px;
  margin-top: 2rem;
}

.btn {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  background: #4e2a84;
  color: white;
  text-decoration: none;
  border-radius: 5px;
  font-weight: bold;
  transition: background 0.3s;
}

.btn:hover {
  background: #6c42a5;
  color: white;
  text-decoration: none;
}

.btn-primary {
  background: #4e2a84;
}

@media (max-width: 768px) {
  .course-highlights {
    grid-template-columns: 1fr;
  }
  
  .course-info {
    grid-template-columns: 1fr;
  }
  
  .hero-section {
    margin: -1rem -1rem 2rem -1rem;
    padding: 1.5rem 1rem;
  }
}
</style>