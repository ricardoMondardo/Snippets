const getInfoFromGit = function() {
        const requestOptions = {
            method: 'GET',
            redirect: 'follow'
        };

      let nameUser = document.getElementById('input-name').value;
      
      fetch(`https://api.github.com/users/${nameUser}`, requestOptions)
        .then(response => response.json())
        .then((result) => {            
            let nameSpan = document.getElementById('user-name');
            let imgUser = document.getElementById('img-user');
            
            nameSpan.innerHTML = result.name;
            imgUser.src = result.avatar_url;

            console.log(result, nameSpan, imgUser);
        })
        .catch(error => console.log('error', error));   

}