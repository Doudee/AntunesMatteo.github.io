import turtle
turtle.tracer(0,0)
turtle.screensize(2000,2000)
turtle;goto(-500,0)
turtle.pu()
turtle.pd()

def dessin(courbe, long, angle):
	for cara in courbe:
		if cara == '+': turtle.left(angle)
		elif cara == '-': turtle.right(angle)
		elif cara in ['F', 'G']: turtle.forward(long)

def regle(chaine):
	nouvelleChaine = ''
	for lettre in chaine:
		if lettre == 'F':
			nouvelleChaine = nouvelleChaine + 'F-G+F+G-F'
		elif lettre == 'G' :
		 	nouvelleChaine = nouvelleChaine + 'GG'
		else :
			nouvelleChaine = nouvelleChaine + lettre
	return courbe

def courbeKoch(motif, niter):
	courbe = motif
	for i in range (niter):
		nouveauMotif = regle(courbe)
		courbe = nouveauMotif
	return courbe

#courbe = courbeKoch('F' ,3)
#dessin(courbe,50 60)

def flocon(motif, niter):
	courbe = courbeKoch(motif, niter)
	flocon = ''
	for _ in range(3)
		flocon += courbe
		flocon += '--'
	return flocon


long = 2
angle = 60
niter = 6
dessin(courbeKoch('F-G-G',3), 40, 120)

turtle.update()
turtle.exitonclick()