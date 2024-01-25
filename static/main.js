$(document).ready(function(){
    console.log('Document ready!!!');

    $.ajax({url: '',
        type:'get',
        contentType: 'application/json',
        success: function(result){
            console.log(result)
            document.getElementById('svg_placeholder').innerHTML = result['svg'];
            }
    })

  $('#BTN_1').click(function(){
    console.log('Clicked !!!')

    $.ajax({url: '',
    type:'post',
    contentType: 'application/json',
    data: JSON.stringify({'variable2':'Clicked'}),
    success:function(result){
        console.log(result)
        document.getElementById('svg_placeholder').innerHTML = result['svg'];
    }
    })
  })

})