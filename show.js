var x;

function fx(){

	var crypto=require('crypto');
	var sha=crypto.createHash('sha256').update(Math.random().toString()).digest('hex');
	var sha2=crypto.createHash('sha256').update(Math.random().toString()).digest('hex');

	console.log("gcc -O2 -Wall -Wno-statistic build-centos-x86/q3cpp build-centos-x86/cpp/"+sha.substr(0,Math.ceil(Math.random()*30))+".o build-centos-x86/cpp/lex.o build-centos-x86/cpp/"+sha2.substr(0,Math.ceil(Math.random()*50))+".o build-centos-x86/cpp/"+sha.substr(0,Math.ceil(Math.random()*10))+".o build-centos-x86/cpp/"+sha+".o build-centos-x86/cpp/eval.o build-centos-x86/cpp/include.o build-centos-x86/cpp/hideset.o build-centos-x86/cpp/getopt.o build-centos-x86/cpp/"+sha2.substr(0,Math.ceil(Math.random()*44)));

	if( Math.ceil(Math.random()*1000)%777 < 321 ) console.log("");
	if( Math.ceil(Math.random()*1000)%778 == 777 ){

		console.log("Configuring.........");
		console.log("Setting...");
		console.log("Compiling.........");
		console.log("Checking.........");
		clearInterval(x);
		x = setInterval(fx, 15000)
	}else{
		clearInterval(x);
		x = setInterval(fx, Math.ceil(Math.random()*2000))
	}

}

x=setInterval(fx,1000)
