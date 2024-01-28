$(document).ready(function(){
    console.log('Document ready!!!');
    const sound_effect = new Audio('static/move-self.mp3');

    window.addEventListener("resize", setWindowSize);
    setWindowSize();

    const inputElement = document.getElementById("FILE_LOAD");
    inputElement.addEventListener("change", handleFiles, false);
    function handleFiles() {
      const fileList = this.files; /* now you can work with the file list */
        console.log(fileList)
    }

    axios.post('/',{'button':'reset'})
        .then((response) => {
            update_view(response)
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

    function update_view(response){
        console.log(response)
              document.getElementById('SVG_PLACEHOLDER').innerHTML = response.data.svg;
              document.getElementById('TITLE').innerHTML = response.data.title;
     };

})