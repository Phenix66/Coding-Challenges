[SECTION .text]
global _start
_start:

;;; execve("/bin//sh",0,0);
mov eax,0x0b
push 0x00
push 0x68732f2f ;hs//
push 0x6e69622f ;nib/
mov ebx,esp
mov ecx,0x0
mov edx,0x0
int 0x80
