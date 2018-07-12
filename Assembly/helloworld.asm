[SECTION .text]
global _start
_start:

;;; write(1, "Hello World!", 12);
mov eax,0x04 ;write sys call
mov ebx,0x01 ;fd for stdout
push 0x0000000a
push 0x21646c72 ;!dlr
push 0x6f57206f ;oW o
push 0x6c6c6548 ;lleH
mov ecx,esp ;esp will point to our string we just pushed
mov edx,0x0d ;char count
int 0x80

;;; exit(0);
mov eax,0x01 ;exit sys call
mov ebx,0x00 ;exit code
int 0x80
