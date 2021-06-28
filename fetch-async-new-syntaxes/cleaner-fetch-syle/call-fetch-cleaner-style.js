const getInfoFromGit = function () {
  return CallApi();
}

async function CallApi() {

      const requestOptions = {
            method: 'GET',
            redirect: 'follow'
        };

      let nameUser = document.getElementById('input-name').value;
      
      const resp = await fetch(`https://api.github.com/users/${nameUser}`, requestOptions)
      const data = await resp.json();

      let nameSpan = document.getElementById('user-name');
      let imgUser = document.getElementById('img-user');
      
      nameSpan.innerHTML = data.name;
      imgUser.src = data.avatar_url;


}