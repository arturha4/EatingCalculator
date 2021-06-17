new Vue({
    el:'#food_app',
    data:{
        food:[]
    },
    created: function (){
        const vm=this;
        axios.get('http://127.0.0.1:8000/api/food/')
            .then(function (responce){
                vm.food=responce.data
            })
    }
})