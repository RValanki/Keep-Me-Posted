<script>
  import logo from "../../assets/kmp-logo-large.png";
  import { onMount } from "svelte";
  import { goto } from "$app/navigation";
  import { updateAuth } from '../../stores/auth-store.js';
  import Logo from "../../components/logo.svelte"
  import LandingPageTitle from "../../components/landingPageTitle.svelte";

  let email = "";
  let password = "";
  let emailValidationString = "";
  let passwordValidationString = "";

  function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  function emailValidation(email) {
    if (email == "") {
      emailValidationString = "Please Enter Email";
      return false;
    } else if (!isValidEmail(email)) {
      emailValidationString = "Please Enter Valid Email";
      return false;
    } else {
      emailValidationString = "";
      return true;
    }
  }

  function passwordValidation(password) {
    if (password == "") {
      passwordValidationString = "Please Enter Password";
      return false;
    } else {
      passwordValidationString = "";
      return true;
    }
  }

  function handleIncorrectEmailOrPassword(response) {
    console.log(response);
    if (
      (response.detail == "Not found!") |
      (response.detail == "No User matches the given query.")
    ) {
      emailValidationString = "Incorrect Email or Password";
      passwordValidationString = "Incorrect Email or Password";
    }
  }

  async function handleSignIn() {
    console.log("Email:", email);
    console.log("Password:", password);

    if (emailValidation(email) & passwordValidation(password)) {
      const data = { email: email, password: password };
      const response = await postData(data);
      handleIncorrectEmailOrPassword(response);
    }
  }

  // Optional: Fetch initial data or perform other tasks on component mount
  onMount(async () => {
    // Fetch initial data or perform other async tasks here
  });

  async function postData(loginData) {
    try {
      const url = "http://127.0.0.1:8000/login";
      const data = loginData;

      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      const responseData = await response.json();
      console.log("Response:", responseData);

      if (response.ok) {
        updateAuth(loginData.email, true)
        goto("/email");
      }

      return responseData;
    } catch (error) {
      console.error("Error:", error);
    }
  }

  function handleSignUpClick() {
    goto("/signup");
  }

</script>

<div class = "login-container">
   

<div class="flex flex-col md:flex-row h-screen w-full">
   <!-- Top Row on Mobile / Left Column on Desktop -->
   <div class="flex md:flex-col w-full md:w-1/2">
       <div class="w-1/4 md:w-full md:flex-1">
         <div class=" ml-4 p-4 sm:p-6 md:p-0 mt-1 md:mt-0 min-w-[100%] md:min-w-[150px] ml-0 md:ml-32 h-full w-1/5 flex flex-col justify-end md:justify-end">
            <Logo class="mt-auto" />
        </div>
    
         
      </div>
       <div class="w-3/4 md:w-full md:flex-1 flex items-center md:items-start">
         <div class = "ml-4 md:ml-32 mt-2 md:mt-4 mb-0">
            <LandingPageTitle title = "Keep Me Posted" subTitle = "Meetings to summaries."/>
         </div>
         
      </div>
   </div>
   <!-- Bottom Row on Mobile / Right Column on Desktop -->
   <div class="w-full md:w-1/2 flex justify-center items-center h-full">
      <div class=" h-full w-full md:w-1/2 flex justify-center items-center">

         <div class="h-full md:h-3/4 w-full md:w-3/5 rounded-[16px]  bg-white min-w-[100%] md:min-w-[450px] min-h-full md:min-h-[500px] ml-0 md:ml-16 mr-0 md:mr-16 ">
            <!-- Content here -->
            hi
          </div>
          
      </div>

   </div>
</div>

</div>





 

