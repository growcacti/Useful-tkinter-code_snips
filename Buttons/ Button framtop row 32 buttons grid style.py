shortcutbar = Frame(root, height=25)


btn1 = Button(shortcutbar, text="show list", command=listshow)
btn1.grid(row=1, column=1)
btn2 = Button(shortcutbar, text="sort", command=listsort)
btn2.grid(row=1, column=2)
btn3 = Button(shortcutbar, text="Clear", command=cleartxt)
btn3.grid(row=1, column=3)
btn4 = Button(shortcutbar, text="square", command=squ_num)
btn4.grid(row=1, column=4)
btn5 = Button(shortcutbar, text="Reversal", command=cmd)
btn5.grid(row=1, column=5)
btn6 = Button(shortcutbar, text="Lowercase", command=lo)
btn6.grid(row=1, column=6)
btn7 = Button(shortcutbar, text="Uppercase", command=up)
btn7.grid(row=1, column=7)
btn8 = Button(shortcutbar, text="cv_chop.py", command=cmd)
btn8.grid(row=1, column=8)
btn9 = Button(shortcutbar, text="9", command=cmd)
btn9.grid(row=1, column=9)
btn10 = Button(shortcutbar, text="10", command=cmd)
btn10.grid(row=1, column=10)
btn11 = Button(shortcutbar, text="11", command=cmd)
btn11.grid(row=1, column=11)
btn12 = Button(shortcutbar, text="12", command=cmd)
btn13.grid(row=1, column=12)
btn14 = Button(shortcutbar, text="13", command=cmd)
btn14.grid(row=1, column=13)
btn15 = Button(shortcutbar, text="14", command=cmd)
btn15.grid(row=1, column=13)
btn16 = Button(shortcutbar, text="15", command=cmd)
btn16.grid(row=1, column=14)
btn17 = Button(shortcutbar, text="16", command=cmd)
btn17.grid(row=1, column=15)
btn18 = Button(shortcutbar, text="17", command=cmd)
btn18.grid(row=1, column=16)
btn19 = Button(shortcutbar, text="18", command=cmd)
btn19.grid(row=1, column=17)
btn20 = Button(shortcutbar, text="19", command=cmd)
btn20.grid(row=1, column=18)
btn21 = Button(shortcutbar, text="20", command=cmd)
btn21.grid(row=1, column=19)

btn22 = Button(shortcutbar, text="21", command=cmd)
btn22.grid(row=1, column=2)
btn23 = Button(shortcutbar, text="22", command=cmd)
btn23.grid(row=2, column=2)
btn24 = Button(shortcutbar, text="23", command=cmd)
btn24.grid(row=2, column=22)
btn25 = Button(shortcutbar, text="24", command=cmd)
btn25.grid(row=2, column=12)
btn26 = Button(shortcutbar, text="25", command=cmd)
btn26.grid(row=2, column=13)
btn27 = Button(shortcutbar, text="26", command=cmd)
btn27.grid(row=2, column=13)
btn28 = Button(shortcutbar, text="27", command=cmd)
btn28.grid(row=2, column=14)
btn29 = Button(shortcutbar, text="28", command=cmd)
btn29.grid(row=2, column=15)
btn30 = Button(shortcutbar, text="29", command=cmd)
btn30.grid(row=2, column=16)
btn31 = Button(shortcutbar, text="30", command=cmd)
btn31.grid(row=2, column=17)
btn32 = Button(shortcutbar, text="31", command=cmd)
btn32.grid(row=2, column=18)
btn33 = Button(shortcutbar, text="32", command=cmd)
btn33.grid(row=2, column=19)


shortcutbar.grid(row=1, column=0, rowspan=3, columnspan=30)
