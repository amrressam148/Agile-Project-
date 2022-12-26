
         document.addEventListener('DOMContentLoaded',function()
         
         {
           
            //by default the submit button will be disabled  
            document.querySelector('#submit').disabled = true;
            document.querySelector('#Fname').onkeyup = () => 
            {
                document.querySelector('#submit').disabled = false; 
            }

            document.querySelector('form').onsubmit = function()
          {
            const name = document.querySelector('#Fname').value;
            alert(`Welcome, ${name}!`);
          };

         })
         function showpassword() {
            var x = document.getElementById("password");
            if (x.type === "password") {
              x.type = "text";
            } else {
              x.type = "password";
            }
          }
         