$(document).ready(function(){
    console.log('Document ready!!!');

    axios.post('/',{'button':'reset'})
    .then((response) => {
        update_view(response)
     }, (error) => {
      console.log(error);
    });


  $('#BTN_MIRROR').click(function(){
    axios.post('/',{'button':'mirror'})
    .then((response) => {
        update_view(response)
      }, (error) => {
      console.log(error);
    });
  })

  $('#BTN_PREV').click(function(){
    axios.post('/',{'button':'prev'})
    .then((response) => {
        update_view(response)
      }, (error) => {
      console.log(error);
    });
  })

    $('#BTN_NEXT').click(function(){
    axios.post('/',{'button':'next'})
    .then((response) => {
              update_view(response)
    }, (error) => {
    console.log(error);
    });
  })

  $('#BTN_RESET').click(function(){
    axios.post('/',{'button':'reset'})
    .then((response) => {
        update_view(response)
     }, (error) => {
      console.log(error);
    });
  })

function update_view(response){
console.log(response)
      document.getElementById('SVG_PLACEHOLDER').innerHTML = response.data.svg;
      document.getElementById('TITLE').innerHTML = response.data.title;

      var sel = document.getElementById("SELECT1");
        var i, L = sel.options.length - 1;
        for(i = L; i >= 0; i--) {
            sel.remove(i);
        }

        var sel_l = Object.keys(response.data.pgn_list).length;
        for(i=0; i<sel_l; i++){
        console.log(response.data.pgn_list[i])
        var option = document.createElement("option");
        option.text = response.data.pgn_list[i];
        sel.add(option);
        }

    };
})