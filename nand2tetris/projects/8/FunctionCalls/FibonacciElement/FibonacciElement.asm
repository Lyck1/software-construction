@256
D=A
@SP
M=D
@retAddrLabel0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(retAddrLabel0)
(Main.fibonacci)
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
A=A-1
D=M-D
@LT_TRUE1
D;JLT
@SP
A=M-1
A=A-1
M=0
@END1
0;JMP
(LT_TRUE1)
@SP
A=M-1
A=A-1
M=-1
(END1)
@SP
M=M-1
@SP
M=M-1
A=M
D=M
@N_LT_2
D;JNE
@N_GE_2
0;JMP
(N_LT_2)
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@ENDFRAME
M=D
@5
D=D-A
A=D
D=M
@RETADDR
M=D
@SP
A=M-1
D=M
@SP
M=M-1
@ARG
A=M
M=D
A=A+1
D=A
@SP
M=D
@ENDFRAME
D=M
D=D-1
A=D
D=M
@THAT
M=D
@ENDFRAME
D=M
D=D-1
D=D-1
A=D
D=M
@THIS
M=D
@ENDFRAME
D=M
D=D-1
D=D-1
D=D-1
A=D
D=M
@ARG
M=D
@ENDFRAME
D=M
D=D-1
D=D-1
D=D-1
D=D-1
A=D
D=M
@LCL
M=D
@RETADDR
A=M
0;JMP
(N_GE_2)
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
A=A-1
D=M
A=A+1
D=D-M
A=A-1
M=D
@SP
M=M-1
@retAddrLabel2
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(retAddrLabel2)
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
A=A-1
D=M
A=A+1
D=D-M
A=A-1
M=D
@SP
M=M-1
@retAddrLabel3
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(retAddrLabel3)
@SP
A=M-1
D=M
@SP
M=M-1
A=M
A=A-1
D=D+M
M=D
@LCL
D=M
@ENDFRAME
M=D
@5
D=D-A
A=D
D=M
@RETADDR
M=D
@SP
A=M-1
D=M
@SP
M=M-1
@ARG
A=M
M=D
A=A+1
D=A
@SP
M=D
@ENDFRAME
D=M
D=D-1
A=D
D=M
@THAT
M=D
@ENDFRAME
D=M
D=D-1
D=D-1
A=D
D=M
@THIS
M=D
@ENDFRAME
D=M
D=D-1
D=D-1
D=D-1
A=D
D=M
@ARG
M=D
@ENDFRAME
D=M
D=D-1
D=D-1
D=D-1
D=D-1
A=D
D=M
@LCL
M=D
@RETADDR
A=M
0;JMP
(Sys.init)
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
@retAddrLabel1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(retAddrLabel1)
(END)
@END
0;JMP
