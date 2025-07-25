
// ==============================   reveal header on scroll

    window.addEventListener('scroll', function() {  
    const header = document.querySelector('#header-nav');  
    if (window.scrollY > 50) { // Adjust the scroll threshold as needed  
        header.classList.add('scrolled');  
    } else {  
        header.classList.remove('scrolled');  
    }  
});  


















// ==============================   header menu toggle





const menuToggle = document.getElementById("menu-toggle");
const openIcon = document.getElementById("open-icon");
const closeIcon = document.getElementById("close-icon");
const popupMenu = document.getElementById("menu");


    menuToggle.addEventListener("click", () => {
        toggleMenu();
    });
    
    




    
    function toggleMenu() {
    
    
    
        if (popupMenu.classList.contains("open")) {

            popupMenu.classList.remove("open");
            openIcon.classList.add("visible");
            closeIcon.classList.remove("visible");
            
        } else {

            popupMenu.classList.add("open");
            openIcon.classList.remove("visible");
            closeIcon.classList.add("visible");
        }
    
        
    }

















/*----------------------form reveal password toggle icon code------------------------------------*/

function togglePassword() {
  var passwordField = document.getElementById("password");
  var toggleIcon = document.getElementById("toggle-icon");

  if (passwordField.type === "password") {

      passwordField.type = "text";
      toggleIcon.classList.remove("fa-eye");
      toggleIcon.classList.add("fa-eye-slash");
  } 
  
  else {
      passwordField.type = "password";
      toggleIcon.classList.remove("fa-eye-slash");
      toggleIcon.classList.add("fa-eye");
  }
}

































// -------------------------- multi drop down -----------------------------------


const buttons = document.querySelectorAll('.toggle-button');


buttons.forEach(button => {
    button.addEventListener('click', () => {
    
        const targetId = button.getAttribute('data-target');
        const content = document.getElementById(targetId);

    
        if (content.style.display === "none" || content.style.display === "") {
            content.style.display = "block";
            content.style.transition = "1s ease";
        } else {
            content.style.display = "none";
        }
    });
});










































// --------------------------------- view profile --------------------------------------


const gallery = document.getElementById('gallery');
  const scrollLeftBtn = document.getElementById('scroll-left');
  const scrollRightBtn = document.getElementById('scroll-right');
  const modal = document.getElementById('previewModal');
  const largeImage = document.getElementById('largeImage');
  const closeModalBtn = document.getElementById('closeModal');

  // Scroll functions
  scrollLeftBtn.onclick = () => {
    gallery.scrollBy({ left: -200, behavior: 'smooth' });
  };
  scrollRightBtn.onclick = () => {
    gallery.scrollBy({ left: 200, behavior: 'smooth' });
  };

  // Handle press and hold for images
  document.querySelectorAll('.pic').forEach(pic => {
    let pressTimer = null;
    let holdTimeout = null;

    const startPress = (e) => {
      e.preventDefault();
      holdTimeout = setTimeout(() => {
        // Show larger preview when held for 4 seconds
        const largeSrc = pic.getAttribute('data-large');
        largeImage.src = largeSrc;
        modal.style.display = 'flex';
      }, 1000);
    };

    const cancelPress = () => {
      clearTimeout(holdTimeout);
    };

    // Mouse events
    pic.addEventListener('mousedown', startPress);
    pic.addEventListener('mouseup', cancelPress);
    pic.addEventListener('mouseleave', cancelPress);

    // Touch events for mobile
    pic.addEventListener('touchstart', startPress);
    pic.addEventListener('touchend', cancelPress);
    pic.addEventListener('touchcancel', cancelPress);

    // Optional: Click to do something else
  });

  // Close modal
  document.getElementById('closeModal').onclick = () => {
    modal.style.display = 'none';
  };

  // Close modal when clicking outside the image
  window.onclick = (e) => {
    if (e.target == modal) {
      modal.style.display = 'none';
    }
  };



















































































  // // -------------------------------  Side bar --------------------------------------


const dropdownBtns = document.querySelectorAll(".dropdown-btn");  
const sidebar = document.getElementById("mySidebar");  
const content = document.getElementById("myContent");  
const toggleBtn = document.getElementById("toggleBtn");  
const openIcon2 = toggleBtn.querySelector('.open');  
const closeIcon2 = toggleBtn.querySelector('.close');  




        // to show dropdown list

        dropdownBtns.forEach(btn => {  
        btn.addEventListener("click", function() {  
                this.classList.toggle("active");  
                const dropdownContent = this.nextElementSibling;  

                if (dropdownContent.style.display === "block") {  
                    dropdownContent.style.display = "none";  
                    this.querySelector('i.uis-down').classList.remove('rotate2');  
                } else {  
                    dropdownContent.style.display = "block";  
                    this.querySelector('i.uis-down').classList.add('rotate2');  
                }  

            });  
        });  




    // To hide and show side bar

        toggleBtn.addEventListener("click", function() {  
        sidebar.classList.toggle("hidden");  
        content.classList.toggle("collapsed");  
        this.classList.toggle("collapsed");  

        if (sidebar.classList.contains("hidden")) {  
            openIcon2.style.display = 'none';  
            closeIcon2.style.display = 'inline-block';  
                //toggleBtn.style.left = '10px'; // Move toggle button to the left 
            } else {  
                openIcon2.style.display = 'inline-block';  
                closeIcon2.style.display = 'none'; 
                //toggleBtn.style.left = '10px'; // Reset toggle button position   
            }  
        });  


    


            // Initialize the icons' visibility and toggle button position
            
            
            if (sidebar.classList.contains("hidden")) {  
                openIcon2.style.display = 'none';  
                closeIcon2.style.display = 'inline-block';  
            } else {  
                openIcon2.style.display = 'inline-block';  
                closeIcon2.style.display = 'none';   
            }  