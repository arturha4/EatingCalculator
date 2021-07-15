new Vue({
    el:'#create_food_app',
     delimiters:['[[',']]'],
    methods:{
        onFileSelected(event){
            console.log(event)
        }
    }
})