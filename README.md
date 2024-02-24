# PHISHGUARD

## Introduction
**PHISHGUARD** is a project I've developed for my diploma, diving into the potential of machine learning to improve online security. Created using Flask, this application leverages logistic regression - a fundamental machine learning technique - to distinguish phishing sites from legitimate ones. My aim with **PHISHGUARD** is to provide a tool that enhances web navigation safety by identifying potential phishing threats, contributing to the broader academic discussion on cybersecurity.

## Features
The **PHISHGUARD** project extends its functionality through the following features, each thoughtfully integrated to support the core objective of enhancing online security through machine learning:
- **Simple User Interface**: Users can start their analysis by simply entering the URL of the website they're curious about right on the homepage.
- **Adaptable Analysis Modes**: Understanding that different users might have different needs, I've incorporated various analysis modes into **PHISHGUARD**. Whether you need a quick check or a more thorough analysis, there's an option for you.
- **Web Scraping for Data Collection**: Based on the selected analysis mode, **PHISHGUARD** scrapes the target website to collect data crucial for the evaluation process. This ensures that the analysis is detailed and specific to the website in question.
- **Detection of Phishing Features**: After collecting the data, **PHISHGUARD** examines the website for signs of phishing. This step is crucial for assessing the potential threat level of a website.
- **Logistic Regression Model for Prediction**: The heart of **PHISHGUARD** lies in its logistic regression model, which predicts whether a website is likely to be phishing or legitimate. This prediction is informed by a detailed analysis of the website's features.
- **Results Presentation**: A results page is generated to show the outcome of the analysis, complete with a visual snapshot of the website. These result pages are designed to be informative and are automatically deleted after five minutes.
- **Option for Detailed Report**: For those who want to dive deeper into the analysis, **PHISHGUARD** can send a detailed report via email. This report provides a comprehensive breakdown of the analysis and the reasoning behind the model's prediction.

