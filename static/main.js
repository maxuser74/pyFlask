$(document).ready(function(){
    console.log('Document ready!!!');

    $.ajax({url: '',
        type:'get',
        contentType: 'application/json',
        success: function(result){
            console.log(result)
            document.getElementById('SVG_PLACEHOLDER').innerHTML = result['svg'];
            document.getElementById('TITLE').innerHTML = result['title'];

            }
    })

  $('#BTN_MIRROR').click(function(){
    console.log('Clicked !!!')

    $.ajax({url: '',
    type:'post',
    contentType: 'application/json',
    data: JSON.stringify({'button':'mirror'}),
    success:function(result){
        console.log(result)
        document.getElementById('SVG_PLACEHOLDER').innerHTML = result['svg'];
        document.getElementById('TITLE').innerHTML = result['title'];
    }
    })
  })

$('#BTN_NEXT').click(function(){
    $.ajax({url: '',
    type:'post',
    contentType: 'application/json',
    data: JSON.stringify({'button':'next'}),
    success:function(result){
        console.log(result)
        document.getElementById('SVG_PLACEHOLDER').innerHTML = result['svg'];
        document.getElementById('TITLE').innerHTML = result['title'];
    }
    })
  })

$('#BTN_PREV').click(function(){
    $.ajax({url: '',
    type:'post',
    contentType: 'application/json',
    data: JSON.stringify({'button':'prev'}),
    success:function(result){
        console.log(result)
        document.getElementById('SVG_PLACEHOLDER').innerHTML = result['svg'];
        document.getElementById('TITLE').innerHTML = result['title'];
    }
    })
  })

$('#BTN_RESET').click(function(){
    $.ajax({url: '',
    type:'post',
    contentType: 'application/json',
    data: JSON.stringify({'button':'reset'}),
    success:function(result){
        console.log(result)
        document.getElementById('SVG_PLACEHOLDER').innerHTML = result['svg'];
        document.getElementById('TITLE').innerHTML = result['title'];
    }
    })
  })

})