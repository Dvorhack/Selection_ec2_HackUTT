#include <stdio.h>
#include <stdlib.h>

void win(){
	system("/bin/sh");
}

void foo(){
	int check =0;
	char buf[10];

	printf("Bonjour, quel est votre nom ?\n");
	gets(buf);

	if(check == 0xc0febabe)
		win();
	else
		printf("Perdu !\n");
}

int main(){
	printf("Bienvenue dans le chall de pwn n°1\n\n");
	setbuf(stdout, 0);
	foo();
}