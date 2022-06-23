var socket = io();

let method = false;
let key = 'Hello World!';
let txt = {
	false: 'Encryption',
	true: 'Decryption',
};

function func() {
	text = document.getElementById('one').value;
	let m = 0;
	if (method) m = 1;
	socket.emit('input', {
		text: text,
		key: key,
		method: m,
	});
}

let toggle = document.getElementById('ed');
let togglelabel = document.getElementById('tgllabel');
toggle.addEventListener('change', function () {
	method = !method;
	togglelabel.innerHTML = txt[method];
	func();
});

let passwordinput = document.getElementById('password');
passwordinput.addEventListener('input', function () {
	key = this.value;
	func();
});

socket.on('output', function (data) {
	document.getElementById('one').classList.remove('is-invalid');
	document.getElementById('two').value = data;
});
socket.on('error', function (data) {
	document.getElementById('one').classList.add('is-invalid');
	document.getElementById('two').value = 'Invalid input';
});
