<script>
  import logo from "./KMPLOGO_TEST.png";
  import { onMount } from "svelte";
  import { goto } from "$app/navigation";
  import { updateAuth } from '../../stores/auth-store.js';

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

<html lang="en">
   <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
   </head>
   <body>
    <div class = "login-container">
      <div class = "kmp-container">
         <div class = "logo-container">
            <img src={logo} alt="Logo" class = "logo-style" />
         </div>
         <div class = "title">
            <h1>Keep Me Posted</h1>
         </div>
         <div class="sub-title">
            Meetings to summaries.
         </div>
      </div>
      <!-- svelte-ignore a11y-no-static-element-interactions -->
      <div class="log-in-card">
         <div class = "heading">
            Log in to your account
         </div>
         <div class="subheading">
            Welcome back! Please enter your details.
         </div>
         <div class = "email-container">
            <div class="email-title">
               Email
            </div>
            <div class="email-input-container">
               <input class = "email-input-style"
                  type="text"
                  bind:value={email}
                  placeholder="name@email.com"
                  />
            </div>
            <div class="email-validation">
               {emailValidationString}
            </div>
         </div>
         <div class="password-container">
            <div class = "password-title">
               Password
            </div>
            <div class = "password-input-container">
               <input class = "password-input-style"
                  type="password"
                  bind:value={password}
                  placeholder="••••••••"
                  />
            </div>
            <div class = "password-validation">
               {passwordValidationString}
            </div>
         </div>
         <!-- svelte-ignore a11y-click-events-have-key-events -->
         <div class = "forgot-password"
            onmouseover="this.style.color='#6941C6'"
            onmouseout="this.style.color='#667085'"
            on:click={() => {
            alert("Womp Womp");
            }}
            >
            Forgot Password?
         </div>
         <div class = "primary-button-container">
            <button
               class = "primary-button"
               on:click={handleSignIn}
               onmouseover="this.style.backgroundColor='#0c4eae'"
               onmouseout="this.style.backgroundColor='#1570EF'"
               >
            Sign In
            </button>
         </div>
         <div class = "secondary-button-container">
            <form method="post" action="?/OAuth2">
               <button
                  class = "secondary-button"
                  alt="google sign in"
                  onmouseover="this.style.backgroundColor='#D0D5DD'"
                  onmouseout="this.style.backgroundColor='white'"
                  >
                  <svg
                     xmlns="http://www.w3.org/2000/svg"
                     x="0px"
                     y="0px"
                     width="4vw"
                     height="3vh"
                     viewBox="0 0 48 48"
                     >
                     <path
                        fill="#FFC107"
                        d="M43.611,20.083H42V20H24v8h11.303c-1.649,4.657-6.08,8-11.303,8c-6.627,0-12-5.373-12-12c0-6.627,5.373-12,12-12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C12.955,4,4,12.955,4,24c0,11.045,8.955,20,20,20c11.045,0,20-8.955,20-20C44,22.659,43.862,21.35,43.611,20.083z"
                        ></path>
                     <path
                        fill="#FF3D00"
                        d="M6.306,14.691l6.571,4.819C14.655,15.108,18.961,12,24,12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C16.318,4,9.656,8.337,6.306,14.691z"
                        ></path>
                     <path
                        fill="#4CAF50"
                        d="M24,44c5.166,0,9.86-1.977,13.409-5.192l-6.19-5.238C29.211,35.091,26.715,36,24,36c-5.202,0-9.619-3.317-11.283-7.946l-6.522,5.025C9.505,39.556,16.227,44,24,44z"
                        ></path>
                     <path
                        fill="#1976D2"
                        d="M43.611,20.083H42V20H24v8h11.303c-0.792,2.237-2.231,4.166-4.087,5.571c0.001-0.001,0.002-0.001,0.003-0.002l6.19,5.238C36.971,39.205,44,34,44,24C44,22.659,43.862,21.35,43.611,20.083z"
                        ></path>
                  </svg>
                  <p class = "secondary-button-text-style">Sign In With Google</p>
               </button>
            </form>
         </div>
         <div class = "sign-up-container">
            <div class = "sign-up-label">
               Don't have an account?
            </div>
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            <!-- svelte-ignore a11y-no-static-element-interactions -->
            <div class = "sign-up-link"
               on:click={handleSignUpClick}
               >
               Sign Up
            </div>
         </div>
      </div>
    </div>
   </body>
</html>

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