<!-- this styling secton contains styles for many components used throughout the page-->
<style>
.login-container {
     margin: 0;
     height: 100vh;
     background: linear-gradient(to left, #53b1fd 0%, #1570ef 100%);
     display: flex;
     justify-content: center;
     align-items: center;
     color: white;
}
 .primary-button {
     background-color: #1570EF;
     color: #fff;
     border: none;
     border-radius: 8px;
     padding: 10px 20px;
     cursor: pointer;
     transition: background-color 0.3s ease-in-out;
     width: 21.5vw;
     position: absolute;
     left: 5.8vw;
     font-weight: 575;
     font-size: calc(0.5vw + 0.8vh);
     height: 5vh;
     text-align: center;
     display: flex;
     justify-content: center;
     align-items: center;
}
 .secondary-button {
     height: 5vh;
     font-size: calc(0.5vw + 0.8vh);
     border: 1px solid #D0D5DD;
     background-color: white;
     color: #344054;
     border-radius: 8px;
     padding: 10px 20px;
     cursor: pointer;
     transition: background-color 0.3s ease-in-out;
     width: 21.5vw;
     position: absolute;
     left: 5.8vw;
     display: flex;
     justify-content: center;
     align-items: center;
}
 .secondary-button-text-style{
     position: relative;
     right: 0.8vw;
}
 .primary-button-container {
     width: 32vw;
     height: 5vh;
     position: absolute;
     top: 47vh;
}
 .secondary-button-container{
     width: 60vh;
     height: 10vh;
     position: absolute;
     top: 53.5vh;
}
 .sign-up-container{
     display: flex;
     justify-content: space-between;
     width: 30vw;
     height: 10vh;
     position: absolute;
     top: 60vh;
}
 .sign-up-label{
     color: #667085;
     width: 50%;
     padding: 10px;
     font-size: calc(0.52vw + 0.5vh);
     font-family: 'Inter', sans-serif;
     font-weight: 400;
     line-height: 20px;
     letter-spacing: 0%;
     position: relative;
     left: 10.5vw;
}
 .sign-up-link{
     color: #6941C6;
     width: 50%;
     padding: 10px;
     font-size: calc(0.52vw + 0.6vh);
     font-family: 'Inter', sans-serif;
     font-weight: 600;
     line-height: 20px;
     letter-spacing: 0%;
     position: absolute;
     left: 19vw;
     cursor: pointer;
}
 .forgot-password{
     width: 10vw;
     height: 10vh;
     color: #667085;
     position: absolute;
     top: 42vh;
     left: 21vw;
     font-size: calc(0.4vw + 0.8vh);
     font-family: 'Inter', sans-serif;
     font-weight: 550;
     line-height: 20px;
     letter-spacing: 0%;
     cursor: pointer;
     transition: color 0.3s ease-in-out;
}
 .password-validation{
     font-size: calc(0.4vw + 0.5vh);
     font-family: 'Inter', sans-serif;
     font-weight: 400;
     line-height: 20px;
     letter-spacing: 0%;
     vertical-align: baseline;
     position: absolute;
     left: 5.8vw;
     color: red;
     top: 7.5vh;
     padding-top: 2.5px;
}
 .password-input-container{
     font-size: 14px;
     font-family: 'Inter', sans-serif;
     font-weight: 500;
     line-height: 20px;
     letter-spacing: 0%;
     vertical-align: baseline;
     position: absolute;
     top: 3vh;
     left: 5.8vw;
}
 .password-input-style{
     font-size: calc(0.4vw + 1vh);
     border: 1px solid #D0D5DD;
     border-radius: 5px;
     padding: 10px;
     width: 20vw;
     height: 2vh;
     letter-spacing: 2px;
}
 .password-title{
     font-size: calc(0.4vw + 1vh);
     font-family: 'Inter', sans-serif;
     font-weight: 500;
     line-height: 20px;
     letter-spacing: 0%;
     vertical-align: baseline;
     position: absolute;
     left: 5.8vw;
     color: #344054;
}
 .password-container{
     width: 60vh;
     height: 10vh;
     position: absolute;
     top: 32vh;
}
 .email-validation{
     font-size: calc(0.4vw + 0.5vh);
     font-family: 'Inter', sans-serif;
     font-weight: 400;
     line-height: 20px;
     letter-spacing: 0%;
     vertical-align: baseline;
     position: absolute;
     left: 5.8vw;
     color: red;
     top: 7.5vh;
     padding-top: 2.2px;
}
 .email-input-style{
     font-size: calc(0.4vw + 1vh);
     border: 1px solid #D0D5DD;
     border-radius: 5px;
     padding: 10px;
     width: 20vw;
     height: 2vh;
}
 .email-input-container{
     font-size: 14px;
     font-family: 'Inter', sans-serif;
     font-weight: 500;
     line-height: 20px;
     letter-spacing: 0%;
     vertical-align: baseline;
     position: absolute;
     top: 3vh;
     left: 5.8vw;
}
 .email-title{
     font-size: calc(0.4vw + 1vh);
     font-family: 'Inter', sans-serif;
     font-weight: 500;
     line-height: 20px;
     letter-spacing: 0%;
     vertical-align: baseline;
     position: absolute;
     left: 5.8vw;
     color: #344054;
}
 .email-container{
     width: 60vh;
     height: 10vh;
     position: absolute;
     top: 22vh;
}
 .subheading{
     width: 60vh;
     height: 10vh;
     color: #667085;
     position: absolute;
     top: 16vh;
     font-size: calc(0.5vw + 1vh);
     font-family: 'Inter', sans-serif;
     font-weight: 350;
     line-height: 24px;
     letter-spacing: 0%;
     vertical-align: baseline;
     left: 5.8vw;
}
 .heading{
     width: 60vh;
     height: 10vh;
     color: #101828;
     position: absolute;
     top: 10vh;
     font-size: calc(1.5vw + 1vh);
     font-family: 'Inter', sans-serif;
     font-weight: 575;
     line-height: 38px;
     letter-spacing: 0%;
     vertical-align: baseline;
     left: 5.8vw;
}
 .log-in-card{
     height: 75vh;
     width: 32vw;
     border-radius: 16px;
     position: absolute;
     right: 12vw;
     background-color: white;
}
 .logo-style{
     width: 100%;
     height: auto;
}
 .sub-title{
     font-size: calc(1vw + 0.9vh);
     font-family: 'Inter', sans-serif;
     font-weight: 100;
     font-style: italic;
     letter-spacing: 0%;
     position: relative;
     top: 0.5vh;
     color: white;
}
 .title{
     font-size: calc(2vw + 2.5vh);
     font-family: 'Inter', sans-serif;
     letter-spacing: 0%;
      font-weight: 550;
     position: relative;
     top: 0.2vh;
}
h1{
   color: white;
}
 .logo-container{
     max-width: 41%;
}
 .kmp-container{
     position: absolute;
     left: 10vw;
     top: 35vh;
}

</style>
