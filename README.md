# Keep-Me-Posted

**Keep Me Posted (KMP)** is a powerful web application designed to streamline your meeting processes by providing concise summaries of meeting discussions. KMP allows users to focus on productive conversations rather than wasting precious time documenting meeting minutes.

## Team Members (2024)


| **Agile Team 1**                                | **Agile Team 2**                               | **Agile Team 3**                               |
|-------------------------------------------------|------------------------------------------------|------------------------------------------------|
| **Danny Leung** <br> *Product Management* <br> 32478704    | **Parul Garg** <br> *Product Management* <br> 32720254      | **Ayesha Tariq** <br> *Product Management* <br> 32497857      |
| **Diya Ramesh** <br> *Product Management* <br> 32336012    | **Angelina Leung** <br> *Product Management* <br> 33114447  | **Afia Farzana** <br> *Product Management* <br> 32501986      |
| **Maureen Pham** <br> *Release Train Engineer* <br> 33117144    | **Zihao (Jeremy) Wang** <br> *Release Train Engineer* <br> 32520433   | **Alex Ung** <br> *Release Train Engineer* <br> 32498853     |
| **Bowen Dong** <br> *Release Train Engineer* <br> 33109834    | **Benjamin Cherian** <br> *Release Train Engineer* <br> 31483534    | **Marcus Wei** <br> *Release Train Engineer* <br> 32503881   |
| **Brenda Dang** <br> *System Architect* <br> 33111197    | **Rohit Valanki** <br> *System Architect* <br> 31451764   | **Harrison Lane** <br> *System Architect* <br> 33110077    |
| **Ahmed Almasry** <br> *System Architect* <br> 31130143    |                                                 |                                                 |

# Installation Guide

Follow these steps to set up and run the Keep Me Posted application locally.

## Prerequisite

Before running the application locally, ensure you have installed node and npm globally - [guide]( https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) 


## Running the Full Application
Ensure you are in the root directory

### On Windows 
To run the application on Windows, execute the run_servers.bat file. You can do this by double-clicking the file in your file explorer or by running the following command in your terminal:
```console
./run_servers.bat
```

### On macOS
To run the servers on macOS, execute the run_servers.sh script. Use the following command in your terminal:
```console
bash run_servers.sh
```

# Required APIs
1. Add a **.env file** to the **KEEP-ME-POSTED** root directory.
2. Add a **.env.local file** to the **frontend** directory.
## Google Gemini
1. Generate an API key and put it in the **.env file** in the following format:

    ```
    GEMINI_API_KEY = "insert API key here"
    ```

2. Click on the project in Google Cloud Console and generate OAuth client IDs by clicking "Create Credentials".

3. Add the IDs to the **.env.local file** in the following format (without the curly brackets):

    ```
    SECRET_CLIENT_ID={insert ID here}

    SECRET_CLIENT_SECRET={insert ID here}

    ```

## AssemblyAI
1. Generate an API key and put it in the **.env file** in the following format:

    ```
    ASSEMBLYAI_API_KEY="insert API key here"
    ```

## API Key History
See [this link](https://docs.google.com/document/d/1eGwRlwuLmwz3y3zsQAngS8fpgq3jqJbLyGa8uDfpx7M/edit?usp=sharing) for the API key history.

# Login Credentials
See [this link](https://docs.google.com/document/d/12utGqgSPGZd5jvaNlT22FTJlpHR073LqWaKULZvcidU/edit) for accounts for:
* AssemblyAI project (API key)
* Django admin account

# UI/UX Prototyping
See [this link](https://www.figma.com/design/2ViXY8jjaYoqQUNvJ0zHOE/Keep-Me-Posted-Designs?node-id=2210-441096&t=XM3WtZ90aTzj3E8g-1) to edit and view the Figma.
