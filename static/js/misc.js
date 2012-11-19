<!--
function appendFramedPage(id, link, user_is_staff) {
	node = document.getElementById(id);
	if (node.frameIsOpen) {
		node.frameIsOpen=false; node.innerHTML='';
	} else {
		node.frameIsOpen=true;
		if (user_is_staff) {
			node.innerHTML='<td width="699" valign="bottom"><iframe src="' + link +
			'" border="0" frameborder="0" align="center" width="699" height="1000">' +
			'</iframe><p>&nbsp;</p></td>'
		} else {
			node.innerHTML='<td width="799" valign="bottom"><iframe src="' + link +
			'" border="0" frameborder="0" align="center" width="799" height="1000">' +
			'</iframe><p>&nbsp;</p></td>';
		}
	}
}
//-->