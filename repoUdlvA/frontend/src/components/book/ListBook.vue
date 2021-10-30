<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Lista de libros</h2>

                <div class="col-md-12">
                    <b-table striped hover :items="bookss" :fields="fieldss"> 
                    </b-table>
                </div>
                <template>
                    <b-button>Editar</b-button>
                    <b-button href="#">Eliminar</b-button>
                </template>
            </div>
        </div>
    </div>
</template>


<script>

export default {

}
</script>

<script>
import axios from 'axios';

export default{
    data () {
        return {
            fieldss:[
                { key:'id',label:'ID'},
                { key:'title',label:'Título'},
                { key:'author_or_authors',label:'Autor(es)'},
                { key:'abstract',label:'Resumen'},
                { key:'act',label:'Acción'},
            ],
            bookss:[]
        }
    },
    methods: {
        getBooks () {
            const path ='http://127.0.0.1:8000/registrar-libros/'
            axios.get(path).then((response) => {
                this.bookss = response.data
            })
            .catch((error) => {
              console.log(error)
            })
        }
    },
    created(){
        this.getBooks()
    },
}
</script>

<style lang="css" scoped>
h1, h2 {
  font-weight: normal;
  color: #a50c28
}
</style>
