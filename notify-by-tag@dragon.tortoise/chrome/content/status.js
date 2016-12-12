/*
 * This is an example I got from the Internet I can't remember the
 * link.  We will deal with this later.
 */
window.addEventListener("load", function(e) { 
	startup(); 
  }, false);

window.setInterval(
	function() {
		startup(); 
	}, 60000); //update date every minute

function startup() {
	var myPanel = document.getElementById("query-status-panel");
	var date = new Date();
	var day = date.getDay();
	var dateString = date.getFullYear() + "." + (date.getMonth()+1) +
    "." + date.getDate();
	myPanel.label = "query status: " + dateString;
}

