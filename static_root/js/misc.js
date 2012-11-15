<!--
function appendFramedPage(id, link) {
	node = document.getElementById(id);
	if (node.frameIsOpen) {
		node.frameIsOpen=false; node.innerHTML='';
	} else {
		node.frameIsOpen=true;
		node.innerHTML='<td width="799">' +
		'<iframe src="' + link +
		'" name="cbframe"></iframe><p>&nbsp;</p>' +
		'</td>';
	}
}
//-->