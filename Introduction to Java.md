# Some Terminologies

Integrated Development Environment(IDE): An environment tool when programmers want to develop software.

Note: Software(SW) controls Hardware(HW).

In Java, we have 3 programming paradigms:
1. Procedural Programming
2. Object-Oriented Programming
3. Generic Programming

Computer Programs: process data under the control of instructions.
## Computer Organization

## A computer system is typically organized into five main logical units
|Unit|Function|
|----|--------|
|Input Unit|Receives data from external devices (e.g., keyboard, mouse, scanner) and converts it into a format that the computer can understand.|
|Output Unit|Displays or presents data to the user (e.g., monitor, printer, speakers).|
|Memory Unit|Stores data and instructions temporarily or permanently. <br> It consists of two main types: <br> - Primary Memory (RAM): Volatile memory used for active programs and data. <br> - Secondary Memory (Hard Drive, SSD): Non-volatile memory for long-term storage.|
|Arithmetic Logic Unit (ALU)|Performs arithmetic (addition, subtraction, multiplication, division) and logical operations (AND, OR, NOT, XOR) on data.|
|Control Unit|Coordinates the activities of all other units, fetches instructions from memory, decodes them, and executes them.|


![스크린샷 2024-12-28 213400](https://github.com/user-attachments/assets/d1d58bab-caea-446f-a00e-7a1b5c85d791)


## Data Hierarchy

Data Hierarchy is a systematic organization of data, often in a hierarchical form. It represents the relationships between different levels of data elements, helping to understand and manage data effectively.

Key Levels in Data Hierarchy
1. Bit: The smallest unit of data, representing a binary value (0 or 1).  
2. Byte: A group of 8 bits, representing a single character.  
3. Field: A collection of related characters representing a single piece of information (e.g., name, age, address).  
4. Record: A group of related fields representing a single entity (e.g., a customer record, an employee record).  
5. File: A collection of related records.  
6. Database: A collection of related files.


Visual Representation:

![스크린샷 2024-12-28 213903](https://github.com/user-attachments/assets/afd9530e-9e89-4ea4-a537-6e20b98748be)


Importance of Data Hierarchy:
 - Data Organization: Provides a structured way to organize and manage data.  
 - Data Retrieval: Facilitates efficient data retrieval and processing.  
 - Data Integrity: Helps maintain data consistency and accuracy.  
 - Data Security: Enables better control over data access and security.  
 - Data Analysis: Supports data analysis and decision-making.


## Machine Language, Assembly Language, High-level language
Visualization:

![스크린샷 2024-12-28 214134](https://github.com/user-attachments/assets/6862e7df-65f3-4503-bc15-ee9ce963330d)


 - Machine language: the most basic level, directly understood by the computer.
 - Assembly language: a step up, using mnemonics for better readability.
 - High-level language: the most abstract, offering the highest level of abstraction for human programmers.

## Object Technology

- Class: blueprint of making an object.
- Object: reusable SW component. 
- Method: performing  a task in a program(function)
- Instantiation: object made by a specific class with its methods. This object is called an instance.
- Attribute: a characteristic or property associated with an object or a class. It's essentially a variable that holds data specific to an object or a class.
- Encapsulation by a class
- Inheritance: the subclass starts with the characteristics of an existing class called superclass.
- Interfaces: collections of related methods that enable them to tell objects what to do. (It implements one or more interfaces.)


## Unified Modeling Language(UML)
Unified Modeling Language(UML): A general-purpose visual modeling language that is intended to provide a standard way to visualize the design of a system.

## Operating System (OS)
The OS is like the driver and the traffic controller of a computer.
Key Roles of the OS:
1. Manages Hardware:
 - Communicates with all the parts of your computer (CPU, RAM, hard drive, mouse, keyboard, etc.).
 - Allocates resources like CPU time and memory to different programs.
 - Handles input/output operations (like when you type or click).
2. Provides a User Interface:
 - Gives you a way to interact with the computer (like the Windows desktop or the macOS interface).
 - Lets you run programs and manage files.
3. Manages Software:
 - Loads and executes programs.
 - Provides a platform for other software to run on.
 - Handles memory management for programs.
4. Ensures Security:
 - Protects your computer from viruses and malware.
 - Controls access to your files and data.

## Keyword for OS

- Kernel: The core part of the OS that directly interacts with the HW.
- Processes: Running programs on the computer.
- Threads: Smaller units within a process that can run concurrently.
- File Systems: How the OS organizes and stores files on your storage devices.
- Virtual Memory: How the OS manages memory to make it appear larger than physical RAM.

# Internet and World Wide Web

TCP(Transmission Control Protocol): connected-oriented, meaning that sender and receiver firstly need to establish a connection based on agreed parameters.
The <b>Internet protocol suite</b>, commonly known as <b>TCP/IP</b>, is a framework for organizing the set of communication protocols used in the Internet and similar computer networks according to functional criteria.

## Internet
Internet: networks for both intraorganizational and interorganizational communication.


IP address: An identifier to locate one another on the Internet.

![image](https://github.com/user-attachments/assets/b5f7f34c-d8fa-46a2-8008-311a2ff69dac)

(source: https://mr-zero.tistory.com/36)

### WWW(World Wide Web): collection of HW and SW related to the Internet that allow users to locate and view documents.
### IoT(Internet of Things): The Internet of Things (IoT) refers to a network of physical devices, vehicles, appliances, and other physical objects that are embedded with sensors, software, and network connectivity, allowing them to collect and share data.

# Categories about SW Technologies

<table>
 <tr>
   <th>Category</th>
   <th>Technology</th>
   <th>Description</th>
   <th>Key Concepts & Examples</th>
   <th>Refactoring Considerations</th>
  </tr>
  <tr>
   <td rowspan="5">Programming Languages</td>
   <td>Python</td>
   <td>High-level, versatile language known for readability and extensive libraries</td>
   <td>Object-Oriented Programming (OOP), Functional Programming, Data Structures (lists, dictionaries), Libraries (NumPy, Pandas, TensorFlow)</td>
   <td>Refactor for better readability, maintainability, performance (e.g., using list comprehensions, optimizing loops)</td>
  </tr>
  <tr>
   <td>JavaScript</td>
   <td>Primarily for front-end web development, also used for back-end and mobile.</td>
   <td>Asynchronous programming, DOM manipulation, popular frameworks (React, Angular, Vue.js)</td>
   <td>Refactor for better performance, code reusability (e.g., breaking down large functions, using functional components)</td>
  </tr>
  <tr>
   <td>Java</td>
   <td>Robust, platform-independent language for enterprise applications and Android</td>
   <td>OOP, JVM (Java Virtual Machine), Spring Framework (popular for enterprise development)</td>
   <td>Refactor to improve modularity, reduce code duplication (e.g., using design patterns like Dependency Injection)</td>
  </tr>
  <tr>
   <td>C#</td>
   <td>Microsoft-developed language for Windows applications, game development, and .NET</td>
   <td>OOP, .NET Framework (ecosystem of libraries and tools), Unity (game engine)</td>
   <td>Refactor to enhance performance, improve code readability (e.g., using LINQ for data querying)</td>
  </tr>
  <tr>
   <td>C++</td>
   <td>High-performance language for systems programming, game development, and performance-critical applications</td>
   <td>Low-level memory management, STL (Standard Template Library)</td>
   <td>Refactor for better performance, memory efficiency (e.g., optimizing algorithms, using smart pointers)</td>
  </tr>
 <tr>
  <td rowspan="2">Databases</td>
  <td>SQL</td>
  <td>Structured Query Language for interacting with relational databases</td>
  <td>Data Definition Language (DDL), Data Manipulation Language (DML), Joins, Indexes</td>
  <td>Refactor for better query performance (e.g., creating indexes, optimizing joins, using stored procedures)</td>
 </tr>
 <tr>
  <td>NoSQL</td>
  <td>Non-relational databases for flexible data storage</td>
  <td>Document databases (MongoDB), Key-value stores (Redis), Graph databases (Neo4j)</td>
  <td>Refactor for scalability, data consistency (e.g., choosing the right NoSQL type for the use case, implementing appropriate data partitioning)</td>
 </tr>
 <tr>
  <td rowspan="2">Web Development</td>
  <td>HTML</td>
  <td>Defines the structure and content of web pages</td>
  <td>Semantic HTML, accessibility</td>
  <td>Refactor for better readability, maintainability, and accessibility (e.g., using meaningful element names, adding ARIA attributes)</td>
 </tr>
 <tr>
  <td>CSS</td>
  <td>Styles the appearance of web pages</td>
  <td>CSS preprocessors (Sass, Less), CSS frameworks (Bootstrap, Materialize)</td>
  <td>Refactor for better maintainability, modularity (e.g., using CSS Modules, BEM naming convention)</td>
 </tr>
 <tr>
  <td>Cloud Computing</td>
  <td>AWS</td>
  <td>Amazon Web Services, a suite of cloud computing services</td>
  <td>EC2 (virtual machines), S3 (object storage), Lambda (serverless computing)</td>
  <td>Refactor for cost optimization, performance improvement, security enhancement (e.g., right-sizing instances, optimizing Lambda functions)</td>
 </tr>
 <tr>
  <td rowspan="2">Mobile Development</td>
  <td>iOS</td>
  <td>Apple's mobile operating system</td>
  <td>Swift (modern language), Objective-C (legacy language), UIKit (framework)</td>
  <td>Refactor for better app performance, user experience (e.g., optimizing image loading, using caching mechanisms)</td>
 </tr>
 <tr>
  <td>Android</td>
  <td>Google's mobile operating system</td>
  <td>Java, Kotlin (modern language), Android SDK</td>
  <td>Refactor for better app performance, user experience (e.g., optimizing layout performance, using background threads)</td>
 </tr>
 <tr>
  <td>Data Science</td>
  <td>Machine Learning</td>
  <td>Algorithms that enable computers to learn from data</td>
  <td>Supervised learning (classification, regression), Unsupervised learning (clustering), Deep learning (neural networks)</td>
  <td>Refactor for better model performance, interpretability (e.g., feature engineering, hyperparameter tuning, model simplification)</td>
 </tr>
 <tr>
  <td>Software Development Methodologies</td>
  <td>Agile</td>
  <td>Iterative approach with flexibility and customer collaboration</td>
  <td>Scrum, Kanban</td>
  <td>Refactor within sprints, continuous integration/continuous delivery (CI/CD)</td>
 </tr>
 <tr>
  <td>Software Development Principles</td>
  <td>SOLID</td>
  <td>Principles for writing clean, maintainable, and extensible code</td>
  <td>Single Responsibility Principle, Open/Closed Principle, Liskov Substitution Principle, Interface Segregation Principle, Dependency Inversion Principle 1</td>
  <td>Refactor to adhere to SOLID principles, improve code quality and maintainability</td>
 </tr>
</table>
