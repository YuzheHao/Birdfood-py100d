function loadXMLDoc()
{
	var xmlhttp;
    xmlhttp=new XMLHttpRequest();
    xmlhttp.open("GET", "ajax_info.txt", true)
	xmlhttp.send();
}