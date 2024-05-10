<script>
    import logo from './KMPLOGO_TEST.png';
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
 
 
     let email = '';
     let password = '';
     let verifyPassword = '';
     let emailValidationString = "";
     let passwordValidationString = "Password must contain at least 8 characters, capital letters, and a special character";
     let passwordValidationStringColor = "#959595";
     let verifyPasswordValidationString = "";

 
     function isValidEmail(email) {
     // You can use a regular expression for email validation
     const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
     return emailRegex.test(email);
   }

   function isValidPassword(password){
    const passwordRegex = /^(?=.*[A-Z])(?=.*[!@#$%^&*()_+,\-.;:'"<>=?\/\[\]{}|`~])(?=.{8,})[a-zA-Z0-9!@#$%^&*()_+,\-.;:'"<>=?\/\[\]{}|`~]*$/;
    return passwordRegex.test(password);
}

 
     function emailValidation(email){
         if (email == ""){
           emailValidationString = "Please Enter Email";
           return false
         }
         else if(!isValidEmail(email)){
           emailValidationString = "Please Enter Valid Email";
           return false
         }
         else{
           emailValidationString = "";
           return true
         }
     }
 
     function passwordValidation(password){
       if(password == "" || !isValidPassword(password)){
           passwordValidationStringColor = "red";
           return false
       }
       else{
           passwordValidationStringColor = "#959595";
           return true
       }
     }

     function verifyPasswordValidation(password, verifyPassword){
        if(verifyPassword == ""){
            verifyPasswordValidationString = "Please Enter Password";
            return false
        }
        else if(verifyPassword != password){
            verifyPasswordValidationString = "Password does not match";
            return false
        }
        else{
            verifyPasswordValidationString = "";
            return true
        }
     }
 
     function handleEmailInUse(response){
        if(response.error = "This email address is already in use"){
            emailValidationString = response['error']
        }
     }

     async function handleSignUp() {
         console.log('Email:', email);
         console.log('Password:', password);
         console.log('VerifyPassword', verifyPassword)

         if(emailValidation(email) & passwordValidation(password) & verifyPasswordValidation(password, verifyPassword)){
            const data = {"username": email, "password": password, "email": email}
            const response = await postData(data)
            handleEmailInUse(response)
         }
 
         // Here you can perform further actions like sending the data to the server
     }
 
    
     // Optional: Fetch initial data or perform other tasks on component mount
     onMount(async () => {
         // Fetch initial data or perform other async tasks here
     });
 
    async function postData(signUpData) {
       try {
         const url = 'http://127.0.0.1:8000/signup'; // Replace with your API endpoint
         const data = signUpData;
 
         const response = await fetch(url, {
           method: 'POST',
           headers: {
             'Content-Type': 'application/json',
           },
           body: JSON.stringify(data),
         });
 
         const responseData = await response.json();
         console.log('Response:', responseData);
 
         if (response.ok){
             goto('/login');
         }
         return responseData
    
       } catch (error) {
         console.error('Error:', error);
       }
     }

     function handleLogInClick() {
    goto('/login');
  }
     

 </script>
   
 
  
 <html lang="en">
 
 <head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Linear Gradient Background</title>
   <style>
     body {
       margin: 0;
       height: 100vh;
       background: linear-gradient(to left, #53B1FD 0%, #1570EF 100%);
       display: flex;
       justify-content: center;
       align-items: center;
       color: white;
     }
 
     .content {
       text-align: center;
     }
   </style>
 </head>
 
 <body>
 
 <div style = "
 position: absolute;
 left: 10vw;
 top: 35vh;">
 
   <div style="max-width: 41%;">
  <img src="{logo}" alt="Logo" style="width: 100%; height: auto;">
</div>
 
 
 
 
<div style = "font-size: calc(2vw + 2.5vh);
font-family: 'Inter', sans-serif;
font-weight: 550;
letter-spacing: 0%;
position: relative; top: 0.2vh;">
    Keep Me Posted
  </div>



  
  <div style = "font-size: calc(1vw + 0.9vh);
font-family: 'Inter', sans-serif;
font-weight: 100;
font-style: italic;
letter-spacing: 0%;
position: relative; top: 0.5vh;
">
    Meetings to summaries.
  </div>
 </div>
 
  
 
 
 
 
 
 
 
   <div style = "height: 75vh; width: 32vw; border-radius: 16px; position: absolute; right: 12vw; background-color: white">
    
 
 
 
 
     <div style = 
     "width: 60vh; height: 10vh; color: #101828; position: absolute; top: 6vh;
     font-size: calc(1.5vw + 1vh);
  font-family: 'Inter', sans-serif;
  font-weight: 575;
  line-height: 38px;
  letter-spacing: 0%;
  vertical-align: baseline;
  left: 5.8vw;
     "
     >
          Sign Up
     </div >
  
  
  
     <div
     style = 
     "width: 60vh; height: 10vh; color: #667085; position: absolute; top: 11vh;
     font-size: calc(0.5vw + 1vh);  
     font-family: 'Inter', sans-serif;
     font-weight: 350;
     line-height: 24px;
     letter-spacing: 0%;
  vertical-align: baseline;
  left: 5.8vw;
     "
     >
      Create an account!
     </div>
  
  
  
     <div style = 
     "width: 60vh; height: 10vh; position: absolute; top: 18vh;">
  
          <div style = 
          "font-size: calc(0.4vw + 1vh);
          font-family: 'Inter', sans-serif;
          font-weight: 500;
          line-height: 20px;
          letter-spacing: 0%;
          vertical-align: baseline;
          position: absolute;
          left: 5.8vw;
          color: #344054;
          "
          
          >
              Email
              
          </div>
          <div style = 
          "font-size: 14px;
          font-family: 'Inter', sans-serif;
          font-weight: 500;
          line-height: 20px;
          letter-spacing: 0%;
          vertical-align: baseline;
          position: absolute;
          top: 3vh;
          left: 5.8vw;
          ">
  
              <input type="text" bind:value={email} style="font-size: calc(0.4vw + 1vh); border: 1px solid #D0D5DD; border-radius: 5px; padding: 10px; width: 20vw; height: 2vh;" placeholder="name@email.com" />
          </div>
          
          <div style = 
          "font-size: calc(0.4vw + 0.5vh);
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
          ">
           {emailValidationString}
          </div>
     </div>
  
     
  
  
  
     <div style = 
     "width: 60vh; height: 10vh; position: absolute; top: 29vh;">
  
          <div style = 
          "font-size: calc(0.4vw + 1vh);
          font-family: 'Inter', sans-serif;
          font-weight: 500;
          line-height: 20px;
          letter-spacing: 0%;
          vertical-align: baseline;
          position: absolute;
          left: 5.8vw;
          color: #344054;
          "
          
          >
              Password
              
          </div>
          <div style = 
          "font-size: 14px;
          font-family: 'Inter', sans-serif;
          font-weight: 500;
          line-height: 20px;
          letter-spacing: 0%;
          vertical-align: baseline;
          position: absolute;
          top: 3vh;
          left: 5.8vw; 
          ">
  
              <input type="password" bind:value={password} style="font-size: calc(0.4vw + 1vh); border: 1px solid #D0D5DD; border-radius: 5px; padding: 10px; width: 20vw; letter-spacing: 2px;" placeholder="••••••••" />
          </div>
 
          <div style = 
          "font-size: calc(0.4vw + 0.5vh);
          font-family: 'Inter', sans-serif;
          font-weight: 400;
          line-height: 2vh;
          letter-spacing: 0%;
          vertical-align: baseline;
          position: absolute;
          left: 5.8vw;
          color: {passwordValidationStringColor};
          top: 7.5vh;
          width: 32vh;
          padding-top: 7px;
          ">
           {passwordValidationString}
          </div>
  
     </div>

     <div style = 
     "width: 60vh; height: 10vh; position: absolute; top: 42.5vh;">
  
          <div style = 
          "font-size: calc(0.4vw + 1vh);
          font-family: 'Inter', sans-serif;
          font-weight: 500;
          line-height: 20px;
          letter-spacing: 0%;
          vertical-align: baseline;
          position: absolute;
          left: 5.8vw;
          color: #344054;
          "
          
          >
              Verify Password
              
          </div>
          <div style = 
          "font-size: 14px;
          font-family: 'Inter', sans-serif;
          font-weight: 500;
          line-height: 20px;
          letter-spacing: 0%;
          vertical-align: baseline;
          position: absolute;
          top: 3vh;
          left: 5.8vw;
          ">
  
              <input type="password" bind:value={verifyPassword} style="font-size: calc(0.4vw + 1vh); border: 1px solid #D0D5DD; border-radius: 5px; padding: 10px; width: 20vw; letter-spacing: 2px;" placeholder="••••••••" />
          </div>
 
          <div style = 
          "font-size: calc(0.4vw + 0.5vh);
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
          ">
            {verifyPasswordValidationString}
          </div>
  
     </div>
  
 
 
     
   
 
     
  
 
     <div style = "
     width: 60vh; height: 10vh;  position: absolute; top: 54vh; 
     ">
     <button on:click={handleSignUp} style="
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
        display: flex; /* Use flexbox */
        justify-content: center; /* Center horizontally */
        align-items: center; /* Center vertically */
    " 
    onmouseover="this.style.backgroundColor='#0c4eae'" 
    onmouseout="this.style.backgroundColor='#1570EF'"
    >
    Sign Up
    </button>
 
     </div>
 
     
 
     <div style="
     width: 60vh; height: 10vh; position: absolute; top: 60.5vh;
 ">   
 <form method="post" action="?/OAuth2">
  <button alt='google sign in' style="
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
      display: flex; /* Use flexbox */
      justify-content: center; /* Center horizontally */
      align-items: center; /* Center vertically */
  " onmouseover="this.style.backgroundColor='#D0D5DD'" onmouseout="this.style.backgroundColor='white'">
  
  <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="4vw" height="3vh" viewBox="0 0 48 48">
    <path fill="#FFC107" d="M43.611,20.083H42V20H24v8h11.303c-1.649,4.657-6.08,8-11.303,8c-6.627,0-12-5.373-12-12c0-6.627,5.373-12,12-12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C12.955,4,4,12.955,4,24c0,11.045,8.955,20,20,20c11.045,0,20-8.955,20-20C44,22.659,43.862,21.35,43.611,20.083z"></path><path fill="#FF3D00" d="M6.306,14.691l6.571,4.819C14.655,15.108,18.961,12,24,12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C16.318,4,9.656,8.337,6.306,14.691z"></path><path fill="#4CAF50" d="M24,44c5.166,0,9.86-1.977,13.409-5.192l-6.19-5.238C29.211,35.091,26.715,36,24,36c-5.202,0-9.619-3.317-11.283-7.946l-6.522,5.025C9.505,39.556,16.227,44,24,44z"></path><path fill="#1976D2" d="M43.611,20.083H42V20H24v8h11.303c-0.792,2.237-2.231,4.166-4.087,5.571c0.001-0.001,0.002-0.001,0.003-0.002l6.19,5.238C36.971,39.205,44,34,44,24C44,22.659,43.862,21.35,43.611,20.083z"></path>
    </svg>
    <p style = "position: relative; right: 0.8vw;" >
      Sign Up With Google
    </p>
    
  </button>
</form>
 </div>
 
  
      
     <div style=
     "display: flex; justify-content: space-between;
     width: 60vh; height: 10vh;  position: absolute; top: 66vh; 
 
     ">
 
         <div style="
         color: #667085;
         width: 50%; padding: 10px;
         font-size: calc(0.52vw + 0.5vh);
 font-family: 'Inter', sans-serif;
 font-weight: 400;
 line-height: 20px;
 letter-spacing: 0%;
 position: absolute;
 left: 10.5vw;
         ">
           Already have an account?
         </div>
 
 
         <div style="
         color: #175CD3;
         width: 50%; padding: 10px;
         font-size: calc(0.52vw + 0.6vh);
 font-family: 'Inter', sans-serif;
 font-weight: 600;
 line-height: 20px;
 letter-spacing: 0%;
 position: absolute;
 left:20vw;
 cursor: pointer;"
 on:click={handleLogInClick}>
           Log In
         </div>
       </div>
       
 
 
  
   </div>
 
 
 
 
 </body>
 
 </html>
 
 
 
 
   
   
   <!-- this styling secton contains styles for many components used throughout the page-->
   <style>
     
   </style>
   