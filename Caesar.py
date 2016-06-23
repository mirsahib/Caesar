try:
	from tkinter import *
except ImportError:
	from Tkinter import *
from tkinter import messagebox

root=Tk()
root.title('The Caesar Cipher')

#function 
def encrypt():
	result = ''
	if step.get()=='Default key is 13':
		shift = 13
	else:
		shift = int(step.get())
	for char in plaintext_entry.get():
		if char.isalpha()==True:
			if ord(char)>=65 and ord(char)<=91:
				result+=chr(((ord(char)-65)+shift)%26 + 65)
			if ord(char)>=97 and ord(char)<=122:
				result+=chr(((ord(char)-97)+shift)%26 + 97)
		else:
			result+=char

	encrypt_result.set(result)
def decrypt():
	result=''
	if step.get()=='Default key is 13':
		shift=13
	else:
		shift = int(step.get())

	for char in plaintext_entry.get():
		if char.isalpha()==True:
			if ord(char)>=65 and ord(char)<=91:
				result+=chr(((ord(char)-65)-shift)%26 + 65)
			if ord(char)>=97 and ord(char)<=122:
				result+=chr(((ord(char)-97)-shift)%26 + 97)
		else:
			result+=char
	decypt_result.set(result)


def delete_key(event):
	if step.get()=='Default key is 13':
		key_entry.delete(0,END)
		key_entry.config(fg='black')
	

def delete_text(event):
	if plaintext_entry.get()=='Default text':
		plaintext_entry.delete(0,END)
		plaintext_entry.config(fg='black')

def about():
	messagebox.showinfo(title='About',message="The Caesar Cipher Beta v0.1\nCopyright@ MIR SAHIB 2016-17")


#menubar

menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
menubar.add_command(label="About",command=about)


#Encryption

#head label
cipher_label=Label(root,text='The Caesar Cipher v0.1',font=('Helvetica',16)).pack(side=TOP,pady=10)
encryption_label = Label(root,text='Encrypt').pack(side=TOP,pady=10)

#rotation key
step = StringVar()
step.set('Default key is 13')
key_entry=Entry(root,textvariable=step,width=80,foreground='grey')
key_entry.bind("<Button-1>", delete_key)
key_entry.pack(pady=10)

#plaintext input
plaintext = StringVar(root,value='Default text')
plaintext_entry = Entry(root,textvariable=plaintext,width=80,fg='grey')
plaintext_entry.bind("<Button-1>",delete_text)
plaintext_entry.pack(pady=10)

#encrypt button
encrypt_button = Button(root,text='Encrypt',bd=2,bg='red',width=20,command=encrypt).pack(pady=10)

#encrypt text
encrypt_result = StringVar()
encrypt_text = Entry(root,textvariable=encrypt_result,width=80,stat='readonly',fg='red').pack(pady=10)

#decryption
decryption_label = Label(root,text='Decrypt').pack(side=TOP,pady=5)
#decypt_text
decypt_result = StringVar()
decrypt_text = Entry(root,textvariable=decypt_result,width=80,stat='readonly',fg='red').pack(pady=5)
#decrypt_button
decrypt_button=Button(root,text='Decrypt',bd=2,bg='green',width=20,command=decrypt).pack(pady=5)

root.config(menu=menubar)


root.mainloop()
