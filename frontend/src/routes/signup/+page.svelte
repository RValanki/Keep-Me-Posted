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
 
   <div style = "" >
     <img src= {logo} alt = "Logo">
   </div>
 
 
 
 
   <div style = "font-size: 50px;
 font-family: 'Inter', sans-serif;
 font-weight: 550;
 letter-spacing: 0%;
 position: relative; top: 0.2vh;">
     Keep Me Posted
   </div>
 
 
 
   
   <div style = "font-size: 22px;
 font-family: 'Inter', sans-serif;
 font-weight: 100;
 font-style: italic;
 letter-spacing: 0%;
 position: relative; top: 0.5vh;
 ">
     Meetings to summaries.
   </div>
 </div>
 
  
 
 
 
 
 
 
 
   <div style = "height: 75vh; width: 60vh; border-radius: 16px; position: absolute; right: 12vw; background-color: white">
    
 
 
 
 
     <div style = 
     "width: 60vh; height: 10vh; color: #101828; position: absolute; top: 6vh;
     font-size: 30px;
  font-family: 'Inter', sans-serif;
  font-weight: 575;
  line-height: 38px;
  letter-spacing: 0%;
  vertical-align: baseline;
  left: 11vh;
     "
     >
          Sign Up
     </div >
  
  
  
     <div
     style = 
     "width: 60vh; height: 10vh; color: #667085; position: absolute; top: 11vh;
     font-size: 16px;
     font-family: 'Inter', sans-serif;
     font-weight: 350;
     line-height: 24px;
     letter-spacing: 0%;
  vertical-align: baseline;
  left: 11vh;
     "
     >
      Create an account!
     </div>
  
  
  
     <div style = 
     "width: 60vh; height: 10vh; position: absolute; top: 18vh;">
  
          <div style = 
          "font-size: 14px;
          font-family: 'Inter', sans-serif;
          font-weight: 500;
          line-height: 20px;
          letter-spacing: 0%;
          vertical-align: baseline;
          position: absolute;
          left: 11vh;
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
          left: 11vh;
          ">
  
              <input type="text" bind:value={email} style="border: 1px solid #D0D5DD; border-radius: 5px; padding: 10px; width: 20vw;" placeholder="name@email.com" />
          </div>
          
          <div style = 
          "font-size: 10.5px;
          font-family: 'Inter', sans-serif;
          font-weight: 400;
          line-height: 20px;
          letter-spacing: 0%;
          vertical-align: baseline;
          position: absolute;
          left: 11vh;
          color: red;
          top: 7.5vh;
          ">
           {emailValidationString}
          </div>
     </div>
  
     
  
  
  
     <div style = 
     "width: 60vh; height: 10vh; position: absolute; top: 29vh;">
  
          <div style = 
          "font-size: 14px;
          font-family: 'Inter', sans-serif;
          font-weight: 500;
          line-height: 20px;
          letter-spacing: 0%;
          vertical-align: baseline;
          position: absolute;
          left: 11vh;
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
          left: 11vh;
          ">
  
              <input type="password" bind:value={password} style="border: 1px solid #D0D5DD; border-radius: 5px; padding: 10px; width: 20vw; letter-spacing: 2px;" placeholder="••••••••" />
          </div>
 
          <div style = 
          "font-size: 10.5px;
          font-family: 'Inter', sans-serif;
          font-weight: 400;
          line-height: 20px;
          letter-spacing: 0%;
          vertical-align: baseline;
          position: absolute;
          left: 11vh;
          color: {passwordValidationStringColor};
          top: 7.5vh;
          width: 32vh;
          ">
           {passwordValidationString}
          </div>
  
     </div>

     <div style = 
     "width: 60vh; height: 10vh; position: absolute; top: 42.5vh;">
  
          <div style = 
          "font-size: 14px;
          font-family: 'Inter', sans-serif;
          font-weight: 500;
          line-height: 20px;
          letter-spacing: 0%;
          vertical-align: baseline;
          position: absolute;
          left: 11vh;
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
          left: 11vh;
          ">
  
              <input type="password" bind:value={verifyPassword} style="border: 1px solid #D0D5DD; border-radius: 5px; padding: 10px; width: 20vw; letter-spacing: 2px;" placeholder="••••••••" />
          </div>
 
          <div style = 
          "font-size: 10.5px;
          font-family: 'Inter', sans-serif;
          font-weight: 400;
          line-height: 20px;
          letter-spacing: 0%;
          vertical-align: baseline;
          position: absolute;
          left: 11vh;
          color: red;
          top: 7.5vh;
          ">
            {verifyPasswordValidationString}
          </div>
  
     </div>
  
 
 
     
   
 
     
  
 
     <div style = "
     width: 60vh; height: 10vh;  position: absolute; top: 54vh; 
     ">
     <button on:click={handleSignUp} style=
     "background-color: #1570EF; color: #fff; border: none; border-radius: 8px; padding: 10px 20px; cursor: pointer;
     transition: background-color 0.3s ease-in-out;
     width: 21.5vw;
     position: absolute;
     left: 11vh;
     font-weight: 575;
     " 
     onmouseover="this.style.backgroundColor='#0c4eae'" 
     onmouseout="this.style.backgroundColor='#1570EF'"
     >
     Sign Up
     </button>
 
     </div>
 
     
 
     <div style="
     width: 60vh; height: 10vh; position: absolute; top: 60vh;
 ">   <form method="post" action="?/OAuth2">
     <button style="border: 1px solid #D0D5DD; background-color: white; color: #344054; border-radius: 8px; padding: 10px 20px; cursor: pointer; transition: background-color 0.3s ease-in-out; width: 21.5vw; position: absolute; left: 11vh;" onmouseover="this.style.backgroundColor='#D0D5DD'" onmouseout="this.style.backgroundColor='white'">
         <img src="https://www.gstatic.com/images/branding/googlelogo/svg/googlelogo_clr_92x30px.svg" alt="Google Logo" style="width: 30px; height: auto; margin-right: 10px;">Sign Up With Google
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
         font-size: 12px;
 font-family: 'Inter', sans-serif;
 font-weight: 400;
 line-height: 20px;
 letter-spacing: 0%;
 position: relative;
 left: 20vh;
         ">
           Already have an account?
         </div>
 
 
         <div style="
         color: #175CD3;
         width: 50%; padding: 10px;
         font-size: 12px;
 font-family: 'Inter', sans-serif;
 font-weight: 600;
 line-height: 20px;
 letter-spacing: 0%;
 position: relative;
 left:7.75vh;
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
   