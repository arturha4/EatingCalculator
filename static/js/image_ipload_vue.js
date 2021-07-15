new Vue({
    el:'#food_create',
    delimiters:['[[',']]'],
    data:{
        food_fields:[]
    },
    methods:{
        checkForm(){
            console.log(this.name)
            console.log(this.fats)
        }
    }

})