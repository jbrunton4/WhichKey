function findKey() {
  var accs = document.getElementById("accidentals_input").value;
  var type = document.getElementById("type").value;

  console.log(accs+type)

  if (type=="sharps" && accs==0) {
    key = "C";
  } else if (type=="flats" && accs==0) {
    key="C";
  } else if (type=="sharps" && accs==1) {
    key = "G";
  } else if (type=="sharps" && accs==2) {
    key = "D";
  } else if (type=="sharps" && accs==3) {
    key = "A";
  } else if (type=="sharps" && accs==4) {
    key = "E";
  } else if (type=="sharps" && accs==5) {
    key = "B";
  } else if (type=="sharps" && accs==6) {
    key = "F#";
  } else if (type=="sharps" && accs==7) {
    key = "C#";
  } else if (type=="flats" && accs==1) {
    key = "F"
  } else if (type=="flats" && accs==2) {
    key = "Bb"
  } else if (type=="flats" && accs==3) {
    key = "Eb"
  } else if (type=="flats" && accs==4) {
    key = "Ab"
  } else if (type=="flats" && accs==5) {
    key = "Db"
  } else if (type=="flats" && accs==6) {
    key = "Gb"
  } else if (type=="flats" && accs==7) {
    key = "Cb"
  } else {
    alert("Please enter a number between 0 and 7.");
  }

  alert("This is they key of " + key);
}
