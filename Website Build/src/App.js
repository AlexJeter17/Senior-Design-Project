// import logo from './AJ_Logo.svg';
// import './App.css';
// import Header from './components/header.tsx';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
        
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;


import React from 'react';
import './App.css';
import Header from './components/header.tsx'; // Adjust path if needed
import logo from './AJ_Logo.svg';
// import projectImage1 from './senior_project/src/Images/4-misconceptions-ai.jpg';
// import projectImage2 from './senior_project/src/Images/React-js.png';
// import projectImage3 from './senior_project/src/Images/Mertics.png'


function App() {
  return (
    <div className="App">
      <Header />

      {/* Main Content */}
      <main>
        <img src={logo} className="App-logo" alt="logo" />
        <section className="intro">
          <h1>Welcome to the Social Media Analytics Dashboard</h1>
          <p>By Alex Jeter</p>
        </section>

        {/* Three Sections for Work */}
        <section className="Mission">
          <h2>Mission Statement</h2>
          <p>Businesses are becoming more and more dependent on digital platforms to engage with their customers, advertise their products, and negotiate the cutthroat environment of the contemporary market economy
             in a time typified by the widespread use of social media. Even the most experienced marketers, however, may become overwhelmed by the sheer amount of data collected across several social media channels, 
             making it more difficult for them to draw useful conclusions and decide on their marketing tactics. Having experienced this problem firsthand, the desire arose to create an advanced yet user-friendly solution: 
             a Social Media Analytics Dashboard that has the potential to completely transform how companies use social media data. </p>

          <div className="project-card">
            {/* <img src={projectImage1} alt="Project 1" /> */}
            <h3>Goal 1</h3>
            <p>The main objective of this research project is to create an intuitive Social Media Analytics Dashboard that can gather, examine, and display important metrics from a variety of social media sites. The dashboard attempts to give users a comprehensive picture of their social media performance in real-time by integrating with other platforms like Instagram, Twitter, TikTok, and others with ease.</p>
            <p>The inability to comprehend and interpret social media indicators in a meaningful way beyond simple numerical values is the root of the issue. These measures might provide an overview of online behavior, but they don't go very far in explaining the underlying desires and motives of users. This lack of understanding can have serious repercussions for companies, affecting their marketing plans, decision-making procedures, and general ability to compete in the digital market.
</p>
          
          </div>

          <div className="project-card">
          {/* <img src={projectImage2} alt="Project 2" /> */}
            <h3>Goal 2</h3>
            <p>The project utilizes Artificial Intelligence (AI) and Machine Learning (ML) to create the Social Media Analytics Dashboard, which aims to tackle the issues associated with analyzing social media data. The decision is based on a thorough assessment of different approaches and how well they correspond with the project's goals.
</p>
            <p>The preference for AI and ML over other approaches is justified by their higher capacity to manage extensive data, offer real-time insights, and adjust to new information. AI and ML provide automation, efficiency, and scalability, unlike traditional data analysis approaches that typically require user intervention and are time-consuming. These technologies have the ability to reveal patterns and insights that would be impractical to identify using traditional methods, giving organizations a competitive advantage in comprehending and interacting with their target audience.
The creation of the Social Media Analytics Dashboard requires a strong and adaptable technology infrastructure capable of managing the ever-changing characteristics of social media data. For this purpose, the project utilizes React.js, a JavaScript package that has transformed the development of interactive user interfaces. React.js stands out due to its numerous notable characteristics that make it an exceptional option for the project.
</p>
          </div>

          <div className="project-card">
          {/* <img src={projectImage3} alt="Project 3" /> */}
            <h3>Goal 3</h3>
            <p>By carefully choosing AI/ML and React.js, the project guarantees a user experience that is both effortless and instinctive, while also being enhanced with data-driven insights. The combination of AI's predictive analysis capabilities and React.js's speed in creating dynamic user interfaces establishes a new benchmark in social media analytics.</p>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="footer">
        <p>&copy; 2024 My Portfolio. All rights reserved.</p>
        <ul className="footer-links">
          <li><a href="#about">About Me</a></li>
          <li><a href="#contact">Contact</a></li>
          <li><a href="#services">Services</a></li>
        </ul>
      </footer>
    </div>
  );
}

export default App;
