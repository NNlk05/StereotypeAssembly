Y=input
T='exit'
S='goto'
R='input'
Q='read'
P='store'
O='print'
N='sub'
M='add'
L=print
K=IndexError
H=ValueError
C=len
import sys as B
U=1024
def V(file_name):
	A=file_name
	try:
		with open(A,'r')as C:D=C.read().lower()
	except K:B.exit('Error: No file name provided')
	except FileNotFoundError:B.exit(f"Error: File '{A}' not found")
	except IOError:B.exit(f"Error: Unable to open or read file '{A}'")
	return D.strip().split(';')
def W(size):return{str(id):0 for id in range(size)}
def A(num):return int(num,16)
def I(index):return G[index]
def F(index,text):G[index]=text
class D:
	def __init__(A,command,line_words):
		B=command
		if B not in J:raise H(f"SyntaxError at {E}, unknown command: {B}")
		A.command=B;A.line_words=line_words;A.execute_command()
	def execute_command(A):
		if A.command==M:A.add()
		elif A.command==N:A.sub()
		elif A.command==O:A.print()
		elif A.command==P:A.store()
		elif A.command==Q:A.read()
		elif A.command==R:A.input()
		elif A.command=='if':A.conditional()
		elif A.command=='gt':A.gt()
		elif A.command=='lt':A.lt()
		elif A.command=='eq':A.eq()
		elif A.command==S:A.goto()
		elif A.command==T:B.exit()
	def add(B):
		if C(B.line_words)==4:D=B.line_words[1],B.line_words[2];E=B.line_words[3];F(E,A(D[0])+A(D[1]))
	def sub(B):
		if C(B.line_words)==4:D=B.line_words[1],B.line_words[2];E=B.line_words[3];F(E,A(D[0])-A(D[1]))
	def print(A):
		if C(A.line_words)==2:B=A.line_words[1];L(I(B))
	def store(B):
		if C(B.line_words)==3:D=B.line_words[1];E=B.line_words[2];F(D,A(E))
	def read(A):
		if C(A.line_words)==2:B=A.line_words[1];L(I(B))
	def input(B):
		if C(B.line_words)==2:D=B.line_words[1];E=Y('Enter value: ');F(D,A(E))
	def conditional(B):
		if C(B.line_words)>=4:
			E=B.line_words[1];F=B.line_words[2];G=B.line_words[3]
			if F=='==':
				if A(E)==A(G):D(B.line_words[4],B.line_words[5:])
			elif F=='!=':
				if A(E)!=A(G):D(B.line_words[4],B.line_words[5:])
			elif F=='>':
				if A(E)>A(G):D(B.line_words[4],B.line_words[5:])
			elif F=='<':
				if A(E)<A(G):D(B.line_words[4],B.line_words[5:])
			elif F=='>=':
				if A(E)>=A(G):D(B.line_words[4],B.line_words[5:])
			elif F=='<=':
				if A(E)<=A(G):D(B.line_words[4],B.line_words[5:])
	def gt(B):
		if C(B.line_words)==3:D=B.line_words[1];E=B.line_words[2];return A(D)>A(E)
	def lt(B):
		if C(B.line_words)==3:D=B.line_words[1];E=B.line_words[2];return A(D)<A(E)
	def eq(B):
		if C(B.line_words)==3:D=B.line_words[1];E=B.line_words[2];return A(D)==A(E)
	def goto(A):
		if C(A.line_words)==2:B=int(A.line_words[1]);global E;E=B-1
def X():
	I=B.argv[1];F=V(I);global G;G=W(U);global J;J=[M,N,O,P,Q,R,'if','gt','lt','eq',S,T];global E;E=0
	while E<C(F):
		try:
			E+=1;L=F.pop(0);A=L.split(' ')
			if not A[0].isdigit():raise H
		except K:B.exit('Error: Reached end of file unexpectedly')
		except H:B.exit(f"Error at line {E}: lines must start with a number")
		for X in A:
			if C(A)==0 or X==';':continue
		D(A[0],A)
if __name__=='__main__':X()