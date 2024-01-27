$(document).ready(function(){
    console.log('Document ready!!!');

    var sound = new Audio('sounds/move-self.mp3');

    window.addEventListener("resize", setWindowSize);
    setWindowSize();

    axios.post('/',{'button':'reset'})
    .then((response) => {
        update_view(response)
        populate_selection(response)
     }, (error) => {
      console.log(error);
    });

function setWindowSize() {
  d_h = $(window).height() - 10;
  d_h_s = d_h.toString();
  d_h_s = d_h_s + 'px'
  document.getElementById("SVG_PLACEHOLDER").style.maxHeight = d_h_s;
  document.getElementById("SVG_PLACEHOLDER").style.maxWidth = d_h_s;
}

    $('#SELECT1').change(function(){
        this_select = $(this).val()
        console.log(this_select);
        document.getElementById('TITLE').innerHTML = this_select;
        axios.post('/',{'select':this_select})
            .then((response) => {
                update_view(response)
            }, (error) => {
        console.log(error);
    });

    })

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

function populate_selection(response){
              var sel = document.getElementById("SELECT1");
                var i, L = sel.options.length - 1;
                for(i = L; i >= 0; i--) {
                    sel.remove(i);
                }

                var sel_l = Object.keys(response.data.pgn_list).length;
                for(i=0; i<sel_l; i++){
                var option = document.createElement("option");
                option.text = response.data.pgn_list[i];
                sel.add(option);

                document.getElementById('SELECT1').value=response.data.title;

                }
}

function update_view(response){
console.log(response)
      document.getElementById('SVG_PLACEHOLDER').innerHTML = response.data.svg;
      document.getElementById('TITLE').innerHTML = response.data.title;
      document.getElementById('SELECT1').value=response.data.title;
       };
})