## Installation Prerequisites
Before you can get started with **PHISHGUARD**, there are a couple of prerequisites that need to be installed on your computer. These tools are essential for cloning the project and running the application smoothly. Please ensure you have the following installed:
### Git
**Git** is a version control system that lets you manage and keep track of your source code history. You'll need Git to clone the **PHISHGUARD** project repository to your local machine.
- **Installation**: You can download Git from the [official website](https://git-scm.com/downloads).
- **Verification**: To verify that Git has been installed, open a terminal and run the following command:
    ```
    git --version
    ```
    If Git has been installed, you should see the version number displayed in the terminal.
### Docker
**Docker** is a platform for developing, shipping, and running applications in containers. By using Docker, you can ensure that **PHISHGUARD** runs consistently across different environments. It simplifies the setup process and manages the application's dependencies for you.
- **Installation**: You can download Docker from the [official website](https://www.docker.com/get-started).
- **Verification**: To verify that Docker has been installed, open a terminal and run the following command:
    ```
    docker --version
    ```
    If Docker has been installed, you should see the version number displayed in the terminal.

## Cloning the Project
To get started with **PHISHGUARD**, you'll need to clone the project repository onto your local machine. Follow the instructions below:
1. **Open your preferred command-line interface (CLI) on your computer.**
    - For **Windows**, you can use:
      - Command Prompt (Press `Win + R`, type `cmd`, and press `Enter`)
      - PowerShell (Press `Win + X`, select `Windows PowerShell`).
    - For **macOS** and **Linux**, you can use:
      - Terminal (Press `Ctrl + Alt + T`).
2. **Navigate to the directory where you want to clone the project.**
    ```
    cd path/to/your/directory
    ```
    Replace `path/to/your/directory` with the path to the directory where you want to store the project files.
3. **Execute the following command to clone the repository:**
    ```
    git clone https://github.com/IvanGeorgievProgramming/phishguard.git
    ```
    After running this command, a new directory named `phishguard` will be created in the specified location, containing the project files. This directory is your local copy of the **PHISHGUARD** project repository.
4. **Navigate to the `phishguard` directory:**
    ```
    cd phishguard
    ```
    This command changes the current directory to the `phishguard` directory, allowing you to access the project files.

## Configuring the Environment
Before running **PHISHGUARD**, you'll need to set up your environment variables by creating a `.env` file. This file contains sensitive information and configurations that the application requires to function properly. Here's how to do it:
1. **Create a `.env` File**:
    - Navigate to the root directory of the project where you cloned the repository.
    - Create a new file named `.env`.
2. **Copy the Example Configuration**:
    - Copy the contents of the provided `.env.example` file:
        ```
        FLASK_DEBUG='False'
        FLASK_HOST='0.0.0.0'
        FLASK_PORT='5000'
        SECRET_KEY='your_secret_key_here'
        HAS_VALID_EMAIL='True'
        EMAIL_SENDER='your_email_here'
        EMAIL_PASSWORD='your_password_here'
        ```
    - Paste the copied contents into the `.env` file you created.
3. **Replace Placeholder Values**:
    - Replace `your_secret_key_here` with a secure secret key of your choice. This key is essential for securing your application and should be kept confidential.
    - Replace `your_email_here` with the email address you want to use for sending detailed reports. This email address should be associated with a Gmail account.
    - Replace `your_password_here` with the password for the email address you specified.
4. **Save the File**:
    - After making the necessary changes, save the `.env` file.

By following these steps, you'll have configured the environment variables required for **PHISHGUARD** to run successfully on your system.

## Running the Application
To run the **PHISHGUARD** application using Docker, run the following commands in the root directory of the project:
1. **Build the Docker Image:**
    ```
    docker build -t phishguard .
    ```
   - This command builds a Docker image named `phishguard` from the Dockerfile located in the current directory (`.`).
   - `docker build`: Initiates the process of building a Docker image.
   - `-t phishguard`: Tags the resulting image with the name `phishguard` for easy reference.
   - `.`: Specifies the build context, indicating that the Dockerfile is located in the current directory.
2. **Run the Docker Container**:
    ```
    docker run -it -p 5000:5000 --name phishguard_container --rm phishguard
    ```
    - This command runs a Docker container using the `phishguard` image previously built.
    - `docker run`: Initiates the process of running a Docker container.
    - `-it`: Allocates a pseudo-TTY (terminal) and keeps STDIN open, allowing interaction with the container.
    - `-p 5000:5000`: Maps port 5000 on the host machine to port 5000 on the container, enabling access to the application from the host.
    - `--name phishguard_container`: Assigns the name `phishguard_container` to the running container for easy identification.
    - `--rm`: Automatically removes the container when it exits.
    - `phishguard`: Specifies the name of the Docker image used to create the container.

## How to Use PHISHGUARD
### Automated .env File Check
Upon initiating **PHISHGUARD**, the application conducts a series of checks to validate and set up your `.env` file, ensuring all necessary configurations are in place:
- **Existence Check**: At startup, **PHISHGUARD** looks for the `.env` file. If it's missing, the application automatically generates a new one populated with default configuration values. This step ensures that all required environment variables are present and correctly set up from the get-go.
- **Configuration Check**: The application reviews each key within the .env file for accuracy. Keys essential for the application's operation, such as `FLASK_DEBUG`, `FLASK_HOST`, and `FLASK_PORT`, are checked for their correct values. If any key is found to be missing or set incorrectly, **PHISHGUARD** automatically updates it to its default value. This includes generating a new `SECRET_KEY` if it's found to be absent, critical for maintaining the application's security integrity.
- **Email Functionality Check**: Email settings, identified by `EMAIL_SENDER` and `EMAIL_PASSWORD`, undergo verification to confirm their validity. Should this verification process fail, you're prompted to provide new credentials. This step is crucial for the detailed report feature to function properly. If the email credentials cannot be verified or if you choose not to use this feature, **PHISHGUARD** disables email functionality, ensuring the application can continue to run without this component.
### Accessing PHISHGUARD
**Launch the Application**: Open a web browser of your choice and enter http://localhost:5000 in the address bar. This action will take you to the **PHISHGUARD** homepage. 
### Home Page
On the home page, **PHISHGUARD** offers a clear and user-friendly interface for conducting website safety analyses:
- **Enter the Website URL**: Central to the home page is the URL input box, where you can type in the full URL of the website you want to check for phishing threats.
- **Select Analysis Mode**: Directly beneath the URL field, you have four distinct analysis options to choose from. These options are designed to accommodate different levels of analysis depth and speed, allowing you to tailor the review to your specific needs:
  - **Complete Site Analysis**: This is the most in-depth analysis mode, providing a comprehensive safety review by examining the entire website thoroughly.
  - **Comprehensive Analysis**: This mode offers a detailed scan of the whole site, which is faster than the complete site analysis. It focuses on the main content that loads interactively, delivering a detailed safety report without the depth of the complete analysis.
  - **Focused Analysis**: For a quicker assessment, this option provides a swift safety snapshot by analyzing the main page and its direct links, targeting immediate risks.
  - **Quick Analysis**: This is the fastest mode, offering a brief overview by focusing on the main page and immediate links. It is quicker but may not detect deeper issues that require more extensive scanning.
- **Analyze the Website**: After entering the URL and selecting the analysis mode, click the `Analyze Now` button to initiate the analysis process. This action triggers **PHISHGUARD** to start examining the website for potential phishing threats.
#### Home Page Preview
![PHISHGUARD Home Page Preview](https://github.com/IvanGeorgievProgramming/phishguard/blob/main/phishguard_screenshots/PHISHGUARD_Home.png)
### Result Page
After initiating the analysis of a website, **PHISHGUARD** will process the inputted data and display the findings on the results page. This page is structured to provide you with actionable insights and further tools for analysis:
- **Result Message**: At the top of the results page, you will see a clear message indicating the safety status of the analyzed website. This message will tell you whether the website is considered safe, suspicious, or likely to be a phishing threat based on the analysis conducted by **PHISHGUARD**.
- **Detailed Analysis via Email**: For users who require more information beyond the initial result message, there is an option to receive a detailed report. Below the result message, you'll find an email input box where you can enter your email address. After submitting your email, **PHISHGUARD** will send a comprehensive analysis report detailing the specific phishing indicators found and an explanation of the overall safety assessment.
- **Secure Website Preview**: Alongside the textual analysis, the results page provides a secure preview of the website. This feature allows you to see a visual representation of the analyzed website without the risk of interacting directly with potential threats. It's a non-interactive snapshot that serves as a visual aid to recall the website you've analyzed, reinforcing the textual information provided by **PHISHGUARD**.
#### Result Page Preview: Legitimate Website
![PHISHGUARD Result Page Preview - Legitimate Website](https://github.com/IvanGeorgievProgramming/phishguard/blob/main/phishguard_screenshots/PHISHGUARD_Result_Legitimate.png)
#### Result Page Preview: Phishing Website
![PHISHGUARD Result Page Preview - Phishing Website](https://github.com/IvanGeorgievProgramming/phishguard/blob/main/phishguard_screenshots/PHISHGUARD_Result_Phishing.png)
#### Detailed Report: Legitimate Website
![PHISHGUARD Detailed Report - Legitimate Website](https://github.com/IvanGeorgievProgramming/phishguard/blob/main/phishguard_screenshots/PHISHGUARD_Analysis_Report_Legitimate.png)
#### Detailed Report: Phishing Website
![PHISHGUARD Detailed Report - Phishing Website](https://github.com/IvanGeorgievProgramming/phishguard/blob/main/phishguard_screenshots/PHISHGUARD_Analysis_Report_Phishing.png)

## Model Training Repository
For those interested in exploring the intricacies of the model's training, including the selection of features, the preprocessing of data, the training process, and the evaluation of the model, I've made the model training repository publicly available. You can access it here:

[PHISHGUARD Model Training Repository](https://github.com/IvanGeorgievProgramming/phishguard_model_training)

## Acknowledgments
I wish to extend my gratitude towards two key sources of inspiration for **PHISHGUARD**:
- **codewithsadee**, for the design inspiration that shaped PHISHGUARD. Their innovative approach to web design, detailed in their [YouTube channel](https://www.youtube.com/@codewithsadee), was invaluable.
- **codinglabsolution**, for their visual elements that enhanced PHISHGUARD's aesthetics, found on their [YouTube channel](https://www.youtube.com/@codinglabsolution).

## Special Thanks
Special thanks to my **diploma supervisor** for their invaluable guidance, and to my **family** and **friends** for their unwavering support. This project wouldn't have been possible without you.
