<!--Email Token Component 

Contains email token functionality and styling

Author: Ayesha Tariq
Last Modified: 12/05/2024 -->
<script>
    import Button from './button.svelte';
    import removeUser from '../assets/remove-user-icon.png';
    
    function handleClick(){
        console.log("Delete button clicked!");

    }

    import { Style } from '@material-ui/icons';
    let inputText = 'tarayesha508@gmail.com';
</script>
  
  <style>
    .email-token {
    width: max-content; /* Adjust as needed */
    height: 2px; /* Adjust as needed */
    border-radius: 50px; /* Half of height to create the oval shape */
    background-color:rgba(211, 211, 211,0.6);
    padding: 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border: 2px solid #dddddd4d;
    color: #363F72;
    font-family: Arial;

    }


  </style>
  
  <div class="email-token">
    {inputText}

    <!-- <Button type="primary" on:click = {handleClick} text="" rounded=true><img class="remove-user-icon" src={removeUser} alt="remove-user-icon"/></Button> -->
    <button on:click={handleClick} style="border-radius:50px; background-color: rgba(211, 211, 211, 0); color: #363F72;  border: none;  cursor:pointer;">X</button>
  </div>

  