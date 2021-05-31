const TOKEN_KEY = 'user-token'


const tokenService = {

    //Obtener token
    getToken(){
        
        //Retornamos valor obtenido en el LS
        return localStorage.getItem(TOKEN_KEY)

    }

}

export {tokenService}