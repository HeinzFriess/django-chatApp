function getDate() {
    const monthNames = ["January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"];
    let dateObj = new Date();
    let month = dateObj.getUTCMonth() + 1; //months from 1-12
    let day = dateObj.getUTCDate();
    let year = dateObj.getUTCFullYear();

    return monthNames[month-1] + " " + day + ", " + year;
  }

  async function sendMessage() {
    let fd = new FormData();
    fd.append('textmessage', messageField.value);
    fd.append('csrfmiddlewaretoken', csrfToken);
    try {
      document.getElementById('messageContainer').innerHTML += `
         <div class="mdl-card" id="toDelete">
          <div class="mdl-card__title">
            <span class="color-gray"> [${getDate()}] : [${userName}] </span>
          </div>
          <div class="mdl-card__media color-gray" >
            ${messageField.value}
          </div>
        </div>
      `;
      let response = await fetch('/chat/', {
        method: 'POST',
        body: fd
      })
      let json = await response.json();

      document.getElementById('toDelete').remove();

      document.getElementById('messageContainer').innerHTML += `
        <div class="mdl-card">
          <div class="mdl-card__title">
            <span class="color-gray"> [${getDate()}] : [${userName}] </span>
          </div>
          <div class="mdl-card__media color-gray" >
            ${messageField.value}
          </div>
        </div>
      `;
      messageField.value = '';
    } catch (error) {
      console.error(error);
    }
  }
