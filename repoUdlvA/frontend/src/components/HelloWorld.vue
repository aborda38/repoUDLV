<template>
  <div class="hello">
    <h1>¡Bienvenidos!</h1>
    <h2>Repositorio Institucional Universidad DLa Vida</h2>



    <b-container>
      <b-row class="justify-content-center mt-4">
        <b-col col md="8">
          <b-card header="Log In" 
            header-bg-variant="danger" header-text-variant="white">

              <b-card-text>

                <b-form @submit.prevent="onSubmit">
                  <b-form-group description="Ingresa tu usuario" label="Username">
                    <b-form-input v-model="username" required></b-form-input>
                  </b-form-group>
                
                  <b-form-group description="Ingresa tu contraseña" label="Password">
                    <b-form-input v-model="password" type="password" required></b-form-input>
                  </b-form-group>
                  <b-button type="submit" variant="outline-danger">Login</b-button>
                </b-form>
              
              </b-card-text>

          </b-card>
        </b-col>
      </b-row>
    </b-container>



    <body class="d-flex flex-column">
        <div id="page-content">
          <div class="container text-center">
            <div class="row justify-content-center">
              <div class="col-md-7">
                <h1 class="fw-light mt-4 text-white"></h1>
                <p class="lead text-white-50"></p>
              </div>
            </div>
          </div>
        </div>
        <footer id="sticky-footer" class="flex-shrink-0 py-4 bg-danger text-light font-weight-bold">
          <div class="container text-center">
            <small> Universidad DLa Vida</small> <br>
            <small>Copyright &copy; Misión TIC 2022</small>
          </div>
        </footer>
    </body>

  </div>    
</template>

<script>
import axios from 'axios';

export default{
    data () {
        return {
          username:"",
          password:"",
        }
    },
    methods: {
        onSubmit(event) {
          let json = {
            "username":this.username,
            "password":this.password,

          };
          axios.post('http://127.0.0.1:8000/auth/', json)
          .then(data =>{
            if(data.data.status == "ok"){
              this.$router.push('libros');
            }
            this.$router.push('libros');
          })
          
        }


    },
}
</script>


<style scoped>
h1, h2 {
  font-weight: normal;
  color: #a50c28
}
ul {
  list-style-type: none;
  padding: 0;
}
</style>
