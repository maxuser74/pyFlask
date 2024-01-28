$(document).ready(function(){
    console.log('Document ready!!!');
    const sound_effect = new Audio('static/move-self.mp3');

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
  navbar_height = document.getElementById("NAVBAR").offsetHeight
  d_h = $(window).height() - navbar_height - 15;
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
          sound_effect.play()
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

$('#BOOTSTRAP_DROPDOWN').click(function(){
    text = $(this).find("option:selected").val;
    console.log(text)
    alert("hi")
});

function populate_selection(response){
    var bs_dropdown = document.getElementById("BOOTSTRAP_DROPDOWN");
    var sel_l = Object.keys(response.data.pgn_list).length;
    for(i=0; i<sel_l; i++){
        var option = document.createElement("option");
        option.text = response.data.pgn_list[i];

        // Boostrap dropdown population
        var li = document.createElement("li");
        var link = document.createElement("a");
        var text = document.createTextNode(option);
        link.appendChild(option);
        link.href = "#";
        link.className = "dropdown-item"
        li.setAttribute("value", option.text);
        li.appendChild(link);
        bs_dropdown.appendChild(li);
    }



}

function update_view(response){
console.log(response)
      document.getElementById('SVG_PLACEHOLDER').innerHTML = response.data.svg;
      document.getElementById('TITLE').innerHTML = response.data.title;
      document.getElementById('SELECT1').value=response.data.title;
       };

})