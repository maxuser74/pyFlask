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
      document.getElementById('SVG_PLACEHOLDER').innerHTML = response.data.svg;
      document.getElementById('TITLE').innerHTML = response.data.title;
};


})